---
title: "Designing classes that use the WordPress plugin API
			

			

				The plugin API is one of the cornerstones of WordPress development. There’s no understating its importance. That’s why it’s such a common WordPress development topic (even here).
This importance doesn’t stop when you start using object-oriented programming. If anything, it gets worse! There are quite a few challenges with using the plugin API with object-oriented programming. The first one often being “What do I do with them?”
It’s the type problem that can stop you in your tracks. You want to learn to use object-oriented programming, but the plugin API gets in your way. You get frustrated with it and go back to what you’re comfortable with. Lucky for you, we’ve already explored it here (using the same link for emphasis!).
So we know how to handle WordPress hooks in a class. That’s good, but, now, we’re going to dig a bit deeper. We’re going to start thinking about the jobs of our classes. Where does the plugin API fit when we start thinking about the responsibility of our classes?

Listening to WordPress"
url: https://carlalexander.ca/designing-classes-wordpress-plugin-api/
slug: designing-classes-wordpress-plugin-api
fetched: 2026-11-18
---

# Designing classes that use the WordPress plugin API
			

			

				The plugin API is one of the cornerstones of WordPress development. There’s no understating its importance. That’s why it’s such a common WordPress development topic (even here).
This importance doesn’t stop when you start using object-oriented programming. If anything, it gets worse! There are quite a few challenges with using the plugin API with object-oriented programming. The first one often being “What do I do with them?”
It’s the type problem that can stop you in your tracks. You want to learn to use object-oriented programming, but the plugin API gets in your way. You get frustrated with it and go back to what you’re comfortable with. Lucky for you, we’ve already explored it here (using the same link for emphasis!).
So we know how to handle WordPress hooks in a class. That’s good, but, now, we’re going to dig a bit deeper. We’re going to start thinking about the jobs of our classes. Where does the plugin API fit when we start thinking about the responsibility of our classes?

Listening to WordPress

## Summary

Encapsulating WordPress hooks (actions/filters) in classes. Managing hook registration, callback methods, and priorities using OOP.

## Code examples

### Example 1

```php
class LoggingListener
{
}
```

### Example 2

```php
class LoggingListener
{
    /**
     * Email addresses to send the log entries to.
     *
     * @var array
     */
    private $emails;

    /**
     * Log entries.
     *
     * @var array
     */
    private $log_entries;

    /**
     * Constructor.
     *
     * @param array $emails
     */
    public function __construct(array $emails)
    {
        $this->emails = $emails;
        $this->log_entries = array();
    }
}
```

### Example 3

```php
class LoggingListener
{
    // ...

    /**
     * Initialize the logging listener with WordPress.
     *
     * @param array $emails
     */
    public static function init(array $emails)
    {
        $self = new self($emails);
    }
}
```

### Example 4

```php
class LoggingListener
{
    // ...

    /**
     * Email all our log entries to the registered email addresses.
     */
    public function email_log_entries()
    {
        if (empty($this->log_entries)) {
            return;
        }

        $message = "Log Entries:\r\n\r\n";

        foreach ($this->log_entries as $log_entry) {
            $message .= "$log_entry\r\n";
        }

        foreach($this->emails as $email) {
            wp_mail($email, sprintf('Your plugin logs [%s]', date('Y-m-d H:i:s')), $message);
        }
    }
}
```

### Example 5

```php
class LoggingListener
{
    // ...

    /**
     * Initialize the logging listener with WordPress.
     *
     * @param array $emails
     */
    public static function init(array $emails)
    {
        $self = new self($emails);

        add_action('shutdown', array($self, 'email_log_entries'));
    }
}
```

### Example 6

```php
class LoggingListener
{
    // ...

    /**
     * Log the details of an option change.
     *
     * @param string $option
     * @param string $old_value
     * @param string $value
     */
    public function log_option_change($option, $old_value, $value)
    {
        $old_value = maybe_serialize($old_value);
        $value = maybe_serialize($value);

        $this->log_entries[] = sprintf('Option "%s" changed from "%s" to "%s".', $option, $old_value, $value);
    }
}
```

### Example 7

```php
class LoggingListener
{
    // ...

    /**
     * Log the details of an option change.
     *
     * @param string $option
     * @param string $old_value
     * @param string $value
     */
    public function log_option_change($option, $old_value, $value)
    {
        if (0 === stripos($option, 'myplugin_')) {
            return;
        }

        $old_value = maybe_serialize($old_value);
        $value = maybe_serialize($value);

        $this->log_entries[] = sprintf('Option "%s" changed from "%s" to "%s".', $option, $old_value, $value);
    }
}
```

### Example 8

```php
class LoggingListener
{
    // ...

    /**
     * Initialize the logging listener with WordPress.
     *
     * @param array $emails
     */
    public static function init(array $emails)
    {
        $self = new self($emails);

        add_action('updated_option', array($self, 'log_option_change'), 10, 3);
        add_action('shutdown', array($self, 'email_log_entries'));
    }
}
```

### Example 9

```php
class LoggingListener
{
    /**
     * Email addresses to send the log entries to.
     *
     * @var array
     */
    private $emails;

    /**
     * Log entries.
     *
     * @var array
     */
    private $log_entries;

    /**
     * Constructor.
     *
     * @param array $emails
     */
    public function __construct(array $emails)
    {
        $this->emails = $emails;
        $this->log_entries = array();
    }

    /**
     * Initialize the logging listener with WordPress.
     *
     * @param array $emails
     */
    public static function init(array $emails)
    {
        $self = new self($emails);

        add_action('updated_option', array($self, 'log_option_change'), 10, 3);
        add_action('shutdown', array($self, 'email_log_entries'));
    }

    /**
     * Email all our log entries to the registered email addresses.
     */
    public function email_log_entries()
    {
        if (empty($this->log_entries)) {
            return;
        }

        $message = "Log Entries:\r\n\r\n";

        foreach ($this->log_entries as $log_entry) {
            $message .= "$log_entry\r\n";
        }

        foreach($this->emails as $email) {
            wp_mail($email, sprintf('Your plugin logs [%s]', date('Y-m-d H:i:s')), $message);
        }
    }

    /**
     * Log the details of an option change.
     *
     * @param string $option
     * @param string $old_value
     * @param string $value
     */
    public function log_option_change($option, $old_value, $value)
    {
        if (0 === stripos($option, 'myplugin_')) {
            return;
        }

        $old_value = maybe_serialize($old_value);
        $value = maybe_serialize($value);

        $this->log_entries[] = sprintf('Option "%s" changed from "%s" to "%s".', $option, $old_value, $value);
    }
}
```

## Source

https://carlalexander.ca/designing-classes-wordpress-plugin-api/
