---
title: "Helping WordPress make friends with the decorator pattern
			

			

				In some plugin circles (also know as the “cool kids club”), the coolest kid on the block is the wpdb class. Plugins go out of their way to be his friend. Lucky guy (or class)!
One plugin that has to be friends with wpdb is HyperDB. If plugins could talk, it would sound a lot like a scene from kindergarden.

HyperDB: Hey WPDB, wanna be friends? I’ll make you the strongest database class there is!

WPDB: Woah, that sounds awesome. I’m in!

HyperDB: There’s only one catch. You can’t be friends with anyone else.

WPDB: Oh ok. *sad face*
HyperDB uses the proxy pattern to give wpdb his new powers. The HyperDB class achieves that by extending the wpdb class. This is also a limitation of the proxy pattern.
A class can only extend one class. This means that it can only have one proxy (in practice). Creating a proxy prevents others from creating one. This leaves other plugins like Query Monitor in the wind.
Query Monitor: Hey WPDB, how would you like to know when you’re sick?

WPDB: I’d love to! I hate being sick.

Query Monitor: Great! All you need to do is become my friend and I’ll help you with that.

WPDB: Sorry Query Monitor, I’m already friends with HyperDB…
This situation is unfortunate for wpdb. HyperDB could use the diagnostic powers that Query Monitor provides. The proxy pattern won’t have it though. It limits these relationships to one or the other.
How can wpdb have as many friends as he wants?
The smart proxy"
url: https://carlalexander.ca/wordpress-decorator-pattern/
slug: wordpress-decorator-pattern
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/helping-wordpress-make-friends-decorator-pattern/
---

# Decorator Pattern
			

			

				In some plugin circles (also know as the “cool kids club”), the coolest kid on the block is the wpdb class. Plugins go out of their way to be his friend. Lucky guy (or class)!
One plugin that has to be friends with wpdb is HyperDB. If plugins could talk, it would sound a lot like a scene from kindergarden.

HyperDB: Hey WPDB, wanna be friends? I’ll make you the strongest database class there is!

WPDB: Woah, that sounds awesome. I’m in!

HyperDB: There’s only one catch. You can’t be friends with anyone else.

WPDB: Oh ok. *sad face*
HyperDB uses the proxy pattern to give wpdb his new powers. The HyperDB class achieves that by extending the wpdb class. This is also a limitation of the proxy pattern.
A class can only extend one class. This means that it can only have one proxy (in practice). Creating a proxy prevents others from creating one. This leaves other plugins like Query Monitor in the wind.
Query Monitor: Hey WPDB, how would you like to know when you’re sick?

WPDB: I’d love to! I hate being sick.

Query Monitor: Great! All you need to do is become my friend and I’ll help you with that.

WPDB: Sorry Query Monitor, I’m already friends with HyperDB…
This situation is unfortunate for wpdb. HyperDB could use the diagnostic powers that Query Monitor provides. The proxy pattern won’t have it though. It limits these relationships to one or the other.
How can wpdb have as many friends as he wants?
The smart proxy

## Summary

Decorator pattern for adding behavior to objects dynamically. Wrapping WordPress objects to extend functionality without modifying original classes.

## Code examples

### Example 1

```php
/**
 * Interface used by classes representing post titles.
 */
interface PostTitleInterface
{
    /**
     * Get the post title.
     *
     * @return string
     */
    public function get_title();
}

/**
 * A simple post title.
 */
class PostTitle implements PostTitleInterface
{
    /**
     * The post title.
     *
     * @var string
     */
    private $title;

    /**
     * Constructor.
     *
     * @param string $title
     */
    public function __construct($title = '')
    {
        $this->title = $title;
    }

    /**
     * Get the post title.
     *
     * @return string
     */
    public function get_title()
    {
        return $this->title;
    }
}
```

### Example 2

```php
/**
 * A sanitized post title.
 */
class SanitizedPostTitle extends PostTitle
{
    /**
     * Get the sanitized post title.
     *
     * @return string
     */
    public function get_title()
    {
        return sanitize_title(parent::get_title());
    }
}
```

### Example 3

```php
/**
 * A post title decorator that sanitizes post titles.
 */
class SanitizePostTitleDecorator implements PostTitleInterface
{
    /**
     * A post title.
     *
     * @var PostTitleInterface
     */
    private $post_title;

    /**
     * Constructor.
     *
     * @param PostTitleInterface $post_title
     */
    public function __construct(PostTitleInterface $post_title)
    {
        $this->post_title = $post_title;
    }

    /**
     * Get the sanitized post title.
     *
     * @return string
     */
    public function get_title()
    {
        return sanitize_title($this->post_title->get_title());
    }
}
```

### Example 4

```php
/**
 * A post title decorator that changes post titles to upper case.
 */
class UpperCasedPostTitleDecorator implements PostTitleInterface
{
    /**
     * A post title.
     *
     * @var PostTitleInterface
     */
    private $post_title;

    /**
     * Constructor.
     *
     * @param PostTitleInterface $post_title
     */
    public function __construct(PostTitleInterface $post_title)
    {
        $this->post_title = $post_title;
    }

    /**
     * Get the upper cased post title.
     *
     * @return string
     */
    public function get_title()
    {
        return strtoupper($this->post_title->get_title());
    }
}
```

### Example 5

```php
$post_title = new PostTitle('A post title');
$post_title = new SanitizePostTitleDecorator($post_title);
$post_title = new UpperCasedPostTitleDecorator($post_title);

// Output: A-POST-TITLE
$title = $post_title->get_title();
```

### Example 6

```php
/**
 * A blank WPDB decorator.
 */
class WPDBDecorator
{
    /**
     * The decorated instance of WPDB.
     *
     * @var mixed
     */
    private $wpdb;

    /**
     * Constructor.
     *
     * @param mixed $wpdb
     */
    public function __construct($wpdb)
    {
        $this->wpdb = $wpdb;
    }

    /**
     * Intercepts all calls to the WPDB object.
     *
     * @param string $method
     * @param array  $arguments
     *
     * @return mixed
     */
    public function __call($method, array $arguments)
    {
        return call_user_func_array(array($this->wpdb, $method), $arguments);
    }

    /**
     * Get the given WPDB variable.
     *
     * @param string $variable
     *
     * @return mixed
     */
    public function __get($variable)
    {
        return $this->wpdb->$variable;
    }

    /**
     * Sets the value of the given WPDB variable.
     *
     * @param string $variable
     * @param mixed  $value
     */
    public function __set($variable, $value)
    {
        $this->wpdb->$variable = $value;
    }

    /**
     * Checks if the given WPDB variable is set.
     *
     * @param string $variable
     *
     * @return bool
     */
    public function __isset($variable)
    {
        return isset($this->wpdb->$variable);
    }

    /**
     * Unsets the given WPDB variable.
     *
     * @param string $variable
     */
    public function __unset($variable)
    {
        unset($this->wpdb->$variable);
    }
}
```

### Example 7

```php
/**
 * Decorator for WPDB that checks for errors.
 */
class WPDBErrorCheckingDecorator
{
    /**
     * The decorated instance of WPDB.
     *
     * @var mixed
     */
    private $wpdb;

    /**
     * Constructor.
     *
     * @param mixed $wpdb
     */
    public function __construct($wpdb)
    {
        $this->wpdb = $wpdb;
    }

    /**
     * Intercepts all calls to the WPDB object. If the method is tracked, performs analysis on it.
     *
     * @param string $method
     * @param array  $arguments
     *
     * @return mixed
     */
    public function __call($method, array $arguments)
    {
        if (!in_array($method, array('delete', 'get_col', 'get_results', 'get_row', 'get_var', 'query', 'update'))) {
            return call_user_func_array(array($this->wpdb, $method), $arguments);
        }

        $return = call_user_func_array(array($this->wpdb, $method), $arguments);

        if ('' !== $this->wpdb->last_error) {
            do_action('wpdb_error', $this->wpdb->last_error, $this->wpdb->last_query);
        }

        return $return;
    }

    /**
     * Get the given WPDB variable.
     *
     * @param string $variable
     *
     * @return mixed
     */
    public function __get($variable)
    {
        return $this->wpdb->$variable;
    }

    /**
     * Sets the value of the given WPDB variable.
     *
     * @param string $variable
     * @param mixed  $value
     */
    public function __set($variable, $value)
    {
        $this->wpdb->$variable = $value;
    }

    /**
     * Checks if the given WPDB variable is set.
     *
     * @param string $variable
     *
     * @return bool
     */
    public function __isset($variable)
    {
        return isset($this->wpdb->$variable);
    }

    /**
     * Unsets the given WPDB variable.
     *
     * @param string $variable
     */
    public function __unset($variable)
    {
        unset($this->wpdb->$variable);
    }
}
```

### Example 8

```php
public function __call($method, array $arguments)
{
    if (!in_array($method, array('delete', 'get_col', 'get_results', 'get_row', 'get_var', 'query', 'update'))) {
        return call_user_func_array(array($this->wpdb, $method), $arguments);
    }

    $return = call_user_func_array(array($this->wpdb, $method), $arguments);

    if ('' !== $this->wpdb->last_error) {
        do_action('wpdb_error', $this->wpdb->last_error, $this->wpdb->last_query);
    }

    return $return;
}
```

### Example 9

```php
global $wpdb;

$wpdb = new WPDBErrorCheckingDecorator($wpdb);
```

## Source

https://carlalexander.ca/wordpress-decorator-pattern/
