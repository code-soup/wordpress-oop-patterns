---
title: "Polymorphism and WordPress: Abstract classes
			

			

				When we covered inheritance, there were some questions about interfaces and abstract classes.

What can you use them for?
What are the advantages?
When should you use them?

These are all great questions that are worth exploring. As the title suggests, “Polymorphism” is the object-oriented feature that helps answer these questions. It’s not an easy feature to grasp.
That’s why most of the article will be about an in-depth example. You’ll see the thought process involved with using it. This will help you understand it better so you can apply it to your own projects.

Many forms. Such polymorphism. Wow."
url: https://carlalexander.ca/polymorphism-wordpress-abstract-classes/
slug: polymorphism-wordpress-abstract-classes
fetched: 2026-11-18
---

# Polymorphism and WordPress: Abstract classes
			

			

				When we covered inheritance, there were some questions about interfaces and abstract classes.

What can you use them for?
What are the advantages?
When should you use them?

These are all great questions that are worth exploring. As the title suggests, “Polymorphism” is the object-oriented feature that helps answer these questions. It’s not an easy feature to grasp.
That’s why most of the article will be about an in-depth example. You’ll see the thought process involved with using it. This will help you understand it better so you can apply it to your own projects.

Many forms. Such polymorphism. Wow.

## Summary

Abstract classes for code reuse. Creating base classes with common functionality while enforcing implementation requirements.

## Code examples

### Example 1

```php
namespace MyPlugin;

/**
 * Shortcode page.
 *
 * @author Carl Alexander
 */
class ShortcodePage
{
    /**
     * My plugin options.
     *
     * @var array
     */
    private $options;

    /**
     * Register the shortcode page with all the appropriate WordPress hooks.
     */
    public static function register()
    {
        $page = new self(get_option('my_plugin_options', array()));

        add_action('admin_init', array($page, 'configure'));
        add_action('admin_menu', array($page, 'add_admin_page'));
    }

    /**
     * Constructor.
     *
     * @param array $options
     */
    public function __construct(array $options)
    {
        $this->options = $options;
    }

    /**
     * Adds the shortcode page to the menu.
     */
    public function add_admin_page()
    {
        add_options_page(__('My Plugin Shortcodes', 'my_plugin'), __('My Plugin Shortcodes', 'my_plugin'), 'install_plugins', 'my_plugin_shortcode', array($this, 'render'));
    }

    /**
     * Configure the shortcode page.
     */
    public function configure()
    {
        // Register settings
        register_setting('my_plugin_shortcode', 'my_plugin_options');

        // General Section
        add_settings_section('my_plugin_shortcode', __('Shortcodes', 'my_plugin'), array($this, 'render_section'), 'my_plugin_shortcode');
        add_settings_field('my_plugin_shortcode_title', __('Shortcode Title', 'my_plugin'), array($this, 'render_shortcode_field'), 'my_plugin_shortcode', 'my_plugin_shortcode');
    }

    /**
     * Renders the shortcode page.
     */
    public function render()
    {
        ?>
        <div class="wrap" id="my-plugin-shortcodes">
            <h1><?php echo __('My Plugin Shortcodes', 'my_plugin') ?></h1>
            <form action="options.php" method="POST">
                <?php settings_fields('my_plugin_shortcode'); ?>
                <?php do_settings_sections('my_plugin_shortcode'); ?>
                <?php submit_button(); ?>
            </form>
        </div>
        <?php
    }

    /**
     * Renders the section.
     */
    public function render_section()
    {
        ?>
        <p><?php _e('Configure MyPlugin shortcodes.', 'my_plugin'); ?></p>
        <?php
    }

    /**
     * Renders the shortcode field.
     */
    public function render_shortcode_field()
    {
        ?>
        <input id="my_plugin_shortcode" name="my_plugin_options[shortcode]" type="text" value="<?php echo $this->options['shortcode']; ?>" />
        <?php
    }
}

/**
 * Options page.
 *
 * @author Carl Alexander
 */
class OptionPage
{
    /**
     * My plugin options.
     *
     * @var array
     */
    private $options;

    /**
     * Register the options page with all the appropriate WordPress hooks.
     */
    public static function register()
    {
        $page = new self(get_option('my_plugin_options', array()));

        add_action('admin_init', array($page, 'configure'));
        add_action('admin_menu', array($page, 'add_admin_page'));
    }

    /**
     * Constructor.
     *
     * @param array $options
     */
    public function __construct(array $options)
    {
        $this->options = $options;
    }

    /**
     * Adds the shortcode page to the menu.
     */
    public function add_admin_page()
    {
        add_options_page(__('My Plugin Options', 'my_plugin'), __('My Plugin Options', 'my_plugin'), 'install_plugins', 'my_plugin_shortcode', array($this, 'render'));
    }

    /**
     * Configure the options page.
     */
    public function configure()
    {
        // Register settings
        register_setting('my_plugin_options', 'my_plugin_options');

        // General Section
        add_settings_section('my_plugin_options', __('Options', 'my_plugin'), array($this, 'render_section'), 'my_plugin_options');
        add_settings_field('my_plugin_options_color', __('Custom color', 'my_plugin'), array($this, 'render_color_field'), 'my_plugin_options', 'my_plugin_options');
    }

    /**
     * Render the options page.
     */
    public function render()
    {
        ?>
        <div class="wrap" id="my-plugin-options">
            <h1><?php echo __('My Plugin Options', 'my_plugin') ?></h1>
            <p>I want some introduction paragraph about my plugin here.</p>
            <form action="options.php" method="POST">
                <?php settings_fields('my_plugin_options'); ?>
                <?php do_settings_sections('my_plugin_options'); ?>
                <?php submit_button(); ?>
            </form>
        </div>
        <?php
    }

    /**
     * Renders the section.
     */
    public function render_section()
    {
        ?>
        <p><?php _e('Customize MyPlugin with these options', 'my_plugin'); ?></p>
        <?php
    }

    /**
     * Renders the color field.
     */
    public function render_color_field()
    {
        ?>
        <input id="my_plugin_color" name="my_plugin_options[color]" type="color" value="<?php echo $this->options['color']; ?>" />
        <?php
    }
}
```

### Example 2

```php
namespace MyPlugin;

/**
 * Base class for all WordPress admin pages.
 *
 * @author Carl Alexander
 */
abstract class AbstractAdminPage
{
    /**
     * My plugin options.
     *
     * @var array
     */
    protected $options;

    /**
     * Register the admin page with all the appropriate WordPress hooks.
     */
    public static function register()
    {
        $page = new static(get_option('my_plugin_options', array()));

        add_action('admin_init', array($page, 'configure'));
        add_action('admin_menu', array($page, 'add_admin_page'));
    }

    /**
     * Constructor.
     *
     * @param array $options
     */
    public function __construct(array $options)
    {
        $this->options = $options;
    }

    /**
     * Adds the admin page to the menu.
     */
    public function add_admin_page()
    {
        add_options_page($this->get_page_title(), $this->get_page_title(), 'install_plugins', $this->get_menu_slug(), array($this, 'render'));
    }

    /**
     * Configure the admin page using the settings API.
     */
    abstract public function configure();

    /**
     * Renders the admin page.
     */
    abstract public function render();

    /**
     * Render a form field.
     *
     * @param string $id
     * @param string $name
     * @param string $value
     * @param string $type
     */
    protected function render_form_field($id, $name, $value = '', $type = 'text')
    {
        ?>
        <input id="<?php echo $id; ?>" name="<?php echo $name; ?>" type="<?php echo $type; ?>" value="<?php echo $value; ?>" />
        <?php
    }

    /**
     * Get the admin page menu slug.
     *
     * @return string
     */
    abstract protected function get_menu_slug();

    /**
     * Get the admin page title.
     *
     * @return string
     */
    abstract protected function get_page_title();
}
```

### Example 3

```php
namespace MyPlugin;

/**
 * Base class for all WordPress admin pages.
 *
 * @author Carl Alexander
 */
abstract class AbstractAdminPage
{
    /**
     * Register the admin page with all the appropriate WordPress hooks.
     */
    public static function register($page = null)
    {
        // If we didn't receive an initiated child class, instantiate one.
        if (null === $page) {
            $page = new static();
        }

        add_action('admin_init', array($page, 'configure'));
        add_action('admin_menu', array($page, 'add_admin_page'));
    }

    // ...
}

/**
 * A WordPress admin page using overloading.
 *
 * @author Carl Alexander
 */
class AdminPage extends AbstractAdminPage
{
    /**
     * My plugin options.
     *
     * @var array
     */
    private $options;

    /**
     * Register the admin page with all the appropriate WordPress hooks.
     */
    public static function register()
    {
        // Create an instance of the admin page with the options
        $page = new self(get_option('my_plugin_options', array()));

        // Pass it up to the main register function
        parent::register($page);
    }

    /**
     * Constructor.
     *
     * @param array $options
     */
    public function __construct(array $options)
    {
        $this->options = $options;
    }
    
    // ...
}
```

### Example 4

```php
namespace MyPlugin;

/**
 * Shortcode page.
 *
 * @author Carl Alexander
 */
class ShortcodePage extends AbstractAdminPage
{
    /**
     * Configure the shortcode page.
     */
    public function configure()
    {
        // Register settings
        register_setting($this->get_menu_slug(), 'my_plugin_options');

        // General Section
        add_settings_section('my_plugin_shortcode', __('Shortcodes', 'my_plugin'), array($this, 'render_section'), $this->get_menu_slug());
        add_settings_field('my_plugin_shortcode_title', __('Shortcode Title', 'my_plugin'), array($this, 'render_shortcode_field'), $this->get_menu_slug(), 'my_plugin_shortcode');
    }

    /**
     * Renders the shortcode page.
     */
    public function render()
    {
        ?>
        <div class="wrap" id="my-plugin-shortcodes">
            <h1><?php echo $this->get_page_title() ?></h1>
            <form action="options.php" method="POST">
                <?php settings_fields($this->get_menu_slug()); ?>
                <?php do_settings_sections($this->get_menu_slug()); ?>
                <?php submit_button(); ?>
            </form>
        </div>
        <?php
    }

    /**
     * Renders the section.
     */
    public function render_section()
    {
        ?>
        <p><?php _e('Configure MyPlugin shortcodes.', 'my_plugin'); ?></p>
        <?php
    }

    /**
     * Renders the shortcode field.
     */
    public function render_shortcode_field()
    {
        $this->render_form_field('my_plugin_shortcode', 'my_plugin_options[shortcode]', $this->options['shortcode']);
    }

    /**
     * Get the shortcode page menu slug.
     *
     * @return string
     */
    protected function get_menu_slug()
    {
        return 'my_plugin_shortcode';
    }

    /**
     * Get the shortcode page title.
     *
     * @return string
     */
    protected function get_page_title()
    {
        return __('My Plugin Shortcodes', 'my_plugin');
    }
}

/**
 * Options page.
 *
 * @author Carl Alexander
 */
class OptionPage extends AbstractAdminPage
{
    /**
     * Configure the options page.
     */
    public function configure()
    {
        // Register settings
        register_setting($this->get_menu_slug(), 'my_plugin_options');

        // General Section
        add_settings_section('my_plugin_options', __('Options', 'my_plugin'), array($this, 'render_section'), $this->get_menu_slug());
        add_settings_field('my_plugin_options_color', __('Custom color', 'my_plugin'), array($this, 'render_color_field'), $this->get_menu_slug(), 'my_plugin_options');
    }

    /**
     * Render the options page.
     */
    public function render()
    {
        ?>
        <div class="wrap" id="my-plugin-options">
            <h1><?php echo $this->get_page_title() ?></h1>
            <p>I want some introduction paragraph about my plugin here.</p>
            <form action="options.php" method="POST">
                <?php settings_fields($this->get_menu_slug()); ?>
                <?php do_settings_sections($this->get_menu_slug()); ?>
                <?php submit_button(); ?>
            </form>
        </div>
        <?php
    }

    /**
     * Renders the section.
     */
    public function render_section()
    {
        ?>
        <p><?php _e('Customize MyPlugin with these options', 'my_plugin'); ?></p>
        <?php
    }

    /**
     * Renders the color field.
     */
    public function render_color_field()
    {
        $this->render_form_field('my_plugin_color', 'my_plugin_options[color]', $this->options['color'], 'color');
    }

    /**
     * Get the options page menu slug.
     *
     * @return string
     */
    protected function get_menu_slug()
    {
        return 'my_plugin_options';
    }

    /**
     * Get the options page title.
     *
     * @return string
     */
    protected function get_page_title()
    {
        return __('My Plugin Options', 'my_plugin');
    }
}
```

### Example 5

```php
namespace MyPlugin;

/**
 * Base class for all WordPress admin pages. This class uses add_admin_page
 * as an abstract method.
 *
 * @author Carl Alexander
 */
abstract class AbstractAdminPage
{
    /**
     * My plugin options.
     *
     * @var array
     */
    protected $options;

    /**
     * Register the admin page with all the appropriate WordPress hooks.
     */
    public static function register()
    {
        $page = new static(get_option('my_plugin_options'), array());

        add_action('admin_init', array($page, 'configure'));
        add_action('admin_menu', array($page, 'add_admin_page'));
    }

    /**
     * Constructor.
     *
     * @param array $options
     */
    public function __construct(array $options)
    {
        $this->options = $options;
    }

    /**
     * Adds the admin page to the menu.
     */
    abstract public function add_admin_page();

    /**
     * Configure the admin page using the settings API.
     */
    abstract public function configure();

    /**
     * Render a form field.
     *
     * @param string $id
     * @param string $name
     * @param string $value
     * @param string $type
     */
    protected function render_form_field($id, $name, $value = '', $type = 'text')
    {
        ?>
        <input id="<?php echo $id; ?>" name="<?php echo $name; ?>" type="<?php echo $type; ?>" value="<?php echo $value; ?>" />
        <?php
    }
}
```

## Source

https://carlalexander.ca/polymorphism-wordpress-abstract-classes/
