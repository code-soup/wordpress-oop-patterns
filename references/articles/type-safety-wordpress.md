---
title: "Thoughts on type safety with WordPress
			

			

				As a WordPress developer, you might be familiar with type hints. These are the elements of your php docblock that let other developers know about the type that you expect a function or method parameter to be. Here’s an example:
/**
 * Return the first element in an array.
 *
 * @param array $array
 */
function first($array)
{
    foreach ($array as $value) {
        return $value
    }
}
@param array $array in the  first function above is the type hint for the array parameter. It tells other developers that we expect the parameter to be an array. But it doesn’t prevent them from passing you an integer or something else that wouldn’t work in a foreach loop.
Preventing these types of errors is what we call type safety. Any time that you write code, you’re making assumptions about the type of the variable you’re working with. That’s why type safety is an important to aspect of programming.
As a developer, you have to make a choice about how you want to deal with type safety. You have three overall approaches to deal with type errors.

You can:

Do nothing and let other developers deal with type errors from not respecting your type hints.
Program your function or method defensively to deal with developers not passing you the correct parameter type.
Have PHP enforce the parameter types of your functions or methods.

Since PHP 7, PHP developers favour the third approach of PHP enforcing type. But, as WordPress developers, we don’t always have that luxury. So it’s important to understand the tradeoffs between these different approaches to type safety.

WordPress still supports older versions of PHP"
url: https://carlalexander.ca/type-safety-wordpress/
slug: type-safety-wordpress
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/thoughts-type-safety-wordpress/
---

# Thoughts on type safety with WordPress
			

			

				As a WordPress developer, you might be familiar with type hints. These are the elements of your php docblock that let other developers know about the type that you expect a function or method parameter to be. Here’s an example:
/**
 * Return the first element in an array.
 *
 * @param array $array
 */
function first($array)
{
    foreach ($array as $value) {
        return $value
    }
}
@param array $array in the  first function above is the type hint for the array parameter. It tells other developers that we expect the parameter to be an array. But it doesn’t prevent them from passing you an integer or something else that wouldn’t work in a foreach loop.
Preventing these types of errors is what we call type safety. Any time that you write code, you’re making assumptions about the type of the variable you’re working with. That’s why type safety is an important to aspect of programming.
As a developer, you have to make a choice about how you want to deal with type safety. You have three overall approaches to deal with type errors.

You can:

Do nothing and let other developers deal with type errors from not respecting your type hints.
Program your function or method defensively to deal with developers not passing you the correct parameter type.
Have PHP enforce the parameter types of your functions or methods.

Since PHP 7, PHP developers favour the third approach of PHP enforcing type. But, as WordPress developers, we don’t always have that luxury. So it’s important to understand the tradeoffs between these different approaches to type safety.

WordPress still supports older versions of PHP

## Summary

Modern PHP type safety features (PHP 7+, PHP 8+) and how to apply them in WordPress. Benefits of strict typing, type hints, and typed properties.

## Code examples

### Example 1

```php
/**
 * Return the first element in an array.
 *
 * @param array $array
 */
function first($array)
{
    foreach ($array as $value) {
        return $value
    }
}
```

### Example 2

```php
/**
 * Change the title of a post
 *
 * @param int $post_id
 * @param string $title
 */
function my_plugin_change_post_title($post_id, $title)
{
    if (!is_int($post_id) || !is_string($title)) {
        return;
    }

    $post = get_post($post_id);
    
    if (!is_object($post)) {
        return;
    }
    
    $post->post_title = $title;
    
    wp_update_post($post);
}
```

## Source

https://carlalexander.ca/type-safety-wordpress/
