---
title: "Designing a system: WordPress routing
			

			

				Developers use WordPress to build all sorts of solutions. They can range from a small website to large application platforms. The larger the project gets, the more common it is to have the need for WordPress to handle custom URLs.
You might want to map a custom URL to a new template, a specific hook or both. These situations get more and more common as you work on larger WordPress projects. This type of problem is a bit of a growing up pain with WordPress.
In framework land, there’s a tool that helps you with that problem. It’s called the routing system. It’s a critical component of most frameworks. It lets you map URLs with different parts of your application.
It’s a tough problem to solve, but a good example of object-oriented design. That’s why we’re going to build one. It’ll show you how object-oriented programming helps you solve harder problems.

But isn’t this the job of the rewrite API?
Not quite. (But excellent question!) The rewrite API allows WordPress to understand human-readable URLs. There’s no question that it’s an important task.
That said, a routing system is a large enough problem that it’s made up of smaller sub-problems. Solving these sub-problems is necessary for the routing system to do its job. And, as you’ll see next, the rewrite API itself only takes care of one of these sub-problems.
The responsibilities of a routing system"
url: https://carlalexander.ca/designing-system-wordpress-routing/
slug: designing-system-wordpress-routing
fetched: 2026-11-18
---

# Designing a system: WordPress routing
			

			

				Developers use WordPress to build all sorts of solutions. They can range from a small website to large application platforms. The larger the project gets, the more common it is to have the need for WordPress to handle custom URLs.
You might want to map a custom URL to a new template, a specific hook or both. These situations get more and more common as you work on larger WordPress projects. This type of problem is a bit of a growing up pain with WordPress.
In framework land, there’s a tool that helps you with that problem. It’s called the routing system. It’s a critical component of most frameworks. It lets you map URLs with different parts of your application.
It’s a tough problem to solve, but a good example of object-oriented design. That’s why we’re going to build one. It’ll show you how object-oriented programming helps you solve harder problems.

But isn’t this the job of the rewrite API?
Not quite. (But excellent question!) The rewrite API allows WordPress to understand human-readable URLs. There’s no question that it’s an important task.
That said, a routing system is a large enough problem that it’s made up of smaller sub-problems. Solving these sub-problems is necessary for the routing system to do its job. And, as you’ll see next, the rewrite API itself only takes care of one of these sub-problems.
The responsibilities of a routing system

## Summary

Custom routing systems beyond WordPress rewrite rules. Creating route definitions and dispatchers for complex applications.

## Code examples

### Example 1

```php
class Route
{
    /**
     * The hook called when this route is matched.
     *
     * @var string
     */
    private $hook;

    /**
     * The URL path that the route needs to match.
     *
     * @var string
     */
    private $path;

    /**
     * The template that the route wants to load.
     *
     * @var string
     */
    private $template;

    /**
     * Constructor.
     *
     * @param string $path
     * @param string $hook
     * @param string $template
     */
    public function __construct($path, $hook = '', $template = '')
    {
        $this->hook = $hook;
        $this->path = $path;
        $this->template = $template;
    }
}
```

### Example 2

```php
class Route
{
    // ...

    /**
     * Get the hook called when this route is matched.
     *
     * @return string
     */
    public function get_hook()
    {
        return $this->hook;
    }

    /**
     * Get the URL path that the route needs to match.
     *
     * @return string
     */
    public function get_path()
    {
        return $this->path;
    }

    /**
     * Get the template that the route wants to load.
     *
     * @return string
     */
    public function get_template()
    {
        return $this->template;
    }
}
```

### Example 3

```php
class Route
{
    // ...

    /**
     * Checks if this route want to call a hook when matched.
     *
     * @return bool
     */
    public function has_hook()
    {
        return !empty($this->hook);
    }

    /**
     * Checks if this route want to load a template when matched.
     *
     * @return bool
     */
    public function has_template()
    {
        return !empty($this->template);
    }
}
```

### Example 4

```php
class Router
{
    /**
     * All registered routes.
     *
     * @var array
     */
    private $routes;

    /**
     * Constructor.
     *
     * @param array $routes
     */
    public function __construct(array $routes = array())
    {
        $this->routes = $routes;
    }
}
```

### Example 5

```php
class Router
{
    // ...

    /**
     * Add a route to the router.
     *
     * @param Route $route
     */
    public function add_route(Route $route)
    {
        $this->routes[] = $route;
    }
}
```

### Example 6

```php
class Router
{
    /**
     * All registered routes.
     *
     * @var Route[]
     */
    private $routes;

    /**
     * Constructor.
     *
     * @param Route[] $routes
     */
    public function __construct(array $routes = array())
    {
        $this->routes = array();

        foreach ($routes as $name => $route) {
            $this->add_route($name, $route);
        }
    }

    // ...
}
```

### Example 7

```php
add_rewrite_rule('^my-plugin$', 'index.php?route_name=my_plugin_index');
```

### Example 8

```php
class Router
{
    // ...

    /**
     * Adds a new WordPress rewrite rule for the given Route.
     *
     * @param string $name
     * @param Route  $route
     */
    private function add_rule($name, Route $route)
    {
        // ...
    }
}
```

### Example 9

```php
class Router
{
    // ...

    /**
     * Add a route to the router. Overwrites a route if it shares the same name as an already registered one.
     *
     * @param string $name
     * @param Route  $route
     */
    public function add_route($name, Route $route)
    {
        $this->routes[$name] = $route;
    }

    // ...
}
```

### Example 10

```php
class Router
{
    /**
     * All registered routes.
     *
     * @var Route[]
     */
    private $routes;

    /**
     * Query variable used to identify routes.
     *
     * @var string
     */
    private $route_variable;

    /**
     * Constructor.
     *
     * @param string  $route_variable
     * @param Route[] $routes
     */
    public function __construct($route_variable = 'route_name', array $routes = array())
    {
        $this->routes = array();
        $this->route_variable = $route_variable;

        foreach ($routes as $name => $route) {
            $this->add_route($name, $route);
        }
    }

    // ...
}
```

### Example 11

```php
class Router
{
    // ...

    /**
     * Generates the regex for the WordPress rewrite API for the given route.
     *
     * @param Route $route
     *
     * @return string
     */
    private function generate_route_regex(Route $route)
    {
        return '^'.ltrim(trim($route->get_path()), '/').'$';
    }
}
```

### Example 12

```php
class Router
{
    // ...

    /**
     * Adds a new WordPress rewrite rule for the given Route.
     *
     * @param string $name
     * @param Route  $route
     * @param string $position
     */
    private function add_rule($name, Route $route, $position = 'top')
    {
        add_rewrite_rule($this->generate_route_regex($route), 'index.php?'.$this->route_variable.'='.$name, $position);
    }

   // ...
}
```

### Example 13

```php
class Router
{
    // ...

    /**
     * Compiles the router into WordPress rewrite rules.
     */
    public function compile()
    {
        foreach ($this->routes as $name => $route) {
            $this->add_rule($name, $route);
        }
    }

    // ...
}
```

### Example 14

```php
class Router
{
    // ...

    /**
     * Compiles the router into WordPress rewrite rules.
     */
    public function compile()
    {
        add_rewrite_tag('%'.$this->route_variable.'%', '(.+)');

        foreach ($this->routes as $name => $route) {
            $this->add_rule($name, $route);
        }
    }

    // ...
}
```

### Example 15

```php
class Router
{
    // ...

    /**
     * Tries to find a matching route using the given query variables. Returns the matching route
     * or a WP_Error.
     *
     * @param array $query_variables
     *
     * @return Route|WP_Error
     */
    public function match(array $query_variables)
    {
        if (empty($query_variables[$this->route_variable])) {
            return new WP_Error('missing_route_variable');
        }

        $route_name = $query_variables[$this->route_variable];

        if (!isset($this->routes[$route_name])) {
            return new WP_Error('route_not_found');
        }

        return $this->routes[$route_name];
    }

    // ...
}
```

### Example 16

```php
class Processor
{
    /**
     * The router.
     *
     * @var Router
     */
    private $router;

    /**
     * Constructor.
     *
     * @param Router $router
     */
    public function __construct(Router $router)
    {
        $this->router = $router;
    }

    /**
     * Initialize processor with WordPress.
     *
     * @param Router $router
     */
    public static function init(Router $router)
    {
        $self = new self($router);
    }
}
```

### Example 17

```php
$router = new Router('my_plugin_route_name');

Processor::init($router);
```

### Example 18

```php
class Processor
{
    /**
     * The router.
     *
     * @var Router
     */
    private $router;

    /**
     * The routes we want to register with WordPress.
     *
     * @var Route[]
     */
    private $routes;

    /**
     * Constructor.
     *
     * @param Router  $router
     * @param Route[] $routes
     */
    public function __construct(Router $router, array $routes = array())
    {
        $this->router = $router;
        $this->routes = $routes;
    }

    /**
     * Initialize processor with WordPress.
     *
     * @param Router  $router
     * @param Route[] $routes
     */
    public static function init(Router $router, array $routes = array())
    {
        $self = new self($router, $routes);
    }
}
```

### Example 19

```php
$router = new Router('my_plugin_route_name');
$routes = array(
    'my_plugin_index' => new Route('/my-plugin'),
);

Processor::init($router, $routes);
```

### Example 20

```php
class Processor
{
    // ...

    /**
     * Initialize processor with WordPress.
     *
     * @param Router  $router
     * @param Route[] $routes
     */
    public static function init(Router $router, array $routes = array())
    {
        $self = new self($router, $routes);

        add_action('init', array($self, 'register_routes'));
    }

    /**
     * Register all our routes into WordPress.
     */
    public function register_routes()
    {
        $routes = apply_filters('my_plugin_routes', $this->routes);

        foreach ($routes as $name => $route) {
            $this->router->add_route($name, $route);
        }
    }
}
```

### Example 21

```php
class Processor
{
    // ...

    /**
     * Register all our routes into WordPress.
     */
    public function register_routes()
    {
        $routes = apply_filters('my_plugin_routes', $this->routes);

        foreach ($routes as $name => $route) {
            $this->router->add_route($name, $route);
        }

        $this->router->compile();
    }
}
```

### Example 22

```php
class Processor
{
    // ...

    /**
     * Register all our routes into WordPress.
     */
    public function register_routes()
    {
        $routes = apply_filters('my_plugin_routes', $this->routes);

        foreach ($routes as $name => $route) {
            $this->router->add_route($name, $route);
        }

        $this->router->compile();

        $routes_hash = md5(serialize($routes));

        if ($routes_hash != get_option('my_plugin_routes_hash')) {
            flush_rewrite_rules();
            update_option('my_plugin_routes_hash', $routes_hash);
        }
    }
}
```

### Example 23

```php
class Processor
{
    // ...

    /**
     * Initialize processor with WordPress.
     *
     * @param Router  $router
     * @param Route[] $routes
     */
    public static function init(Router $router, array $routes = array())
    {
        $self = new self($router, $routes);

        add_action('init', array($self, 'register_routes'));
        add_action('parse_request', array($self, 'match_request'));;
    }

    /**
     * Attempts to match the current request to a route.
     *
     * @param WP $environment
     */
    public function match_request(WP $environment)
    {
        $matched_route = $this->router->match($environment->query_vars);

        if ($matched_route instanceof Route) {
            $this->matched_route = $matched_route;
        }
    }

    // ...
}
```

### Example 24

```php
class Processor
{
    /**
     * Attempts to match the current request to a route.
     *
     * @param WP $environment
     */
    public function match_request(WP $environment)
    {
        $matched_route = $this->router->match($environment->query_vars);

        if ($matched_route instanceof Route) {
            $this->matched_route = $matched_route;
        }

        if ($matched_route instanceof \WP_Error && in_array('route_not_found', $matched_route->get_error_codes())) {
            wp_die($matched_route, 'Route Not Found', array('response' => 404));
        }
    }
}
```

### Example 25

```php
class Processor
{
    // ...

    /**
     * Initialize processor with WordPress.
     *
     * @param Router  $router
     * @param Route[] $routes
     */
    public static function init(Router $router, array $routes = array())
    {
        $self = new self($router, $routes);

        add_action('init', array($self, 'register_routes'));
        add_action('parse_request', array($self, 'match_request'));
        add_action('template_redirect', array($self, 'call_route_hook'));
    }

    /**
     * Checks to see if a route was found. If there's one, it calls the route hook.
     */
    public function call_route_hook()
    {
        // ...
    }

    // ...
}
```

### Example 26

```php
class Processor
{
    // ...

    /**
     * Checks to see if a route was found. If there's one, it calls the route hook.
     */
    public function call_route_hook()
    {
        if (!$this->matched_route instanceof Route || !$this->matched_route->has_hook()) {
            return;
        }

        do_action($this->matched_route->get_hook());
    }

    // ...
}
```

### Example 27

```php
class Processor
{
    // ...

    /**
     * Initialize processor with WordPress.
     *
     * @param Router  $router
     * @param Route[] $routes
     */
    public static function init(Router $router, array $routes = array())
    {
        $self = new self($router, $routes);

        add_action('init', array($self, 'register_routes'));
        add_action('parse_request', array($self, 'match_request'));
        add_action('template_include', array($self, 'load_route_template'));
        add_action('template_redirect', array($self, 'call_route_hook'));
    }

    /**
     * Checks to see if a route was found. If there's one, it loads the route template.
     *
     * @param string $template
     *
     * @return string
     */
    public function load_route_template($template)
    {
        if (!$this->matched_route instanceof Route || !$this->matched_route->has_template()) {
            return $template;
        }

        $route_template = get_query_template($this->matched_route->get_template());

        if (!empty($route_template)) {
            $template = $route_template;
        }

        return $template;
    }

    // ...
}
```

### Example 28

```php
$router = new Router('my_plugin_route_name');
$routes = array(
    'my_plugin_index' => new Route('/my-plugin', '', 'my-plugin-index'),
    'my_plugin_redirect' => new Route('/my-plugin/redirect', 'my_plugin_redirect'),
);

Processor::init($router, $routes);
```

### Example 29

```php
function my_plugin_redirect()
{
    $location = '/';

    if (!empty($_GET['location'])) {
        $location = $_GET['location'];
    }

    wp_redirect($location);
}
add_action('my_plugin_redirect', 'my_plugin_redirect');
```

## Source

https://carlalexander.ca/designing-system-wordpress-routing/
