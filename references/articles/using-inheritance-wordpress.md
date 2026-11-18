---
title: "Using inheritance with WordPress
			

			

				As a WordPress developer, you’re always looking for ways to better reuse your code between projects. Your time is valuable and you don’t want to reinvent the wheel each time you start a new project.
Object-oriented programming can help you with that. In a previous post, I covered why you should learn it. Now it’s time to take things further by going over the main feature for code reuse. You’ve probably heard about it before. It’s called “inheritance“.

Inheritance, what’s that?"
url: https://carlalexander.ca/using-inheritance-wordpress/
slug: using-inheritance-wordpress
fetched: 2026-11-18
---

# Using inheritance with WordPress
			

			

				As a WordPress developer, you’re always looking for ways to better reuse your code between projects. Your time is valuable and you don’t want to reinvent the wheel each time you start a new project.
Object-oriented programming can help you with that. In a previous post, I covered why you should learn it. Now it’s time to take things further by going over the main feature for code reuse. You’ve probably heard about it before. It’s called “inheritance“.

Inheritance, what’s that?

## Summary

Class inheritance patterns in WordPress. Extending classes, overriding methods, and parent-child relationships.

## Code examples

### Example 1

```php
interface Post_Interface
{
    /**
     * Get the CSS class.
     *
     * @return string
     */
    public function get_class();

    /**
     * Get the post type.
     *
     * @return string
     */
    public function get_type();
}
```

### Example 2

```php
class Posts implements Countable
{
    /**
     * @var Post_Interface[]
     */
    protected $posts;

    // ...

    public function count()
    {
        return count($this->posts);
    }
}

$posts = new Posts();

$num_posts = count($posts);
```

### Example 3

```php
class Posts implements IteratorAggregate
{
    /**
     * @var array
     */
    protected $posts;

    // ...

    public function getIterator()
    {
        return new ArrayIterator($this->posts);
    }
}

$posts = new Posts();

foreach ($posts as $post) {
    // Do stuff
}
```

### Example 4

```php
class Posts implements Countable, IteratorAggregate
{
    /**
     * @var array
     */
    protected $posts;

    // ...

    public function count()
    {
        return count($this->posts);
    }

    public function getIterator()
    {
        return new ArrayIterator($this->posts);
    }
}
```

### Example 5

```php
abstract class Abstract_Post implements Post_Interface
{
    /**
     * @var int
     */
    protected $id;

    /**
     * Get the CSS class.
     *
     * @return type
     */
    public function get_class()
    {
        return $this->get_type() . '-' . $this->id;
    }

    abstract public function get_type();
}
```

### Example 6

```php
class Attachment extends Abstract_Post
{
    /**
     * Get the post type.
     *
     * @return string
     */
    public function get_type()
    {
        return 'attachment';
    }
}

$attachment = new Attachment();

$attachment->get_class();
```

### Example 7

```php
class Video extends Attachment
{
    /**
     * Get the post type.
     *
     * @return string
     */
    public function get_type()
    {
        return 'video';
    }
}
```

### Example 8

```php
class Picture extends Attachment
{
    /**
     * Get the post type.
     *
     * @return string
     */
    public function get_type()
    {
        return 'picture-' . parent::get_type();
    }
}
```

### Example 9

```php
/**
 * Save post to the database.
 *
 * @param WP_Post_Interface $post
 */
function save_post(WP_Post_Interface $post)
{
    // You are sure $post implements WP_Post_Interface
}
```

### Example 10

```php
/**
 * Save post to the database.
 *
 * @param mixed $post
 */
function save_post($post)
{
    // You are not sure $post implements WP_Post_Interface
    
    if (!$post instanceof WP_Post_Interface) {
        return;
    }
    
    // You are sure $post implements WP_Post_Interface
}
```

### Example 11

```php
class WP_Test_Widget extends WP_Widget
{
    public function widget($args, $instance)
    {
        echo 'test';
    }
}
```

### Example 12

```php
interface WP_Widget_Interface
{
    /**
     * Register the widget.
     */
    public function register();

    /**
     * Echo the widget content.
     *
     * @param array $args
     * @param array $instance
     */
    public function widget($args, $instance);
}
```

### Example 13

```php
abstract class Abstract_WP_Widget implements WP_Widget_Interface
{
    /**
     * @var array 
     */
    protected $widget_options;
    /**
     * @var string 
     */
    protected $id_base;
    /**
     * @var string 
     */
    protected $name;
    /**
     * @var array 
     */
    protected $control_options;
    /**
     * @var bool 
     */
    protected $number = false;
    /**
     * @var bool
     */
    protected $id = false;
    /**
     * @var bool 
     */
    protected $updated = false;

    /**
     * Constructor
     *
     * @param type $id_base
     * @param type $name
     * @param type $widget_options
     * @param type $control_options
     */
    public function __construct( $id_base, $name, $widget_options = array(), $control_options = array() )
    {
    }

    /**
     * {@inheritdoc}
     */
    final public function register()
    {
    }

    /**
     * Generate the actual widget content.
     */
    final public function display_callback($args, $widget_args = 1)
    {
    }

    /**
     * Generate the control form.
     */
    final public function form_callback($widget_args = 1)
    {
    }

    /**
     * Deal with changed settings.
     *
     * @param mixed $deprecated Not used.
     */
    final public function update_callback($deprecated = 1)
    {
    }

    /**
     * Echo the settings update form.
     *
     * @param array $instance Current settings
     */
    protected function form($instance)
    {
    }

    /**
     * Constructs name attributes for use in form() fields.
     *
     * @param string $field_name
     * 
     * @return string
     */
    protected function get_field_name($field_name) {
    }

    /**
     * Constructs id attributes for use in form() fields.
     *
     * @param string $field_name
     * 
     * @return string
     */
    protected function get_field_id($field_name) {
    }

    /**
     * Update a widget instance.
     *
     * @param array $new_instance
     * @param array $old_instance
     *
     * @return array
     */
    protected function update($new_instance, $old_instance)
    {
    }
}
```

### Example 14

```php
function the_widget($widget, $instance = array(), $args = array()) {
    global $wp_widget_factory;

    $widget_obj = $wp_widget_factory->widgets[$widget];
    if ( !is_a($widget_obj, 'WP_Widget_Interface') )
        return;
    
    // ...
    
    $widget_obj->widget($args, $instance);
}
```

### Example 15

```php
class WP_Widget_Factory {
    var $widgets = array();

    function register($widget_class) {
        $widget_obj = new $widget_class();

        if ( !is_a($widget_obj, 'WP_Widget_Interface') )
            return;

        $this->widgets[$widget_class] = $widget_obj;
    }

    // ...
}
```

## Source

https://carlalexander.ca/using-inheritance-wordpress/
