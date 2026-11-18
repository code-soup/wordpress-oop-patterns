---
title: "Organizing your files in an object-oriented WordPress plugin
			

			

				So you’ve made the plunge to the world of PHP object-oriented programming. You want to use that knowledge to build a plugin or convert your plugin to using objects. That’s great!
We’re going to talk about one of the first hurdles you might face when trying to work with PHP objects. That’s organizing your files. It’s an important topic with no general consensus in the WordPress community.
So why is file organization important? Well, let’s look at the code samples on this site to give you an idea. In general, each code sample tends to have a couple of classes and/or interfaces. They’re also small and only cover one specific WordPress problem.
But once you start building a real plugin, you’ll have to solve a lot of problems. That means that you’ll end up with a lot more classes. It can leave you feeling frustrated and looking for answers to questions like:

What do you do with them?
How do you structure my files and folders to accommodate them?
How do you load all the files containing them?

These are all questions that you’ll get an answer to in this article. So let’s get to it!

The importance of having standards"
url: https://carlalexander.ca/organizing-files-object-oriented-wordpress-plugin/
slug: organizing-files-object-oriented-wordpress-plugin
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/organizing-your-files-object-oriented-wordpress-plugin/
---

# Organizing your files in an object-oriented WordPress plugin
			

			

				So you’ve made the plunge to the world of PHP object-oriented programming. You want to use that knowledge to build a plugin or convert your plugin to using objects. That’s great!
We’re going to talk about one of the first hurdles you might face when trying to work with PHP objects. That’s organizing your files. It’s an important topic with no general consensus in the WordPress community.
So why is file organization important? Well, let’s look at the code samples on this site to give you an idea. In general, each code sample tends to have a couple of classes and/or interfaces. They’re also small and only cover one specific WordPress problem.
But once you start building a real plugin, you’ll have to solve a lot of problems. That means that you’ll end up with a lot more classes. It can leave you feeling frustrated and looking for answers to questions like:

What do you do with them?
How do you structure my files and folders to accommodate them?
How do you load all the files containing them?

These are all questions that you’ll get an answer to in this article. So let’s get to it!

The importance of having standards

## Summary

Directory structure and file organization for OOP WordPress plugins. Namespacing, autoloading, and PSR-4 organization.

## Code examples

### Example 1

```php
/**
 * Autoloads MyPlugin classes using PSR-0 standard.
 *
 * @author Carl Alexander
 */
class MyPlugin_Autoloader
{
    /**
     * Registers MyPlugin_Autoloader as an SPL autoloader.
     *
     * @param boolean $prepend
     */
    public static function register($prepend = false)
    {
        if (version_compare(phpversion(), '5.3.0', '>=')) {
            spl_autoload_register(array(new self, 'autoload'), true, $prepend);
        } else {
            spl_autoload_register(array(new self, 'autoload'));
        }
    }

    /**
     * Handles autoloading of MyPlugin classes.
     *
     * @param string $class
     */
    public static function autoload($class)
    {
        if (0 !== strpos($class, 'MyPlugin')) {
            return;
        }

        if (is_file($file = dirname(__FILE__).'/../'.str_replace(array('_', "\0"), array('/', ''), $class).'.php')) {
            require_once $file;
        }
    }
}
```

### Example 2

```php
if (is_file($file = dirname(__FILE__).'/class-'.strtolower(str_replace(array('_', "\0"), array('-', ''), $class).'.php'))) {
    require_once $file;
}
```

### Example 3

```php
/**
 * Autoloads MyPlugin classes using WordPress convention.
 *
 * @author Carl Alexander
 */
class MyPlugin_Autoloader
{
    /**
     * Registers MyPlugin_Autoloader as an SPL autoloader.
     *
     * @param boolean $prepend
     */
    public static function register($prepend = false)
    {
        if (version_compare(phpversion(), '5.3.0', '>=')) {
            spl_autoload_register(array(new self, 'autoload'), true, $prepend);
        } else {
            spl_autoload_register(array(new self, 'autoload'));
        }
    }

    /**
     * Handles autoloading of MyPlugin classes.
     *
     * @param string $class
     */
    public static function autoload($class)
    {
        if (0 !== strpos($class, 'MyPlugin')) {
            return;
        }

        if (is_file($file = dirname(__FILE__).'/class-'.strtolower(str_replace(array('_', "\0"), array('-', ''), $class).'.php'))) {
            require_once $file;
        }
    }
}
```

### Example 4

```php
require_once __DIR__ . '/MyPlugin/Autoloader.php';
MyPlugin_Autoloader::register();

// Found at /MyPlugin/Plugin.php
$plugin = new MyPlugin_Plugin();
```

### Example 5

```php
require_once __DIR__ . '/_inc/class-myplugin-autoloader.php';
MyPlugin_Autoloader::register();

// Found at /_inc/class-myplugin-plugin.php
$plugin = new MyPlugin_Plugin();
```

## Source

https://carlalexander.ca/organizing-files-object-oriented-wordpress-plugin/
