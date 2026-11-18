---
title: "Designing a class: WordPress AJAX handler
			

			

				Learning object-oriented programming has its fair share of challenges. One of them is the large variety of problems and their solutions. That’s why a lot of solutions revolve around using design patterns.
Sometimes a problem has a clear solution like the WordPress API client. Other times it’s more abstract like how to interact with the plugin API. These abstract problems are a lot harder to define and solve.

That’s why we’ll look at how to design a class to solve one of those abstract problems. I decided to look at AJAX communication. You can use AJAX to do anything. This means that we can only create a generic outline of what an AJAX handler class would look like.
Let’s do a quick overview of AJAX"
url: https://carlalexander.ca/designing-class-wordpress-ajax-handler/
slug: designing-class-wordpress-ajax-handler
fetched: 2026-11-18
---

# Designing a class: WordPress AJAX handler
			

			

				Learning object-oriented programming has its fair share of challenges. One of them is the large variety of problems and their solutions. That’s why a lot of solutions revolve around using design patterns.
Sometimes a problem has a clear solution like the WordPress API client. Other times it’s more abstract like how to interact with the plugin API. These abstract problems are a lot harder to define and solve.

That’s why we’ll look at how to design a class to solve one of those abstract problems. I decided to look at AJAX communication. You can use AJAX to do anything. This means that we can only create a generic outline of what an AJAX handler class would look like.
Let’s do a quick overview of AJAX

## Summary

Encapsulating AJAX endpoints in classes. Nonce verification, capability checks, and response formatting in reusable AJAX handlers.

## Code examples

### Example 1

```php
namespace MyPlugin;

class AjaxHandler
{
    /**
     * Action hook used by the AJAX class.
     *
     * @var string
     */
    const ACTION = 'my_plugin';
    
    /**
     * Action argument used by the nonce validating the AJAX request.
     *
     * @var string
     */
    const NONCE = 'my-plugin-ajax';
}
```

### Example 2

```php
namespace MyPlugin;

class AjaxHandler
{
    /**
     * Register the AJAX handler class with all the appropriate WordPress hooks.
     */
    public static function register()
    {
        $handler = new self();

        add_action('wp_loaded', array($handler, 'register_script'));
    }

    /**
     * Register our AJAX JavaScript.
     */
    public function register_script()
    {
        wp_register_script('wp_ajax', plugins_url('path/to/ajax.js', __FILE__));
        wp_localize_script('wp_ajax', 'wp_ajax_data', $this->get_ajax_data());
        wp_enqueue_script('wp_ajax');
    }

    /**
     * Get the AJAX data that WordPress needs to output.
     *
     * @return array
     */
    private function get_ajax_data()
    {
        return array(
            'action' => self::ACTION,
            'nonce' => wp_create_nonce(AjaxHandler::NONCE)
        );
    }
}
```

### Example 3

```php
namespace MyPlugin;

class AjaxHandler
{
    /**
     * Action hook used by the AJAX class.
     *
     * @var string
     */
    const ACTION = 'my_plugin';

    /**
     * Action argument used by the nonce validating the AJAX request.
     *
     * @var string
     */
    const NONCE = 'my-plugin-ajax';

    /**
     * Register the AJAX handler class with all the appropriate WordPress hooks.
     */
    public static function register()
    {
        $handler = new self();

        add_action('wp_ajax_' . self::ACTION, array($handler, 'handle'));
        add_action('wp_ajax_nopriv_' . self::ACTION, array($handler, 'handle'));
        add_action('wp_loaded', array($handler, 'register_script'));
    }

    /**
     * Handles the AJAX request for my plugin.
     */
    public function handle()
    {
        // Make sure we are getting a valid AJAX request
        check_ajax_referer(self::NONCE);

        // Stand back! I'm about to do... SCIENCE!

        die();
    }

    // ...
}
```

### Example 4

```php
namespace MyPlugin;

class AjaxHandler
{
    /**
     * Get the AJAX data that WordPress needs to output.
     *
     * @return array
     */
    private function get_ajax_data()
    {
        return array(
            'action' => self::ACTION,
            'nonce' => wp_create_nonce(AjaxHandler::NONCE),
            'post_id' => get_the_ID()
        );
    }
}
```

### Example 5

```php
namespace MyPlugin;

class AjaxHandler
{
    // ...

    /**
     * Get the comment text sent by the AJAX request.
     *
     * @return string
     */
    private function get_comment()
    {
        $comment = '';

        if (isset($_POST['comment'])) {
            $comment = sanitize_title($_POST['comment']);
        }

        return $comment;
    }

    /**
     * Get the post ID sent by the AJAX request.
     *
     * @return int
     */
    private function get_post_id()
    {
        $post_id = 0;

        if (isset($_POST['post_id'])) {
            $post_id = intval($_POST['post_id']);
        }

        return $post_id;
    }
}
```

### Example 6

```php
namespace MyPlugin;

class AjaxHandler
{
    /**
     * Get the comment text sent by the AJAX request.
     *
     * @return string
     */
    private function get_comment()
    {
        $comment = '';

        if (isset($_POST['comment'])) {
            $comment = filter_var($_POST['comment'], FILTER_SANITIZE_STRING);
        }

        return $comment;
    }

    /**
     * Get the post ID sent by the AJAX request.
     *
     * @return int
     */
    private function get_post_id()
    {
        $post_id = 0;

        if (isset($_POST['post_id'])) {
            $post_id = absint(filter_var($_POST['post_id'], FILTER_SANITIZE_NUMBER_INT));
        }

        return $post_id;
    }
}
```

### Example 7

```php
namespace MyPlugin;

class AjaxHandler
{
    /**
     * Action argument used by the nonce validating the AJAX request.
     *
     * @var string
     */
    const NONCE = 'my-plugin-ajax';

    /**
     * Handles the AJAX request for my plugin.
     */
    public function handle()
    {
        // Make sure we are getting a valid AJAX request
        check_ajax_referer(self::NONCE);

        // ...

        echo 'Science achieved!';
        die();
    }
}
```

### Example 8

```php
namespace MyPlugin;

class AjaxHandler
{
    /**
     * Action argument used by the nonce validating the AJAX request.
     *
     * @var string
     */
    const NONCE = 'my-plugin-ajax';

    /**
     * Handles the AJAX request for my plugin.
     */
    public function handle()
    {
        // Make sure we are getting a valid AJAX request
        check_ajax_referer(self::NONCE);

        // ...
        
        if ($science instanceof WP_Error) {
            wp_send_json_error('Science failed...');
        }

        wp_send_json_success('Science achieved!');
    }
}
```

### Example 9

```php
namespace MyPlugin;

class AjaxHandler
{
    /**
     * Sends a JSON response with the details of the given error.
     * 
     * @param WP_Error $error
     */
    private function send_error(WP_Error $error)
    {
        wp_send_json(array(
            'code' => $error->get_error_code(),
            'message' => $error->get_error_message()
        ));
    }
}
```

### Example 10

```php
namespace MyPlugin;

class AjaxHandler
{
    /**
     * Action hook used by the AJAX class.
     *
     * @var string
     */
    const ACTION = 'my_plugin';

    /**
     * Action argument used by the nonce validating the AJAX request.
     *
     * @var string
     */
    const NONCE = 'my-plugin-ajax';

    /**
     * Register the AJAX handler class with all the appropriate WordPress hooks.
     */
    public static function register()
    {
        $handler = new self();

        add_action('wp_ajax_' . self::ACTION, array($handler, 'handle'));
        add_action('wp_ajax_nopriv_' . self::ACTION, array($handler, 'handle'));
        add_action('wp_loaded', array($handler, 'register_script'));
    }

    /**
     * Handles the AJAX request for my plugin.
     */
    public function handle()
    {
        // Make sure we are getting a valid AJAX request
        check_ajax_referer(self::NONCE);

        // Stand back! I'm about to try... SCIENCE!

        die();
    }

    /**
     * Register our AJAX JavaScript.
     */
    public function register_script()
    {
        wp_register_script('wp_ajax', plugins_url('path/to/ajax.js', __FILE__));
        wp_localize_script('wp_ajax', 'wp_ajax_data', $this->get_ajax_data());
        wp_enqueue_script('wp_ajax');
    }

    /**
     * Get the AJAX data that WordPress needs to output.
     *
     * @return array
     */
    private function get_ajax_data()
    {
        return array(
            'action' => self::ACTION,
            'nonce' => wp_create_nonce(AjaxHandler::NONCE)
        );
    }

    /**
     * Get the comment text sent by the AJAX request.
     *
     * @return string
     */
    private function get_comment()
    {
        $comment = '';

        if (isset($_POST['comment'])) {
            $comment = filter_var($_POST['comment'], FILTER_SANITIZE_STRING);
        }

        return $comment;
    }

    /**
     * Get the post ID sent by the AJAX request.
     *
     * @return int
     */
    private function get_post_id()
    {
        $post_id = 0;

        if (isset($_POST['post_id'])) {
            $post_id = absint(filter_var($_POST['post_id'], FILTER_SANITIZE_NUMBER_INT));
        }

        return $post_id;
    }

    /**
     * Sends a JSON response with the details of the given error.
     *
     * @param WP_Error $error
     */
    private function send_error(WP_Error $error)
    {
        wp_send_json(array(
            'code' => $error->get_error_code(),
            'message' => $error->get_error_message()
        ));
    }
}

Ajax::register();
```

## Source

https://carlalexander.ca/designing-class-wordpress-ajax-handler/
