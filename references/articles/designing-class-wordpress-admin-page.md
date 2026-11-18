---
title: "Designing a class representing a WordPress admin page
			

			

				A WordPress plugin can have a lot of different components. For example, some might need to use shortcodes to achieve their purpose. While others might need to create custom post types.
But one component that almost every plugin needs is an admin page. (Or they might even need more than one!) That said, designing an admin page using object-oriented programming isn’t that straightforward. There are a lot of different moving pieces that you have to take in consideration in your design.
A well-designed admin page class will combine these different moving pieces into a cohesive class. The key to achieving this is to understand the role of these different moving pieces in the larger picture of an admin page. We’ll do that by analyzing what makes up an admin page in the first place.

Elements of an admin page"
url: https://carlalexander.ca/designing-class-wordpress-admin-page/
slug: designing-class-wordpress-admin-page
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/designing-class-representing-wordpress-admin-page/
---

# Designing a class representing a WordPress admin page
			

			

				A WordPress plugin can have a lot of different components. For example, some might need to use shortcodes to achieve their purpose. While others might need to create custom post types.
But one component that almost every plugin needs is an admin page. (Or they might even need more than one!) That said, designing an admin page using object-oriented programming isn’t that straightforward. There are a lot of different moving pieces that you have to take in consideration in your design.
A well-designed admin page class will combine these different moving pieces into a cohesive class. The key to achieving this is to understand the role of these different moving pieces in the larger picture of an admin page. We’ll do that by analyzing what makes up an admin page in the first place.

Elements of an admin page

## Summary

Creating reusable admin page classes. Encapsulating menu registration, capability checks, and rendering logic.

## Code examples

### Example 1

```php
class MyPlugin_AdminPage
{
}
```

### Example 2

```php
function myplugin_add_admin_page() {
    $admin_page = new MyPlugin_AdminPage();

    // Call add_submenu_page function
}
add_action('admin_menu', 'myplugin_add_admin_page');
```

### Example 3

```php
function myplugin_add_admin_page() {
    $admin_page = new MyPlugin_AdminPage();

    call_user_func_array('add_submenu_page', $admin_page->get_page_arguments());
}
add_action('admin_menu', 'myplugin_add_admin_page');
```

### Example 4

```php
class MyPlugin_AdminPage
{
    // ...

    /**
     * Get the arguments for the "add_submenu_page" function.
     *
     * @return array
     */
    public function get_page_arguments()
    {
        return array(
            'options-general.php',
            'My Plugin Admin Page',
            'My Plugin',
            'install_plugins',
            'myplugin',
            array($this, 'render_page'),
        );
    }
}
```

### Example 5

```php
function myplugin_add_admin_page() {
    $admin_page = new MyPlugin_AdminPage();

    add_submenu_page(
        $admin_page->get_parent_slug(),
        $admin_page->get_page_title(),
        $admin_page->get_menu_title(),
        $admin_page->get_capability(),
        $admin_page->get_slug(),
        array($admin_page, 'render_page')
    );
}
add_action('admin_menu', 'myplugin_add_admin_page');
```

### Example 6

```php
class MyPlugin_AdminPage
{
    // ...

    /**
     * Get the capability required to view the admin page.
     *
     * @return string
     */
    public function get_capability()
    {
        return 'install_plugins';
    }

    /**
     * Get the title of the admin page in the WordPress admin menu.
     *
     * @return string
     */
    public function get_menu_title()
    {
        return 'My Plugin';
    }

    /**
     * Get the title of the admin page.
     *
     * @return string
     */
    public function get_page_title()
    {
        return 'My Plugin Admin Page';
    }

    /**
     * Get the parent slug of the admin page.
     *
     * @return string
     */
    public function get_parent_slug()
    {
        return 'options-general.php';
    }

    /**
     * Get the slug used by the admin page.
     *
     * @return string
     */
    public function get_slug()
    {
        return 'myplugin';
    }
}
```

### Example 7

```php
class MyPlugin_AdminPage
{
    // ...

    /**
     * Configure the admin page using the Settings API.
     */
    public function configure()
    {
        // Register settings
        register_setting($this->get_slug(), 'myplugin_option');
    }

    // ...
}
```

### Example 8

```php
class MyPlugin_AdminPage
{
    // ...

    /**
     * Configure the admin page using the Settings API.
     */
    public function configure()
    {
        /// Register settings
        register_setting($this->get_slug(), 'myplugin_option');

        // Register section and field
        add_settings_section(
            $this->get_slug() . '-section',
            __('Section Title', 'myplugin'),
            array($this, 'render_section'),
            $this->get_slug()
        );
        add_settings_field(
            $this->get_slug() . '-option', 
            __('My option', 'myplugin'),
            array($this, 'render_option_field'), 
            $this->get_slug(), 
            $this->get_slug() . '-section'
        );
    }

    // ...
}
```

### Example 9

```php
class MyPlugin_AdminPage
{
    /**
     * Path to the admin page templates.
     *
     * @var string
     */
    private $template_path;

    /**
     * Constructor.
     *
     * @param string $template_path
     */
    public function __construct($template_path)
    {
        $this->template_path = rtrim($template_path, '/');
    }

    // ...
}
```

### Example 10

```php
class MyPlugin_AdminPage
{
    // ...

    /**
     * Renders the given template if it's readable.
     *
     * @param string $template
     */
    private function render_template($template)
    {
        $template_path = $this->template_path . '/' . $template . '.php';

        if (!is_readable($template_path)) {
            return;
        }

        include $template_path;
    }
}
```

### Example 11

```php
class MyPlugin_AdminPage
{
    // ...

    /**
     * Renders the option field.
     */
    public function render_option_field()
    {
        $this->render_template('option_field');
    }

    /**
     * Render the plugin's admin page.
     */
    public function render_page()
    {
        $this->render_template('page');
    }

    /**
     * Render the top section of the plugin's admin page.
     */
    public function render_section()
    {
        $this->render_template('section');
    }

    // ...
}
```

### Example 12

```php
<div class="wrap" id="myplugin-admin">
    <div id="icon-tools" class="icon32"><br></div>
    <h2><?php echo $this->get_page_title(); ?></h2>
    <?php if (!empty($_GET['updated'])) : ?>
        <div id="setting-error-settings_updated" class="updated settings-error notice is-dismissible">
            <p><strong><?php _e('Settings saved.') ?></strong></p><button type="button" class="notice-dismiss"><span class="screen-reader-text">Dismiss this notice.</span></button>
        </div>
    <?php endif; ?>
    <form action="options.php" method="POST">
        <?php settings_fields($this->get_slug()); ?>
        <?php do_settings_sections($this->get_slug()); ?>
        <?php submit_button(__('Save')); ?>
    </form>
</div>
```

### Example 13

```php
<p><?php _e('A small description about this section of the admin page', 'myplugin'); ?></p>
```

### Example 14

```php
<input type="text" name="myplugin_option" value="<?php get_option('myplugin_option', ''); ?>" />
```

### Example 15

```php
class MyPlugin_AdminPage
{
    /**
     * Path to the admin page templates.
     *
     * @var string
     */
    private $template_path;

    /**
     * Constructor.
     *
     * @param string $template_path
     */
    public function __construct($template_path)
    {
        $this->template_path = rtrim($template_path, '/');
    }

    /**
     * Configure the admin page using the Settings API.
     */
    public function configure()
    {
        /// Register settings
        register_setting($this->get_slug(), 'myplugin_option');

        // Register section and field
        add_settings_section(
            $this->get_slug() . '-section',
            __('Section Title', 'myplugin'),
            array($this, 'render_section'),
            $this->get_slug()
        );
        add_settings_field(
            $this->get_slug() . '-api-status',
            __('My option', 'myplugin'),
            array($this, 'render_option_field'),
            $this->get_slug(),
            $this->get_slug() . '-section'
        );
    }

    /**
     * Get the capability required to view the admin page.
     *
     * @return string
     */
    public function get_capability()
    {
        return 'install_plugins';
    }

    /**
     * Get the title of the admin page in the WordPress admin menu.
     *
     * @return string
     */
    public function get_menu_title()
    {
        return 'My Plugin';
    }

    /**
     * Get the title of the admin page.
     *
     * @return string
     */
    public function get_page_title()
    {
        return 'My Plugin Admin Page';
    }

    /**
     * Get the parent slug of the admin page.
     *
     * @return string
     */
    public function get_parent_slug()
    {
        return 'options-general.php';
    }

    /**
     * Get the slug used by the admin page.
     *
     * @return string
     */
    public function get_slug()
    {
        return 'myplugin';
    }

    /**
     * Renders the option field.
     */
    public function render_option_field()
    {
        $this->render_template('option_field');
    }

    /**
     * Render the plugin's admin page.
     */
    public function render_page()
    {
        $this->render_template('page');
    }

    /**
     * Render the top section of the plugin's admin page.
     */
    public function render_section()
    {
        $this->render_template('section');
    }

    /**
     * Renders the given template if it's readable.
     *
     * @param string $template
     */
    private function render_template($template)
    {
        $template_path = $this->template_path . '/' . $template . '.php';

        if (!is_readable($template_path)) {
            return;
        }

        include $template_path;
    }
}
```

## Source

https://carlalexander.ca/designing-class-wordpress-admin-page/
