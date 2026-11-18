---
title: "How to use placeholders for WordPress translations
			

			

				Have you ever worked on localization with other web frameworks? If so, you might be familiar with the idea of using keys to identify translation strings. These keys are how your translation system finds the localized text to use inside your application.
If you’ve been doing localization with WordPress, you know that it doesn’t work that way. With WordPress, you use the original (usually English) content string as your translation key. This can be convenient because you always know what the original string was.
That said, it’s still possible to do WordPress localization using keys instead content strings. This can be useful if you come from these different programming backgrounds. You might like to keep working the way you’re used to. Let’s look at how you can do that!

Why would use keys for translations?"
url: https://carlalexander.ca/placeholders-wordpress-translations/
slug: placeholders-wordpress-translations
fetched: 2026-11-18
catalog_url: https://carlalexander.ca/how-to-use-placeholders-wordpress-translations/
---

# How to use placeholders for WordPress translations
			

			

				Have you ever worked on localization with other web frameworks? If so, you might be familiar with the idea of using keys to identify translation strings. These keys are how your translation system finds the localized text to use inside your application.
If you’ve been doing localization with WordPress, you know that it doesn’t work that way. With WordPress, you use the original (usually English) content string as your translation key. This can be convenient because you always know what the original string was.
That said, it’s still possible to do WordPress localization using keys instead content strings. This can be useful if you come from these different programming backgrounds. You might like to keep working the way you’re used to. Let’s look at how you can do that!

Why would use keys for translations?

## Summary

Internationalization (i18n) with sprintf-style placeholders. Proper translation string formatting for variable content.

## Code examples

### Example 1

```php
// myplugin/index.php

/*
Plugin Name: My Plugin
Text Domain: myplugin
Author: Carl Alexander
Author URI: https://carlalexander.ca
License: GPL2
*/

/**
 * Add our plugin's admin page
 */
function myplugin_add_admin_page() {
    add_options_page(__('admin.page_title', 'myplugin'), __('admin.menu_title', 'myplugin'), 'install_plugins', 'myplugin', 'myplugin_render_admin_page');
}
add_action('admin_menu', 'myplugin_add_admin_page');

/**
 * Render our plugin's admin page.
 */
function myplugin_render_admin_page() {
    ?>
    <h1><?php _e('admin.page_title', 'myplugin'); ?></h1>
    <p><?php _e('admin.help_text', 'myplugin'); ?></p>
    <?php
}
```

### Example 2

```php
msgid ""
msgstr ""
"Project-Id-Version: My Plugin\n"
"Report-Msgid-Bugs-To: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Language-Team: Carl Alexander\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\n"

msgid "admin.page_title"
msgstr ""

msgid "admin.menu_title"
msgstr ""

msgid "admin.help_text"
msgstr ""
```

### Example 3

```php
msgid ""
msgstr ""
"Project-Id-Version: My Plugin\n"
"Report-Msgid-Bugs-To: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Language-Team: Carl Alexander\n"
"Language: en_US\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\n"

msgid "admin.page_title"
msgstr "My Plugin Settings"

msgid "admin.menu_title"
msgstr "My Plugin"

msgid "admin.help_text"
msgstr "You can find the available plugin settings below."
```

### Example 4

```php
/**
 * Register the plugin's translations files with WordPress.
 */
function myplugin_load_translation() {
    load_plugin_textdomain('myplugin', false, basename(dirname(__FILE__))  . '/translations');
}
add_action('plugins_loaded', 'myplugin_load_translation');
```

### Example 5

```php
/**
 * Enforces the use of the "en_US" locale for translations.
 *
 * This is necessary since we're using placeholder values for text instead of English text.
 *
 * @param string $locale
 * @param string $domain
 *
 * @return string
 */
function myplugin_enforce_locale($locale, $domain) {
    if ('myplugin' == $domain) {
        $locale = 'en_US';
    }

    return $locale;
}
add_filter('plugin_locale', 'myplugin_enforce_locale', 10, 2);
```

## Source

https://carlalexander.ca/placeholders-wordpress-translations/
