---
title: "Polymorphism and WordPress: Interfaces
			

			

				Let’s talk about interfaces. As a WordPress developer, how can they be useful to you and your projects? It’s going to be a tough sell because WordPress core doesn’t use them and we’ll see why this is an issue a bit later. That said, you’ll still find this article useful if you’re looking to:

Learn more about PHP and not just WordPress
Build strong and extensible PHP code
Reduce bugs in your open source plugins
Use open source PHP frameworks

Like the article on abstract classes, you’ll get a detailed example to help you with the topic. It’ll explain how interfaces work and how you can use them. You’ll also get a good idea of the design decisions that warrant the use of an interface.

Reviewing interfaces"
url: https://carlalexander.ca/polymorphism-wordpress-interfaces/
slug: polymorphism-wordpress-interfaces
fetched: 2026-11-18
---

# Polymorphism and WordPress: Interfaces
			

			

				Let’s talk about interfaces. As a WordPress developer, how can they be useful to you and your projects? It’s going to be a tough sell because WordPress core doesn’t use them and we’ll see why this is an issue a bit later. That said, you’ll still find this article useful if you’re looking to:

Learn more about PHP and not just WordPress
Build strong and extensible PHP code
Reduce bugs in your open source plugins
Use open source PHP frameworks

Like the article on abstract classes, you’ll get a detailed example to help you with the topic. It’ll explain how interfaces work and how you can use them. You’ll also get a good idea of the design decisions that warrant the use of an interface.

Reviewing interfaces

## Summary

Using interfaces in WordPress. Contract-based programming, type hinting, and polymorphism through interface implementation.

## Code examples

### Example 1

```php
/**
 * Interface for implementing the conversion to an array.
 */
interface ArrayableInterface
{
    /**
     * Converts the object to an array.
     *
     * @return array
     */
    public function to_array();
}

class WP_User implements ArrayableInterface
{
    // ...

    /**
     * Converts WP_User to an array.
     *
     * @return array
     */
    public function to_array()
    {
        return array(
            'id'           => $this->id,
            'login'        => $this->user_login,
            'email'        => $this->user_email,
            'display_name' => $this->display_name,
            // ...
        );
    }
}
```

### Example 2

```php
class JsonEncoder
{
    // ...

    /**
     * Encodes an object into JSON.
     *
     * @param mixed $object
     *
     * @return string
     */
    public function encode($object)
    {
        if (!$object instanceof ArrayableInterface) {
            return '';
        }

        return json_encode($object->to_array());
    }
}
```

### Example 3

```php
namespace MyPlugin;

/**
 * HookSubscriberInterface is used by an object that needs to subscribe to
 * WordPress action and filter hooks.
 */
interface HookSubscriberInterface
{
    /**
     * Returns an array of actions that the object needs to be subscribed to.
     *
     * @return array
     */
    public static function get_actions();

    /**
     * Returns an array of filters that the object needs to be subscribed to.
     *
     * @return array
     */
    public static function get_filters();
}
```

### Example 4

```php
namespace MyPlugin;

/**
 * HookSubscriberInterface is used by an object that needs to subscribe to
 * WordPress action and filter hooks.
 */
interface HookSubscriberInterface
{
    /**
     * Returns an array of actions that the object needs to be subscribed to.
     *
     * The array key is the name of the action hook. The value can be:
     *
     *  * The method name
     *  * An array with the method name and priority
     *  * An array with the method name, priority and number of accepted arguments
     *
     * For instance:
     *
     *  * array('action_name' => 'method_name')
     *  * array('action_name' => array('method_name', $priority))
     *  * array('action_name' => array('method_name', $priority, $accepted_args))
     *
     * @return array
     */
    public static function get_actions();

    /**
     * Returns an array of filters that the object needs to be subscribed to.
     *
     * The array key is the name of the filter hook. The value can be:
     *
     *  * The method name
     *  * An array with the method name and priority
     *  * An array with the method name, priority and number of accepted arguments
     *
     * For instance:
     *
     *  * array('filter_name' => 'method_name')
     *  * array('filter_name' => array('method_name', $priority))
     *  * array('filter_name' => array('method_name', $priority, $accepted_args))
     *
     * @return array
     */
    public static function get_filters();
}
```

### Example 5

```php
namespace MyPlugin;

/**
 * ActionHookSubscriberInterface is used by an object that needs to subscribe to
 * WordPress action hooks.
 */
interface ActionHookSubscriberInterface
{
    /**
     * Returns an array of actions that the object needs to be subscribed to.
     *
     * The array key is the name of the action hook. The value can be:
     *
     *  * The method name
     *  * An array with the method name and priority
     *  * An array with the method name, priority and number of accepted arguments
     *
     * For instance:
     *
     *  * array('action_name' => 'method_name')
     *  * array('action_name' => array('method_name', $priority))
     *  * array('action_name' => array('method_name', $priority, $accepted_args))
     *
     * @return array
     */
    public static function get_actions();
}

/**
 * FilterHookSubscriberInterface is used by an object that needs to subscribe to
 * WordPress filter hooks.
 */
interface FilterHookSubscriberInterface
{
    /**
     * Returns an array of filters that the object needs to be subscribed to.
     *
     * The array key is the name of the filter hook. The value can be:
     *
     *  * The method name
     *  * An array with the method name and priority
     *  * An array with the method name, priority and number of accepted arguments
     *
     * For instance:
     *
     *  * array('filter_name' => 'method_name')
     *  * array('filter_name' => array('method_name', $priority))
     *  * array('filter_name' => array('method_name', $priority, $accepted_args))
     *
     * @return array
     */
    public static function get_filters();
}
```

### Example 6

```php
namespace MyPlugin;

class PluginAPIManager
{
    /**
     * Registers an object with the WordPress Plugin API.
     *
     * @param mixed $object
     */
    public function register($object)
    {
        if ($object instanceof ActionHookSubscriberInterface) {
            $this->register_actions($object);
        }
        if ($object instanceof FilterHookSubscriberInterface) {
            $this->register_filters($object);
        }
    }

    // ...
}
```

### Example 7

```php
namespace MyPlugin;

class PluginAPIManager
{
    // ...

    /**
     * Regiters an object with all its action hooks.
     *
     * @param ActionHookSubscriberInterface $object
     */
    private function register_actions(ActionHookSubscriberInterface $object)
    {
        foreach ($object->get_actions() as $name => $parameters) {
            $this->register_action($object, $name, $parameters);
        }
    }

    /**
     * Regiters an object with all its filter hooks.
     *
     * @param FilterHookSubscriberInterface $object
     */
    private function register_filters(FilterHookSubscriberInterface $object)
    {
        foreach ($object->get_filters() as $name => $parameters) {
            $this->register_filter($object, $name, $parameters);
        }
    }

    // ...
}
```

### Example 8

```php
namespace MyPlugin;

/**
 * PluginAPIManager handles registering actions and hooks with the
 * WordPress Plugin API.
 */
class PluginAPIManager
{
    // ...

    /**
     * Register an object with a specific action hook.
     *
     * @param ActionHookSubscriberInterface $object
     * @param string                        $name
     * @param mixed                         $parameters
     */
    private function register_action(ActionHookSubscriberInterface $object, $name, $parameters)
    {
        if (is_string($parameters)) {
            add_action($name, array($object, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            add_action($name, array($object, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10, isset($parameters[2]) ? $parameters[2] : 1);
        }
    }

    /**
     * Register an object with a specific filter hook.
     *
     * @param FilterHookSubscriberInterface $object
     * @param string                        $name
     * @param mixed                         $parameters
     */
    private function register_filter(FilterHookSubscriberInterface $object, $name, $parameters)
    {
        if (is_string($parameters)) {
            add_filter($name, array($object, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            add_filter($name, array($object, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10, isset($parameters[2]) ? $parameters[2] : 1);
        }
    }

    // ...
}
```

### Example 9

```php
namespace MyPlugin;

/**
 * PluginAPIManager handles registering actions and hooks with the
 * WordPress Plugin API.
 */
class PluginAPIManager
{
    /**
     * Registers an object with the WordPress Plugin API.
     *
     * @param mixed $object
     */
    public function register($object)
    {
        if ($object instanceof ActionHookSubscriberInterface) {
            $this->register_actions($object);
        }
        if ($object instanceof FilterHookSubscriberInterface) {
            $this->register_filters($object);
        }
    }

    /**
     * Register an object with a specific action hook.
     *
     * @param ActionHookSubscriberInterface $object
     * @param string                        $name
     * @param mixed                         $parameters
     */
    private function register_action(ActionHookSubscriberInterface $object, $name, $parameters)
    {
        if (is_string($parameters)) {
            add_action($name, array($object, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            add_action($name, array($object, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10, isset($parameters[2]) ? $parameters[2] : 1);
        }
    }

    /**
     * Regiters an object with all its action hooks.
     *
     * @param ActionHookSubscriberInterface $object
     */
    private function register_actions(ActionHookSubscriberInterface $object)
    {
        foreach ($object->get_actions() as $name => $parameters) {
            $this->register_action($object, $name, $parameters);
        }
    }

    /**
     * Register an object with a specific filter hook.
     *
     * @param FilterHookSubscriberInterface $object
     * @param string                        $name
     * @param mixed                         $parameters
     */
    private function register_filter(FilterHookSubscriberInterface $object, $name, $parameters)
    {
        if (is_string($parameters)) {
            add_filter($name, array($object, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            add_filter($name, array($object, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10, isset($parameters[2]) ? $parameters[2] : 1);
        }
    }

    /**
     * Regiters an object with all its filter hooks.
     *
     * @param FilterHookSubscriberInterface $object
     */
    private function register_filters(FilterHookSubscriberInterface $object)
    {
        foreach ($object->get_filters() as $name => $parameters) {
            $this->register_filter($object, $name, $parameters);
        }
    }
}
```

### Example 10

```php
namespace MyPlugin;

class Plugin implements ActionHookSubscriberInterface, FilterHookSubscriberInterface
{
    /**
     * Get the action hooks Plugin subscribes to.
     *
     * @return array
     */
    public static function get_actions()
    {
        return array(
            'plugins_loaded' => 'on_plugins_loaded'
        );
    }

    /**
     * Get the filter hooks Plugin subscribes to.
     *
     * @return array
     */
    public static function get_filters()
    {
        return array(
            'the_title' => 'alter_title'
        );
    }

    /**
     * Alter the title.
     *
     * @param string $title
     *
     * @return string
     */
    public function alter_title($title)
    {
        // Alter the title

        return $title
    }

    /**
     * Do operations for Plugin once plugins are loaded.
     */
    public function on_plugins_loaded()
    {
        // Do something useful
    }
}
```

### Example 11

```php
namespace MyPlugin;

$manager = new PluginAPIManager();
$plugin = new Plugin();

$manager->register($plugin);
```

## Source

https://carlalexander.ca/polymorphism-wordpress-interfaces/
