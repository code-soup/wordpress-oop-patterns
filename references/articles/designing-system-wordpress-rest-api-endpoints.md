---
title: "Designing a system: WordPress REST API endpoints
			

			

				Let’s talk about the WordPress REST API. It’s been around for a little while now, and you might have even started using it in your projects. After all, a lot of us are trying to get more into JavaScript. (Zac Gordon has built a great course if you’re looking to get into it.)
But that doesn’t mean that the standard WordPress REST API will be good enough for your project. There’s a good chance that you’ll need to extend it so that you can do more with it. And that’s done using PHP even if you’re working with JavaScript. (Sorry JavaScript lovers!)
That means that this is still a great excuse to use object-oriented programming with WordPress. (Yay!) In fact, it’s an excellent opportunity to piece different object-oriented concepts together. This will let us design a system to extend the WordPress REST API!

Why not use the controller class?"
url: https://carlalexander.ca/designing-system-wordpress-rest-api-endpoints/
slug: designing-system-wordpress-rest-api-endpoints
fetched: 2026-11-18
---

# Designing a system: WordPress REST API endpoints
			

			

				Let’s talk about the WordPress REST API. It’s been around for a little while now, and you might have even started using it in your projects. After all, a lot of us are trying to get more into JavaScript. (Zac Gordon has built a great course if you’re looking to get into it.)
But that doesn’t mean that the standard WordPress REST API will be good enough for your project. There’s a good chance that you’ll need to extend it so that you can do more with it. And that’s done using PHP even if you’re working with JavaScript. (Sorry JavaScript lovers!)
That means that this is still a great excuse to use object-oriented programming with WordPress. (Yay!) In fact, it’s an excellent opportunity to piece different object-oriented concepts together. This will let us design a system to extend the WordPress REST API!

Why not use the controller class?

## Summary

Architecting REST API systems. Creating controllers, route registration, request validation, and response formatting.

## Code examples

### Example 1

```php
/**
 * A WordPress REST API endpoint.
 */
interface MyPlugin_EndpointInterface
{
    /**
     * Get the expected arguments for the REST API endpoint.
     *
     * @return array
     */
    public function get_arguments();

    /**
     * Get the callback used by the REST API endpoint.
     *
     * @return callable
     */
    public function get_callback();

    /**
     * Get the callback used to validate a request to the REST API endpoint.
     *
     * @return callable
     */
    public function get_permission_callback();

    /**
     * Get the HTTP methods that the REST API endpoint responds to.
     *
     * @return mixed
     */
    public function get_methods();
}
```

### Example 2

```php
/**
 * Register an endpoint with the WordPress REST API.
 *
 * @param MyPlugin_EndpointInterface $endpoint
 */
function myplugin_register_endpoint(MyPlugin_EndpointInterface $endpoint)
{
    register_rest_route($namespace, $route, array(
        'args' => $endpoint->get_arguments(),
        'callback' => $endpoint->get_callback(),
        'methods' => $endpoint->get_methods(),
        'permission_callback' => $endpoint->get_permission_callback(),
    ));
}
```

### Example 3

```php
/**
 * Register an endpoint with the WordPress REST API.
 *
 * @param MyPlugin_EndpointInterface $endpoint
 */
function myplugin_register_endpoint(MyPlugin_EndpointInterface $endpoint)
{
    register_rest_route('myplugin/v1', $route, array(
        'args' => $endpoint->get_arguments(),
        'callback' => $endpoint->get_callback(),
        'methods' => $endpoint->get_methods(),
        'permission_callback' => $endpoint->get_permission_callback(),
    ));
}
```

### Example 4

```php
/**
 * A WordPress REST API endpoint.
 */
interface MyPlugin_EndpointInterface
{
    // ...

    /**
     * Get the path pattern of the REST API endpoint.
     *
     * @return string
     */
    public function get_path();

    // ...
}
```

### Example 5

```php
/**
 * Register an endpoint with the WordPress REST API.
 *
 * @param MyPlugin_EndpointInterface $endpoint
 */
function myplugin_register_endpoint(MyPlugin_EndpointInterface $endpoint)
{
    register_rest_route('myplugin/v1', $endpoint->get_path(), array(
        'args' => $endpoint->get_arguments(),
        'callback' => $endpoint->get_callback(),
        'methods' => $endpoint->get_methods(),
        'permission_callback' => $endpoint->get_permission_callback(),
    ));
}
```

### Example 6

```php
/**
 * Register all our endpoints with the WordPress REST API.
 */
function myplugin_register_endpoints()
{
    $endpoints = apply_filters('myplugin_endpoints', array(
        // ...
    ));
    
    foreach ($endpoints as $endpoint) {
        myplugin_register_endpoint($endpoint);
    }
}
add_action('rest_api_init', 'myplugin_register_endpoints');
```

### Example 7

```php
/**
 * Base class for WordPress REST API endpoints.
 */
abstract class MyPlugin_AbstractEndpoint implements MyPlugin_EndpointInterface
{
    /**
     * Get the callback used by the REST API endpoint.
     *
     * @return callable
     */
    final public function get_callback()
    {
        return array($this, 'respond');
    }

    /**
     * Respond to a request to the REST API endpoint.
     *
     * @param WP_REST_Request $request
     *
     * @return mixed
     */
    abstract public function respond(WP_REST_Request $request);
}
```

### Example 8

```php
/**
 * A REST API response for a "200 Ok" response.
 */
class MyPlugin_OkResponse extends WP_REST_Response
{
    /**
     * Constructor.
     *
     * @param mixed $data
     * @param array $headers
     */
    public function __construct($data = null, array $headers = array())
    {
        parent::__construct($data, 200, $headers);
    }
}
```

### Example 9

```php
/**
 * A REST API response for a "201 Created" response.
 */
class MyPlugin_CreatedResponse extends WP_REST_Response
{
    /**
     * Constructor.
     *
     * @param mixed $data
     * @param array $headers
     */
    public function __construct($data = null, array $headers = array())
    {
        parent::__construct($data, 201, $headers);
    }
}
```

### Example 10

```php
/**
 * A WordPress error representing a "404 Not Found" REST API response.
 */
class MyPlugin_NotFoundError extends WP_Error
{
    /**
     * Constructor.
     *
     * @param string $code
     * @param string $message
     */
    public function __construct($code = '', $message = '')
    {
        parent::__construct($code, $message, array('status' => 404));
    }
}
```

### Example 11

```php
/**
 * A WordPress error representing a "404 Not Found" REST API response.
 */
class NotFoundError extends WP_Error
{
    /**
     * Constructor.
     *
     * @param string $code
     * @param string $message
     * @param mixed  $data
     */
    public function __construct($code = '', $message = '', $data = '')
    {
        if (!is_array($data)) {
            $data = (array) $data;
        }

        $data = array_merge($data, array('status' => 404));

        parent::__construct($code, $message, $data);
    }
}
```

### Example 12

```php
/**
 * Register an endpoint with the WordPress REST API.
 *
 * @param MyPlugin_EndpointInterface $endpoint
 */
function myplugin_register_endpoint(MyPlugin_EndpointInterface $endpoint)
{
    register_rest_route('myplugin/v1', $endpoint->get_path(), array(
        'args' => $endpoint->get_arguments(),
        'callback' => $endpoint->get_callback(),
        'methods' => $endpoint->get_methods(),
        'permission_callback' => $endpoint->get_permission_callback(),
    ));
}

/**
 * Register all our endpoints with the WordPress REST API.
 */
function myplugin_register_endpoints()
{
    $endpoints = apply_filters('myplugin_endpoints', array(
        // ...
    ));
    
    foreach ($endpoints as $endpoint) {
        myplugin_register_endpoint($endpoint);
    }
}
add_action('rest_api_init', 'myplugin_register_endpoints');
```

### Example 13

```php
/**
 * Subscriber that manages the integration with the WordPress REST API.
 */
class MyPlugin_RestApiSubscriber implements MyPlugin_SubscriberInterface
{
    /**
     * The WordPress REST API endpoints used by the plugin.
     *
     * @var MyPlugin_EndpointInterface[]
     */
    private $endpoints;

    /**
     * The namespace of the WordPress REST API endpoints managed by the subscriber.
     *
     * @var string
     */
    private $namespace;

    /**
     * Constructor.
     *
     * @param string                       $namespace;
     * @param MyPlugin_EndpointInterface[] $endpoints
     */
    public function __construct($namespace, array $endpoints = array())
    {
        $this->endpoints = array();
        $this->namespace = trim($namespace, '/');

        foreach ($endpoints as $endpoint) {
            $this->add_endpoint($endpoint);
        }
    }

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
            'rest_api_init' => 'register_endpoints',
        );
    }

    /**
     * Register endpoints with the WordPress REST API.
     */
    public function register_endpoints()
    {
        foreach ($this->endpoints as $endpoint) {
            $this->register_endpoint($endpoint);
        }
    }

    /**
     * Add a new WordPress REST API endpoint to the subscriber.
     *
     * @param MyPlugin_EndpointInterface $endpoint
     */
    private function add_endpoint(MyPlugin_EndpointInterface $endpoint)
    {
        $this->endpoints[] = $endpoint;
    }

    /**
     * Get the arguments used to configure the endpoint with the WordPress REST API server.
     *
     * @param MyPlugin_EndpointInterface $endpoint
     *
     * @return array
     */
    private function get_arguments(MyPlugin_EndpointInterface $endpoint)
    {
        return array(
            'args' => $endpoint->get_arguments(),
            'callback' => $endpoint->get_callback(),
            'methods' => $endpoint->get_methods(),
            'permission_callback' => $endpoint->get_permission_callback(),
        );
    }

    /**
     * Register the given endpoint with the WordPress REST API.
     *
     * @param MyPlugin_EndpointInterface $endpoint
     */
    private function register_endpoint(MyPlugin_EndpointInterface $endpoint)
    {
        register_rest_route($this->namespace, $endpoint->get_path(), $this->get_arguments($endpoint));
    }
}
```

### Example 14

```php
/**
 * Subscriber that manages the integration with the WordPress REST API.
 */
class MyPlugin_RestApiSubscriber implements MyPlugin_SubscriberInterface
{
    /**
     * The WordPress REST API endpoints used by the plugin.
     *
     * @var MyPlugin_EndpointInterface[]
     */
    private $endpoints;

    /**
     * The namespace of the WordPress REST API endpoints managed by the subscriber.
     *
     * @var string
     */
    private $namespace;

    /**
     * Constructor.
     *
     * @param string                       $namespace;
     * @param MyPlugin_EndpointInterface[] $endpoints
     */
    public function __construct($namespace, array $endpoints = array())
    {
        $this->endpoints = array();
        $this->namespace = trim($namespace, '/');

        foreach ($endpoints as $endpoint) {
            $this->add_endpoint($endpoint);
        }
    }

    // ...

    /**
     * Add a new WordPress REST API endpoint to the subscriber.
     *
     * @param MyPlugin_EndpointInterface $endpoint
     */
    private function add_endpoint(MyPlugin_EndpointInterface $endpoint)
    {
        $this->endpoints[] = $endpoint;
    }

    // ...
}
```

### Example 15

```php
/**
 * Subscriber that manages the integration with the WordPress REST API.
 */
class MyPlugin_RestApiSubscriber implements MyPlugin_SubscriberInterface
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
            'rest_api_init' => 'register_endpoints',
        );
    }

    /**
     * Register endpoints with the WordPress REST API.
     */
    public function register_endpoints()
    {
        foreach ($this->endpoints as $endpoint) {
            $this->register_endpoint($endpoint);
        }
    }

    // ...

    /**
     * Get the arguments used to configure the endpoint with the WordPress REST API server.
     *
     * @param MyPlugin_EndpointInterface $endpoint
     *
     * @return array
     */
    private function get_arguments(MyPlugin_EndpointInterface $endpoint)
    {
        return array(
            'args' => $endpoint->get_arguments(),
            'callback' => $endpoint->get_callback(),
            'methods' => $endpoint->get_methods(),
            'permission_callback' => $endpoint->get_permission_callback(),
        );
    }

    /**
     * Register the given endpoint with the WordPress REST API.
     *
     * @param MyPlugin_EndpointInterface $endpoint
     */
    private function register_endpoint(MyPlugin_EndpointInterface $endpoint)
    {
        register_rest_route($this->namespace, $endpoint->get_path(), $this->get_arguments($endpoint));
    }
}
```

## Source

https://carlalexander.ca/designing-system-wordpress-rest-api-endpoints/
