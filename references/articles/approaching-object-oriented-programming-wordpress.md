---
title: "How to approach object-oriented programming with WordPress
			

			

				I gave a talk on object-oriented programming with WordPress at WordCamp Miami 2019. This is the companion article that I wrote for it. If you’re just looking for the slides, click here.
You’re a WordPress developer who wants to use object-oriented programming in their next project. You’re already familiar with concepts like inheritance. The issue is that you’re not sure how to apply those concepts to design classes that feel useful.
This isn’t something to feel ashamed about! In fact, it’s a common problem when trying to use object-oriented programming with WordPress. It’s hard to know how to design classes that work well with WordPress. (That’s why this site has so many articles dedicated to that topic.)
But why is this so hard to do? Well, there are a few things going on. And together they create this situation that makes using object-oriented programming with WordPress complicated.

Going back to the beginning"
url: https://carlalexander.ca/approaching-object-oriented-programming-wordpress/
slug: approaching-object-oriented-programming-wordpress
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/how-to-approach-object-oriented-programming-wordpress/
---

# How to approach object-oriented programming with WordPress
			

			

				I gave a talk on object-oriented programming with WordPress at WordCamp Miami 2019. This is the companion article that I wrote for it. If you’re just looking for the slides, click here.
You’re a WordPress developer who wants to use object-oriented programming in their next project. You’re already familiar with concepts like inheritance. The issue is that you’re not sure how to apply those concepts to design classes that feel useful.
This isn’t something to feel ashamed about! In fact, it’s a common problem when trying to use object-oriented programming with WordPress. It’s hard to know how to design classes that work well with WordPress. (That’s why this site has so many articles dedicated to that topic.)
But why is this so hard to do? Well, there are a few things going on. And together they create this situation that makes using object-oriented programming with WordPress complicated.

Going back to the beginning

## Summary

Practical mindset and strategies for applying OOP concepts to WordPress projects. How to think differently about WordPress development.

## Code examples

### Example 1

```php
function get_authors_registered_after($date, $number = 5)
{
    $results = array();
    $authors = get_users('who=authors');

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
class Authors
{
    public function get_registered_after($date, $number = 5)
    {
        $results = array();
        $authors = get_users('who=authors');

        foreach ($authors->results as $author) {
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

## Source

https://carlalexander.ca/approaching-object-oriented-programming-wordpress/
