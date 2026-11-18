---
title: "Designing a system: WordPress admin pages
			

			

				In a previous article, we saw how to design a class to represent a WordPress admin page. The article was an excellent resource for anyone looking to design a class to solve that specific type of problem. But it was only a starting point.
For example, we used the settings API to handle forms. But the settings API doesn’t quite do the job for every use cases. For those other cases, you’re going to need to manage the submission of a form yourself.
But to handle these different use cases, we’re going to need a more solid foundation. So we’re going to take the work that we did to design our admin page class, and we’re going to take it one step further. We’re going to design a whole system for WordPress admin pages.

Reviewing our admin page class"
url: https://carlalexander.ca/designing-system-wordpress-admin-pages/
slug: designing-system-wordpress-admin-pages
fetched: 2026-11-18
---

# Designing a system: WordPress admin pages
			

			

				In a previous article, we saw how to design a class to represent a WordPress admin page. The article was an excellent resource for anyone looking to design a class to solve that specific type of problem. But it was only a starting point.
For example, we used the settings API to handle forms. But the settings API doesn’t quite do the job for every use cases. For those other cases, you’re going to need to manage the submission of a form yourself.
But to handle these different use cases, we’re going to need a more solid foundation. So we’re going to take the work that we did to design our admin page class, and we’re going to take it one step further. We’re going to design a whole system for WordPress admin pages.

Reviewing our admin page class

## Summary

Architecting admin page systems. Separating different types of admin pages (list, edit, view, settings) into cohesive system.

## Code examples

### Example 1

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

### Example 2

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

### Example 3

```php
/**
 * A WordPress admin page.
 */
interface MyPlugin_AdminPageInterface
{
    /**
     * Get the capability required to view the admin page.
     *
     * @return string
     */
    public function get_capability();

    /**
     * Get the title of the admin page in the WordPress admin menu.
     *
     * @return string
     */
    public function get_menu_title();

    /**
     * Get the title of the admin page.
     *
     * @return string
     */
    public function get_page_title();

    /**
     * Get the parent slug of the options page.
     *
     * @return string
     */
    public function get_parent_slug();

    /**
     * Get the slug used by the admin page.
     *
     * @return string
     */
    public function get_slug();

    /**
     * Renders the admin page.
     */
    public function render_page();
}
```

### Example 4

```php
function myplugin_add_admin_pages() {
    $admin_pages = array(
        // Put admin page objects here
    );
 
    foreach ($admin_pages as $admin_page) {
        add_submenu_page(
            $admin_page->get_parent_slug(),
            $admin_page->get_page_title(),
            $admin_page->get_menu_title(),
            $admin_page->get_capability(),
            $admin_page->get_slug(),
            array($admin_page, 'render_page')
        );
    }
}
add_action('admin_menu', 'myplugin_add_admin_pages');
```

### Example 5

```php
/**
 * A WordPress admin page rendered using a PHP template.
 */
abstract class MyPlugin_AbstractRenderedAdminPage implements MyPlugin_AdminPageInterface
{
    /**
     * Path to the admin page's templates.
     *
     * @var string
     */
    protected $template_path;

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
     * Render the admin page.
     */
    public function render_page()
    {
        $this->render_template('page');
    }

    /**
     * Renders the given template if it's readable.
     *
     * @param string $template
     */
    protected function render_template($template)
    {
        $template_path = $this->template_path . '/' . $template . '.php';
 
        if (!is_readable($template_path)) {
            return;
        }
 
        include $template_path;
    }
}
```

### Example 6

```php
/**
 * A WordPress admin page configured using the settings API.
 */
interface MyPlugin_ConfigurableAdminPageInterface extends MyPlugin_AdminPageInterface
{
    /**
     * Configure the admin page using the Settings API.
     */
    public function configure();
}
```

### Example 7

```php
function myplugin_configure_admin_pages() {
    $admin_pages = array(
        // Put admin page objects here
    );
 
    foreach ($admin_pages as $admin_page) {
        if ($admin_page instanceof MyPlugin_ConfigurableAdminPageInterface) {
            $admin_page->configure();
        }
    }
}
add_action('admin_init', 'myplugin_configure_admin_pages');
```

### Example 8

```php
function myplugin_get_admin_pages() {
    return array(
        // Put admin page objects here
    );
}
```

### Example 9

```php
$admin_pages = myplugin_get_admin_pages();
```

### Example 10

```php
/**
 * Subscriber that registers the plugin's admin pages with WordPress.
 */
class MyPlugin_AdminPagesSubscriber implements MyPlugin_SubscriberInterface
{

}
```

### Example 11

```php
/**
 * Subscriber that registers the plugin's admin pages with WordPress.
 */
class MyPlugin_AdminPagesSubscriber implements MyPlugin_SubscriberInterface
{
    /**
     * The admin pages that the subscriber manages.
     *
     * @var MyPlugin_AdminPageInterface[]
     */
    private $admin_pages;

    /**
     * Constructor.
     *
     * @param MyPlugin_AdminPageInterface[] $admin_pages
     */
    public function __construct(array $admin_pages)
    {
        $this->admin_pages = $admin_pages;
    }
}
```

### Example 12

```php
/**
 * Subscriber that registers the plugin's admin pages with WordPress.
 */
class MyPlugin_AdminPagesSubscriber implements MyPlugin_SubscriberInterface
{
    /**
     * The admin pages that the subscriber manages.
     *
     * @var MyPlugin_AdminPageInterface[]
     */
    private $admin_pages;

    /**
     * Constructor.
     *
     * @param MyPlugin_AdminPageInterface[] $admin_pages
     */
    public function __construct(array $admin_pages)
    {
        $this->admin_pages = array();

        foreach ($admin_pages as $admin_page) {
            $this->add_admin_page($admin_page);
        }
    }

    /**
     * Add a new admin page to the subscriber.
     *
     * @param MyPlugin_AdminPageInterface $admin_page
     */
    private function add_admin_page(MyPlugin_AdminPageInterface $admin_page)
    {
        $this->admin_pages[] = $admin_page;
    }
}
```

### Example 13

```php
/**
 * Subscriber that registers the plugin's admin pages with WordPress.
 */
class MyPlugin_AdminPagesSubscriber implements MyPlugin_SubscriberInterface
{
    // ...

    /**
     * Returns an array of events that this subscriber wants to listen to.
     *
     * The array key is the event name. The value can be:
     *
     *  * The method name
     *  * An array with the method name and priority
     *  * An array with the method name, priority and number of accepted arguments
     *
     * For instance:
     *
     *  * array('event_name' => 'method_name')
     *  * array('event_name' => array('method_name', $priority))
     *  * array('event_name' => array('method_name', $priority, $accepted_args))
     *
     * @return array
     */
    public static function get_subscribed_events()
    {
        return array();
    }

    // ...
}
```

### Example 14

```php
/**
 * Subscriber that registers the plugin's admin pages with WordPress.
 */
class MyPlugin_AdminPagesSubscriber implements MyPlugin_SubscriberInterface
{
    // ...

    /**
     * Returns an array of events that this subscriber wants to listen to.
     *
     * The array key is the event name. The value can be:
     *
     *  * The method name
     *  * An array with the method name and priority
     *  * An array with the method name, priority and number of accepted arguments
     *
     * For instance:
     *
     *  * array('event_name' => 'method_name')
     *  * array('event_name' => array('method_name', $priority))
     *  * array('event_name' => array('method_name', $priority, $accepted_args))
     *
     * @return array
     */
    public static function get_subscribed_events()
    {
        return array(
            'admin_init' => 'configure_admin_pages',
            'admin_menu' => 'add_admin_pages',
        );
    }

    /**
     * Adds the plugin's admin pages to the WordPress admin.
     */
    public function add_admin_pages()
    {
        foreach ($this->admin_pages as $admin_page) {
            add_submenu_page(
                $admin_page->get_parent_slug(),
                $admin_page->get_page_title(),
                $admin_page->get_menu_title(),
                $admin_page->get_capability(),
                $admin_page->get_slug(),
                array($admin_page, 'render_page')
            );
        }
    }

    /**
     * Configure the plugin's admin pages using the Settings API.
     */
    public function configure_admin_pages()
    {
        foreach ($this->admin_pages as $admin_page) {
            if ($admin_page instanceof MyPlugin_ConfigurableAdminPageInterface) {
                $admin_page->configure();
            }
        }
    }

    // ...
}
```

## Source

https://carlalexander.ca/designing-system-wordpress-admin-pages/
