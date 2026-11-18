---
title: "WordPress for the adventurous: Plugin API
			

			

				Let’s say that you ran a poll through the WordPress developer community. It asked the following question: “What defines WordPress?”. The odds are that the plugin API would come up near the top.
From a developer’s perspective (and for the sake of my introduction), there’s nothing that defines WordPress like it. It’s the workhorse of the WordPress ecosystem. You use to build anything that you want with WordPress.
There are plenty of articles out there that show you how to use it, but little on how it works. That makes it a bit misunderstood and lonely (APIs have feelings you know).
It’s time we showed some love for this hard worker.

Actions vs Filters"
url: https://carlalexander.ca/wordpress-adventurous-plugin-api/
slug: wordpress-adventurous-plugin-api
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/wordpress-for-adventurous-plugin-api/
---

# WordPress for the adventurous: Plugin API
			

			

				Let’s say that you ran a poll through the WordPress developer community. It asked the following question: “What defines WordPress?”. The odds are that the plugin API would come up near the top.
From a developer’s perspective (and for the sake of my introduction), there’s nothing that defines WordPress like it. It’s the workhorse of the WordPress ecosystem. You use to build anything that you want with WordPress.
There are plenty of articles out there that show you how to use it, but little on how it works. That makes it a bit misunderstood and lonely (APIs have feelings you know).
It’s time we showed some love for this hard worker.

Actions vs Filters

## Summary

Deep dive into WordPress hooks system. How add_action, add_filter, do_action, and apply_filters work internally.

## Code examples

### Example 1

```php
if (!isset($merged_filters[$tag])) {
  ksort($wp_filter[$tag]);
  $merged_filters[$tag] = true;
}
```

### Example 2

```php
function add_action($tag, $function_to_add, $priority = 10, $accepted_args = 1) {
  return add_filter($tag, $function_to_add, $priority, $accepted_args);
}

function add_filter($tag, $function_to_add, $priority = 10, $accepted_args = 1)
```

### Example 3

```php
function apply_filters($tag, $value) 

function do_action($tag, $arg = '')
```

### Example 4

```php
function apply_filters_ref_array($tag, $args)

function do_action_ref_array($tag, $args)
```

### Example 5

```php
if (!isset($wp_actions[$tag]))
  $wp_actions[$tag] = 1;
else
  ++$wp_actions[$tag];
```

### Example 6

```php
function remove_action($tag, $function_to_remove, $priority = 10) {
  return remove_filter($tag, $function_to_remove, $priority);
}

function remove_filter($tag, $function_to_remove, $priority = 10)
```

### Example 7

```php
function remove_all_actions($tag, $priority = false) {
  return remove_all_filters($tag, $priority);
}

function remove_all_filters($tag, $priority = false)
```

### Example 8

```php
function current_action() {
  return current_filter();
}

function current_filter()
```

### Example 9

```php
function doing_action($action = null) {
  return doing_filter($action);
}

function doing_filter($filter = null)
```

### Example 10

```php
function has_action($tag, $function_to_check = false) {
  return has_filter($tag, $function_to_check);
}

function has_filter($tag, $function_to_check = false)
```

### Example 11

```php
function did_action($tag)
```

## Source

https://carlalexander.ca/wordpress-adventurous-plugin-api/
