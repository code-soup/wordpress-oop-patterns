---
title: "WordPress for the adventurous: Loading
			

			

				I’m sure you woke up thinking “I wish I knew more about WordPress loading.”. Ok… maybe not (it’s just me isn’t it?). It’s just not something you deal with every day.
No, plugins and themes make up your days. That’s what you use to build your custom WordPress solutions. There’s no need to know about the internal process that starts up WordPress.
Yet you can’t ignore it once you start building complex WordPress solutions. Or if you plan on distributing a plugin or theme. That changes the dynamic of things.
Your little world with the plugins and themes you know is gone. You’re in the larger (and messier) WordPress world now. That means you have to play nice with everyone else (damn).

That’s why loading is important"
url: https://carlalexander.ca/wordpress-adventurous-loading/
slug: wordpress-adventurous-loading
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/wordpress-for-adventurous-loading/
---

# WordPress for the adventurous: Loading
			

			

				I’m sure you woke up thinking “I wish I knew more about WordPress loading.”. Ok… maybe not (it’s just me isn’t it?). It’s just not something you deal with every day.
No, plugins and themes make up your days. That’s what you use to build your custom WordPress solutions. There’s no need to know about the internal process that starts up WordPress.
Yet you can’t ignore it once you start building complex WordPress solutions. Or if you plan on distributing a plugin or theme. That changes the dynamic of things.
Your little world with the plugins and themes you know is gone. You’re in the larger (and messier) WordPress world now. That means you have to play nice with everyone else (damn).

That’s why loading is important

## Summary

How WordPress bootstraps and loads. Understanding wp-load.php, wp-settings.php, and the WordPress loading sequence.

## Code examples

### Example 1

```php
/**
 * Ensures that the plugin is always the first one to be loaded.
 *
 * @param array $active_plugins
 *
 * @return array
 */
public function ensure_loaded_first(array $active_plugins)
{
    $basename = plugin_basename(__FILE__);
    $key = array_search($basename, $active_plugins);

    if (false !== $key) {
        array_splice($active_plugins, $key, 1);
        array_unshift($active_plugins, $basename);
    }

    return $active_plugins;
}
add_filter('pre_update_option_active_plugins', 'ensure_loaded_first');
add_filter('pre_update_site_option_active_sitewide_plugins', 'ensure_loaded_first');
```

## Source

https://carlalexander.ca/wordpress-adventurous-loading/
