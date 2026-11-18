---
title: "Introduction to WordPress unit testing
			

			

				I gave a talk at WordCamp Toronto 2015 on WordPress unit testing. This is the companion article that I wrote for it. If you’re just looking for the slides, click here.
“But this worked the other day!”
I don’t know about you, but reading that sentence just frustrates me! Don’t you hate when things worked one day and it doesn’t the next. It’s the stuff of (developer) nightmares.
What if there was a way to ward yourself against that evil? Well, you’re in luck because that’s the goal of software testing! It prevents this situation from happening over and over again. On top of that, it helps you improve the quality of the code you write. Awesome!
Now, software testing is a HUGE field. You have a ton of different types of testing. Each with its own purpose (and, sometimes, philosophy). Today, we’re going to focus on just one type of testing. It’s called unit testing.

So what is unit testing?"
url: https://carlalexander.ca/introduction-wordpress-unit-testing/
slug: introduction-wordpress-unit-testing
fetched: 2026-11-18
---

# Introduction to WordPress unit testing
			

			

				I gave a talk at WordCamp Toronto 2015 on WordPress unit testing. This is the companion article that I wrote for it. If you’re just looking for the slides, click here.
“But this worked the other day!”
I don’t know about you, but reading that sentence just frustrates me! Don’t you hate when things worked one day and it doesn’t the next. It’s the stuff of (developer) nightmares.
What if there was a way to ward yourself against that evil? Well, you’re in luck because that’s the goal of software testing! It prevents this situation from happening over and over again. On top of that, it helps you improve the quality of the code you write. Awesome!
Now, software testing is a HUGE field. You have a ton of different types of testing. Each with its own purpose (and, sometimes, philosophy). Today, we’re going to focus on just one type of testing. It’s called unit testing.

So what is unit testing?

## Summary

PHPUnit fundamentals for WordPress. Setting up test environment, writing test cases, and using WordPress testing framework.

## Code examples

### Example 1

```php
wp scaffold plugin unit-tested-plugin --plugin_name="WordPress Unit Test Demo"
```

### Example 2

```php
# tests/bootstrap.php

require_once(dirname(__DIR__) . '/vendor/autoload.php');

$_tests_dir = getenv('WP_TESTS_DIR');
if ( !$_tests_dir ) $_tests_dir = '/tmp/wordpress-tests-lib';

require_once $_tests_dir . '/includes/functions.php';

function _manually_load_plugin() {
    require dirname( __FILE__ ) . '/../unit-tested-plugin.php';
}
tests_add_filter( 'muplugins_loaded', '_manually_load_plugin' );

require $_tests_dir . '/includes/bootstrap.php';
```

### Example 3

```php
# unit-tested-plugin.php

namespace UnitTestDemo;

/**
 * Get a plugin option from the WordPress database.
 *
 * @param string $name
 *
 * @return mixed
 */
function demo_get_option($name)
{
    return get_option('demo_' . $name);
}
```

### Example 4

```php
# tests/test-demo.php

namespace UnitTestDemo;

use phpmock\phpunit\PHPMock;

class DemoTest extends \PHPUnit_Framework_TestCase
{
    use PHPMock;

    // ...
}
```

### Example 5

```php
# tests/test-demo.php

namespace UnitTestDemo;

use phpmock\phpunit\PHPMock;

class DemoTest extends \PHPUnit_Framework_TestCase
{
    use PHPMock;

    public function test_demo_get_option()
    {
        $this->assertEquals('bar', demo_get_option('foo'));
    }
}
```

### Example 6

```php
# tests/test-demo.php

namespace UnitTestDemo;

use phpmock\phpunit\PHPMock;

class DemoTest extends \PHPUnit_Framework_TestCase
{
    use PHPMock;

    public function test_demo_get_option()
    {
        $get_option = $this->getFunctionMock('UnitTestDemo', 'get_option');

        $this->assertEquals('bar', demo_get_option('foo'));
    }
}
```

### Example 7

```php
# tests/test-demo.php

namespace UnitTestDemo;

use phpmock\phpunit\PHPMock;

class DemoTest extends \PHPUnit_Framework_TestCase
{
    use PHPMock;

    public function test_demo_get_option()
    {
        $get_option = $this->getFunctionMock('UnitTestDemo', 'get_option');
        $get_option->expects($this->once())
                   ->with($this->equalTo('demo_foo'))
                   ->willReturn('bar');

        $this->assertEquals('bar', demo_get_option('foo'));
    }
}
```

### Example 8

```php
# unit-tested-plugin.php

namespace UnitTestDemo;

/**
 * Get a plugin option from the WordPress database.
 *
 * @param string $name
 * @param mixed  $default
 *
 * @return mixed
 */
function demo_get_option($name, $default = null)
{
    return get_option('demo_' . $name, $default);
}
```

### Example 9

```php
# tests/test-demo.php

namespace UnitTestDemo;

use phpmock\phpunit\PHPMock;

class DemoTest extends \PHPUnit_Framework_TestCase
{
    use PHPMock;

    public function test_demo_get_option()
    {
        $get_option = $this->getFunctionMock('UnitTestDemo', 'get_option');
        $get_option->expects($this->once())
                   ->with($this->equalTo('demo_foo'), $this->identicalTo(null))
                   ->willReturn('bar');

        $this->assertEquals('bar', demo_get_option('foo'));
    }
}
```

### Example 10

```php
# tests/test-demo.php

namespace UnitTestDemo;

use phpmock\phpunit\PHPMock;

class DemoTest extends \PHPUnit_Framework_TestCase
{
    use PHPMock;

    public function test_demo_get_option_casts_array()
    {
        $get_option = $this->getFunctionMock('UnitTestDemo', 'get_option');
        $get_option->expects($this->once())
                   ->with($this->equalTo('demo_foo'), $this->identicalTo(array()))
                   ->willReturn('bar');

        $this->assertEquals(array('bar'), demo_get_option('foo', array()));
    }
}
```

### Example 11

```php
# unit-tested-plugin.php

namespace UnitTestDemo;

/**
 * Get a plugin option from the WordPress database.
 *
 * @param string $name
 * @param mixed  $default
 *
 * @return mixed
 */
function demo_get_option($name, $default = null)
{
    $option = get_option('demo_' . $name, $default);

    if (is_array($default) && !is_array($option)) {
        $option = (array) $option;
    }

    return $option;
}
```

## Source

https://carlalexander.ca/introduction-wordpress-unit-testing/
