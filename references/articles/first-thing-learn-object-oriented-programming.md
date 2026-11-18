---
title: "The first thing you should learn from object-oriented programming
			

			

				You’ve decided to learn object-oriented programming, but you don’t know where to start. Object-oriented programming has so many concepts and features. The whole thing can feel overwhelming at times. Let’s help you get started on the right foot.
What’s a great place to start? With the feature that you’ll associate the most with object-oriented programming. It’s called encapsulation. Most modern programming languages support encapsulation using classes.

Why should you learn about it first?"
url: https://carlalexander.ca/first-thing-learn-object-oriented-programming/
slug: first-thing-learn-object-oriented-programming
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/first-thing-you-should-learn-from-object-oriented-programming/
---

# The first thing you should learn from object-oriented programming
			

			

				You’ve decided to learn object-oriented programming, but you don’t know where to start. Object-oriented programming has so many concepts and features. The whole thing can feel overwhelming at times. Let’s help you get started on the right foot.
What’s a great place to start? With the feature that you’ll associate the most with object-oriented programming. It’s called encapsulation. Most modern programming languages support encapsulation using classes.

Why should you learn about it first?

## Summary

Core OOP concept to master first. Encapsulation as foundation for understanding objects and classes.

## Code examples

### Example 1

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

https://carlalexander.ca/first-thing-learn-object-oriented-programming/
