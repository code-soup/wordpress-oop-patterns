---
title: "Designing a class to generate HTML content in WordPress
			

			

				As WordPress developers, we often have to generate HTML content for our plugins. (And, if you’re building a theme, that’s pretty much mandatory!) But generating HTML inside a function or method is messy. You have to close your PHP tag, write your HTML, reopen your PHP tag and so on.
This combination of HTML and code isn’t ideal. You’ve coupled your templating to your code in a way that often doesn’t scale well. That’s why it’s common to see such functions or methods grow out of proportion.
The common cause of that is adding conditional logic into the HTML code. This increases the complexity of the code and reduces its readability. So we’d like to avoid that if possible.
It’s worth pointing out that mixing HTML and PHP isn’t bad per se. After all, PHP is also a templating language. We just want to create a proper delimitation between what is regular PHP code and what is PHP template code.
So let’s find a solution to this problem! The twist (well it’s not really a twist for this site…) is that we’re going to use object-oriented programming to do it. We’ll design a class that generates HTML using PHP template.

A shortcode example"
url: https://carlalexander.ca/designing-class-generate-wordpress-html-content/
slug: designing-class-generate-wordpress-html-content
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/designing-class-generate-html-content-wordpress/
---

# Designing a class to generate HTML content in WordPress
			

			

				As WordPress developers, we often have to generate HTML content for our plugins. (And, if you’re building a theme, that’s pretty much mandatory!) But generating HTML inside a function or method is messy. You have to close your PHP tag, write your HTML, reopen your PHP tag and so on.
This combination of HTML and code isn’t ideal. You’ve coupled your templating to your code in a way that often doesn’t scale well. That’s why it’s common to see such functions or methods grow out of proportion.
The common cause of that is adding conditional logic into the HTML code. This increases the complexity of the code and reduces its readability. So we’d like to avoid that if possible.
It’s worth pointing out that mixing HTML and PHP isn’t bad per se. After all, PHP is also a templating language. We just want to create a proper delimitation between what is regular PHP code and what is PHP template code.
So let’s find a solution to this problem! The twist (well it’s not really a twist for this site…) is that we’re going to use object-oriented programming to do it. We’ll design a class that generates HTML using PHP template.

A shortcode example

## Summary

Template/view rendering systems using classes. Separating HTML generation from business logic with builder or template classes.

## Code examples

### Example 1

```php
function myplugin_display_comment_shortcode($attributes)
{
    if (!is_array($attributes) || !isset($attributes['id'])) {
        return '<!-- Missing comment ID -->';
    } elseif (!is_numeric($attributes['id'])) {
        return '<!-- Invalid comment ID -->';
    }

    $comment = get_comment($attributes['id']);

    if (!$comment instanceof WP_Comment) {
        return '<!-- No comment found -->';
    }

    return '<blockquote>'
         . "<div>{$comment->comment_content}</div>"
         . "<div>- {$comment->comment_author}</div>"
         . '</blockquote>';
}
add_shortcode('myplugin_comment', 'myplugin_display_comment_shortcode');
```

### Example 2

```php
class MyPlugin_HighlightedCommentGenerator
{
}
```

### Example 3

```php
<?php
/**
 * Highlighted comment template.
 *
 * Available variables:
 *
 *  WP_Commment $comment
 */
?>
<blockquote>
    <div><?php esc_html_e($comment->comment_content); ?></div>
    <div>- <?php esc_html_e($comment->comment_author); ?></div>
</blockquote>
```

### Example 4

```php
class MyPlugin_HighlightedCommentGenerator
{
    /**
     * Generates the highlighted comment HTML for the given comment.
     *
     * @param WP_Comment $comment
     *
     * @return string
     */
    public function generate(WP_Comment $comment)
    {
        ob_start();

        include __DIR__ . 'highlighted-comment.php';

        return ob_get_clean();
    }
}
```

### Example 5

```php
class MyPlugin_HighlightedCommentGenerator
{
    /**
     * Generates the highlighted comment HTML for the given comment.
     *
     * @param WP_Comment $comment
     *
     * @return string
     */
    public function generate(WP_Comment $comment)
    {
        $template_path = apply_filters('myplugin_highlighted_comment_template_path', __DIR__ . 'highlighted-comment.php');

        if (!is_readable($template_path)) {
            return sprintf('<!-- Could not read "%s" file -->', $template_path);
        }

        ob_start();

        include $template_path;

        return ob_get_clean();
    }
}
```

### Example 6

```php
class MyPlugin_HighlightedCommentGenerator
{
    /**
     * Generates the highlighted comment HTML for the given comment.
     *
     * @param WP_Comment $comment
     *
     * @return string
     */
    public function generate(WP_Comment $comment)
    {
        $template_path = get_query_template('myplugin-highlighted-comment');

        if (empty($template_path)) {
            $template_path = __DIR__ . 'highlighted-comment.php';
        }

        ob_start();

        include $template_path;

        return ob_get_clean();
    }
}
```

### Example 7

```php
class MyPlugin_HighlightedCommentGenerator
{
    /**
     * Generates the highlighted comment HTML for the given comment.
     *
     * @param WP_Comment $comment
     *
     * @return string
     */
    public function generate(WP_Comment $comment)
    {
        $template_path = $this->get_template_path();

        if (!is_readable($template_path)) {
            return sprintf('<!-- Could not read "%s" file -->', $template_path);
        }

        ob_start();

        include $template_path;

        return ob_get_clean();
    }

    /**
     * Get the path of PHP template that the comment generator will use.
     *
     * @return string
     */
    private function get_template_path()
    {
        $template_path = get_query_template('myplugin-highlighted-comment');

        if (empty($template_path)) {
            $template_path = __DIR__ . 'highlighted-comment.php';
        }

        return apply_filters('myplugin_highlighted_comment_template_path', $template_path);
    }
}
```

### Example 8

```php
class MyPlugin_CommentGenerator
{
    /**
     * Path to the default template used by the highlighted comment generator.
     *
     * @var string
     */
    private $default_template_path;

    /**
     * Name of the filter used to filter the template path.
     * 
     * @var string
     */
    private $filter_name;

    /**
     * Template name used by the `get_query_template` function.
     * 
     * @var string
     */
    private $query_template_name;

    /**
     * Constructor.
     *
     * @param string $default_template_path
     * @param string $filter_name
     * @param string $query_template_name
     */
    public function __construct($default_template_path, $filter_name, $query_template_name)
    {
        $this->default_template_path = $default_template_path;
        $this->filter_name = $filter_name;
        $this->query_template_name = $query_template_name;
    }

    // ...
}
```

### Example 9

```php
class MyPlugin_CommentGenerator
{
    // ...

    /**
     * Get the path of PHP template that the comment generator will use.
     *
     * @return string
     */
    private function get_template_path()
    {
        $template_path = get_query_template($this->query_template_name);

        if (empty($template_path)) {
            $template_path = $this->default_template_path;
        }

        return apply_filters($this->filter_name, $template_path);
    }
}
```

### Example 10

```php
$comment_generator = new MyPlugin_CommentGenerator(
    __DIR__ . 'highlighted-comment.php', 
    'myplugin_highlighted_comment_template_path', 
    'myplugin-highlighted-comment'
);
```

### Example 11

```php
function myplugin_display_comment_shortcode($attributes)
{
    if (!is_array($attributes) || !isset($attributes['id'])) {
        return '<!-- Missing comment ID -->';
    } elseif (!is_numeric($attributes['id'])) {
        return '<!-- Invalid comment ID -->';
    }

    $comment = get_comment($attributes['id']);

    if (!$comment instanceof WP_Comment) {
        return '<!-- No comment found -->';
    }

    $comment_generator = new MyPlugin_CommentGenerator(
        __DIR__ . 'highlighted-comment.php',
        'myplugin_highlighted_comment_template_path',
        'myplugin-highlighted-comment'
    );

    return $comment_generator->generate($comment);
}
add_shortcode('myplugin_comment', 'myplugin_display_comment_shortcode');
```

### Example 12

```php
class MyPlugin_CommentGenerator
{
    /**
     * Path to the default template used by the highlighted comment generator.
     *
     * @var string
     */
    private $default_template_path;

    /**
     * Name of the filter used to filter the template path.
     *
     * @var string
     */
    private $filter_name;

    /**
     * Template name used by the `get_query_template` function.
     *
     * @var string
     */
    private $query_template_name;

    /**
     * Constructor.
     *
     * @param string $default_template_path
     * @param string $filter_name
     * @param string $query_template_name
     */
    public function __construct($default_template_path, $filter_name, $query_template_name)
    {
        $this->default_template_path = $default_template_path;
        $this->filter_name = $filter_name;
        $this->query_template_name = $query_template_name;
    }

    /**
     * Generates the highlighted comment HTML for the given comment.
     *
     * @param WP_Comment $comment
     *
     * @return string
     */
    public function generate(WP_Comment $comment)
    {
        $template_path = $this->get_template_path();

        if (!is_readable($template_path)) {
            return sprintf('<!-- Could not read "%s" file -->', $template_path);
        }

        ob_start();

        include $template_path;

        return ob_get_clean();
    }

    /**
     * Get the path of PHP template that the comment generator will use.
     *
     * @return string
     */
    private function get_template_path()
    {
        $template_path = get_query_template($this->query_template_name);

        if (empty($template_path)) {
            $template_path = $this->default_template_path;
        }

        return apply_filters($this->filter_name, $template_path);
    }
}
```

## Source

https://carlalexander.ca/designing-class-generate-wordpress-html-content/
