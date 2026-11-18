---
title: "WordPress for the adventurous: Rewrite API
			

			

				The story behind rewrite API plays out almost like a Disney movie. You have WordPress and the human (played by you!). Two different worlds. Two different languages.
WordPress is a machine and only understands if you talk to it as such. You need to use a cold language of numbers and code so that it can understand you. Do you need to see a WordPress post? You need to ask him using query variables like p=123.
On the other hand, humans are friendly and talkative. They expect to talk to someone using words. They want to see URLs with the post-title and not query variables.
The rewrite API is the translator that brought these two unlikely friends together. Rewrite rules convert your post-title into the p=123 query variable WordPress wants. Both sides get their happy ending (yay!).

How does the rewrite API do this?"
url: https://carlalexander.ca/wordpress-adventurous-rewrite-api/
slug: wordpress-adventurous-rewrite-api
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/wordpress-for-adventurous-rewrite-api/
---

# WordPress for the adventurous: Rewrite API
			

			

				The story behind rewrite API plays out almost like a Disney movie. You have WordPress and the human (played by you!). Two different worlds. Two different languages.
WordPress is a machine and only understands if you talk to it as such. You need to use a cold language of numbers and code so that it can understand you. Do you need to see a WordPress post? You need to ask him using query variables like p=123.
On the other hand, humans are friendly and talkative. They expect to talk to someone using words. They want to see URLs with the post-title and not query variables.
The rewrite API is the translator that brought these two unlikely friends together. Rewrite rules convert your post-title into the p=123 query variable WordPress wants. Both sides get their happy ending (yay!).

How does the rewrite API do this?

## Summary

WordPress rewrite system internals. How pretty permalinks work, rewrite rules, query vars, and custom endpoints.

## Code examples

### Example 1

```php
function add_rewrite_rule($regex, $redirect, $after = 'bottom')
```

### Example 2

```php
function welcome_rewrite_rule()
{
    add_rewrite_rule('^welcome$', 'index.php?p=1', 'top');
}
add_action('init', 'welcome_rewrite_rule');
```

### Example 3

```php
function add_rewrite_tag($tag, $regex, $query = '')
```

### Example 4

```php
function postname_tag()
{
    add_rewrite_tag('%postname%', '([^/]+)', 'name=');
}
add_action('init', 'postname_tag');
```

### Example 5

```php
function add_rewrite_endpoint($name, $places, $query_var = null)
```

### Example 6

```php
function print_endpoint()
{
    add_rewrite_endpoint('print', EP_PERMALINK | EP_PAGES);
}
add_action('init', 'print_endpoint');
```

### Example 7

```php
function add_permastruct($name, $struct, $args = array())
```

### Example 8

```php
function add_feed($feedname, $function)
```

### Example 9

```php
function flush_rewrite_rules($hard = true)
```

### Example 10

```php
function myplugin_flush_rewrite_rules()
{
    if (get_option('myplugin_flush_rewrite_rules')) {
        flush_rewrite_rules();
        delete_option('myplugin_flush_rewrite_rules');
    }
}
add_action('init', 'myplugin_flush_rewrite_rules', 99);
```

## Source

https://carlalexander.ca/wordpress-adventurous-rewrite-api/
