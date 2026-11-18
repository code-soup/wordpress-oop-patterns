---
title: "Designing a system: WP-CLI commands
			

			

				Ymir, the WordPress serverless DevOps platform that I’m building, has a lot of distinct parts. There’s the Laravel application which I’ve talked about. But there’s also a WordPress plugin that acts as the bridge between the AWS infrastructure and WordPress.
Part of the bridging process revolves around offloading certain tasks to WP-CLI. This was an architectural decision which deserves its own article. (You can read a short Twitter thread on it here.) That said, this meant that each offloaded task needed its own WP-CLI command.
And there were quite a few tasks to offload! This was an opportunity to use object-oriented programming to design a new system for WordPress. This system will handle the creation and registration of these WP-CLI commands.

How do you create a WP-CLI command?"
url: https://carlalexander.ca/designing-system-wp-cli-commands/
slug: designing-system-wp-cli-commands
fetched: 2026-11-18
---

# Designing a system: WP-CLI commands
			

			

				Ymir, the WordPress serverless DevOps platform that I’m building, has a lot of distinct parts. There’s the Laravel application which I’ve talked about. But there’s also a WordPress plugin that acts as the bridge between the AWS infrastructure and WordPress.
Part of the bridging process revolves around offloading certain tasks to WP-CLI. This was an architectural decision which deserves its own article. (You can read a short Twitter thread on it here.) That said, this meant that each offloaded task needed its own WP-CLI command.
And there were quite a few tasks to offload! This was an opportunity to use object-oriented programming to design a new system for WordPress. This system will handle the creation and registration of these WP-CLI commands.

How do you create a WP-CLI command?

## Summary

Building WP-CLI command systems. Command registration, argument parsing, and output formatting for CLI tools.

## Code examples

### Example 1

```php
$hello_command = function( $args, $assoc_args ) {
    list( $name ) = $args;
    $type = $assoc_args['type'];
    WP_CLI::$type( "Hello, $name!" );
    if ( isset( $assoc_args['honk'] ) ) {
        WP_CLI::log( 'Honk!' );
    }
};
WP_CLI::add_command( 'example hello', $hello_command, [
    'shortdesc' => 'Prints a greeting.',
    'synopsis' => [
        [
            'type' => 'positional',
            'name' => 'name',
            'description' => 'The name of the person to greet.',
            'optional' => false,
            'repeating' => false,
        ],
        [
            'type' => 'assoc',
            'name' => 'type',
            'description' => 'Whether or not to greet the person with success or error.',
            'optional' => true,
            'default' => 'success',
            'options' => ['success', 'error'],
        ],
        [
            'type' => 'flag',
            'name' => 'honk',
            'optional' => true,
        ],
    ],
]);
```

### Example 2

```php
namespace MyPlugin;

class WpCliCommands
{
    // ...

    public function command1()
    {
        // ...
    }

    public function command2()
    {
        // ...
    }
}
$commands = new WpCliCommands();
\WP_CLI::add_command('myplugin', $commands);
```

### Example 3

```php
class InvokableClass
{
    public function __invoke($text)
    {
        echo $text;
    }
}
$object = new InvokableClass();
$object('test');
```

### Example 4

```php
namespace MyPlugin\Command;

/**
 * A WP-CLI command.
 */
interface CommandInterface
{
}
```

### Example 5

```php
namespace MyPlugin\Command;

/**
 * A WP-CLI command.
 */
interface CommandInterface
{
    /**
     * Get the command name.
     *
     * @return string
     */
    public function get_name();
}
```

### Example 6

```php
namespace MyPlugin\Command;

/**
 * A WP-CLI command.
 */
interface CommandInterface
{
    /**
     * Executes the command.
     *
     * @param array $arguments
     * @param array $options
     */
    public function __invoke($arguments, $options);

    // ...
}
```

### Example 7

```php
namespace MyPlugin\Command;

/**
 * A WP-CLI command.
 */
interface CommandInterface
{
    // ...

    /**
     * Get the positional and associative arguments a command accepts.
     *
     * @return array
     */
    public function get_synopsis();
}
```

### Example 8

```php
namespace MyPlugin\Command;

/**
 * A WP-CLI command.
 */
interface CommandInterface
{
    // ...

    /**
     * Get the command description.
     *
     * @return string
     */
    public function get_description();

    // ...
}
```

### Example 9

```php
use MyPlugin\Command\MyCommand;

\WP_CLI::error(sprintf('Please run the "%s" command first', MyCommand::get_name()));
```

### Example 10

```php
use MyPlugin\Command\CommandInterface;

function myplugin_add_command(CommandInterface $command) 
{
    if (!defined('WP_CLI') || !WP_CLI || !class_exists('\WP_CLI')) {
        return;
    }

    \WP_CLI::add_command($command->get_name(), $command, [
        'shortdesc' => $command->get_description(),
        'synopsis' => $command->get_synopsis(),
    ]);
}
```

### Example 11

```php
namespace MyPlugin\Command;

abstract class AbstractCommand implements CommandInterface
{
}
```

### Example 12

```php
namespace MyPlugin\Command;

abstract class AbstractCommand implements CommandInterface
{
    /**
     * {@inheritdoc}
     */
    public function get_synopsis()
    {
        return [];
    }
}
```

### Example 13

```php
namespace MyPlugin\Command;

abstract class AbstractCommand implements CommandInterface
{
    /**
     * {@inheritdoc}
     */
    final public function get_name()
    {
        return sprintf('my-plugin %s', $this->get_command_name());
    }

    // ...

    /**
     * Get the "my-plugin" command name.
     *
     * @return string
     */
    abstract protected function get_command_name();
}
```

### Example 14

```php
namespace MyPlugin\Command;

class MyCommand extends AbstractCommand
{
    // ...

    /**
     * {@inheritdoc}
     */
    protected function get_command_name()
    {
        return 'my-command';
    }
}
```

### Example 15

```php
namespace MyPlugin\Command

class CreateAttachmentMetadataCommand extends AbstractCommand
{
    /**
     * {@inheritdoc}
     */
    public function __invoke($arguments, $options)
    {
        $attachment = get_post($arguments[0]);

        wp_update_attachment_metadata($attachment->ID, wp_generate_attachment_metadata($attachment->ID, get_attached_file($attachment->ID));

        \WP_CLI::success(sprintf('Created metadata for attachment "%s"', $attachment->ID));
    }

    /**
     * {@inheritdoc}
     */
    public function get_description()
    {
        return 'Creates the metadata for the given attachment';
    }

    /**
     * {@inheritdoc}
     */
    public function get_synopsis()
    {
        return [
            [
                'type' => 'positional',
                'name' => 'attachment_id',
                'description' => 'The ID of the attachment',
            ],
        ];
    }

    /**
     * {@inheritdoc}
     */
    protected function get_command_name()
    {
        return 'create-attachment-metadata';
    }
}
```

## Source

https://carlalexander.ca/designing-system-wp-cli-commands/
