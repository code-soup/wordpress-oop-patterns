---
title: "Designing classes for the WordPress options API
			

			

				Much like the plugin API, it’s almost impossible to build a plugin without using the options API. This can be a problem if you’re trying to learn object-oriented programming with WordPress. You need a way to build a class around it.
Lucky for us, this is a lot less complicated to do than with the plugin API. The options API is really nothing more than an API around a data store. Our job as designers is simple. We need to design a class that mirrors this API.
That said, we don’t have to limit ourselves to just copying the options API as is. We can also push things further by adding some extra functionality around it. This is what makes designing a class around the options API so interesting.

Review options API"
url: https://carlalexander.ca/designing-classes-wordpress-options-api/
slug: designing-classes-wordpress-options-api
fetched: 2026-11-18
---

# Designing classes for the WordPress options API
			

			

				Much like the plugin API, it’s almost impossible to build a plugin without using the options API. This can be a problem if you’re trying to learn object-oriented programming with WordPress. You need a way to build a class around it.
Lucky for us, this is a lot less complicated to do than with the plugin API. The options API is really nothing more than an API around a data store. Our job as designers is simple. We need to design a class that mirrors this API.
That said, we don’t have to limit ourselves to just copying the options API as is. We can also push things further by adding some extra functionality around it. This is what makes designing a class around the options API so interesting.

Review options API

## Summary

Encapsulating WordPress options in classes. Type-safe option retrieval and storage using OOP wrappers.

## Code examples

### Example 1

```php
/**
 * Manages options using the WordPress options API.
 */
class MyPlugin_Options
{
    /**
     * Gets the option for the given name. Returns the default value if the value does not exist.
     *
     * @param string $name
     * @param mixed  $default
     *
     * @return mixed
     */
    public function get($name, $default = null)
    {
        return get_option($name, $default);
    }

    /**
     * Removes the option with the given name.
     *
     * @param string $name
     */
    public function remove($name)
    {
        delete_option($name);
    }

    /**
     * Sets an option. Overwrites the existing option if the name is already in use.
     *
     * @param string $name
     * @param mixed  $value
     */
    public function set($name, $value)
    {
        update_option($name, $value);
    }
}
```

### Example 2

```php
/**
 * Manages options using the WordPress options API.
 */
class MyPlugin_Options
{
    // ...

    /**
     * Checks if the option with the given name exists or not.
     *
     * @param string $name
     *
     * @return bool
     */
    public function has($name)
    {
        return null !== $this->get($name);
    }

    // ...
}
```

### Example 3

```php
update_option('myplugin_option', array());
```

### Example 4

```php
$maybe_array = get_option('myplugin_option', array());

foreach ($maybe_array as $item) {
    // ...
}
```

### Example 5

```php
$maybe_array = (array) get_option('myplugin_option', array());

foreach ($maybe_array as $item) {
    // ...
}
```

### Example 6

```php
/**
 * Manages options using the WordPress options API.
 */
class MyPlugin_Options
{
    // ...

    /**
     * Gets the option for the given name. Returns the default value if the value does not exist.
     *
     * @param string $name
     * @param mixed  $default
     *
     * @return mixed
     */
    public function get($name, $default = null)
    {
        $option = get_option($name, $default);

        if (is_array($default) && !is_array($option)) {
            $option = (array) $option;
        }

        return $option;
    }

    // ...
}
```

### Example 7

```php
/**
 * Manages options using the WordPress options API.
 */
class MyPlugin_Options
{
    /**
     * The prefix used by all option names.
     *
     * @var string
     */
    private $prefix;

    /**
     * Constructor.
     *
     * @param string $prefix
     */
    public function __construct($prefix = '')
    {
        $this->prefix = $prefix;
    }

    // ...
}
```

### Example 8

```php
/**
 * Manages options using the WordPress options API.
 */
class MyPlugin_Options
{
    // ...

    /**
     * Gets the option for the given name. Returns the default value if the value does not exist.
     *
     * @param string $name
     * @param mixed  $default
     *
     * @return mixed
     */
    public function get($name, $default = null)
    {
        $option = get_option($this->prefix . $name, $default);

        if (is_array($default) && !is_array($option)) {
            $option = (array) $option;
        }

        return $option;
    }

    /**
     * Checks if the option with the given name exists or not.
     *
     * @param string $name
     *
     * @return bool
     */
    public function has($name)
    {
        return null !== $this->get($name);
    }

    /**
     * Removes the option with the given name.
     *
     * @param string $name
     */
    public function remove($name)
    {
        delete_option($this->prefix . $name);
    }

    /**
     * Sets an option. Overwrites the existing option if the name is already in use.
     *
     * @param string $name
     * @param mixed  $value
     */
    public function set($name, $value)
    {
        update_option($this->prefix . $name, $value);
    }
}
```

### Example 9

```php
/**
 * Manages options using the WordPress options API using a prefix.
 */
class MyPlugin_PrefixedOptions extends MyPlugin_Options
{
    /**
     * The prefix used by all option names.
     *
     * @var string
     */
    private $prefix;

    /**
     * Constructor.
     *
     * @param string $prefix
     */
    public function __construct($prefix)
    {
        $this->prefix = $prefix;
    }

    /**
     * Gets the option for the given name. Returns the default value if the value does not exist.
     *
     * @param string $name
     * @param mixed  $default
     *
     * @return mixed
     */
    public function get($name, $default = null)
    {
        return parent::get($this->prefix.$name, $default);
    }

    /**
     * Checks if the option with the given name exists or not.
     *
     * @param string $name
     *
     * @return bool
     */
    public function has($name)
    {
        return parent::has($name);
    }

    /**
     * Removes the option with the given name.
     *
     * @param string $name
     */
    public function remove($name)
    {
        parent::remove($this->prefix.$name);
    }

    /**
     * Sets an option. Overwrites the existing option if the name is already in use.
     *
     * @param string $name
     * @param mixed  $value
     */
    public function set($name, $value)
    {
        parent::set($this->prefix.$name, $value);
    }
}
```

### Example 10

```php
/**
 * Manages options using the WordPress options API.
 */
class MyPlugin_Options
{
    /**
     * The prefix used by all option names.
     *
     * @var string
     */
    private $prefix;

    /**
     * Constructor.
     *
     * @param string $prefix
     */
    public function __construct($prefix = '')
    {
        $this->prefix = $prefix;
    }

    /**
     * Get the option name used to store the option in the WordPress database.
     *
     * @param string $name
     *
     * @return string
     */
    public function get_option_name($name)
    {
        return $this->prefix . $name;
    }

    // ...
}
```

### Example 11

```php
/**
 * Manages options using the WordPress options API.
 */
class MyPlugin_Options
{
    // ...

    /**
     * Gets the option for the given name. Returns the default value if the value does not exist.
     *
     * @param string $name
     * @param mixed  $default
     *
     * @return mixed
     */
    public function get($name, $default = null)
    {
        $option = get_option($this->get_option_name($name), $default);

        if (is_array($default) && !is_array($option)) {
            $option = (array) $option;
        }

        return $option;
    }

    /**
     * Checks if the option with the given name exists or not.
     *
     * @param string $name
     *
     * @return bool
     */
    public function has($name)
    {
        return null !== $this->get($name);
    }

    /**
     * Removes the option with the given name.
     *
     * @param string $name
     */
    public function remove($name)
    {
        delete_option($this->get_option_name($name));
    }

    /**
     * Sets an option. Overwrites the existing option if the name is already in use.
     *
     * @param string $name
     * @param mixed  $value
     */
    public function set($name, $value)
    {
        update_option($this->get_option_name($name), $value);
    }
}
```

### Example 12

```php
register_setting('myplugin_admin', $options->get_option_name('option_name'));
```

### Example 13

```php
/**
 * Manages site options using the WordPress options API.
 */
class MyPlugin_SiteOptions
{
    /**
     * Gets the site option for the given name. Returns the default value if the value does not exist.
     *
     * @param string $name
     * @param mixed  $default
     *
     * @return mixed
     */
    public function get($name, $default = null)
    {
        $option = get_site_option($name, $default);

        if (is_array($default) && !is_array($option)) {
            $option = (array) $option;
        }

        return $option;
    }

    /**
     * Checks if the site option with the given name exists or not.
     *
     * @param string $name
     *
     * @return bool
     */
    public function has($name)
    {
        return null !== $this->get($name);
    }

    /**
     * Removes the site option with the given name.
     *
     * @param string $name
     */
    public function remove($name)
    {
        delete_site_option($name);
    }

    /**
     * Sets a site option. Overwrites the existing site option if the name is already in use.
     *
     * @param string $name
     * @param mixed  $value
     */
    public function set($name, $value)
    {
        update_site_option($name, $value);
    }
}
```

### Example 14

```php
abstract class MyPlugin_AbstractOptions
{
    /**
     * Checks if the option with the given name exists or not.
     *
     * @param string $name
     *
     * @return bool
     */
    public function has($name)
    {
        return null !== $this->get($name);
    }

    /**
     * Gets the option for the given name. Returns the default value if the value does not exist.
     *
     * @param string $name
     * @param mixed  $default
     *
     * @return mixed
     */
    abstract public function get($name, $default = null);

    /**
     * Removes the option with the given name.
     *
     * @param string $name
     */
    abstract public function remove($name);

    /**
     * Sets an option. Overwrites the existing option if the name is already in use.
     *
     * @param string $name
     * @param mixed  $value
     */
    abstract public function set($name, $value);
}
```

### Example 15

```php
/**
 * Manages options using the WordPress options API.
 */
class MyPlugin_Options extends MyPlugin_AbstractOptions
{
    /**
     * Gets the option for the given name. Returns the default value if the value does not exist.
     *
     * @param string $name
     * @param mixed  $default
     *
     * @return mixed
     */
    public function get($name, $default = null)
    {
        $option = get_option($name, $default);

        if (is_array($default) && !is_array($option)) {
            $option = (array) $option;
        }

        return $option;
    }

    /**
     * Removes the option with the given name.
     *
     * @param string $name
     */
    public function remove($name)
    {
        delete_option($name);
    }

    /**
     * Sets an option. Overwrites the existing option if the name is already in use.
     *
     * @param string $name
     * @param mixed  $value
     */
    public function set($name, $value)
    {
        update_option($name, $value);
    }
}

/**
 * Manages site options using the WordPress options API.
 */
class MyPlugin_SiteOptions extends MyPlugin_AbstractOptions
{
    /**
     * Gets the site option for the given name. Returns the default value if the value does not exist.
     *
     * @param string $name
     * @param mixed  $default
     *
     * @return mixed
     */
    public function get($name, $default = null)
    {
        $option = get_site_option($name, $default);

        if (is_array($default) && !is_array($option)) {
            $option = (array) $option;
        }

        return $option;
    }

    /**
     * Removes the site option with the given name.
     *
     * @param string $name
     */
    public function remove($name)
    {
        delete_site_option($name);
    }

    /**
     * Sets a site option. Overwrites the existing site option if the name is already in use.
     *
     * @param string $name
     * @param mixed  $value
     */
    public function set($name, $value)
    {
        update_site_option($name, $value);
    }
}
```

## Source

https://carlalexander.ca/designing-classes-wordpress-options-api/
