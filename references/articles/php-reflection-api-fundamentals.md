---
title: "PHP reflection API fundamentals
			

			

				Do you ever take the time to read the code of your favourite PHP framework or library? If you have, there’s a good chance that you might have seen them use PHP’s reflection API. And, if you don’t read other people’s code, you should start doing it! (It’s a great learning tool.)
Now, let’s get back to the reflection API. This is an API that gets used quite a lot by framework and library developers. But the funny thing is that it’s almost never talked about when you’re looking at resources to learn PHP. (Or even advanced PHP resources for that matter.)
This is unfortunate. That’s because PHP’s reflection API serves a unique and important purpose. That’s why developers that build our frameworks and libraries use it so much.

What’s a reflection?"
url: https://carlalexander.ca/php-reflection-api-fundamentals/
slug: php-reflection-api-fundamentals
fetched: 2026-11-18
---

# PHP reflection API fundamentals
			

			

				Do you ever take the time to read the code of your favourite PHP framework or library? If you have, there’s a good chance that you might have seen them use PHP’s reflection API. And, if you don’t read other people’s code, you should start doing it! (It’s a great learning tool.)
Now, let’s get back to the reflection API. This is an API that gets used quite a lot by framework and library developers. But the funny thing is that it’s almost never talked about when you’re looking at resources to learn PHP. (Or even advanced PHP resources for that matter.)
This is unfortunate. That’s because PHP’s reflection API serves a unique and important purpose. That’s why developers that build our frameworks and libraries use it so much.

What’s a reflection?

## Summary

PHP Reflection API for inspecting and manipulating classes at runtime. Building advanced DI containers, test utilities, and dynamic code analysis.

## Code examples

### Example 1

```php
$classReflection = new ReflectionClass('SomeClass');

$object = new SomeClass();
$objectReflection = new ReflectionObject($object);
```

### Example 2

```php
$object = new SomeClass();
$objectReflection = new ReflectionObject($object);

$someProperty = $objectReflection->getProperty('someProperty');
```

### Example 3

```php
$object = new SomeClass();
$objectReflection = new ReflectionObject($object);

$somePropertyReflection = $objectReflection->getProperty('someProperty');

$somePropertyValue = $somePropertyReflection->getValue($object);
```

### Example 4

```php
$object1 = new SomeClass();
$object2 = new SomeClass();

$objectReflection = new ReflectionObject($object1);

$somePropertyReflection = $objectReflection->getProperty('someProperty');

$somePropertyValue1 = $somePropertyReflection->getValue($object1);
$somePropertyValue2 = $somePropertyReflection->getValue($object2);
```

### Example 5

```php
class User
{
    /**
     * The user ID.
     *
     * @var int
     */
    private $id;

    /**
     * The user's login.
     *
     * @var string
     */
    private $login;

    /**
     * The user's password.
     *
     * @var string
     */
    private $password;

    /**
     * Constructor.
     *
     * @param string $login
     * @param string $password
     */
    public function __construct($login, $password)
    {
        $this->login = $login;
        $this->password = $password;
    }
}
```

### Example 6

```php
class User
{
    // ...

    /**
     * Set the ID of a user.
     *
     * @param int $id
     */
    public function setId($id)
    {
        if (!empty($this->id)) {
            return;
        }

        $this->id = $id;
    }
}
```

### Example 7

```php
class UserRepository
{
    /**
     * The user's login.
     *
     * @var mysqli
     */
    private $mysql;

    // ...

    public function persist(User $user) 
    {
        $result = $this->mysql->query('INSERT INTO ...');

        if (!$result) {
            throw new \Exception($this->mysql->error);
        }

        $userReflection = new ReflectionObject($user);
        $idPropertyReflection = $userReflection->getProperty('id');

        $idPropertyReflection->setAccessible(true);
        $idPropertyReflection->setValue($user, $this->mysql->insert_id);
        $idPropertyReflection->setAccessible(false);

        return $user;
    }
}
```

### Example 8

```php
class User
{
    // ...

    /**
     * Constructor.
     *
     * @param string $login
     * @param string $password
     */
    public function __construct($login, $password)
    {
        $this->login = $login;
        $this->password = $this->maybeEncode($password);
    }

    /**
     * Encodes the password using the BCRYPT algorithm if it's not already
     * encoded.
     *
     * @param string $password
     *
     * @return string
     */
    private function maybeEncode($password)
    {
        if (!password_needs_rehash($password, PASSWORD_BCRYPT)) {
            return $password;
        }

        return password_hash($password, PASSWORD_BCRYPT);
    }
}
```

### Example 9

```php
$userReflection = new ReflectionObject($user);

$maybeEncodeReflection = $userReflection->getMethod('maybeEncode');

$maybeEncodeReflection->setAccessible(true);
$maybeEncodeReflection->invoke($user, $password);
$maybeEncodeReflection->setAccessible(false);
```

### Example 10

```php
$userReflection = new ReflectionObject($user);

$maybeEncodeReflection = $userReflection->getMethod('maybeEncode');

$maybeEncodeClosure = $maybeEncodeReflection->getClosure($user);

$maybeEncodeClosure($password);
```

## Source

https://carlalexander.ca/php-reflection-api-fundamentals/
