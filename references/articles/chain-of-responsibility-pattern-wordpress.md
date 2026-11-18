---
title: "Using the chain-of-responsibility pattern to hash WordPress passwords
			

			

				“Passwords Evolved” is an open source WordPress plugin that I’ve built and maintained over the years. It’s a security plugin that prevents someone from using a password that has appeared in a data breach. To do that, it leverages the “Have I Been Pwned?” API to check if the password you’re using was found in a breach.
The plugin also changes the hashing function used to hash WordPress passwords. Initially, the plugin only supported the bcrypt hashing function. This hashing function has been standard since PHP 5.5.
Since PHP 7.0, it’s been possible to hash passwords using a newer function called Argon2. Argon2 is available natively since PHP 7.2. Before that, you had to use the libsodium library to use Argon2 with PHP. There’s also a libsodium compatibility layer starting in WordPress 5.2.
Checking for and using all these different hashing functions sounds like a headache waiting to happen. But, in fact, it’s not that hard to design a set of classes to handle all these different cases. The “Chain-of-Responsibility” pattern was created for situations such as this one.

What is the “Chain-of-Responsibility” pattern?"
url: https://carlalexander.ca/chain-of-responsibility-pattern-wordpress/
slug: chain-of-responsibility-pattern-wordpress
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/using-chain-responsibility-pattern-hash-wordpress-passwords/
---

# Chain of Responsibility Pattern
			

			

				“Passwords Evolved” is an open source WordPress plugin that I’ve built and maintained over the years. It’s a security plugin that prevents someone from using a password that has appeared in a data breach. To do that, it leverages the “Have I Been Pwned?” API to check if the password you’re using was found in a breach.
The plugin also changes the hashing function used to hash WordPress passwords. Initially, the plugin only supported the bcrypt hashing function. This hashing function has been standard since PHP 5.5.
Since PHP 7.0, it’s been possible to hash passwords using a newer function called Argon2. Argon2 is available natively since PHP 7.2. Before that, you had to use the libsodium library to use Argon2 with PHP. There’s also a libsodium compatibility layer starting in WordPress 5.2.
Checking for and using all these different hashing functions sounds like a headache waiting to happen. But, in fact, it’s not that hard to design a set of classes to handle all these different cases. The “Chain-of-Responsibility” pattern was created for situations such as this one.

What is the “Chain-of-Responsibility” pattern?

## Summary

Chain of responsibility pattern for sequential processing. Creating pipelines where each handler decides whether to process or pass to next handler. Example uses password hashing but applies to validation, scanning, filtering.

## Code examples

### Example 1

```php
/**
 * A password hasher hashes a password using a hashing algorithm.
 */
interface PasswordHasherInterface
{
    /**
     * Hashes the given password. Returns null if unable to hash password.
     *
     * @param string $password
     *
     * @return string|null
     */
    public function hash_password($password);

    /**
     * Checks if the password hasher supports the given hash for verification.
     *
     * @param string $hash
     *
     * @return bool
     */
    public function is_hash_supported($hash);

    /**
     * Checks if the given hash is valid. If a hash is invalid, we need to rehash it.
     *
     * @param string $hash
     *
     * @return bool
     */
    public function is_hash_valid($hash);

    /**
     * Validates that the given password matches the given hash.
     *
     * @param string $password
     * @param string $hash
     *
     * @return bool
     */
    public function is_password_valid($password, $hash);
}
```

### Example 2

```php
/**
 * Password hasher that uses the builtin WordPress password hasher.
 */
class WordPressPasswordHasher implements PasswordHasherInterface
{
    /**
     * WordPress password hasher.
     *
     * @var \PasswordHash
     */
    private $wordpress_hasher;

    /**
     * Constructor.
     *
     * @param \PasswordHash $wordpress_hasher
     */
    public function __construct(\PasswordHash $wordpress_hasher)
    {
        $this->wordpress_hasher = $wordpress_hasher;
    }

    /**
     * {@inheritdoc}
     */
    public function hash_password($password)
    {
        return $this->wordpress_hasher->HashPassword($password);
    }

    /**
     * {@inheritdoc}
     */
    public function is_hash_supported($hash)
    {
        return 0 === strpos($hash, '$P$');
    }

    /**
     * {@inheritdoc}
     */
    public function is_hash_valid($hash)
    {
        return false;
    }

    /**
     * {@inheritdoc}
     */
    public function is_password_valid($password, $hash)
    {
        return $this->wordpress_hasher->CheckPassword($password, $hash);
    }
}
```

### Example 3

```php
/**
 * Password hasher that uses the native PHP password hashing functions.
 */
class NativePasswordHasher implements PasswordHasherInterface
{
    /**
     * Algorithm used when hashing a password.
     *
     * @var int
     */
    private $algorithm;

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->algorithm = PASSWORD_DEFAULT;

        if (defined('PASSWORD_ARGON2ID')) {
            $this->algorithm = PASSWORD_ARGON2ID;
        } elseif (defined('PASSWORD_ARGON2I')) {
            $this->algorithm = PASSWORD_ARGON2I;
        }
    }

    /**
     * {@inheritdoc}
     */
    public function hash_password($password)
    {
        return password_hash($password, $this->algorithm);
    }

    /**
     * {@inheritdoc}
     */
    public function is_hash_supported($hash)
    {
        if (0 === strpos($hash, '$argon2id$')) {
            return defined('PASSWORD_ARGON2ID');
        } elseif (0 === strpos($hash, '$argon2i$')) {
            return defined('PASSWORD_ARGON2I');
        }

        return 0 === strpos($hash, '$2');
    }

    /**
     * {@inheritdoc}
     */
    public function is_hash_valid($hash)
    {
        return !password_needs_rehash($hash, $this->algorithm);
    }

    /**
     * {@inheritdoc}
     */
    public function is_password_valid($password, $hash)
    {
        return password_verify($password, $hash);
    }
}
```

### Example 4

```php
/**
 * Manages a chain of password hashers.
 */
class PasswordHasherChain implements PasswordHasherInterface
{
}
```

### Example 5

```php
/**
 * Manages a chain of password hashers.
 */
class PasswordHasherChain implements PasswordHasherInterface
{
    /**
     * The password hashers that the chain handles.
     *
     * @var PasswordHasherInterface[]
     */
    private $password_hashers;

    /**
     * Constructor.
     *
     * @param PasswordHasherInterface[] $password_hashers
     */
    public function __construct(array $password_hashers = [])
    {
        $this->password_hashers = $password_hashers;
    }

    // ...
}
```

### Example 6

```php
/**
 * Manages a chain of password hashers.
 */
class PasswordHasherChain implements PasswordHasherInterface
{
    /**
     * The password hashers that the chain handles.
     *
     * @var PasswordHasherInterface[]
     */
    private $password_hashers;

    /**
     * Constructor.
     *
     * @param PasswordHasherInterface[] $password_hashers
     */
    public function __construct(array $password_hashers = [])
    {
        $this->password_hashers = array_filter($password_hashers, function ($password_hasher) {
            return $password_hasher instanceof PasswordHasherInterface;
        });
    }

    // ...
}
```

### Example 7

```php
/**
 * Manages a chain of password hashers.
 */
class PasswordHasherChain implements PasswordHasherInterface
{
    // ...

    /**
     * Get the password hasher that supports the given hash.
     *
     * @param string $hash
     *
     * @return PasswordHasherInterface|null
     */
    private function get_password_hasher($hash)
    {
        return array_reduce($this->password_hashers, function ($found, PasswordHasherInterface $password_hasher) use ($hash) {
            if (!$found instanceof PasswordHasherInterface && $password_hasher->is_hash_supported($hash)) {
                $found = $password_hasher;
            }
            return $found;
        });
    }
}
```

### Example 8

```php
/**
 * Manages a chain of password hashers.
 */
class PasswordHasherChain implements PasswordHasherInterface
{
    // ...

    /**
     * {@inheritdoc}
     */
    public function is_hash_supported($hash)
    {
        return $this->get_password_hasher($hash) instanceof PasswordHasherInterface;
    }

    /**
     * {@inheritdoc}
     */
    public function is_hash_valid($hash)
    {
        $password_hasher = $this->get_password_hasher($hash);

        if (!$password_hasher instanceof PasswordHasherInterface) {
            return false;
        }

        return $password_hasher->is_hash_valid($hash);
    }

    // ...
}
```

### Example 9

```php
/**
 * Manages a chain of password hashers.
 */
class PasswordHasherChain implements PasswordHasherInterface
{
    // ...

    /**
     * {@inheritdoc}
     */
    public function hash_password($password)
    {
        $hash = array_reduce($this->password_hashers, function ($hash, PasswordHasherInterface $password_hasher) use ($password) {
            if (empty($hash)) {
                $hash = $password_hasher->hash_password($password);
            }

            return $hash;
        });

        if (empty($hash)) {
            throw new \RuntimeException('Could not create a hash for the given password.');
        }

        return $hash;
    }

    // ...

    /**
     * {@inheritdoc}
     */
    public function is_password_valid($password, $hash)
    {
        return array_reduce($this->password_hashers, function ($check, PasswordHasherInterface $password_hasher) use ($password, $hash) {
            if (true !== $check) {
                $check = $password_hasher->is_password_valid($password, $hash);
            }

            return $check;
        }, false);
    }

    // ...
}
```

### Example 10

```php
if (!class_exists('PasswordHash')) {
    require_once ABSPATH . WPINC . '/class-phpass.php';
}

$password_hasher = new PasswordHasherChain([
    new NativePasswordHasher(),
    new WordPressPasswordHasher(new \PasswordHash(8, true)),
]);
```

## Source

https://carlalexander.ca/chain-of-responsibility-pattern-wordpress/
