---
title: "Using dependency injection with WordPress
			

			

				As you use object-oriented programming with WordPress more and more, you’re going to encounter new sets of problems. These problems aren’t as simple as the ones that you encountered when you started. But that’s also good news. It also means that you’re making progress.
One set of problems that you start to encounter as you advance in your use of object-oriented programming deal with scaling. As your code has more and more classes, it becomes a challenge to assemble these classes together. That’s why in the past we looked at how to design a class whose job was to do that.
But there are other problems that come with having a lot of classes in your code. It’s how much your classes depend on other classes. This is what we call coupling in programming. (Not just object-oriented programming.)
To help with coupling, a famous software engineer (Robert C. Martin who’s also known as Uncle Bob) created the dependency inversion principle. It helps you decouple your classes by making dependencies external to them. (There’s more to it than that. But this is one of the core elements of the dependency inversion principle.)
This reduces coupling but creates a new problem as well. That problem is that you can’t initialize objects inside your class anymore. You have to pass them to your own object through its constructor or some other method like a setter method.
This makes it even harder to assemble your classes together. This is why software engineers created dependency injection. It’s a programming technique that helps solve this problem.
Most web application frameworks use it in some form or another. But that’s not the case with WordPress since a lot of its code isn’t object-oriented. That said, if you want to build an object-oriented plugin for WordPress, it’s pretty much mandatory. Lucky for us, it’s not that hard to use dependency injection in your own code!

A small warning about PHP versions"
url: https://carlalexander.ca/dependency-injection-wordpress/
slug: dependency-injection-wordpress
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/using-dependency-injection-wordpress/
---

# Using dependency injection with WordPress
			

			

				As you use object-oriented programming with WordPress more and more, you’re going to encounter new sets of problems. These problems aren’t as simple as the ones that you encountered when you started. But that’s also good news. It also means that you’re making progress.
One set of problems that you start to encounter as you advance in your use of object-oriented programming deal with scaling. As your code has more and more classes, it becomes a challenge to assemble these classes together. That’s why in the past we looked at how to design a class whose job was to do that.
But there are other problems that come with having a lot of classes in your code. It’s how much your classes depend on other classes. This is what we call coupling in programming. (Not just object-oriented programming.)
To help with coupling, a famous software engineer (Robert C. Martin who’s also known as Uncle Bob) created the dependency inversion principle. It helps you decouple your classes by making dependencies external to them. (There’s more to it than that. But this is one of the core elements of the dependency inversion principle.)
This reduces coupling but creates a new problem as well. That problem is that you can’t initialize objects inside your class anymore. You have to pass them to your own object through its constructor or some other method like a setter method.
This makes it even harder to assemble your classes together. This is why software engineers created dependency injection. It’s a programming technique that helps solve this problem.
Most web application frameworks use it in some form or another. But that’s not the case with WordPress since a lot of its code isn’t object-oriented. That said, if you want to build an object-oriented plugin for WordPress, it’s pretty much mandatory. Lucky for us, it’s not that hard to use dependency injection in your own code!

A small warning about PHP versions

## Summary

Dependency injection fundamentals for WordPress. Constructor injection, service containers, and managing class dependencies without global state.

## Code examples

### Example 1

```php
class MyPlugin_Container
{
}
```

### Example 2

```php
class MyPlugin_Container
{
    /**
     * Values stored inside the container.
     *
     * @var array
     */
    private $values;

    /**
     * Constructor.
     *
     * @param array $values
     */
    public function __construct(array $values = array())
    {
        $this->values = $values;
    }

    // ...
}
```

### Example 3

```php
class MyPlugin_Container implements ArrayAccess
{
}
```

### Example 4

```php
class MyPlugin_Container implements ArrayAccess
{
    // ...

    /**
     * Checks if there's a value in the container for the given key.
     *
     * @param mixed $key
     *
     * @return bool
     */
    public function offsetExists($key)
    {
        return array_key_exists($key, $this->values);
    }

    /**
     * Sets a value inside of the container.
     *
     * @param mixed $key
     * @param mixed $value
     */
    public function offsetSet($key, $value)
    {
        $this->values[$key] = $value;
    }

    /**
     * Unset the value in the container for the given key.
     *
     * @param mixed $key
     */
    public function offsetUnset($key)
    {
        unset($this->values[$key]);
    }

    // ...
}
```

### Example 5

```php
$myplugin_class = function () {
    return new MyPlugin_Class();
};
```

### Example 6

```php
$myplugin_object1 = $myplugin_class();
$myplugin_object2 = $myplugin_class();
```

### Example 7

```php
$myplugin_class_service = function ()  {
    static $object;

    if (!$object instanceof MyPlugin_Class) {
        $object = new MyPlugin_Class();
    }

    return $object;
};
```

### Example 8

```php
$myplugin_object1 = $myplugin_class_service();
$myplugin_object2 = $myplugin_class_service();
```

### Example 9

```php
$container['myplugin_class'] = function () {
    return new MyPlugin_Class();
};

$myplugin_object = $container['myplugin_class'];
```

### Example 10

```php
$container['myplugin_class'] = function () {
    return new MyPlugin_Class();
};
$container['myplugin_variable'] = 'variable';

$myplugin_object = $container['myplugin_class'];
$myplugin_variable = $container['myplugin_variable'];
```

### Example 11

```php
class MyPlugin_Container implements ArrayAccess
{
    // ...

    public function offsetGet($key)
    {
        if (!array_key_exists($key, $this->values)) {
            return new WP_Error('no_value_found', sprintf('Container doesn\'t have a value stored for the "%s" key.', $key));
        }

        return $this->values[$key] instanceof Closure ? $this->values[$key]() : $this->values[$key];
    }

    // ...
}
```

### Example 12

```php
class MyPlugin_Container implements ArrayAccess
{
    // ...

   public function service(Closure $closure)
    {
        return function () use ($closure) {
            static $object;

            if (null === $object) {
                $object = $closure();
            }

            return $object;
        };
    }

    // ...
}
```

### Example 13

```php
$container['service'] = $container->service(function () {
    return new MyPlugin_Class();
});
```

### Example 14

```php
$container['myplugin_class'] = function (MyPlugin_Container $container) {
    return new MyPlugin_Class($container['service']);
};
```

### Example 15

```php
class MyPlugin_Container implements ArrayAccess
{
    // ...

    public function offsetGet($key)
    {
        if (!array_key_exists($key, $this->values)) {
            return new WP_Error('no_value_found', sprintf('Container doesn\'t have a value stored for the "%s" key.', $key));
        }

        return $this->values[$key] instanceof Closure ? $this->values[$key]($this) : $this->values[$key];
    }

    // ...

    public function service(Closure $closure)
    {
        return function (MyPlugin_Container $container) use ($closure) {
            static $object;

            if (null === $object) {
                $object = $closure($container);
            }

            return $object;
        };
    }
}
```

### Example 16

```php
interface MyPlugin_ContainerConfigurationInterface
{
    /**
     * Modifies the given dependency injection container.
     *
     * @param MyPlugin_Container $container
     */
    public function modify(MyPlugin_Container $container);
}
```

### Example 17

```php
class MyPlugin_ComponentConfiguration implements MyPlugin_ContainerConfigurationInterface
{
    public function modify(MyPlugin_Container $container)
    {
        $container['component_parameter'] = get_option('myplugin_component_parameter', 'default_value');

        $container['component_service'] = $container->service(function (MyPlugin_Container $container) {
            return new MyPlugin_ComponentClass($container['component_parameter']);
        });
    }
}
```

### Example 18

```php
class MyPlugin_WordPressConfiguration implements MyPlugin_ContainerConfigurationInterface
{
    public function modify(MyPlugin_Container $container)
    {
        $container['wordpress_database'] = $container->service(function (MyPlugin_Container $container) {
            global $wpdb;

            return $wpdb;
        });

        $container['wordpress_query'] = function (MyPlugin_Container $container) {
            return new WP_Query();
        };

        $container['wordpress_user'] = wp_get_current_user();
    }
}
```

### Example 19

```php
class MyPlugin_Container implements ArrayAccess
{
    // ...

    /**
     * Configure the container using the given container configuration objects.
     *
     * @param array $configurations
     */
    public function configure(array $configurations)
    {
        foreach ($configurations as $configuration) {
            $configuration->modify($this);
        }
    }

    // ...
}
```

### Example 20

```php
$container = new MyPlugin_Container();
$container->configure(array(
   new MyPlugin_ComponentConfiguration(), 
   new MyPlugin_WordPressConfiguration(), 
));
```

### Example 21

```php
class MyPlugin_Container implements ArrayAccess
{
    /**
     * Values stored inside the container.
     *
     * @var array
     */
    private $values;

    /**
     * Constructor.
     *
     * @param array $values
     */
    public function __construct(array $values = array())
    {
        $this->values = $values;
    }

    /**
     * Configure the container using the given container configuration objects.
     *
     * @param array $configurations
     */
    public function configure(array $configurations)
    {
        foreach ($configurations as $configuration) {
            $configuration->modify($this);
        }
    }

    /**
     * Checks if there's a value in the container for the given key.
     *
     * @param mixed $key
     *
     * @return bool
     */
    public function offsetExists($key)
    {
        return array_key_exists($key, $this->values);
    }

    /**
     * Get a value from the container.
     *
     * @param mixed $key
     *
     * @return mixed|WP_Error
     */
    public function offsetGet($key)
    {
        if (!array_key_exists($key, $this->values)) {
            return new WP_Error('no_value_found', sprintf('Container doesn\'t have a value stored for the "%s" key.', $key));
        }

        return $this->values[$key] instanceof Closure ? $this->values[$key]($this) : $this->values[$key];
    }

    /**
     * Sets a value inside of the container.
     *
     * @param mixed $key
     * @param mixed $value
     */
    public function offsetSet($key, $value)
    {
        $this->values[$key] = $value;
    }

    /**
     * Unset the value in the container for the given key.
     *
     * @param mixed $key
     */
    public function offsetUnset($key)
    {
        unset($this->values[$key]);
    }

    /**
     * Creates a closure used for creating a service using the given callable.
     *
     * @param Closure $closure
     *
     * @return Closure
     */
    public function service(Closure $closure)
    {
        return function (MyPlugin_Container $container) use ($closure) {
            static $object;

            if (null === $object) {
                $object = $closure($container);
            }

            return $object;
        };
    }
}
```

## Source

https://carlalexander.ca/dependency-injection-wordpress/
