---
title: "Designing a class around WordPress hooks
			

			

				Have you met this “Carl” guy? He’s always blabbing about “object-oriented this” and “object-oriented that”. You decide to dip your toes into the subject (maybe he’s on to something…).
You try to apply a subset of what he teaches by creating a class. You start to code it. Life is good. And then it happens. You need to use a WordPress hook.
What do you with them?

Three possible solutions"
url: https://carlalexander.ca/designing-class-wordpress-hooks/
slug: designing-class-wordpress-hooks
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/designing-class-around-wordpress-hooks/
---

# Designing a class around WordPress hooks
			

			

				Have you met this “Carl” guy? He’s always blabbing about “object-oriented this” and “object-oriented that”. You decide to dip your toes into the subject (maybe he’s on to something…).
You try to apply a subset of what he teaches by creating a class. You start to code it. Life is good. And then it happens. You need to use a WordPress hook.
What do you with them?

Three possible solutions

## Summary

Building classes specifically designed to work with WordPress hooks. Separating hook registration from business logic.

## Code examples

### Example 1

```php
class MyPlugin
{
    public function __construct()
    {
        $this->init();
    }

    public function init()
    {
        add_action('wp_loaded', array($this, 'on_loaded'));
    }

    public function on_loaded()
    {
        // ...
    }
}
```

### Example 2

```php
class MyPlugin
{
    public function init()
    {
        add_action('wp_loaded', array($this, 'on_loaded'));
    }

    public function on_loaded()
    {
        // ...
    }
}

$my_plugin = new MyPlugin();
$my_plugin->init();
```

### Example 3

```php
class MyPlugin
{
    public static function init()
    {
        $self = new self();
        add_action('wp_loaded', array($self, 'on_loaded'));
    }

    public function on_loaded()
    {
        // ...
    }
}

MyPlugin::init();
```

### Example 4

```php
class MyPlugin
{
    public static function init()
    {
        $self = new self();
        add_action('wp_loaded', array($self, 'on_loaded'));
    }

    public function on_loaded()
    {
        // ...
    }
}

add_action('plugins_loaded', array('MyPlugin', 'init'));
```

### Example 5

```php
class MyPlugin
{
    public function on_loaded()
    {
        // ...
    }
}

function load_my_plugin()
{
    $my_plugin = new MyPlugin();
    add_action('wp_loaded', array($my_plugin, 'on_loaded'));
}
add_action('plugins_loaded', 'load_my_plugin');
```

### Example 6

```php
class MyPlugin
{
    public function on_loaded()
    {
        // ...
    }
}

$my_plugin = new MyPlugin();
add_action('wp_loaded', array($my_plugin, 'on_loaded'));
```

## Source

https://carlalexander.ca/designing-class-wordpress-hooks/
