---
title: "Designing a class to create complex WordPress queries
			

			

				Alright, it’s time to continue our journey building our awesome WP_Query_Builder class! So far, we’ve only designed it to build simple WordPress queries. But not all WordPress queries are simple or easy to model using just a cascading method.
It’s even possible that you’ve run into the limits of the WP_Query_Builder already. The class that we created then wasn’t a complete solution. It had some serious limitations if you were a WP_Query expert. You couldn’t use it to perform complex WordPress queries.
What do we mean by complex WordPress queries? We mean queries that use a complex WP_Query query parameters. At the moment, there are three of them: date_query, meta_query and tax_query.
So, for this article, we’re going to back to our WP_Query_Builder class. We’ll add support for one of these complex WP_Query query parameters. We won’t go over all three due to how complex they are. But you can apply what you’ve seen for this one query parameter to design a fluent interface for the other two.

The story so far…"
url: https://carlalexander.ca/designing-class-complex-wordpress-queries/
slug: designing-class-complex-wordpress-queries
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/designing-class-create-complex-wordpress-queries/
---

# Designing a class to create complex WordPress queries
			

			

				Alright, it’s time to continue our journey building our awesome WP_Query_Builder class! So far, we’ve only designed it to build simple WordPress queries. But not all WordPress queries are simple or easy to model using just a cascading method.
It’s even possible that you’ve run into the limits of the WP_Query_Builder already. The class that we created then wasn’t a complete solution. It had some serious limitations if you were a WP_Query expert. You couldn’t use it to perform complex WordPress queries.
What do we mean by complex WordPress queries? We mean queries that use a complex WP_Query query parameters. At the moment, there are three of them: date_query, meta_query and tax_query.
So, for this article, we’re going to back to our WP_Query_Builder class. We’ll add support for one of these complex WP_Query query parameters. We won’t go over all three due to how complex they are. But you can apply what you’ve seen for this one query parameter to design a fluent interface for the other two.

The story so far…

## Summary

Query builder pattern for complex WP_Query operations. Fluent interfaces for constructing queries programmatically with method chaining.

## Code examples

### Example 1

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

### Example 2

```php
array(
    'taxonomy' => 'category',
    'terms' => array( 1, 4 ),
    'field' => 'term_id',
    'operator' => 'NOT IN',
    'include_children' => false,
);
```

### Example 3

```php
array(
    'relation' => 'AND',
    array(
        'taxonomy' => 'category',
        'terms' => '1',
    ),
   array(
       'taxonomy' => 'category',
       'field' => 'slug',
       'terms' => 'some-category-slug',
       'operator' => 'NOT IN',
    ),
);
```

### Example 4

```php
$query = new WP_Query(array(
    'tax_query' => array(
        'relation' => 'OR',
        array(
            'taxonomy' => 'post_format',
            'field' => 'slug',
            'terms' => 'some-post-format-slug',
        ),
        array(
            'relation' => 'AND',
            array(
                'taxonomy' => 'category',
                'terms' => '1',
            ),
            array(
                'taxonomy' => 'category',
                'field' => 'slug',
                'terms' => 'some-category-slug',
                'operator' => 'NOT IN',
            ),
        ),
    )
));
```

### Example 5

```php
class WP_Query_Builder
{
    // ...

    /**
     * Generates a taxonomy array.
     *
     * @param string $taxonomy
     * @param array|string $terms
     * @param string $field
     * @param string $operator
     * @param bool $include_children
     *
     * @return array
     */
    public function taxonomy($taxonomy, $terms, $field = 'term_id', $operator = 'IN', $include_children = true)
    {
        if (!is_array($terms)) {
            $terms = array($terms);
        }

        return array(
            'taxonomy' => $taxonomy,
            'field' => $field,
            'terms' => $terms,
            'operator' => $operator,
            'include_children' => $include_children,
        );
    }
}
```

### Example 6

```php
class WP_Query_Builder
{
    // ...

    /**
     * Generates a taxonomy array for a category.
     * 
     * @param array|string $categories
     * @param string $field
     * @param string $operator
     * @param bool $include_children
     *
     * @return array
     */
    public function category($categories, $field = 'term_id', $operator = 'IN', $include_children = true)
    {
        return $this->taxonomy('category', $categories, $field, $operator, $include_children);
    }
}
```

### Example 7

```php
class WP_Query_Builder
{
    // ...

    /**
     * Generates a taxonomy array where posts don't have 
     * one of the given taxonomy terms.
     *
     * @param string $taxonomy
     * @param array|string $terms
     * @param string $field
     * @param bool $include_children
     *
     * @return array
     */
    public function not_in_taxonomy($taxonomy, $terms, $field = 'term_id', $include_children = true)
    {
        return $this->taxonomy($taxonomy, $terms, $field, 'NOT IN', $include_children);
    }
}
```

### Example 8

```php
class WP_Query_Builder
{
    // ...

    /**
     * Generates a taxonomy array where posts don't have 
     * one of the given categories.
     *
     * @param array|string $categories
     * @param string $field
     * @param bool $include_children
     *
     * @return array
     */
    public function in_category($categories, $field = 'term_id', $include_children = true)
    {
        return $this->not_in_taxonomy('category', $categories, $field, $include_children);
    }
}
```

### Example 9

```php
class WP_Query_Builder
{
    // ...

   /**
     * Generates a group of query arrays using the given query arrays. The query
     * result must match all the given query arrays.
     *
     * @param array ...$query_arrays
     *
     * @return array
     */
    public function and_where()
    {
        $query_arrays = func_get_args();

        $query_arrays['relation'] = 'AND';

        return $query_arrays;
    }
}
```

### Example 10

```php
$query_builder->and_where(
    $query_builder->category('1'),
    $query_builder->not_in_category('some-category-slug', 'slug')
);
```

### Example 11

```php
array(
    array(
        'taxonomy' => 'category',
        'field' => 'term_id',
        'terms' => array('1'),
        'operator' => 'IN',
        'include_children' => true,
    ),
    array(
        'taxonomy' => 'category',
        'field' => 'slug',
        'terms' => array('some-category-slug'),
        'operator' => 'NOT IN',
        'include_children' => true,
    ),
    'relation' => 'AND',
);
```

### Example 12

```php
$query_builder->or_where(
   $query_builder->taxonomy('post_format', 'some-post-format-slug', 'slug'),
   $query_builder->and_where(
       $query_builder->category('1'),
       $query_builder->not_in_category('some-category-slug', 'slug')
   )
);
```

### Example 13

```php
class WP_Query_Builder
{
    // ...

   /**
     * Generates a group of query arrays using the given query arrays. The query
     * result must match one of the given query arrays.
     *
     * @param array ...$query_arrays
     *
     * @return array
     */
    public function or_where()
    {
        $query_arrays = func_get_args();

        $query_arrays['relation'] = 'OR';

        return $query_arrays;
    }
}
```

### Example 14

```php
class WP_Query_Builder
{
    // ...

    /**
     * Specify the taxonomy of the posts that the query will retrieve.
     * 
     * @param array $taxonomy_query
     *
     * @return self
     */
    public function where_taxonomy(array $taxonomy_query)
    {
        $this->query_arguments['tax_query'] = $taxonomy_query;

        return $this;
    }
}
```

### Example 15

```php
$query_builder = new WP_Query_Builder();
$posts = $query_builder->select('*')
                       ->from('post')
                       ->where_taxonomy(
                           $query_builder->and_where(
                               $query_builder->in_taxonomy('category', '5')),
                               $query_builder->not_in_category('some-category-slug', 'slug')
                           )
                       )
                       ->limit(3)
                       ->get_results();
```

### Example 16

```php
$posts = $query_builder->select('*')
                       ->from('post')
                       ->where_taxonomy(
                           $query_builder->category('5'),
                           $query_builder->not_in_category('some-category-slug', 'slug')
                       )
                       ->limit(3)
                       ->get_results();
```

### Example 17

```php
class WP_Query_Builder
{
    // ...

    /**
     * Specify the taxonomy of the posts that the query will retrieve.
     * 
     * @param array ...$taxonomies
     *
     * @return self
     */
    public function where_taxonomy()
    {
        $this->query_arguments['tax_query'] = array_reduce(func_get_args(), array($this, 'merge_query_argument'));

        return $this;
    }
}
```

### Example 18

```php
class WP_Query_Builder
{
    // ...

    /**
     * Merges the given query array argument into the given query.
     *
     * @param mixed $query
     * @param array $query_argument
     *
     * @return array
     */
    private function merge_query_argument($query, array $query_argument)
    {
        if (!is_array($query)) {
            $query = array();
        }

        if (!isset($query_argument['relation'])) {
            $query_argument = array($query_argument);
            $query_argument['relation'] = 'AND';
        }

        $query['relation'] = $query_argument['relation'];
        unset($query_argument['relation']);

        foreach ($query_argument as $query_array) {
            $query[] = $query_array;
        }

        return $query;
    }
}
```

### Example 19

```php
$query = new WP_Query(array(
    'fields' => 'ids',
    'post_type' => 'post',
    'tax_query' => array(
        'relation' => 'OR',
        array(
            'taxonomy' => 'post_format',
            'field' => 'slug',
            'terms' => 'some-post-format-slug',
        ),
        array(
            'relation' => 'AND',
            array(
                'taxonomy' => 'category',
                'terms' => '1',
            ),
            array(
                'taxonomy' => 'category',
                'field' => 'slug',
                'terms' => 'some-category-slug',
                'operator' => 'NOT IN',
            ),
        ),
    ),
    'posts_per_page' => 3,
));
$posts = $query->posts
```

### Example 20

```php
$posts = $query_builder->select('ids')
                       ->from('post')
                       ->where_taxonomy(
                           $query_builder->or_where(
                               $query_builder->taxonomy('post_format', 'some-post-format-slug', 'slug'),
                               $query_builder->and_where(
                                   $query_builder->category('1'),
                                   $query_builder->not_in_category('some-category-slug', 'slug')
                               )
                           )
                       )
                       ->limit(3)
                       ->get_results();
```

## Source

https://carlalexander.ca/designing-class-complex-wordpress-queries/
