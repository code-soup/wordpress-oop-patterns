---
title: "Designing a class to assemble plugin classes
			

			

				Learning object-oriented programming with WordPress is a lot like embarking on an epic journey. You’ll experience some lows, some highs and some downright frustrating moments. But it’s all part of the learning process.
And, so far, we’ve done quite a bit of progress on our journey. We’ve looked at various WordPress problems. And we then solved them using a class or combination of classes.
We call this process “object-oriented design“. It’s been the focus of a lot of the articles on this site. Because of that, there’s a good chance that you’ve begun using it in your own projects. (And if you haven’t, you should try it!)
When that happens, you’ll start to notice that your project has a lot of classes. This tends to become a problem for a lot of developers. They wonder, “How do I assemble all these classes together!?” It’s not unusual for them to revert back to the standard WordPress way of doing things when that happens.
This is the problem that we’re going to explore in this article. We’ll look at how you can solve it using a dedicated class for it. To do this, we’ll start thinking about the job of the main plugin class.

Defining the plugin class"
url: https://carlalexander.ca/designing-class-assemble-plugin/
slug: designing-class-assemble-plugin
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/designing-class-assemble-plugin-classes/
---

# Designing a class to assemble plugin classes
			

			

				Learning object-oriented programming with WordPress is a lot like embarking on an epic journey. You’ll experience some lows, some highs and some downright frustrating moments. But it’s all part of the learning process.
And, so far, we’ve done quite a bit of progress on our journey. We’ve looked at various WordPress problems. And we then solved them using a class or combination of classes.
We call this process “object-oriented design“. It’s been the focus of a lot of the articles on this site. Because of that, there’s a good chance that you’ve begun using it in your own projects. (And if you haven’t, you should try it!)
When that happens, you’ll start to notice that your project has a lot of classes. This tends to become a problem for a lot of developers. They wonder, “How do I assemble all these classes together!?” It’s not unusual for them to revert back to the standard WordPress way of doing things when that happens.
This is the problem that we’re going to explore in this article. We’ll look at how you can solve it using a dedicated class for it. To do this, we’ll start thinking about the job of the main plugin class.

Defining the plugin class

## Summary

Service provider/container pattern for WordPress plugins. Bootstrap classes that instantiate and wire up dependencies for entire plugin.

## Code examples

### Example 1

```php
myplugin/
├── src/
│ └── MyPlugin/
│ ├── EventManagement/
│ │ ├── EventManager.php
│ │ └── SubscriberInterface.php
│ ├── Routing/
│ │ ├── Route.php
│ │ └── Router.php
│ ├── Subscriber/
│ │ └── CustomPostTypeSubscriber.php
│ ├── Autoloader.php
│ └── Plugin.php
└── myplugin.php
```

### Example 2

```php
class MyPlugin_Plugin
{
}
```

### Example 3

```php
/*
Plugin Name: My plugin
*/

// Setup class autoloader
require_once dirname(__FILE__) . '/src/MyPlugin/Autoloader.php';
MyPlugin_Autoloader::register();
```

### Example 4

```php
class MyPlugin_Plugin
{
    /**
     * The plugin event manager.
     *
     * @var MyPlugin_EventManagement_EventManager
     */
    private $event_manager;

    /**
     * The plugin router.
     *
     * @var MyPlugin_Routing_Router
     */
    private $router;

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->event_manager = new MyPlugin_EventManagement_EventManager();
        $this->router = new MyPlugin_Routing_Router();
    }
}
```

### Example 5

```php
/*
Plugin Name: My plugin
*/

// Setup class autoloader
require_once dirname(__FILE__) . '/src/MyPlugin/Autoloader.php';
MyPlugin_Autoloader::register();

$myplugin = new MyPlugin_Plugin();
```

### Example 6

```php
class MyPlugin_Plugin
{
    // ...

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->event_manager = new MyPlugin_EventManagement_EventManager();
        $this->router = new MyPlugin_Routing_Router();

        $this->event_manager->add_subscriber(new MyPlugin_Subscriber_CustomPostTypeSubscriber());
    }
}
```

### Example 7

```php
class MyPlugin_Plugin
{
    // ...

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->event_manager = new MyPlugin_EventManagement_EventManager();
        $this->router = new MyPlugin_Routing_Router();

        foreach ($this->get_subscribers() as $subscriber) {
            $this->event_manager->add_subscriber($subscriber);
        }
    }

    /**
     * Get the plugin event subscribers.
     *
     * @return MyPlugin_EventManagement_SubscriberInterface[]
     */
    private function get_subscribers()
    {
        return array(
            new MyPlugin_Subscriber_CustomPostTypeSubscriber(),
        );
    }
}
```

### Example 8

```php
class MyPlugin_Plugin
{
    // ...

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->event_manager = new MyPlugin_EventManagement_EventManager();
        $this->router = new MyPlugin_Routing_Router();

        foreach ($this->get_routes() as $route) {
            $this->router->add_route($route);
        }

        foreach ($this->get_subscribers() as $subscriber) {
            $this->event_manager->add_subscriber($subscriber);
        }
    }

    /**
     * Get the plugin routes.
     *
     * @return MyPlugin_Routing_Route[]
     */
    private function get_routes()
    {
        return array(
            // Our plugin routes
        );
    }

    // ...
}
```

### Example 9

```php
class MyPlugin_Plugin
{
    // ...

    /**
     * Get the plugin routes.
     *
     * @return MyPlugin_Routing_Route[]
     */
    private function get_routes()
    {
        return $this->event_manager->filter('myplugin_routes', array(
            // Our plugin routes
        ));
    }

    /**
     * Get the plugin event subscribers.
     *
     * @return MyPlugin_EventManagement_SubscriberInterface[]
     */
    private function get_subscribers()
    {
        return $this->event_manager->filter('myplugin_subscriber'myplugin_routes', s', array(
            new MyPlugin_Subscriber_CustomPostTypeSubscriber(),
        ));
    }
}
```

### Example 10

```php
class MyPlugin_Plugin
{
    // ...

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->event_manager = new MyPlugin_EventManagement_EventManager();
        $this->router = new MyPlugin_Routing_Router();
    }

    /**
     * Loads the plugin into WordPress.
     */
    public function load()
    {
        foreach ($this->get_routes() as $route) {
            $this->router->add_route($route);
        }

        foreach ($this->get_subscribers() as $subscriber) {
            $this->event_manager->add_subscriber($subscriber);
        }
    }

    // ...
}
```

### Example 11

```php
/*
Plugin Name: My plugin
*/

// Setup class autoloader
require_once dirname(__FILE__) . '/src/MyPlugin/Autoloader.php';
MyPlugin_Autoloader::register();

$myplugin = new MyPlugin_Plugin();
add_action('wp_loaded', array($myplugin, 'load');
```

### Example 12

```php
class MyPlugin_Plugin
{
    // ...

    /**
     * Flag to track if the plugin is loaded.
     *
     * @var bool
     */
    private $loaded;

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->event_manager = new MyPlugin_EventManagement_EventManager();
        $this->loaded = false;
        $this->router = new MyPlugin_Routing_Router();
    }

    /**
     * Loads the plugin into WordPress.
     */
    public function load()
    {
        if ($this->loaded) {
            return;
        }

        foreach ($this->get_routes() as $route) {
            $this->router->add_route($route);
        }

        foreach ($this->get_subscribers() as $subscriber) {
            $this->event_manager->add_subscriber($subscriber);
        }

        $this->loaded = true;
    }

    // ...
}
```

### Example 13

```php
/*
Plugin Name: My plugin
*/

// Setup class autoloader
require_once dirname(__FILE__) . '/src/MyPlugin/Autoloader.php';
MyPlugin_Autoloader::register();

$myplugin = new MyPlugin_Plugin(__FILE__);
add_action('wp_loaded', array($myplugin, 'load');
```

### Example 14

```php
class MyPlugin_Plugin
{
    // ...

    /**
     * The basename of the plugin.
     *
     * @var string
     */
    private $basename;

    /**
     * Constructor.
     *
     * @param string $file
     */
    public function __construct($file)
    {
        $this->basename = plugin_basename($file);
        $this->event_manager = new MyPlugin_EventManagement_EventManager();
        $this->loaded = false;
        $this->router = new MyPlugin_Routing_Router();
    }

    // ...
}
```

## Source

https://carlalexander.ca/designing-class-assemble-plugin/
