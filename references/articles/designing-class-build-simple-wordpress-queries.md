---
title: "Designing a class to build simple WordPress queries
			

			

				In a previous article, we looked at how you could create a class to manage WordPress posts. We ended creating a class who’s job it was to interact with the WordPress database. And it did that quite well!
As part of its job, our class also had to be able to query the WordPress database. To do that, we made it easier to reuse code around the WP_Query class. We achieved that by creating methods that used predefined query arguments.
But have you ever looked at the codex page for WP_Query? Holy Moley, there are a lot of query parameters in there! It’s pretty intimidating and not always easy to use in practice.
That’s the problem that we’re going to look at in this article. We’ll design a class to simplify how we build WP_Query objects. It’ll handle all the complexity around WP_Query query parameters for you. The result should be an easier way for you for you to create WordPress queries.

How do you make WordPress queries easier?"
url: https://carlalexander.ca/designing-class-build-simple-wordpress-queries/
slug: designing-class-build-simple-wordpress-queries
fetched: 2026-11-18
---

# Designing a class to build simple WordPress queries
			

			

				In a previous article, we looked at how you could create a class to manage WordPress posts. We ended creating a class who’s job it was to interact with the WordPress database. And it did that quite well!
As part of its job, our class also had to be able to query the WordPress database. To do that, we made it easier to reuse code around the WP_Query class. We achieved that by creating methods that used predefined query arguments.
But have you ever looked at the codex page for WP_Query? Holy Moley, there are a lot of query parameters in there! It’s pretty intimidating and not always easy to use in practice.
That’s the problem that we’re going to look at in this article. We’ll design a class to simplify how we build WP_Query objects. It’ll handle all the complexity around WP_Query query parameters for you. The result should be an easier way for you for you to create WordPress queries.

How do you make WordPress queries easier?

## Summary

Creating simple query abstractions for common WP_Query patterns. Reducing boilerplate when fetching posts by common criteria.

## Code examples

### Example 1

```php
// WP_Query example
$query = new WP_Query(array(
    'fields' => 'ids',
    'post_type' => 'page',
    'orderby' => 'ID',
    'posts_per_page' => 5,
));
$posts = $query->get_posts();

// WP_Query_Builder example
$query_builder = new WP_Query_Builder();
$posts = $query_builder->select('ids')
                       ->from('page')
                       ->order_by('ID')
                       ->limit(5)
                       ->get_results();
```

### Example 2

```php
class WP_Query_Builder
{
}
```

### Example 3

```php
class WP_Query_Builder
{
    /**
     * The query arguments collected by the query builder.
     *
     * @var array
     */
    private $query_arguments;

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->query_arguments = array()
    }
}
```

### Example 4

```php
class WP_Query_Builder
{
    /**
     * The query arguments collected by the query builder.
     *
     * @var array
     */
    private $query_arguments;

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->query_arguments = array(
            'no_found_rows' => true,
            'update_post_meta_cache' => false,
            'update_post_term_cache' => false,
        );
    }
}
```

### Example 5

```php
class WP_Query_Builder
{
    /**
     * The query arguments collected by the query builder.
     *
     * @var array
     */
    private $query_arguments;

    /**
     * Constructor.
     *
     * @param array $query_arguments
     */
    public function __construct(array $query_arguments = array())
    {
        $this->query_arguments = array_merge(array(
            'no_found_rows' => true,
            'update_post_meta_cache' => false,
            'update_post_term_cache' => false,
        ), $query_arguments);
    }
}
```

### Example 6

```php
class WP_Query_Builder
{
    // ...

    /**
     * A method that implements method cascading.
     *
     * @param string $argument
     *
     * @return self
     */
    public function cascading_method($argument)
    {
        if (empty($argument)) {
            return $this;
        }

        // Do something with $argument.

       $this->query_arguments['query_parameter'] = $argument;

        return $this;
    }
}
```

### Example 7

```php
class WP_Query_Builder
{
    // ...

    /**
     * Specify the columns that the query will retrieve.
     *
     * Overwrites previous specification criteria if called multiple times.
     *
     * @param string $select
     *
     * @return self
     */
    public function select($select)
    {
        if (empty($select) || !is_string($select)) {
            return $this;
        }

        $this->query_arguments['fields'] = $select;

        return $this;
    }
}
```

### Example 8

```php
class WP_Query_Builder
{
    // ...

   /**
     * Specify the post types that the query will retrieve. 
     * 
     * Can be a comma separated string or an array. Overwrites previous
     * specification criteria if called multiple times.
     *
     * @param string|array $from
     *
     * @return self
     */
    public function from($from)
    {
        if (is_string($from)) {
            $from = array_map('trim', explode(',', $from));
        } elseif (!is_array($from)) {
            return $this;
        }

        $this->query_arguments['post_type'] = $from;

        return $this;
    }
}
```

### Example 9

```php
class WP_Query_Builder
{
    // ...

    /**
     * Specify the order of the query results.
     *
     * Overwrites previous specification criteria if called multiple times.
     *
     * @param string|array $sort
     * @param string $order
     *
     * @return self
     */
    public function order_by($sort, $order = 'DESC')
    {
        if (empty($sort) || (!is_array($sort) && !is_string($sort))) {
            return $this;
        } elseif (!is_string($order) || !in_array(strtoupper($order), array('ASC', 'DESC'))) {
            $order = 'DESC';
        }

        $this->query_arguments['orderby'] = $sort;
        $this->query_arguments['order'] = $order;

        return $this;
    }
}
```

### Example 10

```php
class WP_Query_Builder
{
    // ...

    /**
     * Specify the maximum number of results that the query will retrieve.
     *
     * Overwrites previous specification criteria if called multiple times.
     *
     * @param int $limit
     *
     * @return self
     */
    public function limit($limit)
    {
        if (!is_numeric($limit)) {
            return $this;
        }

        $this->query_arguments['posts_per_page'] = (int) $limit;

        return $this;
    }
}
```

### Example 11

```php
class WP_Query_Builder
{
    // ...

    /**
     * Query WordPress using the current specifications of the builder.
     *
     * @return WP_Post[]
     */
    public function get_results()
    {
        $query = new WP_Query($this->query_arguments);

        return $query->posts;
    }
}
```

### Example 12

```php
class WP_Query_Builder
{
    /**
     * The query arguments collected by the query builder.
     *
     * @var array
     */
    private $query_arguments;

    /**
     * Constructor.
     *
     * @param array $query_arguments
     */
    public function __construct(array $query_arguments = array())
    {
        $this->query_arguments = array_merge(array(
            'no_found_rows' => true,
            'update_post_meta_cache' => false,
            'update_post_term_cache' => false,
        ), $query_arguments);
    }

    /**
     * Specify the post types that the query will retrieve.
     *
     * Can be a comma separated string or an array. Overwrites previous
     * specification criteria if called multiple times.
     *
     * @param string|array $from
     *
     * @return self
     */
    public function from($from)
    {
        if (is_string($from)) {
            $from = array_map('trim', explode(',', $from));
        } elseif (!is_array($from)) {
            return $this;
        }

        $this->query_arguments['post_type'] = $from;

        return $this;
    }

    /**
     * Query WordPress using the current specifications of the builder.
     *
     * @return WP_Post[]
     */
    public function get_results()
    {
        $query = new WP_Query($this->query_arguments);

        return $query->posts;
    }

    /**
     * Specify the maximum number of results that the query will retrieve.
     *
     * Overwrites previous specification criteria if called multiple times.
     *
     * @param int $limit
     *
     * @return self
     */
    public function limit($limit)
    {
        if (!is_numeric($limit)) {
            return $this;
        }

        $this->query_arguments['posts_per_page'] = (int) $limit;

        return $this;
    }

    /**
     * Specify the order of the query results.
     *
     * Overwrites previous specification criteria if called multiple times.
     *
     * @param string|array $sort
     * @param string $order
     *
     * @return self
     */
    public function order_by($sort, $order = 'DESC')
    {
        if (empty($sort) || (!is_array($sort) && !is_string($sort))) {
            return $this;
        } elseif (!is_string($order) || !in_array(strtoupper($order), array('ASC', 'DESC'))) {
            $order = 'DESC';
        }

        $this->query_arguments['orderby'] = $sort;
        $this->query_arguments['order'] = $order;

        return $this;
    }

    /**
     * Specify the columns that the query will retrieve.
     *
     * Overwrites previous specification criteria if called multiple times.
     *
     * @param string $select
     *
     * @return self
     */
    public function select($select)
    {
        if (empty($select) || !is_string($select)) {
            return $this;
        }

        $this->query_arguments['fields'] = $select;

        return $this;
    }
}
```

## Source

https://carlalexander.ca/designing-class-build-simple-wordpress-queries/
