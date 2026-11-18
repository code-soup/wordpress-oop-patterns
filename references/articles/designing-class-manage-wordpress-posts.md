---
title: "Designing a class to manage WordPress posts
			

			

				When building a plugin, it’s not uncommon to need to fetch posts from the database. After all, you might be using your own custom post type. Or maybe, you built a special functionality on top of posts and you want to find them that way. Those are just a few reasons why your plugin might need to query WordPress for posts.
Regardless of the reason, the standard way of doing that is to use the WP_Query class. This lets us create WordPress queries in a safe way outside the loop. The problem is that they’re not easy to reuse.
For example, let’s say that you want a query to fetch only one result. You’re always going to need to add the 'posts_per_page' => 1 and 'no_found_rows' => true query arguments. That last one removes the SQL_CALC_FOUND_ROWS query used by WordPress pagination. (You don’t need to paginate one result!) This lets us improve performance a bit by removing the unnecessary query.
Now, you’d need to copy these two query arguments whenever you create a query to fetch a single result. This is far from ideal. So let’s look at designing a solution to this problem. Using object-oriented programming, of course!

The job"
url: https://carlalexander.ca/designing-class-manage-wordpress-posts/
slug: designing-class-manage-wordpress-posts
fetched: 2026-11-18
---

# Designing a class to manage WordPress posts
			

			

				When building a plugin, it’s not uncommon to need to fetch posts from the database. After all, you might be using your own custom post type. Or maybe, you built a special functionality on top of posts and you want to find them that way. Those are just a few reasons why your plugin might need to query WordPress for posts.
Regardless of the reason, the standard way of doing that is to use the WP_Query class. This lets us create WordPress queries in a safe way outside the loop. The problem is that they’re not easy to reuse.
For example, let’s say that you want a query to fetch only one result. You’re always going to need to add the 'posts_per_page' => 1 and 'no_found_rows' => true query arguments. That last one removes the SQL_CALC_FOUND_ROWS query used by WordPress pagination. (You don’t need to paginate one result!) This lets us improve performance a bit by removing the unnecessary query.
Now, you’d need to copy these two query arguments whenever you create a query to fetch a single result. This is far from ideal. So let’s look at designing a solution to this problem. Using object-oriented programming, of course!

The job

## Summary

Repository pattern for WordPress. Creating a class that acts as a collection interface for custom post types. Abstracting WP_Query behind repository methods for cleaner code.

## Code examples

### Example 1

```php
class Repository
{
}
```

### Example 2

```php
class Repository
{
    /**
     * Add a post to the repository. Returns the post ID or a WP_Error.
     *
     * @param array $post
     *
     * @return int|WP_Error
     */
    public function add(array $post)
    {
        return wp_insert_post($post, true);
    }
}
```

### Example 3

```php
class Repository
{
    // ...

    /**
     * Find a post using the given post ID.
     *
     * @param int $id
     *
     * @return WP_Post|null
     */
    public function find_by_id($id)
    {
        $query = new WP_Query(array(
            'p' => $id,
            'posts_per_page' => 1,
            'no_found_rows' => true,
            'update_post_meta_cache' => false,
            'update_post_term_cache' => false,
        ));
        $posts = $query->get_posts();

        return !empty($posts[0]) ? $posts[0] : null;
    }
}
```

### Example 4

```php
class Repository
{
    // ...

    /**
     * Remove the given post from the repository.
     *
     * @param WP_Post $post
     * @param bool    $force
     */
    public function remove(WP_Post $post, $force = false)
    {
        wp_delete_post($post->ID, $force);
    }
}
```

### Example 5

```php
class Repository
{
    // ...

    /**
     * Update a post in the repository. Returns the post ID or a WP_Error.
     *
     * @param array $post
     *
     * @return int|WP_Error
     */
    public function update(array $post)
    {
        return wp_update_post($post, true);
    }
}
```

### Example 6

```php
class Repository
{
    /**
     * Add a post to the repository. Returns the post ID or a WP_Error.
     *
     * @param array $post
     *
     * @return int|WP_Error
     */
    public function add(array $post)
    {
        return wp_insert_post($post, true);
    }

    /**
     * Find a post using the given post ID.
     *
     * @param int $id
     *
     * @return WP_Post|null
     */
    public function find_by_id($id)
    {
        $query = new WP_Query(array(
            'p' => $id,
            'posts_per_page' => 1,
            'no_found_rows' => true,
            'update_post_meta_cache' => false,
            'update_post_term_cache' => false,
        ));
        $posts = $query->get_posts();

        return !empty($posts[0]) ? $posts[0] : null;
    }

    /**
     * Remove the given post from the repository.
     *
     * @param WP_Post $post
     * @param bool    $force
     */
    public function remove(WP_Post $post, $force = false)
    {
        wp_delete_post($post->ID, $force);
    }

    /**
     * Update a post in the repository. Returns the post ID or a WP_Error.
     *
     * @param array $post
     *
     * @return int|WP_Error
     */
    public function update(array $post)
    {
        return wp_update_post($post, true);
    }
}
```

### Example 7

```php
class Repository
{
    /**
     * Save a post into the repository. Returns the post ID or a WP_Error.
     *
     * @param array $post
     *
     * @return int|WP_Error
     */
    public function save(array $post)
    {
        if (!empty($post['ID'])) {
            return wp_update_post($post, true);
        }

        return wp_insert_post($post, true);
    }
}
```

### Example 8

```php
class Repository
{
    /**
     * WordPress query object.
     *
     * @var WP_Query
     */
    private $query;

    /**
     * Constructor.
     *
     * @param WP_Query $query
     */
    public function __construct(WP_Query $query)
    {
        $this->query = $query;
    }
}
```

### Example 9

```php
class Repository
{
    // ...

    /**
     * Initialize the repository.
     *
     * @return Repository
     */
    public static function init()
    {
        return new self(new WP_Query());
    }
}
```

### Example 10

```php
class Repository
{
    // ...

    /**
     * Find a post using the given post ID.
     *
     * @param int $id
     *
     * @return WP_Post|null
     */
    public function find_by_id($id)
    {
        $posts = $this->query->query(array(
            'p' => $id,
            'posts_per_page' => 1,
            'no_found_rows' => true,
            'update_post_meta_cache' => false,
            'update_post_term_cache' => false,
        ));

        return !empty($posts[0]) ? $posts[0] : null;
    }
}
```

### Example 11

```php
class Repository
{
    // ...

    /**
     * Find all post objects for the given query.
     *
     * @param array $query
     *
     * @return WP_Post[]
     */
    private function find(array $query)
    {
        $query = array_merge(array(
            'no_found_rows' => true,
            'update_post_meta_cache' => true,
            'update_post_term_cache' => false,
        ), $query);

        return $this->query->query($query);
    }
}
```

### Example 12

```php
class Repository
{
    // ...

    /**
     * Find a single post object for the given query. Returns null
     * if it doesn't find one.
     *
     * @param array $query
     *
     * @return WP_Post|null
     */
    private function find_one(array $query)
    {
        $query = array_merge($query, array(
            'posts_per_page' => 1,
        ));

        $posts = $this->find($query);

        return !empty($posts[0]) ? $posts[0] : null;
    }
}
```

### Example 13

```php
class Repository
{
    // ...

    /**
     * Find a post using the given post ID.
     *
     * @param int $id
     *
     * @return WP_Post|null
     */
    public function find_by_id($id)
    {
        return $this->find_one(array('p' => $id));
    }
}
```

### Example 14

```php
class Repository
{
    // ...

    /**
     * Find posts written by the given author.
     *
     * @param WP_User $author
     * @param int     $limit
     *
     * @return WP_Post[]
     */
    public function find_by_author(WP_User $author, $limit = 10)
    {
        return $this->find(array(
            'author' => $author->ID,
            'posts_per_page' => $limit,
        ));
    }
}
```

### Example 15

```php
$repository = Repository::init();

// find_by_id example
$post = $repository->find_by_id(1);

// find_by_author example
$current_user = wp_get_current_user();
$posts = array();
if ($current_user instanceof WP_User) {
    $posts = $repository->find_by_author($current_user);
}
```

### Example 16

```php
class Repository
{
    /**
     * WordPress query object.
     *
     * @var WP_Query
     */
    private $query;

    /**
     * Constructor.
     *
     * @param WP_Query $query
     */
    public function __construct(WP_Query $query)
    {
        $this->query = $query;
    }

    /**
     * Initialize the repository.
     *
     * @uses PHP 5.3
     *
     * @return self
     */
    public static function init()
    {
        return new self(new WP_Query());
    }

    /**
     * Find posts written by the given author.
     *
     * @param WP_User $author
     * @param int     $limit
     *
     * @return WP_Post[]
     */
    public function find_by_author(WP_User $author, $limit = 10)
    {
        return $this->find(array(
            'author' => $author->ID,
            'posts_per_page' => $limit,
        ));
    }

    /**
     * Find a post using the given post ID.
     *
     * @param int $id
     *
     * @return WP_Post|null
     */
    public function find_by_id($id)
    {
        return $this->find_one(array('p' => $id));
    }

    /**
     * Save a post into the repository. Returns the post ID or a WP_Error.
     *
     * @param array $post
     *
     * @return int|WP_Error
     */
    public function save(array $post)
    {
        if (!empty($post['ID'])) {
            return wp_update_post($post, true);
        }

        return wp_insert_post($post, true);
    }

    /**
     * Find all post objects for the given query.
     *
     * @param array $query
     *
     * @return WP_Post[]
     */
    private function find(array $query)
    {
        $query = array_merge(array(
            'no_found_rows' => true,
            'update_post_meta_cache' => true,
            'update_post_term_cache' => false,
        ), $query);

        return $this->query->query($query);
    }

    /**
     * Find a single post object for the given query. Returns null
     * if it doesn't find one.
     *
     * @param array $query
     *
     * @return WP_Post|null
     */
    private function find_one(array $query)
    {
        $query = array_merge($query, array(
            'posts_per_page' => 1,
        ));

        $posts = $this->find($query);

        return !empty($posts[0]) ? $posts[0] : null;
    }
}
```

## Source

https://carlalexander.ca/designing-class-manage-wordpress-posts/
