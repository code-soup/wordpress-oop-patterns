---
title: "Mastering the use of PHP conditionals
			

			

				No set of control structures is more pervasive in programming than if, elseif and else. With a few exceptions, you’ll use at least one per function or method that you write. There’s just no way around it.
But conditionals (that’s what we call these control structures) fit in the “easy to learn, hard to master” category. In fact, they’re so easy to use that you can develop some bad habits around them. (This is also a problem with loops.) This can lead to code that’s complex and hard to read or even test.
That said, it’s possible to develop good programming habits with conditionals. This is what this article will try to help you with. We’ll go over some programming techniques that can help make conditionals more manageable.

How does PHP evaluate multiple conditionals?"
url: https://carlalexander.ca/mastering-php-conditionals/
slug: mastering-php-conditionals
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/mastering-use-php-conditionals/
---

# Mastering the use of PHP conditionals
			

			

				No set of control structures is more pervasive in programming than if, elseif and else. With a few exceptions, you’ll use at least one per function or method that you write. There’s just no way around it.
But conditionals (that’s what we call these control structures) fit in the “easy to learn, hard to master” category. In fact, they’re so easy to use that you can develop some bad habits around them. (This is also a problem with loops.) This can lead to code that’s complex and hard to read or even test.
That said, it’s possible to develop good programming habits with conditionals. This is what this article will try to help you with. We’ll go over some programming techniques that can help make conditionals more manageable.

How does PHP evaluate multiple conditionals?

## Summary

Advanced conditional logic in PHP. Best practices for if/else, switch statements, ternary operators, and null coalescing.

## Code examples

### Example 1

```php
if (is_array($array) && !empty($var)) {
    do_something($array, $var);
}
```

### Example 2

```php
if (is_array($array)) {
    if (!empty($var)) {
        do_something($array, $var);
    }
}
```

### Example 3

```php
if (false && do_something())
    // ...
} elseif (false and do_something())
    // ...
} elseif (true || do_something())
    // ...
} elseif (true or do_something())
    // ...
}
```

### Example 4

```php
if (is_array($array) && !empty($array) || !empty($var)) {
    do_something($array, $var);
}
```

### Example 5

```php
if ((is_array($array) && !empty($array)) || !empty($var)) {
    do_something($array, $var);
}
```

### Example 6

```php
function do_something_to_array($array)
{
    if (is_array($array)) {
        $array = clean_array($array);
    }

    return $array;
}
```

### Example 7

```php
function do_something_to_array($array)
{
    if (!is_array($array)) {
        return $array;
    }

    return clean_array($array);
}
```

### Example 8

```php
function do_something_to_array($array)
{
    if (is_array($array)) {
        $array = clean_array($array);

        if (count($array) == 1) {
            return current($array);
        }
    }

    return $array;
}
```

### Example 9

```php
function do_something_to_array($array)
{
    if (!is_array($array)) {
        return $array;
    }

    $array = clean_array($array);

    if (count($array) == 1) {
        return current($array);
    }

    return $array
}
```

### Example 10

```php
function create_something(array $data)
{
    if (empty($data['type'])) {
        $data['type'] = 'post';
    }

    if ('page' == $data['type']) {
        if (empty($data['title'])) {
            $data['title'] = 'Default page title';
        }

        // Do stuff with page data

        save($data);
    } elseif ('post' == $data['type']) {
        if (empty($data['title'])) {
            $data['title'] = 'Default post title';
        }

        // Do stuff with post data

        save($data);
    }
}
```

### Example 11

```php
function create_page(array $page_data)
{
    if (empty($page_data['title'])) {
        $page_data['title'] = 'Default page title';
    }

    // Do stuff with page data

    save($page_data);
}


function create_post(array $post_data)
{
    if (empty($post_data['title'])) {
        $post_data['title'] = 'Default post title';
    }

    // Do stuff with post data

    save($post_data);
}

function create_something(array $data)
{
    if (empty($data['type'])) {
        $data['type'] = 'post';
    }

    if ('page' == $data['type']) {
        create_page($data);
    } elseif ('post' == $data['type']) {
        create_post($data);
    }
}
```

### Example 12

```php
function create_something(array $data)
{
    if (empty($data['type'])) {
        $data['type'] = 'post';
    }

    // ...
}
```

### Example 13

```php
function create_something(array $data)
{
    $data['type'] = empty($data['type']) ? 'post' : $data['type']

    // ...
}
```

### Example 14

```php
function do_something($maybe_array) {
    if (is_array($maybe_array)) {
        foreach($maybe_array as $value) {
            do_something_else($value);
        }
    } else {
        do_something_else($maybe_array);
    }
}
```

### Example 15

```php
function do_something($maybe_array) {
    if (!is_array($maybe_array)) {
        $maybe_array = array($maybe_array);
    }
    
    foreach($maybe_array as $value) {
        do_something_else($value);
    }
}
```

## Source

https://carlalexander.ca/mastering-php-conditionals/
