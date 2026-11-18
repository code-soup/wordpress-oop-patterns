---
title: "Designing entities using WordPress custom post types
			

			

				Custom post types are one the most powerful features of WordPress. You can use them to save any type of data that you want in the wp_posts table. Most plugins that build complex features on top of WordPress (e.g. WooCommerce) rely on them.
But custom post types aren’t just useful for developing new features on top of WordPress. They also allow us to rethink how we use object-oriented programming with WordPress. And, as we’ll see, this is an important step in your journey learning object-oriented programming with WordPress.
That’s because having a different view of custom post types will expand your object-oriented design horizons. They’ll help you build new types of classes that you might not have considered before. And this can be a game-changer when creating larger object-oriented plugins or themes.

Reviewing how to use an interface with custom post types"
url: https://carlalexander.ca/designing-entities-wordpress-custom-post-types/
slug: designing-entities-wordpress-custom-post-types
fetched: 2026-11-18
---

# Designing entities using WordPress custom post types
			

			

				Custom post types are one the most powerful features of WordPress. You can use them to save any type of data that you want in the wp_posts table. Most plugins that build complex features on top of WordPress (e.g. WooCommerce) rely on them.
But custom post types aren’t just useful for developing new features on top of WordPress. They also allow us to rethink how we use object-oriented programming with WordPress. And, as we’ll see, this is an important step in your journey learning object-oriented programming with WordPress.
That’s because having a different view of custom post types will expand your object-oriented design horizons. They’ll help you build new types of classes that you might not have considered before. And this can be a game-changer when creating larger object-oriented plugins or themes.

Reviewing how to use an interface with custom post types

## Summary

How to separate business logic (entities) from persistence (custom post types). Creating domain entities that don't know about WordPress database structure. The difference between entities and models.

## Code examples

### Example 1

```php
/**
 * Interface for WordPress custom post types.
 */
interface MyPlugin_PostTypeInterface
{
    /**
     * Get the post data as a wp_insert_post compatible array.
     *
     * @return array
     */
    public function get_post_data();
 
    /**
     * Get all the post meta as a key-value associative array.
     *
     * @return array
     */
    public function get_post_meta();
}
```

### Example 2

```php
/**
 * Insert or update a custom post type.
 *
 * @param MyPlugin_PostTypeInterface $post
 * @param bool                                            $wp_error
 *
 * @return int|WP_Error
 */
function wp_insert_custom_post(MyPlugin_PostTypeInterface $post, $wp_error = false)
{
    $post_id = wp_insert_post($post->get_post_data(), $wp_error);
 
    if (0 === $post_id || $post_id instanceof WP_Error) {
        return $post_id;
    }
 
    foreach ($post->get_post_meta() as $key => $value) {
        update_post_meta($post_id, $key, $value);
    }
 
    return $post_id;
}
```

### Example 3

```php
class MyPlugin_Product
{
}
```

### Example 4

```php
class MyPlugin_Product
{
    /**
     * Flag to see if the product is available or not.
     *
     * @var bool
     */
    private $available;

    /**
     * The name of the product.
     *
     * @var string
     */
    private $name;

    /**
     * The price of the product.
     *
     * @var string
     */
    private $price;

    /**
     * The product's universal code.
     *
     * @var string
     */
    private $product_code;
}
```

### Example 5

```php
class MyPlugin_Product
{
    /**
     * Change the price of a product.
     *
     * @return string
     */
    public function change_price($new_price)
    {
        $this->price = $new_price;
    }
}
```

### Example 6

```php
class MyPlugin_Product
{
    // ...

    /**
     * Change the price of a product.
     *
     * @param mixed
     */
    public function change_price($new_price)
    {
        if (!is_numeric($new_price)) {
            throw new \InvalidArgumentException('A product must have a "price" that is a non-negative number.');
        } elseif ($new_price < 0) {
            throw new \InvalidArgumentException('A product must have a "price" that isn\'t negative.');
        } elseif (!is_float($new_price)) {
            $new_price = (float) $new_price;
        }

        $this->price = number_format($new_price, 2, '.', '');
    }
}
```

### Example 7

```php
class MyPlugin_Product implements MyPlugin_PostTypeInterface
{
    // ...
}
```

### Example 8

```php
class MyPlugin_Product implements MyPlugin_PostTypeInterface
{
    /**
     * The post type used by products.
     *
     * @var string
     */
    const POST_TYPE = 'myplugin_product';

    /**
     * Flag to see if the product is available or not.
     *
     * @var bool
     */
    private $available;

    /**
     * The name of the product.
     *
     * @var string
     */
    private $name;

    /**
     * The price of the product.
     *
     * @var string
     */
    private $price;

    /**
     * The product's universal code.
     *
     * @var string
     */
    private $product_code;

    // ...

    /**
     * Get the post data as a wp_insert_post compatible array.
     *
     * @return array
     */
    public function get_post_data()
    {
        return array(
            'comment_status' => 'closed',
            'post_name' => $this->name,
            'post_title' => $this->name,
            'post_type' => self::POST_TYPE,
            'post_status' => $this->available ? 'publish' : 'draft',
        );
     }

    /**
     * Get all the post meta as a key-value associative array.
     *
     * @return array
     */
    public function get_post_meta();
    {
        return array(
            'myplugin_product_price' => $this->price,
            'myplugin_product_code' => $this->product_code,
        );
     }
}
```

## Source

https://carlalexander.ca/designing-entities-wordpress-custom-post-types/
