---
title: "Improving a system: Different types of WordPress admin pages
			

			

				In a previous article, we saw how to design a system for WordPress admin pages. The article was an excellent resource for anyone looking for a system to solve that specific type of problem. But it was only a starting point. (That said, you should take the time to read it before reading this article.)
All that we did was convert code from another article into the WordPress admin page system. We didn’t look at any other use cases besides the ones covered in that article already. But the reality is that there are a lot of them.
For example, the article only looked at how to add submenu pages. But there are other types of admin pages besides that one. The admin page system should be able to handle them all.
This is one of several advanced use cases that you might encounter with the WordPress admin page system. That’s why the system as we saw it so far is a great place to start. But handing these uses cases like different types of admin pages might be necessary depending on the kind of project that you’re working on.

Top-level menus"
url: https://carlalexander.ca/improving-system-wordpress-admin-page-types/
slug: improving-system-wordpress-admin-page-types
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/improving-system-different-types-wordpress-admin-pages/
---

# Improving a system: Different types of WordPress admin pages
			

			

				In a previous article, we saw how to design a system for WordPress admin pages. The article was an excellent resource for anyone looking for a system to solve that specific type of problem. But it was only a starting point. (That said, you should take the time to read it before reading this article.)
All that we did was convert code from another article into the WordPress admin page system. We didn’t look at any other use cases besides the ones covered in that article already. But the reality is that there are a lot of them.
For example, the article only looked at how to add submenu pages. But there are other types of admin pages besides that one. The admin page system should be able to handle them all.
This is one of several advanced use cases that you might encounter with the WordPress admin page system. That’s why the system as we saw it so far is a great place to start. But handing these uses cases like different types of admin pages might be necessary depending on the kind of project that you’re working on.

Top-level menus

## Summary

Distinguishing between admin page types and creating appropriate abstractions for each. List pages vs edit pages vs settings pages.

## Code examples

### Example 1

```php
/**
 * A WordPress top-level menu page.
 */
interface MyPlugin_MenuPageInterface
{

}

/**
 * A WordPress submenu page.
 */
interface MyPlugin_SubmenuPageInterface
{

}
```

### Example 2

```php
/**
 * A WordPress admin page.
 */
interface MyPlugin_AdminPageInterface
{
    // ...
}

/**
 * A WordPress top-level menu page.
 */
interface MyPlugin_MenuPageInterface extends MyPlugin_AdminPageInterface
{

}

/**
 * A WordPress submenu page.
 */
interface MyPlugin_SubmenuPageInterface extends MyPlugin_AdminPageInterface
{

}
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
```
/**
 * A WordPress submenu page.
 */
interface MyPlugin_SubmenuPageInterface extends MyPlugin_AdminPageInterface
{
    /**
     * Get the parent slug of the admin page.
     *
     * @return string
     */
    public function get_parent_slug();
}
```
```

### Example 5

```php
/**
 * A WordPress top-level menu page.
 */
interface MyPlugin_MenuPageInterface extends MyPlugin_AdminPageInterface
{
    /**
     * Get the URL of the icon used by the admin page.
     *
     * You can also return:
     * - A base64-encoded SVG using a data URI, which will be colored to match the color scheme. This should begin with 'data:image/svg+xml;base64,'.
     * - The name of a Dashicons helper class to use a font icon, e.g. 'dashicons-chart-pie'.
     * - The value 'none' to leave div.wp-menu-image empty so an icon can be added via CSS.
     *
     * @return string
     */
    public function get_icon_url();

    /**
     * Get the position of the admin page in the menu order of the WordPress admin sidebar.
     *
     * @return int
     */
    public function get_position();
}
```

### Example 6

```php
/**
 * Subscriber that registers the plugin's admin pages with WordPress.
 */
class MyPlugin_AdminPagesSubscriber implements MyPlugin_SubscriberInterface
{
    // ...

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

    // ...
}
```

### Example 7

```php
/**
 * Subscriber that registers the plugin's admin pages with WordPress.
 */
class MyPlugin_AdminPagesSubscriber implements MyPlugin_SubscriberInterface
{
    // ...

    /**
     * Adds the plugin's admin pages to the WordPress admin.
     */
    public function add_admin_pages()
    {
        foreach ($this->admin_pages as $admin_page) {
            if ($admin_page instanceof MyPlugin_MenuPageInterface) {
                add_menu_page(
                    $admin_page->get_page_title(),
                    $admin_page->get_menu_title(),
                    $admin_page->get_capability(),
                    $admin_page->get_slug(),
                    array($admin_page, 'render_page'),
                    $admin_page->get_icon_url(),
                    $admin_page->get_position()
                );
            } elseif ($admin_page instanceof MyPlugin_SubmenuPageInterface) {
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
    }

    // ...
}
```

### Example 8

```php
class MyPlugin_AdminPage implements MyPlugin_SubmenuPageInterface
{
    // ...

    /**
     * Get the parent slug of the admin page.
     *
     * @return string
     */
    public function get_parent_slug()
    {
        return 'options-general.php';
    }

    // ...
}
```

### Example 9

```php
class MyPlugin_NetworkAdminPage extends MyPlugin_AdminPage
{
    // ...

    /**
     * Get the parent slug of the admin page.
     *
     * @return string
     */
    public function get_parent_slug()
    {
        return 'settings.php';
    }

    // ...
}
```

### Example 10

```php
class MyPlugin_AdminPage implements MyPlugin_SubmenuPageInterface
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

    // ...
}
```

### Example 11

```php
class MyPlugin_NetworkAdminPage extends MyPlugin_AdminPage
{
    // ...

    /**
     * Get the capability required to view the admin page.
     *
     * @return string
     */
    public function get_capability()
    {
        return 'manage_network_plugins';
    }

    // ...
}
```

### Example 12

```php
$admin_page = is_multisite() 
            ? new MyPlugin_NetworkAdminPage()
            : new MyPlugin_AdminPage();
```

### Example 13

```php
class MyPlugin_AdminPage implements MyPlugin_SubmenuPageInterface
{
    /**
     * Flag whether WordPress 
     *
     * @var bool
     */
    private $is_multisite;

    /**
     * Constructor.
     *
     * @param bool $is_multisite
     */
    public function __construct($is_multisite = false)
    {
        $this->is_multisite = $is_multisite;
    }

    // ...
}
```

### Example 14

```php
class MyPlugin_AdminPage implements MyPlugin_SubmenuPageInterface
{
    /**
     * Flag whether WordPress 
     *
     * @var bool
     */
    private $is_multisite;

    /**
     * Constructor.
     *
     * @param bool $is_multisite
     */
    public function __construct($is_multisite = false)
    {
        $this->is_multisite = $is_multisite;
    }

    /**
     * Get the capability required to view the admin page.
     *
     * @return string
     */
    public function get_capability()
    {
        return $this->is_multisite ? 'manage_network_plugins' : 'install_plugins';
    }

    // ...

    /**
     * Get the parent slug of the admin page.
     *
     * @return string
     */
    public function get_parent_slug()
    {
        return $this->is_multisite ? 'settings.php' : 'options-general.php';
    }

    // ...
}
```

## Source

https://carlalexander.ca/improving-system-wordpress-admin-page-types/
