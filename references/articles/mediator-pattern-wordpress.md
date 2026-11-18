---
title: "The mediator pattern in WordPress
			

			

				Let’s talk about the plugin API. You can’t write a plugin without using it. Well that’s not quite true. You could, but you’d have a hard (and unpleasant) time without it though. That’s because it’s the cornerstone of your interaction with WordPress.

This means that you can’t build an object-oriented plugin without taking it in consideration. That’s also when the headaches start. You try to find a solution to the problem. You often go back to the usual solutions such as:

Turning your classes into singletons.
Using the API in your constructor.
Flipping a table.

None of the these are great solutions to the problem (especially that last one). But that’s because you’ve been focusing on your problems. You want that sweet plugin you’ve been coding to be object-oriented (who doesn’t?).
Meanwhile, you didn’t stop and think about the plugin API. What does it want?
What does the Plugin API want?"
url: https://carlalexander.ca/mediator-pattern-wordpress/
slug: mediator-pattern-wordpress
fetched: 2026-11-18
---

# Mediator Pattern
			

			

				Let’s talk about the plugin API. You can’t write a plugin without using it. Well that’s not quite true. You could, but you’d have a hard (and unpleasant) time without it though. That’s because it’s the cornerstone of your interaction with WordPress.

This means that you can’t build an object-oriented plugin without taking it in consideration. That’s also when the headaches start. You try to find a solution to the problem. You often go back to the usual solutions such as:

Turning your classes into singletons.
Using the API in your constructor.
Flipping a table.

None of the these are great solutions to the problem (especially that last one). But that’s because you’ve been focusing on your problems. You want that sweet plugin you’ve been coding to be object-oriented (who doesn’t?).
Meanwhile, you didn’t stop and think about the plugin API. What does it want?
What does the Plugin API want?

## Summary

Mediator pattern for managing communication between objects. Reducing coupling by having objects communicate through a central mediator instead of directly.

## Code examples

### Example 1

```php
/**
 * Action_Hook_SubscriberInterface is used by an object that needs to subscribe to
 * WordPress action hooks.
 */
interface Action_Hook_SubscriberInterface
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
 * Filter_Hook_SubscriberInterface is used by an object that needs to subscribe to
 * WordPress filter hooks.
 */
interface Filter_Hook_SubscriberInterface
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

### Example 2

```php
/**
 * WP_Plugin_API_Manager handles registering actions and hooks with the
 * WordPress Plugin API.
 */
class WP_Plugin_API_Manager
{
    /**
     * Registers an object with the WordPress Plugin API.
     *
     * @param mixed $object
     */
    public function register($object)
    {
        if ($object instanceof Action_Hook_SubscriberInterface) {
            $this->register_actions($object);
        }
        if ($object instanceof Filter_Hook_SubscriberInterface) {
            $this->register_filters($object);
        }
    }
 
    /**
     * Register an object with a specific action hook.
     *
     * @param Action_Hook_SubscriberInterface $object
     * @param string                          $name
     * @param mixed                           $parameters
     */
    private function register_action(Action_Hook_SubscriberInterface $object, $name, $parameters)
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
     * @param Action_Hook_SubscriberInterface $object
     */
    private function register_actions(Action_Hook_SubscriberInterface $object)
    {
        foreach ($object->get_actions() as $name => $parameters) {
            $this->register_action($object, $name, $parameters);
        }
    }
 
    /**
     * Register an object with a specific filter hook.
     *
     * @param Filter_Hook_SubscriberInterface $object
     * @param string                          $name
     * @param mixed                           $parameters
     */
    private function register_filter(Filter_Hook_SubscriberInterface $object, $name, $parameters)
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
     * @param Filter_Hook_SubscriberInterface $object
     */
    private function register_filters(Filter_Hook_SubscriberInterface $object)
    {
        foreach ($object->get_filters() as $name => $parameters) {
            $this->register_filter($object, $name, $parameters);
        }
    }
}
```

## Source

https://carlalexander.ca/mediator-pattern-wordpress/
