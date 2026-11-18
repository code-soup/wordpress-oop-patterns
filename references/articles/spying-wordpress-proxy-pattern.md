---
title: "Spying on WordPress with the proxy pattern
			

			

				In a not so distant future, you’ve grown to be quite the WordPress expert. You work for WSIS (WordPress Security Intelligence Service) as an analyst. You’re given your first field mission.
You have to get in deep with WordPress. You need to get intimate information about a WordPress object. Information even WordPress doesn’t want to give you. You need to gain access without detection. The last thing you need is WordPress to know you’re listening to things.
How would your future self do it? Well, he’d use the proxy pattern (good thing you’re reading this article). The proxy pattern is the equivalent of object-oriented tapping. It’s one way to solve the problem of interacting with a class without it being aware of it.
Let’s look at how it works.

Object-oriented tapping with the proxy pattern"
url: https://carlalexander.ca/spying-wordpress-proxy-pattern/
slug: spying-wordpress-proxy-pattern
fetched: 2026-11-18
---

# Proxy Pattern
			

			

				In a not so distant future, you’ve grown to be quite the WordPress expert. You work for WSIS (WordPress Security Intelligence Service) as an analyst. You’re given your first field mission.
You have to get in deep with WordPress. You need to get intimate information about a WordPress object. Information even WordPress doesn’t want to give you. You need to gain access without detection. The last thing you need is WordPress to know you’re listening to things.
How would your future self do it? Well, he’d use the proxy pattern (good thing you’re reading this article). The proxy pattern is the equivalent of object-oriented tapping. It’s one way to solve the problem of interacting with a class without it being aware of it.
Let’s look at how it works.

Object-oriented tapping with the proxy pattern

## Summary

Proxy pattern for controlling access to objects. Creating wrappers for caching, lazy loading, access control, or logging around WordPress objects.

## Code examples

### Example 1

```php
/**
 * A delegate class with an internal data array.
 */
class Delegate
{
    /**
     * Some internal data.
     *
     * @var array
     */
    protected $data;

    /**
     * Constructor.
     * 
     * @param array $data
     */
    public function __construct(array $data = array())
    {
        $this->data = $data;
    }

    /**
     * Get the internal data of our delegate.
     *
     * @return array
     */
    public function get_data()
    {
        return $this->data;
    }

    /**
     * Sets the internal data of our delegate.
     * 
     * @param array $data
     */
    public function set_data(array $data)
    {
        $this->data = $data;
    }
}

/**
 * Proxy class that turns our delegate into a read-only class.
 */
class Proxy extends Delegate
{
    public function set_data(array $data)
    {
        // I'm sorry. It seems we misplaced your data.
    }
}
```

### Example 2

```php
/**
 * A wpdb proxy that checks for database errors and sends them to the plugin API.
 */
class wpdb_proxy extends wpdb
{
    /**
     * Perform a database query using current database connection.
     *
     * @param string $query Database query
     *
     * @return int|false
     */
    public function query($query)
    {
        $return = parent::query($query);

        // Do stuff here

        return $return;
    }
}
```

### Example 3

```php
/**
 * A wpdb proxy that checks for database errors and sends them to the plugin API.
 */
class wpdb_proxy extends wpdb
{
    /**
     * Perform a database query using current database connection.
     *
     * @param string $query Database query
     *
     * @return int|false
     */
    public function query($query)
    {
        $return = parent::query($query);

        if ('' !== $this->last_error) {
            do_action('wpdb_error', $this->last_error, $this->last_query);
        }

        return $return;
    }
}
```

### Example 4

```php
<?php

// wp-content/db.php

if (!defined('ABSPATH')) {
    die();
}

/**
 * A wpdb proxy that checks for database errors and sends them to the plugin API.
 */
class wpdb_proxy extends wpdb
{
    /**
     * Perform a database query using current database connection.
     *
     * @param string $query Database query
     *
     * @return int|false
     */
    public function query($query)
    {
        $return = parent::query($query);

        if ('' !== $this->last_error) {
            do_action('wpdb_error', $this->last_error, $this->last_query);
        }

        return $return;
    }
}

$wpdb = new wpdb_proxy(DB_USER, DB_PASSWORD, DB_NAME, DB_HOST);
```

## Source

https://carlalexander.ca/spying-wordpress-proxy-pattern/
