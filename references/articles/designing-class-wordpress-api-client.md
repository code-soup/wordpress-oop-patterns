---
title: "Designing a class: WordPress API client
			

			

				As a WordPress developer, learning object-oriented programming seems daunting at first. It’s one thing to learn all the concepts, but theory will only get you so far.
You want to see how you can do it in practice. How do you start from nothing and end up with a working class. That’s why I’m going to share how I built a client for the WordPress REST API. You’ll get to see how I use object-oriented design in practice.

Some background"
url: https://carlalexander.ca/designing-class-wordpress-api-client/
slug: designing-class-wordpress-api-client
fetched: 2026-11-18
---

# Designing a class: WordPress API client
			

			

				As a WordPress developer, learning object-oriented programming seems daunting at first. It’s one thing to learn all the concepts, but theory will only get you so far.
You want to see how you can do it in practice. How do you start from nothing and end up with a working class. That’s why I’m going to share how I built a client for the WordPress REST API. You’ll get to see how I use object-oriented design in practice.

Some background

## Summary

Creating classes for external API integration. Handling HTTP requests, authentication, error handling, and response parsing.

## Code examples

### Example 1

```php
class WP_API_Client
{
    /**
     * Base path for all API user resources.
     *
     * @var string
     */
    const ENDPOINT_USERS = '/wp-json/wp/v2/users';

    // ...
}
```

### Example 2

```php
class WP_API_Client
{
    /**
     * Base URL for the WordPress site that the client is connecting to.
     *
     * @var string
     */
    private $base_url;

    /**
     * WordPress HTTP transport used for communication.
     *
     * @var WP_Http
     */
    private $http;

    /**
     * The authorization token used by the client.
     *
     * @var string
     */
    private $token;

    /**
     * Constructor.
     *
     * @param WP_Http $http
     * @param string  $base_url
     * @param string  $token
     */
    public function __construct(WP_Http $http, $base_url, $token)
    {
        $this->http = $http;
        $this->base_url = $base_url;
        $this->token = $token;
    }

    // ...
}
```

### Example 3

```php
class WP_API_Client
{
    /**
     * Constructor.
     *
     * @param WP_Http $http
     * @param string  $base_url
     * @param string  $username
     * @param string  $password
     */
    public function __construct(WP_Http $http, $base_url, $username, $password)
    {
        $this->http = $http;
        $this->base_url = $base_url;
        $this->token = base64_encode($username . ':' . $password);
    }

    // ...
}
```

### Example 4

```php
class WP_API_Client
{
    /**
     * Creates an API client from WordPress global objects.
     *
     * @param string $base_url
     * @param string $token
     *
     * @return WP_API_Client
     */
    public static function create($base_url, $token)
    {
        return new self(_wp_http_get_object(), $base_url, $token);
    }

    // ...
}
```

### Example 5

```php
class WP_API_Client
{
    /**
     * Retrieve a subset of the site's users.
     *
     * @param  array   $filters
     * @param  string  $context
     * @param  integer $page
     *
     * @return array|WP_Error
     */
    public function get_users(array $filters = array(), $context = 'view', $page = 1)
    {
        // ...
    }

    // ...
}
```

### Example 6

```php
class WP_API_Client
{
    /**
     * Builds a full API request URL from the given endpoint URL and query string arguments.
     *
     * @param string $endpoint
     * @param array  $query
     *
     * @return string
     */
    private function build_url($endpoint, array $query = array())
    {
        $url = $this->base_url.$endpoint;

        if (!empty($query)) {
            $url .= '?'.http_build_query($query);
        }

        return $url;
    }

    // ...
}
```

### Example 7

```php
class WP_API_Client
{
    /**
     * Retrieve a subset of the site's users.
     *
     * @param  array   $filters
     * @param  string  $context
     * @param  integer $page
     *
     * @return array|WP_Error
     */
    public function get_users(array $filters = array(), $context = 'view', $page = 1)
    {
        return $this->get($this->build_url(self::ENDPOINT_USERS, array('filter' => $filters, 'context' => $context, 'page' => $page)));
    }

    // ...
}
```

### Example 8

```php
class WP_API_Client
{
    /**
     * Performs a GET request using the WordPress HTTP transport. Returns a WP_Error
     * on error.
     *
     * @param string $url
     * @param array  $args
     *
     * @return array|WP_Error
     */
    private function get($url, array $args = array())
    {
        $response = $this->http->get($url, $this->build_args($args));

        // ...
    }


    // ...
}
```

### Example 9

```php
class WP_API_Client
{
    /**
     * Builds the WordPress HTTP transport arguments.
     *
     * @param array
     *
     * @return array
     */
    private function build_args(array $args = array())
    {
        return array_merge_recursive($args,
            array(
            'headers' => array(
                'Authorization' => 'Basic '.$this->token,
            ),
        ));
    }

    // ...
}
```

### Example 10

```php
class WP_API_Client
{
    /**
     * Extracts the response headers from the given response.
     *
     * @param array
     *
     * @return array
     */
    private function get_response_headers(array $response)
    {
        if (!isset($response['headers']) || !is_array($response['headers'])) {
            return array();
        }

        return $response['headers'];
    }

    /**
     * Extracts the status code from the given response.
     *
     * @param array $response
     *
     * @return int|null
     */
    private function get_response_status_code(array $response)
    {
        if (!isset($response['response']) || !isset($response['response']['code'])) {
            return null;
        }

        return $response['response']['code'];
    }

    // ...
}
```

### Example 11

```php
class WP_API_Client
{
    /**
     * Performs a GET request using the WordPress HTTP transport. Returns a WP_Error
     * on error.
     *
     * @param string $url
     * @param array  $args
     *
     * @return array|WP_Error
     */
    private function get($url, array $args = array())
    {
        $response = $this->http->get($url, $this->build_args($args));

        if (is_array($response) && $this->is_successful($response)) {
            $response = $this->decode_response($response);
        }

        // ...

        return $response
    }

    // ...
}
```

### Example 12

```php
class WP_API_Client
{
    /**
     * Checks if the given response is considered successful as per the HTTP specification.
     * This means that the response has a 2xx status code.
     *
     * @param array $response
     *
     * @return bool
     */
    private function is_successful(array $response)
    {
        $status_code = $this->get_response_status_code($response);

        if (null === $status_code) {
            return false;
        }

        return $status_code >= 200 && $status_code < 300;
    }

    // ...
}
```

### Example 13

```php
class WP_API_Client
{
    /**
     * Decodes the JSON object returned in given response. Returns a WP_Error on error.
     *
     * @param array $response
     *
     * @return array|WP_Error
     */
    private function decode_response(array $response)
    {
        $decoded = array();
        $headers = $this->get_response_headers($response);

        if (!isset($headers['content-type']) || false === stripos($headers['content-type'], 'application/json')) {
            return new WP_Error('invalid_response', 'The content-type of the response needs to be "application/json".');
        }

        if (isset($response['body'])) {
            $decoded = json_decode($response['body'], true);
        }

        if (null === $decoded) {
            return new WP_Error('invalid_json', 'The JSON response couldn\'t be decoded.');
        }

        return $decoded;
    }

    // ...
}
```

### Example 14

```php
class WP_API_Client
{
    /**
     * Performs a GET request using the WordPress HTTP transport. Returns a WP_Error
     * on error.
     *
     * @param string $url
     * @param array  $args
     *
     * @return array|WP_Error
     */
    private function get($url, array $args = array())
    {
        $response = $this->http->get($url, $this->build_args($args));

        if (is_array($response) && $this->is_successful($response)) {
            $response = $this->decode_response($response);
        } elseif (is_array($response) && !$this->is_successful($response)) {
            $response = $this->convert_response_to_error($response);
        }

        return $response;
    }

    // ...
}
```

### Example 15

```php
class WP_API_Client
{
    /**
     * Converts the given response to a WP_Error object.
     *
     * @param array $response
     *
     * @return WP_Error
     */
    private function convert_response_to_error(array $response)
    {
        $response = $this->decode_response($response);
        $error = new WP_Error();

        if ($response instanceof WP_Error) {
            $error = $response;
        } elseif (is_array($response)) {
            array_walk($response, array($this, 'add_response_error'), $error);
        }

        return $error;
    }

    // ...
}
```

### Example 16

```php
class WP_API_Client
{
    /**
     * Adds the response error to the given WP_Error instance.
     *
     * @param mixed    $response
     * @param mixed    $key
     * @param WP_Error $error
     */
    private function add_response_error($response, $key, WP_Error $error)
    {
        if (!is_array($response)) {
            return;
        }

        $error->add(
            isset($response['code']) ? $response['code'] : '',
            isset($response['message']) ? $response['message'] : ''
        );
    }

    // ...
}
```

## Source

https://carlalexander.ca/designing-class-wordpress-api-client/
