---
title: "Dependency inversion principle and WordPress
			

			

				So let’s talk about coupling! Coupling is a complicated problem because you can never get rid of it completely. All that you can do is control how much it spreads. And there’s more than one way to do that.
One of these ways is the dependency inversion principle. It’s one of the most important principles in object-oriented design. And it’s why it’s part of the famous SOLID design principles. (It’s the “D” in SOLID.)
The dependency inversion principle isn’t something that you see with WordPress. That’s because most WordPress developers don’t use object-oriented programming. (But it’s always a good time to start if you’re not using it!) And the dependency inversion principle only helps when you’ve been using it for a while.
But what makes the dependency inversion principle special? Why is it such almost a mandatory aspect of object-oriented design? These are good questions that you deserve an answer to.

What is the dependency inversion principle?"
url: https://carlalexander.ca/dependency-inversion-principle-wordpress/
slug: dependency-inversion-principle-wordpress
fetched: 2026-11-18
---

# Dependency inversion principle and WordPress
			

			

				So let’s talk about coupling! Coupling is a complicated problem because you can never get rid of it completely. All that you can do is control how much it spreads. And there’s more than one way to do that.
One of these ways is the dependency inversion principle. It’s one of the most important principles in object-oriented design. And it’s why it’s part of the famous SOLID design principles. (It’s the “D” in SOLID.)
The dependency inversion principle isn’t something that you see with WordPress. That’s because most WordPress developers don’t use object-oriented programming. (But it’s always a good time to start if you’re not using it!) And the dependency inversion principle only helps when you’ve been using it for a while.
But what makes the dependency inversion principle special? Why is it such almost a mandatory aspect of object-oriented design? These are good questions that you deserve an answer to.

What is the dependency inversion principle?

## Summary

Applying dependency inversion (high-level modules shouldn't depend on low-level modules). Creating abstractions and interfaces to decouple WordPress-specific code from domain logic.

## Code examples

### Example 1

```php
class MyPlugin_Plugin
{
    /**
     * MyPlugin admin page
     * 
     * @var MyPlugin_AdminPage
     */
    private $admin_page;
    
    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->admin_page = new MyPlugin_AdminPage();
    }

    // ...
}

class MyPlugin_AdminPage
{
    /**
     * MyPlugin options
     *
     * @var MyPlugin_Options
     */
    private $options;
    
    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->options = new MyPlugin_Options();
    }

    // ...
}

class MyPlugin_Options
{
    /**
     * MyPlugin options
     * 
     * @var array
     */
    private $options;

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->options = array();
    }

    // ...
}
```

### Example 2

```php
interface MyPlugin_OptionsInterface
{
    /**
     * Gets the option for the given name. Returns the default value if 
     * the value does not exist.
     *
     * @param string $name
     * @param mixed  $default
     *
     * @return mixed
     */
    public function get($name, $default = null);

    /**
     * Sets an option.
     *
     * @param string $name
     * @param mixed  $value
     */
    public function set($name, $value);
}
```

### Example 3

```php
class MyPlugin_Options implements MyPlugin_OptionsInterface
{
    /**
     * MyPlugin options
     *
     * @var array
     */
    private $options;

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->options = array();
    }

    /**
     * {@inheritdoc}
     */
    public function get($name, $default = null)
    {
        return isset($this->options[$name]) ? $this->options[$name] : $default;
    }

    /**
     * {@inheritdoc}
     */
    public function set($name, $value)
    {
        $this->options[$name] = $value;
    }

    // ...
}
```

### Example 4

```php
class MyPlugin_AdminPage
{
    /**
     * MyPlugin options
     *
     * @var MyPlugin_OptionsInterface
     */
    private $options;

    /**
     * Constructor.
     */
    public function __construct(MyPlugin_OptionsInterface $options)
    {
        $this->options = $options;
    }

    // ...
}
```

### Example 5

```php
class MyPlugin_Plugin
{
    /**
     * MyPlugin admin page
     *
     * @var MyPlugin_AdminPageInterface
     */
    private $admin_page;

    /**
     * Constructor.
     */
    public function __construct(MyPlugin_AdminPageInterface $admin_page)
    {
        $this->admin_page = $admin_page;
    }

    /**
     * Loads the plugin into WordPress.
     */
    public function load()
    {
        $this->admin_page->register();
    }

    // ...
}
$myplugin = new MyPlugin_Plugin($admin_page);
add_action('wp_loaded', array($myplugin, 'load'));
```

### Example 6

```php
interface MyPlugin_AdminPageInterface
{
    /**
     * Register the admin page with WordPress when WordPress loads.
     */
    public function register();
}
```

### Example 7

```php
class MyPlugin_AdminPage implements MyPlugin_AdminPageInterface
{
    // ...

    /**
     * Register the admin page with WordPress when WordPress loads.
     */
    public function register()
    {
    }

    // ...
}
```

### Example 8

```php
class MyPlugin_AdminPage implements MyPlugin_AdminPageInterface
{
    // ...

    /**
     * Display plugin admin page.
     */
    public function display_page()
    {
        // ...
    }

    /**
     * Register the admin page with WordPress when WordPress loads.
     */
    public function register()
    {
        add_menu_page('My Plugin Admin Page', 'My Plugin Admin Page', 'edit_posts', 'myplugin_admin_page', array($this, 'display_page'));
    }

    // ...
}
```

### Example 9

```php
class MyPlugin_AdminPage implements MyPlugin_AdminPageInterface
{
    // ...

    /**
     * Add admin page to WordPress admin menu.
     */
    public function add_page()
    {
        add_menu_page('My Plugin Admin Page', 'My Plugin Admin Page', 'edit_posts', 'myplugin_admin_page', array($this, 'display_page'));
    }

    /**
     * Display plugin admin page.
     */
    public function display_page()
    {
        // ...
    }

    /**
     * Register the admin page with WordPress when WordPress loads.
     */
    public function register()
    {
        add_action('admin_menu', array($this, 'add_page'));
    }

    // ...
}
```

## Source

https://carlalexander.ca/dependency-inversion-principle-wordpress/
