---
title: "How to use the static keyword with WordPress
			

			

				This site has a lot of object-oriented programming articles. Most of them focus on solving WordPress problems using object-oriented programming. This is great when you’re comfortable with object-oriented programming.
But most WordPress developers aren’t that comfortable with it. (You’d think there’d be a book on that or something.) It’s one thing to read about basic concepts like encapsulation and inheritance. It’s another to put them in practice. There are a lot of obstacles that you have to overcome.
One of these obstacles is the proper use of the static keyword. Static methods are a great object-oriented tool to use. But, like all good things, we can also abuse it if we’re not careful.
This happens a lot more in the WordPress development world than anywhere else. And there are good reasons for that. We’ll look at why that is and what you can do about it.

What is the static keyword?"
url: https://carlalexander.ca/static-keyword-wordpress/
slug: static-keyword-wordpress
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/how-to-use-static-keyword-wordpress/
---

# How to use the static keyword with WordPress
			

			

				This site has a lot of object-oriented programming articles. Most of them focus on solving WordPress problems using object-oriented programming. This is great when you’re comfortable with object-oriented programming.
But most WordPress developers aren’t that comfortable with it. (You’d think there’d be a book on that or something.) It’s one thing to read about basic concepts like encapsulation and inheritance. It’s another to put them in practice. There are a lot of obstacles that you have to overcome.
One of these obstacles is the proper use of the static keyword. Static methods are a great object-oriented tool to use. But, like all good things, we can also abuse it if we’re not careful.
This happens a lot more in the WordPress development world than anywhere else. And there are good reasons for that. We’ll look at why that is and what you can do about it.

What is the static keyword?

## Summary

Static methods, static properties, and static variables in WordPress context. When to use static vs instance members.

## Code examples

### Example 1

```php
class A_WP_Class
{
    /**
     * Actions that A_WP_Class hooks to.
     *
     * @var array
     */
    private static $actions = array('wp_loaded');

    /**
     * Get the actions that A_WP_Class hooks to.
     *
     * @return array
     */
    public static function get_actions()
    {
        return self::$actions;
    }
}

A_WP_Class::get_actions();
```

### Example 2

```php
function increment()
{
    static $counter = 0;

    echo $counter;

    $counter++;
}

increment(); // Echoes "0"
increment(); // Echoes "1"
increment(); // Echoes "2"
```

### Example 3

```php
class Post
{
    // ...

    /**
     * Sanitizes the given text by removing or encoding dangerous characters.
     *
     * @param string $text
     *
     * @return string
     */
    private static function sanitize($text)
    {
        return strip_tags($text);
    }
}
```

### Example 4

```php
class Counter
{
    /**
     * Current counter value.
     *
     * @var int
     */
    private static $count = 0;

    /**
     * Increment counter by 1.
     */
    public static function increment()
    {
        self::$count++;
    }

    /**
     * Get the current counter value.
     *
     * @return int
     */
    public static function get_count()
    {
        return self::$count;
    }
}
```

### Example 5

```php
class A_WP_Class
{
    /**
     * Get the actions that A_WP_Class hooks to.
     *
     * @return array
     */
    public static function get_actions()
    {
        return array('wp_loaded');
    }
}
```

### Example 6

```php
class A_WP_Class
{
    public static function do_something_on_init()
    {
        // ...
    }
}

add_action('init', array('A_WP_Class', 'do_something_on_init'));
```

### Example 7

```php
namespace MyPlugin;

class Utilities
{
    /**
     * Check if the plugin is active
     *
     * @return bool
     */
    public static function is_plugin_active()
    {
        // ...
    }
}
```

### Example 8

```php
namespace MyPlugin;

class Plugin
{
    /**
     * Check if the plugin is active
     *
     * @return bool
     */
    public static function is_active()
    {
        // ...
    }
}
```

### Example 9

```php
namespace MyPlugin;

class Plugin
{
    /**
     * Flag to track if the plugin is active.
     *
     * @var bool
     */
    private $active;

    /**
     * Check if the plugin is active
     *
     * @return bool
     */
    public function is_active()
    {
        return $this->active;
    }
}
```

## Source

https://carlalexander.ca/static-keyword-wordpress/
