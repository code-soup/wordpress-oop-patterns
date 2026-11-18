---
title: "Saving WordPress custom post types using an interface
			

			

				Custom post types are a powerful WordPress functionality. Everyone that works with WordPress long enough ends up using them. A custom post type can be anything. That flexibility is the source of much of its power. When using custom post type, you’re only limited by your imagination (trademark pending).
This flexibility also makes it a great use case for designing an interface. This article will put you in the interface creator seat. Exciting, I know!
As the interface creator, you’re in charge of designing the interface contract. This means that you get to dictate how someone use your interface (insert evil laughter here). It’s not all (evil) roses though.
The job gives you quite a lot of responsibility. This can make it hard for you to know where to start or what to do. Lucky for you, that’s what this article will help you with.

How WordPress handles post data"
url: https://carlalexander.ca/saving-wordpress-custom-post-types-using-interface/
slug: saving-wordpress-custom-post-types-using-interface
fetched: 2026-11-18
---

# Saving WordPress custom post types using an interface
			

			

				Custom post types are a powerful WordPress functionality. Everyone that works with WordPress long enough ends up using them. A custom post type can be anything. That flexibility is the source of much of its power. When using custom post type, you’re only limited by your imagination (trademark pending).
This flexibility also makes it a great use case for designing an interface. This article will put you in the interface creator seat. Exciting, I know!
As the interface creator, you’re in charge of designing the interface contract. This means that you get to dictate how someone use your interface (insert evil laughter here). It’s not all (evil) roses though.
The job gives you quite a lot of responsibility. This can make it hard for you to know where to start or what to do. Lucky for you, that’s what this article will help you with.

How WordPress handles post data

## Summary

Using interfaces to define persistence contracts for custom post types. Separating entity serialization from WordPress save operations.

## Code examples

### Example 1

```php
$post_id = wp_insert_post($post_data);

foreach ($post_meta as $key => $value) {
    update_post_meta($post_id, $key, $value);
}
```

### Example 2

```php
namespace MyPlugin;

/**
 * Interface for WordPress custom post types.
 */
interface PostTypeInterface
{
}
```

### Example 3

```php
namespace MyPlugin;

/**
 * A Product.
 */
class Product implements PostTypeInterface
{
    /**
     * The key used by the product post type.
     *
     * @var string
     */
    const POST_TYPE = 'product';

    /**
     * The description of the product.
     *
     * @var string
     */
    private $description;

    /**
     * The name of the product.
     *
     * @var string
     */
    private $name;

    /**
     * The price of the product.
     *
     * @var float
     */
    private $price;

    /**
     * Constructor.
     *
     * @param string $name
     * @param float  $price
     * @param string $description
     */
    public function __construct($name, $price, $description = '')
    {
        $this->description = $description;
        $this->name = $name;
        $this->price = $price;
    }
}
```

### Example 4

```php
register_post_type(Product:POST_TYPE);
```

### Example 5

```php
namespace MyPlugin;

/**
 * Insert or update a custom post type.
 * 
 * @param PostTypeInterface $post
 * @param bool              $wp_error
 *
 * @return int|WP_Error
 */
function wp_insert_custom_post(PostTypeInterface $post, $wp_error = false)
{
}
```

### Example 6

```php
namespace MyPlugin;

interface PostTypeInterface
{
    /**
     * Get the post data as a wp_insert_post compatible array.
     *
     * @return array
     */
    public function get_post_data();
}
```

### Example 7

```php
function wp_insert_custom_post(PostTypeInterface $post, $wp_error = false)
{
    return wp_insert_post($post->get_post_data(), $wp_error);
}
```

### Example 8

```php
namespace MyPlugin;

class Product implements PostTypeInterface
{
    // ...

    /**
     * Get the product data as a wp_insert_post compatible array.
     *
     * @return array
     */
    public function get_post_data()
    {
        return array(
            'post_content' => $this->description,
            'post_title' => $this->name,
            'post_status' => 'publish',
            'post_type' => self::POST_TYPE
        );
    }
}
```

### Example 9

```php
namespace MyPlugin;

interface PostTypeInterface
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

### Example 10

```php
namespace MyPlugin;

function wp_insert_custom_post(PostTypeInterface $post, $wp_error = false)
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

### Example 11

```php
namespace MyPlugin;

class Product implements PostTypeInterface
{
    // ...

    /**
     * Get the product data as a wp_insert_post compatible array.
     *
     * @return array
     */
    public function get_post_data()
    {
        return array(
            'post_content' => $this->description,
            'post_title' => $this->name,
            'post_status' => 'publish',
            'post_type' => self:POST_TYPE
        );
    }

    /**
     * Get all the post meta as a key-value associative array.
     *
     * @return array
     */
    public function get_post_meta()
    {
        return array(
          'price' => $this->price
        );
    }
}
```

### Example 12

```php
namespace MyPlugin;

$product = new Product('My awesome product', 49.99);
wp_insert_custom_post($product);
```

### Example 13

```php
namespace MyPlugin;

/**
 * Interface for WordPress custom post types.
 */
interface PostTypeInterface
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

/**
 * A Product.
 */
class Product implements PostTypeInterface
{
    /**
     * The key used by the product post type.
     *
     * @var string
     */
    const POST_TYPE = 'product';

    /**
     * The description of the product.
     *
     * @var string
     */
    private $description;

    /**
     * The name of the product.
     *
     * @var string
     */
    private $name;

    /**
     * The price of the product.
     *
     * @var float
     */
    private $price;

    /**
     * Constructor.
     *
     * @param string $name
     * @param float  $price
     * @param string $description
     */
    public function __construct($name, $price, $description = '')
    {
        $this->description = $description;
        $this->name = $name;
        $this->price = $price;
    }

    /**
     * Get the product data as a wp_insert_post compatible array.
     *
     * @return array
     */
    public function get_post_data()
    {
        return array(
            'post_content' => $this->description,
            'post_title' => $this->name,
            'post_status' => 'publish',
            'post_type' => self:POST_TYPE
        );
    }

    /**
     * Get all the post meta as a key-value associative array.
     *
     * @return array
     */
    public function get_post_meta()
    {
        return array(
          'price' => $this->price
        );
    }
}

/**
 * Insert or update a custom post type.
 *
 * @param PostTypeInterface $post
 * @param bool              $wp_error
 *
 * @return int|WP_Error
 */
function wp_insert_custom_post(PostTypeInterface $post, $wp_error = false)
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

/**
 * Registers our product custom post type.
 */
function register_custom_post_product() {
    register_post_type(Product::POST_TYPE);
}
add_action('init', 'register_custom_post_product');
```

## Source

https://carlalexander.ca/saving-wordpress-custom-post-types-using-interface/
