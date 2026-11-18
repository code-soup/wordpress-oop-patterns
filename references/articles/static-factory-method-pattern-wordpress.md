---
title: "Using the static factory method pattern with WordPress
			

			

				If you use object-oriented programming, there’s a good chance that you’re familiar with the constructor. It’s this special method that an object-oriented programming language uses to initialize a new object.  In PHP (and a lot of other object-oriented programming languages), the __construct method is a special method reserved for the role of constructor.
The role of the constructor isn’t always well understood. This is especially true when you’re new to object-oriented programming. You know the method exists, but you’re not too sure how to use it.
This can lead to some less than ideal practices around constructors. This is especially true in the WordPress world where two such practices are popular. First, there’s the habit of putting hooks in the constructor. And, because of that habit, WordPress developers tend to overuse the singleton pattern.
These two practices show a misunderstanding of the role that a constructor plays inside a class. This isn’t how object-oriented programming wants you to use constructors. There are other ways to solve those problems without sacrificing the role of a constructor.
Now, this isn’t to say that constructors don’t have any problems either. They do! In fact, that’s why we’re looking at the static factory method pattern. It solves one common problem that constructors have in PHP.

The problem with constructors"
url: https://carlalexander.ca/static-factory-method-pattern-wordpress/
slug: static-factory-method-pattern-wordpress
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/using-static-factory-method-pattern-wordpress/
---

# Static Factory Method Pattern
			

			

				If you use object-oriented programming, there’s a good chance that you’re familiar with the constructor. It’s this special method that an object-oriented programming language uses to initialize a new object.  In PHP (and a lot of other object-oriented programming languages), the __construct method is a special method reserved for the role of constructor.
The role of the constructor isn’t always well understood. This is especially true when you’re new to object-oriented programming. You know the method exists, but you’re not too sure how to use it.
This can lead to some less than ideal practices around constructors. This is especially true in the WordPress world where two such practices are popular. First, there’s the habit of putting hooks in the constructor. And, because of that habit, WordPress developers tend to overuse the singleton pattern.
These two practices show a misunderstanding of the role that a constructor plays inside a class. This isn’t how object-oriented programming wants you to use constructors. There are other ways to solve those problems without sacrificing the role of a constructor.
Now, this isn’t to say that constructors don’t have any problems either. They do! In fact, that’s why we’re looking at the static factory method pattern. It solves one common problem that constructors have in PHP.

The problem with constructors

## Summary

Static factory methods for object creation. Alternative to constructors that provides more flexibility in object instantiation.

## Code examples

### Example 1

```php
class MyPlugin_SomeClass
{
    // ...
}

$some_class = new MyPlugin_SomeClass();
$some_class->do_something($argument1);
$some_class->do_something($argument2, $argument3);
```

### Example 2

```php
class MyPlugin_SomeClass
{
    function __call($name, $arguments)
    {
        if ('do_something' == $name && 1 == count($arguments)) {
            // ...
        } elseif ('do_something' == $name && 2 == count($arguments)) {
            // ...
        }
    }
}

$some_class = new MyPlugin_SomeClass();
$some_class->do_something($argument1);
$some_class->do_something($argument1, $argument2);
```

### Example 3

```php
class MyPlugin_SomeClass
{
    public function do_something()
    {
        $arguments = func_get_args();

        if (1 == count($arguments)) {
            // ...
        } elseif (2 == count($arguments)) {
            // ...
        }
    }
}

$some_class = new MyPlugin_SomeClass();
$some_class->do_something($argument1);
$some_class->do_something($argument2, $argument3);
```

### Example 4

```php
class MyPlugin_SomeClass
{
    public function do_something(...$arguments)
    {
        if (1 == count($arguments)) {
            // ...
        } elseif (2 == count($arguments)) {
            // ...
        }
    }
}

$some_class = new MyPlugin_SomeClass();
$some_class->do_something($argument1);
$some_class->do_something($argument2, $argument3);
```

### Example 5

```php
class MyPlugin_SomeClass
{
    function __call($name, $arguments)
    {
        if ('__construct' == $name && 1 == count($arguments)) {
            // ...
        }
    }
}

$some_class = new MyPlugin_SomeClass($argument1);
```

### Example 6

```php
class MyPlugin_SomeClass
{
    public function __construct()
    {
        $arguments = func_get_args();

        if (1 == count($arguments)) {
            // ...
        } elseif (2 == count($arguments)) {
            // ...
        }
    }
}
```

### Example 7

```php
class MyPlugin_Product
{
    /**
     * The Product's ID. Not the WordPress post ID.
     *
     * @var string
     */
    private $id;

    /**
     * The name of the product.
     *
     * @var string
     */
    private $name;

    /**
     * The type of the product.
     *
     * @var string
     */
    private $type;

    /**
     * Constructor.
     *
     * @param string $id
     * @param string $name
     * @param string $type
     */
    public function __construct($id, $name, $type)
    {
        $this->id = $id;
        $this->name = $name;
        $this->type = $type;
    }

    // ...
}
```

### Example 8

```php
class MyPlugin_Product
{
    // ...

    /**
     * Creates a new product from API data.
     *
     * @param mixed $object
     *
     * @return MyPlugin_Product|null
     */
    public static function from_api($object)
    {
        // ...
    }

    // ...
}
```

### Example 9

```php
class MyPlugin_Product
{
    // ...

    /**
     * Creates a new product from API data.
     *
     * @param mixed $object
     *
     * @return MyPlugin_Product|null
     */
    public static function from_api($object)
    {
        if (is_string($object)) {
            $object = json_decode($object);
        }

        if (is_array($object) && isset($object['id'], $object['name'], $object['type'])) {
            return new self($object['id'], $object['name'], $object['type']);
        } elseif ($object instanceof stdClass && isset($object->id, $object->name, $object->type)) {
            return new self($object->id, $object->name, $object->type);
        }
    }

    // ...
}
```

### Example 10

```php
class MyPlugin_Product
{
    // ...

    /**
     * Creates a new product from a post object.
     *
     * @param WP_Post $post
     *
     * @return MyPlugin_Product|null
     */
    public static function from_post(WP_Post $post)
    {
        if (!isset($post->myplugin_product_id, $post->myplugin_product_name, $post->myplugin_product_type)) {
            return;
        }

        return new self($post->myplugin_product_id, $post->myplugin_product_name, $post->myplugin_product_type);
    }

    // ...
}
```

## Source

https://carlalexander.ca/static-factory-method-pattern-wordpress/
