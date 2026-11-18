---
title: "Introduction to WordPress acceptance testing
			

			

				As a WordPress developer, the topic of testing isn’t something that we hear about that often. And, if we do hear about it, it’s more often than not just one specific type of testing: unit testing. (That’s even the one that I’ve thought first!) In fact, it’s not uncommon to associate testing with unit testing because of this.
But software testing is an enormous field. There are a lot of different types of testing. While they might not all be as useful as unit testing, they still all serve a specific purpose.
That said, there are other types of testing that are as useful (or almost as useful!) as unit testing. Acceptance testing is one of them. It’s especially useful if you’re a plugin or theme developer.

Defining acceptance testing"
url: https://carlalexander.ca/introduction-wordpress-acceptance-testing/
slug: introduction-wordpress-acceptance-testing
fetched: 2026-11-18
---

# Introduction to WordPress acceptance testing
			

			

				As a WordPress developer, the topic of testing isn’t something that we hear about that often. And, if we do hear about it, it’s more often than not just one specific type of testing: unit testing. (That’s even the one that I’ve thought first!) In fact, it’s not uncommon to associate testing with unit testing because of this.
But software testing is an enormous field. There are a lot of different types of testing. While they might not all be as useful as unit testing, they still all serve a specific purpose.
That said, there are other types of testing that are as useful (or almost as useful!) as unit testing. Acceptance testing is one of them. It’s especially useful if you’re a plugin or theme developer.

Defining acceptance testing

## Summary

End-to-end testing for WordPress using Codeception or similar tools. Testing complete user workflows through browser automation.

## Code examples

### Example 1

```php
<?php
/**
 * Test summary: Look the "powered by WordPress" message on the homepage.
 *
 * Test details:
 * - Go to the homepage
 * - Look for the "Proudly powered by WordPress" message
 */
$I = new AcceptanceTester( $scenario );
$I->wantTo( 'Test that we can see the "powered by WordPress" message.' );

// Go to the homepage
$I->amOnPage('/');

// Look for the "powered by WordPress" message
$I->see('Proudly powered by WordPress');
```

## Source

https://carlalexander.ca/introduction-wordpress-acceptance-testing/
