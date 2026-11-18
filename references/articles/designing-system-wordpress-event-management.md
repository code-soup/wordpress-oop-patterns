---
title: "Designing a system: WordPress event management
			

			

				In a previous article, we went over the concept of events and event listeners. These were classes who were in charge of a specific aspect of an application. This was a more abstract job that touched several parts of an application.
We also saw how you could design these event listeners in WordPress. It required that you rethink how you use the plugin API. (Yes, this is going to be another plugin API article :P)
We’re going to keep going with this idea of events and event listeners. We’re going to design a system for them. We’ll call it an “event management” system. It’s an important tool in your journey to master object-oriented programming in WordPress.

On actions and filters"
url: https://carlalexander.ca/designing-system-wordpress-event-management/
slug: designing-system-wordpress-event-management
fetched: 2026-11-18
---

# Designing a system: WordPress event management
			

			

				In a previous article, we went over the concept of events and event listeners. These were classes who were in charge of a specific aspect of an application. This was a more abstract job that touched several parts of an application.
We also saw how you could design these event listeners in WordPress. It required that you rethink how you use the plugin API. (Yes, this is going to be another plugin API article :P)
We’re going to keep going with this idea of events and event listeners. We’re going to design a system for them. We’ll call it an “event management” system. It’s an important tool in your journey to master object-oriented programming in WordPress.

On actions and filters

## Summary

Event-driven architecture in WordPress. Creating event systems for loosely coupled communication between components.

## Code examples

### Example 1

```php
class PluginAPIManager
{
    /**
     * Adds a callback to a specific hook of the WordPress plugin API.
     *
     * @uses add_filter()
     *
     * @param string   $hook_name
     * @param callable $callback
     * @param int      $priority
     * @param int      $accepted_args
     */
    public function add_callback($hook_name, $callback, $priority = 10, $accepted_args = 1)
    {
        add_filter($hook_name, $callback, $priority, $accepted_args);
    }

    /**
     * Executes all the callbacks registered with the given hook.
     *
     * @uses do_action()
     *
     * @param string $hook_name
     */
    public function execute()
    {
        $args = func_get_args();
        return call_user_func_array('do_action', $args);
    }

    /**
     * Filters the given value by applying all the changes from the callbacks
     * registered with the given hook. Returns the filtered value.
     *
     * @uses apply_filters()
     *
     * @param string $hook_name
     * @param mixed  $value
     *
     * @return mixed
     */
    public function filter()
    {
        $args = func_get_args();
        return call_user_func_array('apply_filters', $args);
    }

    /**
     * Get the name of the hook that WordPress plugin API is executing. Returns
     * false if it isn't executing a hook.
     *
     * @uses current_filter()
     *
     * @return string|bool
     */
    public function get_current_hook()
    {
        return current_filter();
    }

    /**
     * Checks the WordPress plugin API to see if the given hook has
     * the given callback. The priority of the callback will be returned
     * or false. If no callback is given will return true or false if
     * there's any callbacks registered to the hook.
     *
     * @uses has_filter()
     *
     * @param string $hook_name
     * @param mixed  $callback
     *
     * @return bool|int
     */
    public function has_callback($hook_name, $callback = false)
    {
        return has_filter($hook_name, $callback);
    }

    /**
     * Removes the given callback from the given hook. The WordPress plugin API only
     * removes the hook if the callback and priority match a registered hook.
     *
     * @uses remove_filter()
     *
     * @param string   $hook_name
     * @param callable $callback
     * @param int      $priority
     *
     * @return bool
     */
    public function remove_callback($hook_name, $callback, $priority = 10)
    {
        return remove_filter($hook_name, $callback, $priority);
    }
}
```

### Example 2

```php
interface SubscriberInterface
{
    /**
     * Returns an array of hooks that this subscriber wants to register with
     * the WordPress plugin API.
     *
     * The array key is the name of the hook. The value can be:
     *
     *  * The method name
     *  * An array with the method name and priority
     *  * An array with the method name, priority and number of accepted arguments
     *
     * For instance:
     *
     *  * array('hook_name' => 'method_name')
     *  * array('hook_name' => array('method_name', $priority))
     *  * array('hook_name' => array('method_name', $priority, $accepted_args))
     *
     * @return array
     */
    public static function get_subscribed_hooks();
}
```

### Example 3

```php
class EventManager
{
    /**
     * Contains all the code from PluginAPIManager
     */
}
```

### Example 4

```php
class EventManager
{
    // ...

    /**
     * Add an event subscriber.
     *
     * The event manager registers all the hooks that the given subscriber 
     * wants to register with the WordPress Plugin API.
     *
     * @param SubscriberInterface $subscriber
     */
    public function add_subscriber(SubscriberInterface $subscriber)
    {
        foreach ($subscriber->get_subscribed_hooks() as $hook_name => $parameters) {
            $this->add_subscriber_callback($subscriber, $hook_name, $parameters);
        }
    }

    /**
     * Adds the given subscriber's callback to a specific hook
     * of the WordPress plugin API.
     *
     * @param SubscriberInterface $subscriber
     * @param string              $hook_name
     * @param mixed               $parameters
     */
    private function add_subscriber_callback(SubscriberInterface $subscriber, $hook_name, $parameters)
    {
        if (is_string($parameters)) {
            $this->add_callback($hook_name, array($subscriber, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            $this->add_callback($hook_name, array($subscriber, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10, isset($parameters[2]) ? $parameters[2] : 1);
        }
    }
}
```

### Example 5

```php
class EventManager
{
    // ...

    /**
     * Remove an event subscriber.
     *
     * The event manager removes all the hooks that the given subscriber
     * wants to register with the WordPress Plugin API.
     *
     * @param SubscriberInterface $subscriber
     */
    public function remove_subscriber(SubscriberInterface $subscriber)
    {
        foreach ($subscriber->get_subscribed_hooks() as $hook_name => $parameters) {
            $this->remove_subscriber_callback($subscriber, $hook_name, $parameters);
        }
    }

    /**
     * Removes the given subscriber's callback to a specific hook
     * of the WordPress plugin API.
     *
     * @param SubscriberInterface $subscriber
     * @param string              $hook_name
     * @param mixed               $parameters
     */
    private function remove_subscriber_callback(SubscriberInterface $subscriber, $hook_name, $parameters)
    {
        if (is_string($parameters)) {
            $this->remove_callback($hook_name, array($subscriber, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            $this->remove_callback($hook_name, array($subscriber, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10);
        }
    }
}
```

### Example 6

```php
class EventManager
{
    /**
     * Adds a callback to a specific hook of the WordPress plugin API.
     *
     * @uses add_filter()
     *
     * @param string   $hook_name
     * @param callable $callback
     * @param int      $priority
     * @param int      $accepted_args
     */
    public function add_callback($hook_name, $callback, $priority = 10, $accepted_args = 1)
    {
        add_filter($hook_name, $callback, $priority, $accepted_args);
    }

    /**
     * Add an event subscriber.
     *
     * The event manager registers all the hooks that the given subscriber
     * wants to register with the WordPress Plugin API.
     *
     * @param SubscriberInterface $subscriber
     */
    public function add_subscriber(SubscriberInterface $subscriber)
    {
        foreach ($subscriber->get_subscribed_hooks() as $hook_name => $parameters) {
            $this->add_subscriber_callback($subscriber, $hook_name, $parameters);
        }
    }

    /**
     * Executes all the callbacks registered with the given hook.
     *
     * @uses do_action()
     *
     * @param string $hook_name
     */
    public function execute()
    {
        $args = func_get_args();
        return call_user_func_array('do_action', $args);
    }

    /**
     * Filters the given value by applying all the changes from the callbacks
     * registered with the given hook. Returns the filtered value.
     *
     * @uses apply_filters()
     *
     * @param string $hook_name
     * @param mixed  $value
     *
     * @return mixed
     */
    public function filter()
    {
        $args = func_get_args();
        return call_user_func_array('apply_filters', $args);
    }

    /**
     * Get the name of the hook that WordPress plugin API is executing. Returns
     * false if it isn't executing a hook.
     *
     * @uses current_filter()
     *
     * @return string|bool
     */
    public function get_current_hook()
    {
        return current_filter();
    }

    /**
     * Checks the WordPress plugin API to see if the given hook has
     * the given callback. The priority of the callback will be returned
     * or false. If no callback is given will return true or false if
     * there's any callbacks registered to the hook.
     *
     * @uses has_filter()
     *
     * @param string $hook_name
     * @param mixed  $callback
     *
     * @return bool|int
     */
    public function has_callback($hook_name, $callback = false)
    {
        return has_filter($hook_name, $callback);
    }

    /**
     * Removes the given callback from the given hook. The WordPress plugin API only
     * removes the hook if the callback and priority match a registered hook.
     *
     * @uses remove_filter()
     *
     * @param string   $hook_name
     * @param callable $callback
     * @param int      $priority
     *
     * @return bool
     */
    public function remove_callback($hook_name, $callback, $priority = 10)
    {
        return remove_filter($hook_name, $callback, $priority);
    }

    /**
     * Remove an event subscriber.
     *
     * The event manager removes all the hooks that the given subscriber
     * wants to register with the WordPress Plugin API.
     *
     * @param SubscriberInterface $subscriber
     */
    public function remove_subscriber(SubscriberInterface $subscriber)
    {
        foreach ($subscriber->get_subscribed_hooks() as $hook_name => $parameters) {
            $this->remove_subscriber_callback($subscriber, $hook_name, $parameters);
        }
    }

    /**
     * Adds the given subscriber's callback to a specific hook
     * of the WordPress plugin API.
     *
     * @param SubscriberInterface $subscriber
     * @param string              $hook_name
     * @param mixed               $parameters
     */
    private function add_subscriber_callback(SubscriberInterface $subscriber, $hook_name, $parameters)
    {
        if (is_string($parameters)) {
            $this->add_callback($hook_name, array($subscriber, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            $this->add_callback($hook_name, array($subscriber, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10, isset($parameters[2]) ? $parameters[2] : 1);
        }
    }

    /**
     * Removes the given subscriber's callback to a specific hook
     * of the WordPress plugin API.
     *
     * @param SubscriberInterface $subscriber
     * @param string              $hook_name
     * @param mixed               $parameters
     */
    private function remove_subscriber_callback(SubscriberInterface $subscriber, $hook_name, $parameters)
    {
        if (is_string($parameters)) {
            $this->remove_callback($hook_name, array($subscriber, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            $this->remove_callback($hook_name, array($subscriber, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10);
        }
    }
}
```

### Example 7

```php
class EventManager extends PluginAPIManager
{
    /**
     * Add an event subscriber.
     *
     * The event manager registers all the hooks that the given subscriber
     * wants to register with the WordPress Plugin API.
     *
     * @param SubscriberInterface $subscriber
     */
    public function add_subscriber(SubscriberInterface $subscriber)
    {
        foreach ($subscriber->get_subscribed_hooks() as $hook_name => $parameters) {
            $this->add_subscriber_callback($subscriber, $hook_name, $parameters);
        }
    }

    /**
     * Remove an event subscriber.
     *
     * The event manager removes all the hooks that the given subscriber
     * wants to register with the WordPress Plugin API.
     *
     * @param SubscriberInterface $subscriber
     */
    public function remove_subscriber(SubscriberInterface $subscriber)
    {
        foreach ($subscriber->get_subscribed_hooks() as $hook_name => $parameters) {
            $this->remove_subscriber_callback($subscriber, $hook_name, $parameters);
        }
    }

    /**
     * Adds the given subscriber's callback to a specific hook
     * of the WordPress plugin API.
     *
     * @param SubscriberInterface $subscriber
     * @param string              $hook_name
     * @param mixed               $parameters
     */
    private function add_subscriber_callback(SubscriberInterface $subscriber, $hook_name, $parameters)
    {
        if (is_string($parameters)) {
            $this->add_callback($hook_name, array($subscriber, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            $this->add_callback($hook_name, array($subscriber, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10, isset($parameters[2]) ? $parameters[2] : 1);
        }
    }

    /**
     * Removes the given subscriber's callback to a specific hook
     * of the WordPress plugin API.
     *
     * @param SubscriberInterface $subscriber
     * @param string              $hook_name
     * @param mixed               $parameters
     */
    private function remove_subscriber_callback(SubscriberInterface $subscriber, $hook_name, $parameters)
    {
        if (is_string($parameters)) {
            $this->remove_callback($hook_name, array($subscriber, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            $this->remove_callback($hook_name, array($subscriber, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10);
        }
    }
}
```

### Example 8

```php
class EventManager
{
    /**
     * The WordPress plugin API manager.
     *
     * @var PluginAPIManager
     */
    private $plugin_api_manager;

    /**
     * Constructor.
     *
     * @param PluginAPIManager $plugin_api_manager
     */
    public function __construct(PluginAPIManager $plugin_api_manager)
    {
        $this->plugin_api_manager = $plugin_api_manager;
    }
}
```

### Example 9

```php
class EventManager
{
    // ...

    /**
     * Adds the given event listener to the list of event listeners
     * that listen to the given event.
     *
     * @param string   $event_name
     * @param callable $listener
     * @param int      $priority
     * @param int      $accepted_args
     */
    public function add_listener($event_name, $listener, $priority = 10, $accepted_args = 1)
    {
        $this->plugin_api_manager->add_callback($event_name, $listener, $priority, $accepted_args);
    }
}
```

### Example 10

```php
interface SubscriberInterface
{
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
    public static function get_subscribed_events();
}
```

### Example 11

```php
class EventManager
{
    // ...

    /**
     * Adds an event subscriber.
     *
     * The event manager adds the given subscriber to the list of event listeners 
     * for all the events that it wants to listen to.
     *
     * @param SubscriberInterface $subscriber
     */
    public function add_subscriber(SubscriberInterface $subscriber)
    {
        foreach ($subscriber->get_subscribed_events() as $event_name => $parameters) {
            $this->add_subscriber_listener($subscriber, $event_name, $parameters);
        }
    }

    /**
     * Adds the given subscriber listener to the list of event listeners
     * that listen to the given event.
     *
     * @param SubscriberInterface $subscriber
     * @param string              $event_name
     * @param mixed               $parameters
     */
    private function add_subscriber_listener(SubscriberInterface $subscriber, $event_name, $parameters)
    {
        if (is_string($parameters)) {
            $this->add_listener($event_name, array($subscriber, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            $this->add_listener($event_name, array($subscriber, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10, isset($parameters[2]) ? $parameters[2] : 1);
        }
    }
}
```

### Example 12

```php
class EventManager
{
    /**
     * The WordPress plugin API manager.
     *
     * @var PluginAPIManager
     */
    private $plugin_api_manager;

    /**
     * Constructor.
     *
     * @param PluginAPIManager $plugin_api_manager
     */
    public function __construct(PluginAPIManager $plugin_api_manager)
    {
        $this->plugin_api_manager = $plugin_api_manager;
    }

    /**
     * Adds the given event listener to the list of event listeners
     * that listen to the given event.
     *
     * @param string   $event_name
     * @param callable $listener
     * @param int      $priority
     * @param int      $accepted_args
     */
    public function add_listener($event_name, $listener, $priority = 10, $accepted_args = 1)
    {
        $this->plugin_api_manager->add_callback($event_name, $listener, $priority, $accepted_args);
    }

    /**
     * Adds an event subscriber.
     *
     * The event manager adds the given subscriber to the list of event listeners 
     * for all the events that it wants to listen to.
     *
     * @param SubscriberInterface $subscriber
     */
    public function add_subscriber(SubscriberInterface $subscriber)
    {
        foreach ($subscriber->get_subscribed_events() as $event_name => $parameters) {
            $this->add_subscriber_listener($subscriber, $event_name, $parameters);
        }
    }

    /**
     * Removes the given event listener from the list of event listeners
     * that listen to the given event.
     *
     * @param string   $event_name
     * @param callable $listener
     * @param int      $priority
     */
    public function remove_listener($event_name, $listener, $priority = 10)
    {
        $this->plugin_api_manager->remove_callback($event_name, $listener, $priority);
    }

    /**
     * Removes an event subscriber.
     *
     * The event manager removes the given subscriber from the list of event listeners 
     * for all the events that it wants to listen to.
     *
     * @param SubscriberInterface $subscriber
     */
    public function remove_subscriber(SubscriberInterface $subscriber)
    {
        foreach ($subscriber->get_subscribed_events() as $event_name => $parameters) {
            $this->remove_subscriber_listener($subscriber, $event_name, $parameters);
        }
    }

    /**
     * Adds the given subscriber listener to the list of event listeners
     * that listen to the given event.
     *
     * @param SubscriberInterface $subscriber
     * @param string              $event_name
     * @param mixed               $parameters
     */
    private function add_subscriber_listener(SubscriberInterface $subscriber, $event_name, $parameters)
    {
        if (is_string($parameters)) {
            $this->add_listener($event_name, array($subscriber, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            $this->add_listener($event_name, array($subscriber, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10, isset($parameters[2]) ? $parameters[2] : 1);
        }
    }

    /**
     * Adds the given subscriber listener to the list of event listeners
     * that listen to the given event.
     *
     * @param SubscriberInterface $subscriber
     * @param string              $event_name
     * @param mixed               $parameters
     */
    private function remove_subscriber_listener(SubscriberInterface $subscriber, $event_name, $parameters)
    {
        if (is_string($parameters)) {
            $this->remove_listener($event_name, array($subscriber, $parameters));
        } elseif (is_array($parameters) && isset($parameters[0])) {
            $this->remove_listener($event_name, array($subscriber, $parameters[0]), isset($parameters[1]) ? $parameters[1] : 10);
        }
    }
}
```

### Example 13

```php
interface EventManagerAwareSubscriberInterface extends SubscriberInterface
{
    /**
     * Set the WordPress event manager for the subscriber.
     *
     * @param EventManager $event_manager
     */
    public function set_event_manager(EventManager $event_manager);
}
```

### Example 14

```php
abstract class AbstractEventManagerAwareSubscriber implements EventManagerAwareSubscriberInterface
{
    /**
     * The WordPress event manager.
     *
     * @var EventManager
     */
    protected $event_manager;

    /**
     * Set the WordPress event manager for the subscriber.
     *
     * @param EventManager $event_manager
     */
    public function set_event_manager(EventManager $event_manager)
    {
        $this->event_manager = $event_manager;
    }
}
```

### Example 15

```php
class EventManager extends PluginAPIManager
{
    /**
     * Add an event subscriber.
     *
     * The event manager registers all the hooks that the given subscriber
     * wants to register with the WordPress Plugin API.
     *
     * @param SubscriberInterface $subscriber
     */
    public function add_subscriber(SubscriberInterface $subscriber)
    {
        if ($subscriber instanceof EventManagerAwareSubscriberInterface) {
            $subscriber->set_event_manager($this);
        }

        foreach ($subscriber->get_subscribed_hooks() as $hook_name => $parameters) {
            $this->add_subscriber_callback($subscriber, $hook_name, $parameters);
        }
    }

    // ...
}
```

### Example 16

```php
interface PluginAPIManagerAwareSubscriberInterface extends SubscriberInterface
{
    /**
     * Set the WordPress Plugin API manager for the subscriber.
     *
     * @param PluginAPIManager $plugin_api_manager
     */
    public function set_plugin_api_manager(PluginAPIManager $plugin_api_manager);
}

abstract class AbstractPluginAPIManagerAwareSubscriber implements PluginAPIManagerAwareSubscriberInterface
{
    /**
     * WordPress Plugin API manager.
     *
     * @var PluginAPIManager
     */
    protected $plugin_api_manager;

    /**
     * Set the WordPress Plugin API manager for the subscriber.
     *
     * @param PluginAPIManager $plugin_api_manager
     */
    public function set_plugin_api_manager(PluginAPIManager $plugin_api_manager)
    {
        $this->plugin_api_manager = $plugin_api_manager;
    }
}

class EventManager
{
    // ...

    /**
     * Adds an event subscriber.
     *
     * The event manager adds the given subscriber to the list of event listeners
     * for all the events that it wants to listen to.
     *
     * @param SubscriberInterface $subscriber
     */
    public function add_subscriber(SubscriberInterface $subscriber)
    {
        if ($subscriber instanceof PluginAPIManagerAwareSubscriberInterface) {
            $subscriber->set_plugin_api_manager($this->plugin_api_manager);
        }

        foreach ($subscriber->get_subscribed_events() as $event_name => $parameters) {
            $this->add_subscriber_listener($subscriber, $event_name, $parameters);
        }
    }
}
```

### Example 17

```php
$event_manager = new EventManager();
```

### Example 18

```php
class LoginErrorSubscriber implements SubscriberInterface
{
    // Empty!
}
```

### Example 19

```php
class LoginErrorSubscriber implements SubscriberInterface
{
    /**
     * Returns an array of hooks that this subscriber wants to register with
     * the WordPress plugin API.
     *
     * @return array
     */
    public static function get_subscribed_hooks()
    {
        return array(
            'shake_error_codes' => 'add_error_code',
            'wp_login_errors' => 'add_error',
        );
    }
}
```

### Example 20

```php
class LoginErrorSubscriber implements SubscriberInterface
{
    /**
     * The error code that our login error subscriber creates.
     */
    const ERROR_CODE = 'my-login-error-code';

    // ...
}
```

### Example 21

```php
class LoginErrorSubscriber implements SubscriberInterface
{
    // ...

    /**
     * Add our error to the login errors.
     *
     * @param WP_Error $error
     *
     * @return WP_Error
     */
    public function add_error(WP_Error $error)
    {
        if (!isset($_GET[self::ERROR_CODE])) {
            return $error;
        }

        $error->add(self::ERROR_CODE, 'The error message displayed on the login screen.');

        return $error;
    }
}
```

### Example 22

```php
class LoginErrorSubscriber implements SubscriberInterface
{
    // ...

    /**
     * Add our error code to the handled login error codes.
     *
     * @param array $error_codes
     *
     * @return array
     */
    public function add_error_code(array $error_codes)
    {
        $error_codes[] = self::ERROR_CODE;

        return $error_codes;
    }
}
```

### Example 23

```php
$event_manager = new EventManager();
$event_manager->add_subscriber(new LoginErrorSubscriber());
```

## Source

https://carlalexander.ca/designing-system-wordpress-event-management/
