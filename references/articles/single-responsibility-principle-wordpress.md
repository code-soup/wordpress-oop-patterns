---
title: "Single responsibility principle, WordPress and You
			

			

				For WordPress developers, it can be hard to improve your PHP skills. You lack the resources or tutorials to drive home these concepts. This happened just a few weeks ago when Nathaniel asked for help with his Stack Overflow question.
He was looking for help applying the single responsibility principle with WordPress. I sent him a bunch of replies but closed off saying I needed to write a post about it. This article is a detailed explanation of my thoughts following that conversation.
As WordPress developer, you might have started working with or looking into object-oriented programming. Maybe you even heard of something called SOLID.
As a whole, SOLID can be an intimidating topic. But the single responsibility principle is just one part of it (it’s the ‘S’ in SOLID). That makes it a more manageable topic to discuss and help you with.
At the end of this article, you should have a better understanding of it. You can also use the provided code samples in your own plugins and themes.

Single Responsibility Principle explained"
url: https://carlalexander.ca/single-responsibility-principle-wordpress/
slug: single-responsibility-principle-wordpress
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/single-responsibility-principle-wordpress-you/
---

# Single responsibility principle, WordPress and You
			

			

				For WordPress developers, it can be hard to improve your PHP skills. You lack the resources or tutorials to drive home these concepts. This happened just a few weeks ago when Nathaniel asked for help with his Stack Overflow question.
He was looking for help applying the single responsibility principle with WordPress. I sent him a bunch of replies but closed off saying I needed to write a post about it. This article is a detailed explanation of my thoughts following that conversation.
As WordPress developer, you might have started working with or looking into object-oriented programming. Maybe you even heard of something called SOLID.
As a whole, SOLID can be an intimidating topic. But the single responsibility principle is just one part of it (it’s the ‘S’ in SOLID). That makes it a more manageable topic to discuss and help you with.
At the end of this article, you should have a better understanding of it. You can also use the provided code samples in your own plugins and themes.

Single Responsibility Principle explained

## Summary

Ensuring classes have one reason to change. Breaking down large WordPress classes into focused, single-purpose components.

## Code examples

### Example 1

```php
namespace WPMemeShortcode;

class Plugin
{
    /**
     * Loads the plugin into WordPress.
     */
    public static function load()
    {
        // ...
    }
}
```

### Example 2

```php
namespace WPMemeShortcode;

class Options
{
    /**
     * @var array
     */
    private $options;

    /**
     * Constructor.
     *
     * @param array $options
     */
    public function __construct(array $options = array())
    {
        $this->options = $options;
    }

    /**
     * Gets the option for the given name. Returns the default value if the
     * value does not exist.
     *
     * @param string $name
     * @param mixed  $default
     *
     * @return mixed
     */
    public function get($name, $default = null)
    {
        if (!$this->has($name)) {
            return $default;
        }

        return $this->options[$name];
    }

    /**
     * Checks if the option exists or not.
     *
     * @param string $name
     *
     * @return bool
     */
    public function has($name)
    {
        return isset($this->options[$name]);
    }

    /**
     * Sets an option. Overwrites the existing option if the name is already in use.
     *
     * @param string $name
     * @param mixed  $value
     */
    public function set($name, $value)
    {
        $this->options[$name] = $value;
    }
}
```

### Example 3

```php
namespace WPMemeShortcode;

class AdminPage
{
    /**
     * @var Options
     */
    private $options;

    /**
     * Constructor.
     *
     * @param Options $options
     */
    public function __construct(Options $options)
    {
        $this->options = $options;
    }

    /**
     * Adds the admin page to the menu.
     */
    public function addAdminPage()
    {
        add_options_page(__('WordPress Meme Shortcode', 'wp_meme_shortcode'), __('Meme Shortcode', 'wp_meme_shortcode'), 'install_plugins', 'wp_meme_shortcode', array($this, 'render'));
    }

    /**
     * Configure the option page using the settings API.
     */
    public function configure()
    {
        // Register settings
        register_setting('wp_meme_shortcode', 'wp_meme_shortcode');

        // General Section
        add_settings_section('wp_meme_shortcode_general', __('General', 'wp_meme_shortcode'), array($this, 'renderGeneralSection'), 'wp_meme_shortcode');
        add_settings_field('wp_meme_shortcode_size', __('Default Image Size', 'wp_meme_shortcode'), array($this, 'renderSizeField'), 'wp_meme_shortcode', 'wp_meme_shortcode_general');
    }

    /**
     * Renders the admin page using the Settings API.
     */
    public function render()
    {
        ?>
        <div class="wrap" id="wp-meme-shortcode-admin">
            <h2><?php _e('WordPress Meme Shortcode', 'wp_meme_shortcode'); ?></h2>
            <form action="options.php" method="POST">
                <?php settings_fields('wp_meme_shortcode'); ?>
                <?php do_settings_sections('wp_meme_shortcode'); ?>
                <?php submit_button(); ?>
            </form>
        </div>
        <?php
    }

    /**
     * Renders the general section.
     */
    public function renderGeneralSection()
    {
        ?>
        <p><?php _e('Configure WordPress Meme Shortcode.', 'wp_meme_shortcode'); ?></p>
        <?php
    }

    /**
     * Renders the size field.
     */
    public function renderSizeField()
    {
        ?>
        <input id="wp_meme_shortcode_size" name="wp_meme_shortcode[size]" type="number" value="<?php echo $this->options->get('size', '500'); ?>" />
        <?php
    }
}
```

### Example 4

```php
namespace WPMemeShortcode;

class Shortcode
{
    /**
     * @var Options
     */
    private $options;

    /**
     * Constructor.
     *
     * @param Options $options
     */
    public function __construct(Options $options)
    {
        $this->options = $options;
    }

    /**
     * Handles the output of the shortcode.
     *
     * @param array  $attributes
     * @param string $content
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
namespace WPMemeShortcode;

class AdminPage
{
    /**
     * Register the admin page class with all the appropriate WordPress hooks.
     *
     * @param Options $options
     */
    public static function register(Options $options)
    {
        $page = new self($options);

        add_action('admin_init', array($page, 'configure'));
        add_action('admin_menu', array($page, 'addAdminPage'));
    }

    // ...

}
```

### Example 6

```php
namespace WPMemeShortcode;

class Options
{
    /**
     * Load the plugin options from WordPress.
     *
     * @return Options
     */
    public static function load()
    {
        $options = get_option('wp_meme_shortcode', array());

        return new self($options);
    }

    // ...

}
```

## Source

https://carlalexander.ca/single-responsibility-principle-wordpress/
