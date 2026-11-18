---
title: "Importing data into WordPress using the strategy pattern
			

			

				Being a plugin developer isn’t easy. You have to get your plugin to work with WordPress. But more often than not, you also need it to interact with other plugins.
This interaction can take various forms. For example, you might need to modify another plugin’s behaviour using the plugin API. Or you might want to help customers migrate away from another plugin (or product) to yours.
This second scenario is the one that we’re going to look at in this article. It’s a good opportunity to introduce a new software design pattern. We call it the strategy pattern.

What is the strategy pattern?"
url: https://carlalexander.ca/importing-data-wordpress-strategy-pattern/
slug: importing-data-wordpress-strategy-pattern
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/importing-data-wordpress-using-strategy-pattern/
---

# Strategy Pattern
			

			

				Being a plugin developer isn’t easy. You have to get your plugin to work with WordPress. But more often than not, you also need it to interact with other plugins.
This interaction can take various forms. For example, you might need to modify another plugin’s behaviour using the plugin API. Or you might want to help customers migrate away from another plugin (or product) to yours.
This second scenario is the one that we’re going to look at in this article. It’s a good opportunity to introduce a new software design pattern. We call it the strategy pattern.

What is the strategy pattern?

## Summary

Strategy pattern for interchangeable algorithms. Defining family of algorithms (importers, data sources) and making them interchangeable at runtime.

## Code examples

### Example 1

```php
class Importer
{
}
```

### Example 2

```php
interface DataConverterInterface
{
}
```

### Example 3

```php
class Importer
{
    /**
     * The data converter used by the importer.
     *
     * @var DataConverterInterface
     */
    private $converter;

    /**
     * Constructor.
     *
     * @param DataConverterInterface $converter
     */
    public function __construct(DataConverterInterface $converter)
    {
        $this->converter = $converter;
    }
}
```

### Example 4

```php
class Importer
{
    // ...

    /**
     * Import a data file.
     * 
     * @param string $filename
     *
     * @return bool|WP_Error
     */
    public function import($filename)
    {
        if (!is_readable($filename)) {
            return new WP_Error('file_unreadable', sprintf('Unable to read "%" data file.', $filename));
        }

        // ...        

        return true;
    }
}
```

### Example 5

```php
class Importer
{
    // ...

    /**
     * Import a data file.
     * 
     * @param string $filename
     *
     * @return bool|WP_Error
     */
    public function import_from_file($filename)
    {
        if (!is_readable($filename)) {
            return new WP_Error('file_unreadable', sprintf('Unable to read "%" data file.', $filename));
        }

        $import_data = file($filename, FILE_IGNORE_NEW_LINES);

        if (!is_array($import_data)) {
            return new WP_Error('parse_error', sprintf('Failed to parse the "%" data file.', $filename));
        }

        // ...        

        return true;
    }
}
```

### Example 6

```php
class CustomerImporter
{
    // ...
}

interface CustomerDataConverterInterface
{
    // ...
}
```

### Example 7

```php
class CustomerImporter
{
    // ...

    /**
     * Import a customer data file.
     * 
     * @param string $filename
     *
     * @return bool|WP_Error
     */
    public function import_from_file($filename)
    {
        if (!is_readable($filename)) {
            return new WP_Error('file_unreadable', sprintf('Unable to read "%" customer data file.', $filename));
        }

        $customer_data = file($filename, FILE_IGNORE_NEW_LINES);

        if (!is_array($customer_data)) {
            return new WP_Error('parse_error', sprintf('Failed to parse the "%" customer data file.', $filename));
        }

        // ...        

        return true;
    }
}
```

### Example 8

```php
class CustomerImporter
{
    // ...

    /**
     * Add a new customer into the WordPress database.
     *
     * @param string $name
     * @param string $email
     * @param string $details
     *
     * @return int|WP_Error
     */
    private function add_customer($name, $email, $details = '')
    {
        $customer_id = wp_insert_post(array(
            'post_title' => $name,
            'post_content' => $details,
            'post_status' => 'publish',
            'post_type' => 'customer'
        ), true);

        if ($customer_id instanceof WP_Error) {
            return $customer_id;
        }

        update_post_meta($customer_id, 'email', $email);

        return $customer_id;
    }
}
```

### Example 9

```php
interface CustomerDataConverterInterface
{
    /**
     * Convert the given data array into an array of customers. The returned
     * array should use the following format:
     *
     * array(
     *     array(
     *         'name'    => (string) Name of the customer.
     *         'email'   => (string) Email address of the customer.
     *         'details' => (string) The customer details.
     *     )
     * )
     *
     * @param array $data
     *
     * @return array
     */
    public function convert(array $data);
}
```

### Example 10

```php
class CustomerImporter
{
    // ...

    /**
     * Import a customer data file.
     *
     * @param string $filename
     *
     * @return bool|WP_Error
     */
    public function import_from_file($filename)
    {
        if (!is_readable($filename)) {
            return new WP_Error('file_unreadable', sprintf('Unable to read "%" customer data file.', $filename));
        }

        $customer_data = file($filename, FILE_IGNORE_NEW_LINES);

        if (!is_array($customer_data)) {
            return new WP_Error('parse_error', sprintf('Failed to parse the "%" customer data file.', $filename));
        }

        $customers = $this->converter->convert($customer_data);

        // ...

        return true;
    }
}
```

### Example 11

```php
class CustomerImporter
{
    // ...

    /**
     * Import a customer data file.
     *
     * @param string $filename
     *
     * @return bool|WP_Error
     */
    public function import_from_file($filename)
    {
        if (!is_readable($filename)) {
            return new WP_Error('file_unreadable', sprintf('Unable to read "%" customer data file.', $filename));
        }

        $customer_data = file($filename, FILE_IGNORE_NEW_LINES);

        if (!is_array($customer_data)) {
            return new WP_Error('parse_error', sprintf('Failed to parse the "%" customer data file.', $filename));
        }

        $customers = $this->converter->convert($customer_data);

        foreach ($customers as $customer) {
            $this->add_customer($customer['name'], $customer['email'], $customer['details']);
        }

        return true;
    }
}
```

### Example 12

```php
class CSVCustomerDataConverter implements CustomerDataConverterInterface
{
}
```

### Example 13

```php
class CSVCustomerDataConverter implements CustomerDataConverterInterface
{
    /**
     * Convert the given CSV data array into an array of customers. The returned
     * array should use the following format:
     *
     * @param array $data
     *
     * @return array
     */
    public function convert(array $data)
    {
        // ..
    }
}
```

### Example 14

```php
class CSVCustomerDataConverter implements CustomerDataConverterInterface
{
    /**
     * Convert the given CSV data array into an array of customers. The returned
     * array should use the following format:
     *
     * @param array $data
     *
     * @return array
     */
    public function convert(array $data)
    {
        $customers = array();

        foreach ($data as $row) {
            $row = str_getcsv($row);
            $customers[] = array(
                'name' => $row[0],
                'email' => $row[1],
                'details' => $row[2],
            );
        }

        return $customers;
    }
}
```

## Source

https://carlalexander.ca/importing-data-wordpress-strategy-pattern/
