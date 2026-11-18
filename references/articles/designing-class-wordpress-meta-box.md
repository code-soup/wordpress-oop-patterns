---
title: "Designing a class to represent a WordPress meta box
			

			

				In a previous article, we discussed how to design a class representing a WordPress admin page. This was important because almost every plugin or theme needs an admin page. But this isn’t the only common thing that plugins or themes add to the WordPress admin.
Another one of those is the meta box. If you’re not familiar with meta boxes, they’re the draggable boxes that you see on the post editing screen. It’s quite common for plugins and themes to add post-specific functionality through them.
This makes them a good topic to discuss with object-oriented programming. (Is there really a bad topic to discuss with object-oriented programming!?) And, as we’ll see, meta boxes have a lot of in common with admin pages. This means that designing a class to represent them will be a lot like what we did for admin pages.

What makes a meta box?"
url: https://carlalexander.ca/designing-class-wordpress-meta-box/
slug: designing-class-wordpress-meta-box
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/designing-class-represent-wordpress-meta-box/
---

# Designing a class to represent a WordPress meta box
			

			

				In a previous article, we discussed how to design a class representing a WordPress admin page. This was important because almost every plugin or theme needs an admin page. But this isn’t the only common thing that plugins or themes add to the WordPress admin.
Another one of those is the meta box. If you’re not familiar with meta boxes, they’re the draggable boxes that you see on the post editing screen. It’s quite common for plugins and themes to add post-specific functionality through them.
This makes them a good topic to discuss with object-oriented programming. (Is there really a bad topic to discuss with object-oriented programming!?) And, as we’ll see, meta boxes have a lot of in common with admin pages. This means that designing a class to represent them will be a lot like what we did for admin pages.

What makes a meta box?

## Summary

Encapsulating metabox logic in classes. Registration, rendering, and saving metabox data using OOP.

## Code examples

### Example 1

```php
class MyPlugin_MetaBox
{
}
```

### Example 2

```php
class MyPlugin_MetaBox
{
    // ...
 
    /**
     * Get the arguments for the "add_meta_box" function.
     *
     * @return array
     */
    public function get_meta_box_arguments()
    {
        return array(
            'meta-box-id',
            'Meta Box Title',
            array($this, 'render_meta_box'),
        );
    }
}
```

### Example 3

```php
function myplugin_add_meta_box() {
    $meta_box = new MyPlugin_MetaBox();
 
    call_user_func_array('add_meta_box', $meta_box->get_meta_box_arguments());
}
add_action('add_meta_boxes', 'myplugin_add_meta_box');
```

### Example 4

```php
function myplugin_add_meta_box() {
    $meta_box = new MyPlugin_MetaBox();
 
    add_meta_box($meta_box->get_id(), $meta_box->get_title(), $meta_box->get_callback(), $meta_box->get_screens(), $meta_box->get_context(), $meta_box->get_priority());
}
add_action('add_meta_boxes', 'myplugin_add_meta_box');
```

### Example 5

```php
class MyPlugin_MetaBox
{
    /**
     * Get the callable that will the content of the meta box.
     *
     * @return callable
     */
    public function get_callback()
    {
        return array($this, 'render_meta_box');
    }

    /**
     * Get the screen context where the meta box should display.
     *
     * @return string
     */
    public function get_context()
    {
        return 'advanced';
    }

    /**
     * Get the ID of the meta box.
     *
     * @return string
     */
    public function get_id()
    {
        return 'meta-box-id';
    }

    /**
     * Get the display priority of the meta box.
     *
     * @return string
     */
    public function get_priority()
    {
        return 'default';
    }

    /**
     * Get the screen(s) where the meta box will appear.
     *
     * @return array|string|WP_Screen
     */
    public function get_screens()
    {
        return null;
    }

    /**
     * Get the title of the meta box.
     *
     * @return string
     */
    public function get_title()
    {
        return 'Meta Box Title';
    }
}
```

### Example 6

```php
class MyPlugin_MetaBox
{
    /**
     * Screen context where the meta box should display.
     *
     * @var string
     */
    private $context;

    /**
     * The ID of the meta box.
     *
     * @var string
     */
    private $id;

    /**
     * The display priority of the meta box.
     *
     * @var string
     */
    private $priority;

    /**
     * Screens where this meta box will appear.
     *
     * @var string[]
     */
    private $screens;

    /**
     * The title of the meta box.
     *
     * @var string
     */
    private $title;

    /**
     * Constructor.
     *
     * @param string   $id
     * @param string   $title
     * @param string   $context
     * @param string   $priority
     * @param string[] $screens
     */
    public function __construct($id, $title, $context = 'advanced', $priority = 'default', $screens = array())
    {
        if (is_string($screens)) {
            $screens = (array) $screens;
        }

        $this->context = $context;
        $this->id = $id;
        $this->priority = $priority;
        $this->screens = $screens;
        $this->title = $title;
    }

    /**
     * Get the screen context where the meta box should display.
     *
     * @return string
     */
    public function get_context()
    {
        return $this->context;
    }

    /**
     * Get the ID of the meta box.
     *
     * @return string
     */
    public function get_id()
    {
        return $this->id;
    }

    /**
     * Get the display priority of the meta box.
     *
     * @return string
     */
    public function get_priority()
    {
        return $this->priority;
    }

    /**
     * Get the screen(s) where the meta box will appear.
     *
     * @return array|string|WP_Screen
     */
    public function get_screens()
    {
        return $this->screens;
    }

    /**
     * Get the title of the meta box.
     *
     * @return string
     */
    public function get_title()
    {
        return $this->title;
    }
}
```

### Example 7

```php
class MyPlugin_MetaBox
{
    // ...

    /**
     * Get the callable that will the content of the meta box.
     *
     * @return callable
     */
    public function get_callback()
    {
        return array($this, 'render');
    }

    // ...

    /**
     * Render the content of the meta box.
     *
     * @param WP_Post $post
     */
    public function render(WP_Post $post)
    {
        ?>
        <p>Post title: <?php echo $post->post_title; ?></p>
        <?php
    }
}
```

### Example 8

```php
abstract class MyPlugin_MetaBox
{
    // ...

    /**
     * Get the callable that will the content of the meta box.
     *
     * @return callable
     */
    public function get_callback()
    {
        return array($this, 'render');
    }

    // ...

    /**
     * Render the content of the meta box.
     *
     * @param WP_Post $post
     */
    abstract public function render(WP_Post $post);
}
```

### Example 9

```php
class MyPlugin_PostTitleMetaBox extends MyPlugin_MetaBox
{
    /**
     * Render the content of the meta box.
     *
     * @param WP_Post $post
     */
    public function render(WP_Post $post)
    {
        ?>
        <p>Post title: <?php echo $post->post_title; ?></p>
        <?php
    }
}
```

### Example 10

```php
class MyPlugin_MetaBox
{
    /**
     * Screen context where the meta box should display.
     *
     * @var string
     */
    private $context;

    /**
     * The ID of the meta box.
     *
     * @var string
     */
    private $id;

    /**
     * The display priority of the meta box.
     *
     * @var string
     */
    private $priority;

    /**
     * Screens where this meta box will appear.
     *
     * @var string[]
     */
    private $screens;

    /**
     * Path to the template used to display the content of the meta box.
     *
     * @var string
     */
    private $template;

    /**
     * The title of the meta box.
     *
     * @var string
     */
    private $title;

    /**
     * Constructor.
     *
     * @param string   $id
     * @param string   $emplate
     * @param string   $title
     * @param string   $context
     * @param string   $priority
     * @param string[] $screens
     */
    public function __construct($id, $template, $title, $context = 'advanced', $priority = 'default', $screens = array())
    {
        if (is_string($screens)) {
            $screens = (array) $screens;
        }

        $this->context = $context;
        $this->id = $id;
        $this->priority = $priority;
        $this->screens = $screens;
        $this->template = rtrim($template, '/');
        $this->title = $title;
    }

    // ...
}
```

### Example 11

```php
class MyPlugin_MetaBox
{
    // ...

    /**
     * Render the content of the meta box using a PHP template.
     *
     * @param WP_Post $post
     */
    public function render(WP_Post $post)
    {
        if (!is_readable($this->template)) {
           return;
        }

        include $this->template;
    }
}
```

### Example 12

```php
<p>Post title: <?php echo $post->post_title; ?></p>
```

### Example 13

```php
/**
 * A WordPress meta box that appears in the editor.
 */
class MyPlugin_MetaBox
{
    /**
     * Screen context where the meta box should display.
     *
     * @var string
     */
    private $context;

    /**
     * The ID of the meta box.
     *
     * @var string
     */
    private $id;

    /**
     * The display priority of the meta box.
     *
     * @var string
     */
    private $priority;

    /**
     * Screens where this meta box will appear.
     *
     * @var string[]
     */
    private $screens;

    /**
     * Path to the template used to display the content of the meta box.
     *
     * @var string
     */
    private $template;

    /**
     * The title of the meta box.
     *
     * @var string
     */
    private $title;

    /**
     * Constructor.
     *
     * @param string   $id
     * @param string   $emplate
     * @param string   $title
     * @param string   $context
     * @param string   $priority
     * @param string[] $screens
     */
    public function __construct($id, $template, $title, $context = 'advanced', $priority = 'default', $screens = array())
    {
        if (is_string($screens)) {
            $screens = (array) $screens;
        }

        $this->context = $context;
        $this->id = $id;
        $this->priority = $priority;
        $this->screens = $screens;
        $this->template = rtrim($template, '/');
        $this->title = $title;
    }

    /**
     * Get the callable that will the content of the meta box.
     *
     * @return callable
     */
    public function get_callback()
    {
        return array($this, 'render');
    }

    /**
     * Get the screen context where the meta box should display.
     *
     * @return string
     */
    public function get_context()
    {
        return $this->context;
    }

    /**
     * Get the ID of the meta box.
     *
     * @return string
     */
    public function get_id()
    {
        return $this->id;
    }

    /**
     * Get the display priority of the meta box.
     *
     * @return string
     */
    public function get_priority()
    {
        return $this->priority;
    }

    /**
     * Get the screen(s) where the meta box will appear.
     *
     * @return array|string|WP_Screen
     */
    public function get_screens()
    {
        return $this->screens;
    }

    /**
     * Get the title of the meta box.
     *
     * @return string
     */
    public function get_title()
    {
        return $this->title;
    }

    /**
     * Render the content of the meta box using a PHP template.
     *
     * @param WP_Post $post
     */
    public function render(WP_Post $post)
    {
        if (!is_readable($this->template)) {
            return;
        }

        include $this->template;
    }
}
```

## Source

https://carlalexander.ca/designing-class-wordpress-meta-box/
