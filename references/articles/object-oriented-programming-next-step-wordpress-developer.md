---
title: "Why object-oriented programming is your next step as a WordPress developer
			

			

				You’re a WordPress developer. You might have a few plugins under your belt or a theme or two. You build WordPress sites for clients or just for yourself. You’ve heard of object-oriented programming, but, each time you look into it, it makes no sense!
You tell yourself object-oriented programming isn’t useful or worth the trouble. The goal of this article is to focus on explaining this value to you. At the end of this article, you should have a clear understanding of why you should learn it.

Managing your expectation"
url: https://carlalexander.ca/object-oriented-programming-next-step-wordpress-developer/
slug: object-oriented-programming-next-step-wordpress-developer
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/why-object-oriented-programming-next-step-wordpress-developer/
---

# Why object-oriented programming is your next step as a WordPress developer
			

			

				You’re a WordPress developer. You might have a few plugins under your belt or a theme or two. You build WordPress sites for clients or just for yourself. You’ve heard of object-oriented programming, but, each time you look into it, it makes no sense!
You tell yourself object-oriented programming isn’t useful or worth the trouble. The goal of this article is to focus on explaining this value to you. At the end of this article, you should have a clear understanding of why you should learn it.

Managing your expectation

## Summary

Foundational concepts for transitioning from procedural WordPress development to object-oriented programming. Explains benefits of OOP for WordPress plugin/theme development.

## Code examples

### Example 1

```php
/**
 * Get all the authors registered after the given date.
 *
 * @param string  $date
 * @param integer $number
 *
 * @return array
 */
function get_authors_registered_after($date, $number = 5)
{
    $results = array();
    $authors = get_users('who=authors&orderby=registered&order=desc');

    foreach ($authors as $author) {
        if ($author->user_registered > $date) {
            $results[] = $author;
        }

        if (count($results) >= $number) {
            break;
        }
    }

    return $results;
}
```

### Example 2

```php
/**
 * Get all the authors registered after the given date.
 *
 * @param string  $date
 * @param integer $number
 *
 * @return array
 */
function get_authors_registered_after($date, $number = 5)
{
    $results = array();
    $query = new WP_User_Query(array(
        'who'     => 'authors',
        'orderby' => 'registered',
        'order'   => 'desc'
    ));

    foreach ($query->results as $author) {
        if ($author->user_registered > $date) {
            $results[] = $author;
        }

        if (count($results) >= $number) {
            break;
        }
    }

    return $results;
}
```

### Example 3

```php
class Authors 
{
    /**
     * Get all the authors registered after the given date.
     *
     * @param string  $date
     * @param integer $number
     *
     * @return array
     */
    public function get_registered_after($date, $number = 5)
    {
        $results = array();
        $query = new WP_User_Query(array(
            'who'     => 'authors',
            'orderby' => 'registered',
            'order'   => 'desc'
        ));

        foreach ($query->results as $author) {
            if ($author->user_registered > $date) {
                $results[] = $author;
            }

            if (count($results) >= $number) {
                break;
            }
        }

        return $results;
    }
}
```

### Example 4

```php
/**
 * Hooks a function or method to a specific filter action.
 */
function add_filter( $tag, $function_to_add, $priority = 10, $accepted_args = 1 ) {
    global $wp_filter, $merged_filters;

    $idx = _wp_filter_build_unique_id($tag, $function_to_add, $priority);
    $wp_filter[$tag][$priority][$idx] = array('function' => $function_to_add, 'accepted_args' => $accepted_args);
    unset( $merged_filters[ $tag ] );
    return true;
}

/**
 * Call the functions added to a filter hook.
 */
function apply_filters( $tag, $value ) {
    global $wp_filter, $merged_filters, $wp_current_filter;

    $args = array();

    // Do 'all' actions first
    if ( isset($wp_filter['all']) ) {
        $wp_current_filter[] = $tag;
        $args = func_get_args();
        _wp_call_all_hook($args);
    }

    if ( !isset($wp_filter[$tag]) ) {
        if ( isset($wp_filter['all']) )
            array_pop($wp_current_filter);
        return $value;
    }

    if ( !isset($wp_filter['all']) )
        $wp_current_filter[] = $tag;

    // Sort
    if ( !isset( $merged_filters[ $tag ] ) ) {
        ksort($wp_filter[$tag]);
        $merged_filters[ $tag ] = true;
    }

    reset( $wp_filter[ $tag ] );

    if ( empty($args) )
        $args = func_get_args();

    do {
        foreach( (array) current($wp_filter[$tag]) as $the_ )
            if ( !is_null($the_['function']) ){
                $args[1] = $value;
                $value = call_user_func_array($the_['function'], array_slice($args, 1, (int) $the_['accepted_args']));
            }

    } while ( next($wp_filter[$tag]) !== false );

    array_pop( $wp_current_filter );

    return $value;
}
```

### Example 5

```php
class WP_Filters
{
    protected $filters = array();

    /**
     * Hooks a function or method to a specific filter action.
     *
     * @param string  $tag
     * @param mixed   $function
     * @param integer $priority
     * @param integer $accepted_args
     */
    public function add($tag, $function, $priority = 10, $accepted_args = 1)
    {
    }

    /**
     * Call the functions added to a filter hook.
     *
     * @param string $tag
     * @param mixed $value
     */
    public function apply($tag, $value)
    {
    }

    /**
     * Remove all of the hooks from a filter.
     * 
     * @param string  $tag
     */
    public function clear($tag)
    {
    }

    /**
     * Removes a function from a specified filter hook.
     *
     * @param string  $tag
     * @param mixed   $function
     * @param integer $priority
     */
    public function remove($tag, $function, $priority = 10)
    {
    }

    /**
     * Build Unique ID for storage and retrieval.
     *
     * @param string  $tag
     * @param mixed   $function
     * @param integer $priority
     */
    protected function build_unique_id($tag, $function, $priority)
    {
    }
}
```

## Source

https://carlalexander.ca/object-oriented-programming-next-step-wordpress-developer/
