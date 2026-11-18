---
title: "Coupling and cohesion in WordPress and beyond
			

			

				A concept that comes up a lot while doing object-oriented design is coupling. We use it to describe how connected the different parts of your code are to one another. But, even explained like that, the concept of coupling can still be a hard to grasp.
On top of that, we often pair it with another concept called cohesion. We use cohesion to describe how well the different parts of your code fit together. This tells us whether everything was well-designed or not.
In fact, this is why coupling and cohesion are so important. There’s a strong relationship between them and the quality of your code. Code that doesn’t have any major coupling or cohesion problem is more often of higher quality. It’s more maintainable, reusable and less prone to problems.
That’s why you want to keep these two concepts in the back of your mind when programming. But that’s easier said than done when these concepts aren’t well understood. That’s why we’ll demystify them today.

Defining coupling and cohesion"
url: https://carlalexander.ca/coupling-cohesion-wordpress/
slug: coupling-cohesion-wordpress
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/coupling-cohesion-wordpress-beyond/
---

# Coupling and cohesion in WordPress and beyond
			

			

				A concept that comes up a lot while doing object-oriented design is coupling. We use it to describe how connected the different parts of your code are to one another. But, even explained like that, the concept of coupling can still be a hard to grasp.
On top of that, we often pair it with another concept called cohesion. We use cohesion to describe how well the different parts of your code fit together. This tells us whether everything was well-designed or not.
In fact, this is why coupling and cohesion are so important. There’s a strong relationship between them and the quality of your code. Code that doesn’t have any major coupling or cohesion problem is more often of higher quality. It’s more maintainable, reusable and less prone to problems.
That’s why you want to keep these two concepts in the back of your mind when programming. But that’s easier said than done when these concepts aren’t well understood. That’s why we’ll demystify them today.

Defining coupling and cohesion

## Summary

Understanding and managing coupling between WordPress components. Increasing cohesion within classes while reducing coupling between them.

## Code examples

### Example 1

```php
class MyPlugin_Utilities
{
    /**
     * Check if the plugin is active.
     *
     * @return bool
     */
    public function is_plugin_active()
    {
        // ...
    }

    /**
     * Get the name of the web server running PHP.
     *
     * @return string
     */
    public function get_web_server() 
    {
        // ...
    }
}
```

### Example 2

```php
/**
 * Search for posts with the given title.
 * 
 * @param string $title
 * @param int $limit
 *
 * @return array|null
 */
function my_plugin_search_posts_by_title($title, $limit = 5)
{
    global $wpdb;

    return $wpdb->get_results("SELECT * FROM {$wpdb->posts} WHERE post_title LIKE '%$title%' LIMIT $limit");
}
```

### Example 3

```php
/**
 * Get the global wpdb object.
 *
 * @return wpdb|WP_Error
 */
function my_plugin_get_wpdb()
{
    global $wpdb;

    return $wpdb;
}

/**
 * Search for posts with the given title.
 *
 * @param string $title
 * @param int $limit
 *
 * @return array|null
 */
function my_plugin_search_posts_by_title($title, $limit = 5)
{
    $wpdb = my_plugin_get_wpdb();

    return $wpdb->get_results("SELECT * FROM {$wpdb->posts} WHERE post_title LIKE '%$title%' LIMIT $limit");
}
```

### Example 4

```php
class WPMemeShortcode_Shortcode
{
    /**
     * @var WPMemeShortcode_Options
     */
    private $options;
 
    /**
     * Constructor.
     *
     * @param WPMemeShortcode_Options $options
     */
    public function __construct(WPMemeShortcode_Options $options)
    {
        $this->options = $options;
    }
 
    /**
     * Handles the output of the shortcode.
     *
     * @param array  $attributes
     * @param string $content
     *
     * @return string
     */
    public function handle(array $attributes, $content = null)
    {
        // Do nothing if no ID is given or it is not numeric
        if (!isset($attributes['id']) || !is_numeric($attributes['id'])) {
            return $content;
        }
 
        // If no size is given or it is not a numeric value, get default.
        if (!isset($attributes['size']) || !is_numeric($attributes['size'])) {
            $attributes['size'] = $this->options->get('size', '500');
        }
 
        return "<img src=\"http://cdn.memegenerator.net/instances/{$attributes['size']}x/{$attributes['id']}.jpg\" />";
    }
}
```

### Example 5

```php
class WPMemeShortcode_Shortcode
{
    /**
     * @var int
     */
    private $default_size;

    /**
     * Constructor.
     *
     * @param int $default_size
     */
    public function __construct($default_size)
    {
        $this->default_size = $default_size;
    }

    /**
     * Handles the output of the shortcode.
     *
     * @param array  $attributes
     * @param string $content
     *
     * @return string
     */
    public function handle(array $attributes, $content = null)
    {
        // Do nothing if no ID is given or it is not numeric
        if (!isset($attributes['id']) || !is_numeric($attributes['id'])) {
            return $content;
        }

        // If no size is given or it is not a numeric value, get default.
        if (!isset($attributes['size']) || !is_numeric($attributes['size'])) {
            $attributes['size'] = $this->default_size;
        }

        return "<img src=\"http://cdn.memegenerator.net/instances/{$attributes['size']}x/{$attributes['id']}.jpg\" />";
    }
}
```

### Example 6

```php
class MyPlugin_Base
{
    protected $variable;

    /**
     * Constructor.
     *
     * @param $variable
     */
    public function __construct($variable)
    {
        $this->variable = filter_var($variable, FILTER_SANITIZE_ENCODED);
    }

    /**
     * Get the variable.
     *
     * @return mixed
     */
    public function get_variable()
    {
        return $this->variable;
    }
}
```

### Example 7

```php
class MyPlugin_Derived extends MyPlugin_Base
{
    /**
     * Set the variable.
     *
     * @param $variable
     */
    public function set_variable($variable)
    {
        $this->variable = $variable;
    }
}
```

### Example 8

```php
class MyPlugin_Base
{
    private $variable;

    /**
     * Constructor.
     *
     * @param $variable
     */
    public function __construct($variable)
    {
        $this->variable = filter_var($variable, FILTER_SANITIZE_ENCODED);
    }

    /**
     * Get the variable.
     *
     * @return mixed
     */
    public function get_variable()
    {
        return $this->variable;
    }
}
```

### Example 9

```php
class MyPlugin_Derived extends MyPlugin_Base
{
    protected $derived_variable;

    /**
     * Constructor.
     *
     * @param $variable
     */
    public function __construct($variable)
    {
        parent::__construct($variable);
        
        $this->derived_variable = $variable;
    }

    /**
     * Get the variable.
     *
     * @return mixed
     */
    public function get_variable()
    {
        return $this->derived_variable;
    }

    /**
     * Set the variable.
     *
     * @param $variable
     */
    public function set_variable($variable)
    {
        $this->derived_variable = $variable;
    }
}
```

### Example 10

```php
class MyPlugin_Base
{
    private $variable;

    /**
     * Constructor.
     *
     * @param $variable
     */
    public function __construct($variable)
    {
        $this->variable = filter_var($variable, FILTER_SANITIZE_ENCODED);
    }

    /**
     * Get the variable.
     *
     * @return mixed
     */
    final public function get_variable()
    {
        return $this->variable;
    }
}
```

### Example 11

```php
interface MyPlugin_BaseInterface
{
    /**
     * Get the variable.
     *
     * @return mixed
     */
    public function get_variable();
}
```

### Example 12

```php
class MyPlugin_Base implements MyPlugin_BaseInterface
{
    protected $variable;

    /**
     * Constructor.
     *
     * @param $variable
     */
    public function __construct($variable)
    {
        $this->variable = filter_var($variable, FILTER_SANITIZE_ENCODED);
    }

    /**
     * Get the variable.
     *
     * @return mixed
     */
    public function get_variable()
    {
        return $this->variable;
    }
}
```

### Example 13

```php
/**
 * Get the variable of a MyPlugin_Base object.
 *
 * @param MyPlugin_Base $base
 * 
 * @return mixed
 */
function my_plugin_get_base_variable(MyPlugin_Base $base)
{
    $variable = $base->get_variable();
    
    // Do something with $variable
    
    return $variable;
}
```

### Example 14

```php
/**
 * Get the variable of a MyPlugin_Base object.
 *
 * @param MyPlugin_BaseInterface $base
 * 
 * @return mixed
 */
function my_plugin_get_base_variable(MyPlugin_BaseInterface $base)
{
    $variable = $base->get_variable();
    
    // Do something with $variable
    
    return $variable;
}
```

## Source

https://carlalexander.ca/coupling-cohesion-wordpress/
