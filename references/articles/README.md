# Article index

Generated 2026-11-18. One local file per Carl Alexander article.

- [Why object-oriented programming is your next step as a WordPress developer
			

			

				You’re a WordPress developer. You might have a few plugins under your belt or a theme or two. You build WordPress sites for clients or just for yourself. You’ve heard of object-oriented programming, but, each time you look into it, it makes no sense!
You tell yourself object-oriented programming isn’t useful or worth the trouble. The goal of this article is to focus on explaining this value to you. At the end of this article, you should have a clear understanding of why you should learn it.

Managing your expectation](object-oriented-programming-next-step-wordpress-developer.md) — https://carlalexander.ca/object-oriented-programming-next-step-wordpress-developer/
- [How to approach object-oriented programming with WordPress
			

			

				I gave a talk on object-oriented programming with WordPress at WordCamp Miami 2019. This is the companion article that I wrote for it. If you’re just looking for the slides, click here.
You’re a WordPress developer who wants to use object-oriented programming in their next project. You’re already familiar with concepts like inheritance. The issue is that you’re not sure how to apply those concepts to design classes that feel useful.
This isn’t something to feel ashamed about! In fact, it’s a common problem when trying to use object-oriented programming with WordPress. It’s hard to know how to design classes that work well with WordPress. (That’s why this site has so many articles dedicated to that topic.)
But why is this so hard to do? Well, there are a few things going on. And together they create this situation that makes using object-oriented programming with WordPress complicated.

Going back to the beginning](approaching-object-oriented-programming-wordpress.md) — https://carlalexander.ca/approaching-object-oriented-programming-wordpress/
- [On becoming a WordPress expert
			

			

				This all started with a thought experiment about WordPress recruiting. Something I’ve done a fair amount of in the past.
Let’s say I’m looking to hire a WordPress expert. What defines that person as a top tier WordPress developer? What knowledge or characteristics am I looking for?
WordPress powers a large part of the web. It’s also the livelihood for thousands of developers. Those are amazing things, but it also creates problems. One of them is that it’s hard to evaluate your or someone else’s skill level.
So we’re going to look into that. It’s worth noting that there’s no definitive or objective answer to that question. We’re all biased. We have our own opinions on what it means to be an expert.

That doesn’t mean that you shouldn’t try to answer the question. The goal here is to help you think about where you stand on the topic. It’s also an opportunity to think about where you are and where you’d like to be.
Let’s focus on things you can learn](becoming-wordpress-expert.md) — https://carlalexander.ca/becoming-wordpress-expert/
- [Thoughts on type safety with WordPress
			

			

				As a WordPress developer, you might be familiar with type hints. These are the elements of your php docblock that let other developers know about the type that you expect a function or method parameter to be. Here’s an example:
/**
 * Return the first element in an array.
 *
 * @param array $array
 */
function first($array)
{
    foreach ($array as $value) {
        return $value
    }
}
@param array $array in the  first function above is the type hint for the array parameter. It tells other developers that we expect the parameter to be an array. But it doesn’t prevent them from passing you an integer or something else that wouldn’t work in a foreach loop.
Preventing these types of errors is what we call type safety. Any time that you write code, you’re making assumptions about the type of the variable you’re working with. That’s why type safety is an important to aspect of programming.
As a developer, you have to make a choice about how you want to deal with type safety. You have three overall approaches to deal with type errors.

You can:

Do nothing and let other developers deal with type errors from not respecting your type hints.
Program your function or method defensively to deal with developers not passing you the correct parameter type.
Have PHP enforce the parameter types of your functions or methods.

Since PHP 7, PHP developers favour the third approach of PHP enforcing type. But, as WordPress developers, we don’t always have that luxury. So it’s important to understand the tradeoffs between these different approaches to type safety.

WordPress still supports older versions of PHP](type-safety-wordpress.md) — https://carlalexander.ca/type-safety-wordpress/
- [Thoughts on teaching object-oriented programming with WordPress and over-engineering
			

			

				This site has grown a lot in the last year or so. We’ve spent a lot of time going over object-oriented solutions to WordPress problems. So much so that, we have a small library’s worth of material that you can refer to.
With any type of growth, criticism will arise. This is a good thing. I’m a big proponent of “Strong opinions, weakly held“. But this can’t happen without discussion and debate. In the long run, I always feel it leads to a better outcome. (Well, that’s as long you don’t get stuck just debating!)
Recently, there was a debate on the nature of the solutions that you’ll see on this site. They’re over-engineered. I think this is a valid criticism and I wanted to share some of my thoughts on the whole thing.

My teaching thesis](teaching-object-oriented-programming-overengineering.md) — https://carlalexander.ca/teaching-object-oriented-programming-overengineering/
- [Designing entities using WordPress custom post types
			

			

				Custom post types are one the most powerful features of WordPress. You can use them to save any type of data that you want in the wp_posts table. Most plugins that build complex features on top of WordPress (e.g. WooCommerce) rely on them.
But custom post types aren’t just useful for developing new features on top of WordPress. They also allow us to rethink how we use object-oriented programming with WordPress. And, as we’ll see, this is an important step in your journey learning object-oriented programming with WordPress.
That’s because having a different view of custom post types will expand your object-oriented design horizons. They’ll help you build new types of classes that you might not have considered before. And this can be a game-changer when creating larger object-oriented plugins or themes.

Reviewing how to use an interface with custom post types](designing-entities-wordpress-custom-post-types.md) — https://carlalexander.ca/designing-entities-wordpress-custom-post-types/
- [Designing a class to manage WordPress posts
			

			

				When building a plugin, it’s not uncommon to need to fetch posts from the database. After all, you might be using your own custom post type. Or maybe, you built a special functionality on top of posts and you want to find them that way. Those are just a few reasons why your plugin might need to query WordPress for posts.
Regardless of the reason, the standard way of doing that is to use the WP_Query class. This lets us create WordPress queries in a safe way outside the loop. The problem is that they’re not easy to reuse.
For example, let’s say that you want a query to fetch only one result. You’re always going to need to add the 'posts_per_page' => 1 and 'no_found_rows' => true query arguments. That last one removes the SQL_CALC_FOUND_ROWS query used by WordPress pagination. (You don’t need to paginate one result!) This lets us improve performance a bit by removing the unnecessary query.
Now, you’d need to copy these two query arguments whenever you create a query to fetch a single result. This is far from ideal. So let’s look at designing a solution to this problem. Using object-oriented programming, of course!

The job](designing-class-manage-wordpress-posts.md) — https://carlalexander.ca/designing-class-manage-wordpress-posts/
- [Saving WordPress custom post types using an interface
			

			

				Custom post types are a powerful WordPress functionality. Everyone that works with WordPress long enough ends up using them. A custom post type can be anything. That flexibility is the source of much of its power. When using custom post type, you’re only limited by your imagination (trademark pending).
This flexibility also makes it a great use case for designing an interface. This article will put you in the interface creator seat. Exciting, I know!
As the interface creator, you’re in charge of designing the interface contract. This means that you get to dictate how someone use your interface (insert evil laughter here). It’s not all (evil) roses though.
The job gives you quite a lot of responsibility. This can make it hard for you to know where to start or what to do. Lucky for you, that’s what this article will help you with.

How WordPress handles post data](saving-wordpress-custom-post-types-using-interface.md) — https://carlalexander.ca/saving-wordpress-custom-post-types-using-interface/
- [Using dependency injection with WordPress
			

			

				As you use object-oriented programming with WordPress more and more, you’re going to encounter new sets of problems. These problems aren’t as simple as the ones that you encountered when you started. But that’s also good news. It also means that you’re making progress.
One set of problems that you start to encounter as you advance in your use of object-oriented programming deal with scaling. As your code has more and more classes, it becomes a challenge to assemble these classes together. That’s why in the past we looked at how to design a class whose job was to do that.
But there are other problems that come with having a lot of classes in your code. It’s how much your classes depend on other classes. This is what we call coupling in programming. (Not just object-oriented programming.)
To help with coupling, a famous software engineer (Robert C. Martin who’s also known as Uncle Bob) created the dependency inversion principle. It helps you decouple your classes by making dependencies external to them. (There’s more to it than that. But this is one of the core elements of the dependency inversion principle.)
This reduces coupling but creates a new problem as well. That problem is that you can’t initialize objects inside your class anymore. You have to pass them to your own object through its constructor or some other method like a setter method.
This makes it even harder to assemble your classes together. This is why software engineers created dependency injection. It’s a programming technique that helps solve this problem.
Most web application frameworks use it in some form or another. But that’s not the case with WordPress since a lot of its code isn’t object-oriented. That said, if you want to build an object-oriented plugin for WordPress, it’s pretty much mandatory. Lucky for us, it’s not that hard to use dependency injection in your own code!

A small warning about PHP versions](dependency-injection-wordpress.md) — https://carlalexander.ca/dependency-injection-wordpress/
- [Dependency inversion principle and WordPress
			

			

				So let’s talk about coupling! Coupling is a complicated problem because you can never get rid of it completely. All that you can do is control how much it spreads. And there’s more than one way to do that.
One of these ways is the dependency inversion principle. It’s one of the most important principles in object-oriented design. And it’s why it’s part of the famous SOLID design principles. (It’s the “D” in SOLID.)
The dependency inversion principle isn’t something that you see with WordPress. That’s because most WordPress developers don’t use object-oriented programming. (But it’s always a good time to start if you’re not using it!) And the dependency inversion principle only helps when you’ve been using it for a while.
But what makes the dependency inversion principle special? Why is it such almost a mandatory aspect of object-oriented design? These are good questions that you deserve an answer to.

What is the dependency inversion principle?](dependency-inversion-principle-wordpress.md) — https://carlalexander.ca/dependency-inversion-principle-wordpress/
- [Single responsibility principle, WordPress and You
			

			

				For WordPress developers, it can be hard to improve your PHP skills. You lack the resources or tutorials to drive home these concepts. This happened just a few weeks ago when Nathaniel asked for help with his Stack Overflow question.
He was looking for help applying the single responsibility principle with WordPress. I sent him a bunch of replies but closed off saying I needed to write a post about it. This article is a detailed explanation of my thoughts following that conversation.
As WordPress developer, you might have started working with or looking into object-oriented programming. Maybe you even heard of something called SOLID.
As a whole, SOLID can be an intimidating topic. But the single responsibility principle is just one part of it (it’s the ‘S’ in SOLID). That makes it a more manageable topic to discuss and help you with.
At the end of this article, you should have a better understanding of it. You can also use the provided code samples in your own plugins and themes.

Single Responsibility Principle explained](single-responsibility-principle-wordpress.md) — https://carlalexander.ca/single-responsibility-principle-wordpress/
- [Coupling and cohesion in WordPress and beyond
			

			

				A concept that comes up a lot while doing object-oriented design is coupling. We use it to describe how connected the different parts of your code are to one another. But, even explained like that, the concept of coupling can still be a hard to grasp.
On top of that, we often pair it with another concept called cohesion. We use cohesion to describe how well the different parts of your code fit together. This tells us whether everything was well-designed or not.
In fact, this is why coupling and cohesion are so important. There’s a strong relationship between them and the quality of your code. Code that doesn’t have any major coupling or cohesion problem is more often of higher quality. It’s more maintainable, reusable and less prone to problems.
That’s why you want to keep these two concepts in the back of your mind when programming. But that’s easier said than done when these concepts aren’t well understood. That’s why we’ll demystify them today.

Defining coupling and cohesion](coupling-cohesion-wordpress.md) — https://carlalexander.ca/coupling-cohesion-wordpress/
- [Using the chain-of-responsibility pattern to hash WordPress passwords
			

			

				“Passwords Evolved” is an open source WordPress plugin that I’ve built and maintained over the years. It’s a security plugin that prevents someone from using a password that has appeared in a data breach. To do that, it leverages the “Have I Been Pwned?” API to check if the password you’re using was found in a breach.
The plugin also changes the hashing function used to hash WordPress passwords. Initially, the plugin only supported the bcrypt hashing function. This hashing function has been standard since PHP 5.5.
Since PHP 7.0, it’s been possible to hash passwords using a newer function called Argon2. Argon2 is available natively since PHP 7.2. Before that, you had to use the libsodium library to use Argon2 with PHP. There’s also a libsodium compatibility layer starting in WordPress 5.2.
Checking for and using all these different hashing functions sounds like a headache waiting to happen. But, in fact, it’s not that hard to design a set of classes to handle all these different cases. The “Chain-of-Responsibility” pattern was created for situations such as this one.

What is the “Chain-of-Responsibility” pattern?](chain-of-responsibility-pattern-wordpress.md) — https://carlalexander.ca/chain-of-responsibility-pattern-wordpress/
- [Importing data into WordPress using the strategy pattern
			

			

				Being a plugin developer isn’t easy. You have to get your plugin to work with WordPress. But more often than not, you also need it to interact with other plugins.
This interaction can take various forms. For example, you might need to modify another plugin’s behaviour using the plugin API. Or you might want to help customers migrate away from another plugin (or product) to yours.
This second scenario is the one that we’re going to look at in this article. It’s a good opportunity to introduce a new software design pattern. We call it the strategy pattern.

What is the strategy pattern?](importing-data-wordpress-strategy-pattern.md) — https://carlalexander.ca/importing-data-wordpress-strategy-pattern/
- [Using the static factory method pattern with WordPress
			

			

				If you use object-oriented programming, there’s a good chance that you’re familiar with the constructor. It’s this special method that an object-oriented programming language uses to initialize a new object.  In PHP (and a lot of other object-oriented programming languages), the __construct method is a special method reserved for the role of constructor.
The role of the constructor isn’t always well understood. This is especially true when you’re new to object-oriented programming. You know the method exists, but you’re not too sure how to use it.
This can lead to some less than ideal practices around constructors. This is especially true in the WordPress world where two such practices are popular. First, there’s the habit of putting hooks in the constructor. And, because of that habit, WordPress developers tend to overuse the singleton pattern.
These two practices show a misunderstanding of the role that a constructor plays inside a class. This isn’t how object-oriented programming wants you to use constructors. There are other ways to solve those problems without sacrificing the role of a constructor.
Now, this isn’t to say that constructors don’t have any problems either. They do! In fact, that’s why we’re looking at the static factory method pattern. It solves one common problem that constructors have in PHP.

The problem with constructors](static-factory-method-pattern-wordpress.md) — https://carlalexander.ca/static-factory-method-pattern-wordpress/
- [Spying on WordPress with the proxy pattern
			

			

				In a not so distant future, you’ve grown to be quite the WordPress expert. You work for WSIS (WordPress Security Intelligence Service) as an analyst. You’re given your first field mission.
You have to get in deep with WordPress. You need to get intimate information about a WordPress object. Information even WordPress doesn’t want to give you. You need to gain access without detection. The last thing you need is WordPress to know you’re listening to things.
How would your future self do it? Well, he’d use the proxy pattern (good thing you’re reading this article). The proxy pattern is the equivalent of object-oriented tapping. It’s one way to solve the problem of interacting with a class without it being aware of it.
Let’s look at how it works.

Object-oriented tapping with the proxy pattern](spying-wordpress-proxy-pattern.md) — https://carlalexander.ca/spying-wordpress-proxy-pattern/
- [The mediator pattern in WordPress
			

			

				Let’s talk about the plugin API. You can’t write a plugin without using it. Well that’s not quite true. You could, but you’d have a hard (and unpleasant) time without it though. That’s because it’s the cornerstone of your interaction with WordPress.

This means that you can’t build an object-oriented plugin without taking it in consideration. That’s also when the headaches start. You try to find a solution to the problem. You often go back to the usual solutions such as:

Turning your classes into singletons.
Using the API in your constructor.
Flipping a table.

None of the these are great solutions to the problem (especially that last one). But that’s because you’ve been focusing on your problems. You want that sweet plugin you’ve been coding to be object-oriented (who doesn’t?).
Meanwhile, you didn’t stop and think about the plugin API. What does it want?
What does the Plugin API want?](mediator-pattern-wordpress.md) — https://carlalexander.ca/mediator-pattern-wordpress/
- [How to use teaching as a learning tool
			

			

				I spoke at WordCamp Atlanta 2017 on how you could use teaching as a learning tool. This is the companion article that I wrote for it. If you’re just looking for the slides, click here.
As WordPress developers (or developers in general), we’re always looking to improve our skills. We read blog posts, watch screencasts, listen to talks at WordCamps and so on. These are all great ways to learn new things.
But there’s one way to hone your programming skills that doesn’t get as much attention as it should. It’s “learning by teaching“. Teaching is a great way to improve your skills as a developer.
Now, you might be wondering, “Seriously, how can teaching make me a better developer?” People don’t tend to associate teaching with skill building. After all, how could you teach something if you didn’t know it already?
That’s a good question! It does feel like this shouldn’t be able to work. But it does! And that’s why it’s worth taking a better look at this idea of “learning by teaching”.

How can teaching improve your programming skills?](use-teaching-learning-tool.md) — https://carlalexander.ca/use-teaching-learning-tool/
- [Designing a system: WordPress admin pages
			

			

				In a previous article, we saw how to design a class to represent a WordPress admin page. The article was an excellent resource for anyone looking to design a class to solve that specific type of problem. But it was only a starting point.
For example, we used the settings API to handle forms. But the settings API doesn’t quite do the job for every use cases. For those other cases, you’re going to need to manage the submission of a form yourself.
But to handle these different use cases, we’re going to need a more solid foundation. So we’re going to take the work that we did to design our admin page class, and we’re going to take it one step further. We’re going to design a whole system for WordPress admin pages.

Reviewing our admin page class](designing-system-wordpress-admin-pages.md) — https://carlalexander.ca/designing-system-wordpress-admin-pages/
- [Improving a system: Different types of WordPress admin pages
			

			

				In a previous article, we saw how to design a system for WordPress admin pages. The article was an excellent resource for anyone looking for a system to solve that specific type of problem. But it was only a starting point. (That said, you should take the time to read it before reading this article.)
All that we did was convert code from another article into the WordPress admin page system. We didn’t look at any other use cases besides the ones covered in that article already. But the reality is that there are a lot of them.
For example, the article only looked at how to add submenu pages. But there are other types of admin pages besides that one. The admin page system should be able to handle them all.
This is one of several advanced use cases that you might encounter with the WordPress admin page system. That’s why the system as we saw it so far is a great place to start. But handing these uses cases like different types of admin pages might be necessary depending on the kind of project that you’re working on.

Top-level menus](improving-system-wordpress-admin-page-types.md) — https://carlalexander.ca/improving-system-wordpress-admin-page-types/
- [Designing a class representing a WordPress admin page
			

			

				A WordPress plugin can have a lot of different components. For example, some might need to use shortcodes to achieve their purpose. While others might need to create custom post types.
But one component that almost every plugin needs is an admin page. (Or they might even need more than one!) That said, designing an admin page using object-oriented programming isn’t that straightforward. There are a lot of different moving pieces that you have to take in consideration in your design.
A well-designed admin page class will combine these different moving pieces into a cohesive class. The key to achieving this is to understand the role of these different moving pieces in the larger picture of an admin page. We’ll do that by analyzing what makes up an admin page in the first place.

Elements of an admin page](designing-class-wordpress-admin-page.md) — https://carlalexander.ca/designing-class-wordpress-admin-page/
- [Designing a class to represent a WordPress meta box
			

			

				In a previous article, we discussed how to design a class representing a WordPress admin page. This was important because almost every plugin or theme needs an admin page. But this isn’t the only common thing that plugins or themes add to the WordPress admin.
Another one of those is the meta box. If you’re not familiar with meta boxes, they’re the draggable boxes that you see on the post editing screen. It’s quite common for plugins and themes to add post-specific functionality through them.
This makes them a good topic to discuss with object-oriented programming. (Is there really a bad topic to discuss with object-oriented programming!?) And, as we’ll see, meta boxes have a lot of in common with admin pages. This means that designing a class to represent them will be a lot like what we did for admin pages.

What makes a meta box?](designing-class-wordpress-meta-box.md) — https://carlalexander.ca/designing-class-wordpress-meta-box/
- [Designing a system: WordPress REST API endpoints
			

			

				Let’s talk about the WordPress REST API. It’s been around for a little while now, and you might have even started using it in your projects. After all, a lot of us are trying to get more into JavaScript. (Zac Gordon has built a great course if you’re looking to get into it.)
But that doesn’t mean that the standard WordPress REST API will be good enough for your project. There’s a good chance that you’ll need to extend it so that you can do more with it. And that’s done using PHP even if you’re working with JavaScript. (Sorry JavaScript lovers!)
That means that this is still a great excuse to use object-oriented programming with WordPress. (Yay!) In fact, it’s an excellent opportunity to piece different object-oriented concepts together. This will let us design a system to extend the WordPress REST API!

Why not use the controller class?](designing-system-wordpress-rest-api-endpoints.md) — https://carlalexander.ca/designing-system-wordpress-rest-api-endpoints/
- [Designing a system: WordPress event management
			

			

				In a previous article, we went over the concept of events and event listeners. These were classes who were in charge of a specific aspect of an application. This was a more abstract job that touched several parts of an application.
We also saw how you could design these event listeners in WordPress. It required that you rethink how you use the plugin API. (Yes, this is going to be another plugin API article :P)
We’re going to keep going with this idea of events and event listeners. We’re going to design a system for them. We’ll call it an “event management” system. It’s an important tool in your journey to master object-oriented programming in WordPress.

On actions and filters](designing-system-wordpress-event-management.md) — https://carlalexander.ca/designing-system-wordpress-event-management/
- [Designing a system: WordPress routing
			

			

				Developers use WordPress to build all sorts of solutions. They can range from a small website to large application platforms. The larger the project gets, the more common it is to have the need for WordPress to handle custom URLs.
You might want to map a custom URL to a new template, a specific hook or both. These situations get more and more common as you work on larger WordPress projects. This type of problem is a bit of a growing up pain with WordPress.
In framework land, there’s a tool that helps you with that problem. It’s called the routing system. It’s a critical component of most frameworks. It lets you map URLs with different parts of your application.
It’s a tough problem to solve, but a good example of object-oriented design. That’s why we’re going to build one. It’ll show you how object-oriented programming helps you solve harder problems.

But isn’t this the job of the rewrite API?
Not quite. (But excellent question!) The rewrite API allows WordPress to understand human-readable URLs. There’s no question that it’s an important task.
That said, a routing system is a large enough problem that it’s made up of smaller sub-problems. Solving these sub-problems is necessary for the routing system to do its job. And, as you’ll see next, the rewrite API itself only takes care of one of these sub-problems.
The responsibilities of a routing system](designing-system-wordpress-routing.md) — https://carlalexander.ca/designing-system-wordpress-routing/
- [Designing a system: WP-CLI commands
			

			

				Ymir, the WordPress serverless DevOps platform that I’m building, has a lot of distinct parts. There’s the Laravel application which I’ve talked about. But there’s also a WordPress plugin that acts as the bridge between the AWS infrastructure and WordPress.
Part of the bridging process revolves around offloading certain tasks to WP-CLI. This was an architectural decision which deserves its own article. (You can read a short Twitter thread on it here.) That said, this meant that each offloaded task needed its own WP-CLI command.
And there were quite a few tasks to offload! This was an opportunity to use object-oriented programming to design a new system for WordPress. This system will handle the creation and registration of these WP-CLI commands.

How do you create a WP-CLI command?](designing-system-wp-cli-commands.md) — https://carlalexander.ca/designing-system-wp-cli-commands/
- [Designing classes that use the WordPress plugin API
			

			

				The plugin API is one of the cornerstones of WordPress development. There’s no understating its importance. That’s why it’s such a common WordPress development topic (even here).
This importance doesn’t stop when you start using object-oriented programming. If anything, it gets worse! There are quite a few challenges with using the plugin API with object-oriented programming. The first one often being “What do I do with them?”
It’s the type problem that can stop you in your tracks. You want to learn to use object-oriented programming, but the plugin API gets in your way. You get frustrated with it and go back to what you’re comfortable with. Lucky for you, we’ve already explored it here (using the same link for emphasis!).
So we know how to handle WordPress hooks in a class. That’s good, but, now, we’re going to dig a bit deeper. We’re going to start thinking about the jobs of our classes. Where does the plugin API fit when we start thinking about the responsibility of our classes?

Listening to WordPress](designing-classes-wordpress-plugin-api.md) — https://carlalexander.ca/designing-classes-wordpress-plugin-api/
- [Designing a class around WordPress hooks
			

			

				Have you met this “Carl” guy? He’s always blabbing about “object-oriented this” and “object-oriented that”. You decide to dip your toes into the subject (maybe he’s on to something…).
You try to apply a subset of what he teaches by creating a class. You start to code it. Life is good. And then it happens. You need to use a WordPress hook.
What do you with them?

Three possible solutions](designing-class-wordpress-hooks.md) — https://carlalexander.ca/designing-class-wordpress-hooks/
- [Designing a class to assemble plugin classes
			

			

				Learning object-oriented programming with WordPress is a lot like embarking on an epic journey. You’ll experience some lows, some highs and some downright frustrating moments. But it’s all part of the learning process.
And, so far, we’ve done quite a bit of progress on our journey. We’ve looked at various WordPress problems. And we then solved them using a class or combination of classes.
We call this process “object-oriented design“. It’s been the focus of a lot of the articles on this site. Because of that, there’s a good chance that you’ve begun using it in your own projects. (And if you haven’t, you should try it!)
When that happens, you’ll start to notice that your project has a lot of classes. This tends to become a problem for a lot of developers. They wonder, “How do I assemble all these classes together!?” It’s not unusual for them to revert back to the standard WordPress way of doing things when that happens.
This is the problem that we’re going to explore in this article. We’ll look at how you can solve it using a dedicated class for it. To do this, we’ll start thinking about the job of the main plugin class.

Defining the plugin class](designing-class-assemble-plugin.md) — https://carlalexander.ca/designing-class-assemble-plugin/
- [Designing a class: WordPress AJAX handler
			

			

				Learning object-oriented programming has its fair share of challenges. One of them is the large variety of problems and their solutions. That’s why a lot of solutions revolve around using design patterns.
Sometimes a problem has a clear solution like the WordPress API client. Other times it’s more abstract like how to interact with the plugin API. These abstract problems are a lot harder to define and solve.

That’s why we’ll look at how to design a class to solve one of those abstract problems. I decided to look at AJAX communication. You can use AJAX to do anything. This means that we can only create a generic outline of what an AJAX handler class would look like.
Let’s do a quick overview of AJAX](designing-class-wordpress-ajax-handler.md) — https://carlalexander.ca/designing-class-wordpress-ajax-handler/
- [Designing a class: WordPress API client
			

			

				As a WordPress developer, learning object-oriented programming seems daunting at first. It’s one thing to learn all the concepts, but theory will only get you so far.
You want to see how you can do it in practice. How do you start from nothing and end up with a working class. That’s why I’m going to share how I built a client for the WordPress REST API. You’ll get to see how I use object-oriented design in practice.

Some background](designing-class-wordpress-api-client.md) — https://carlalexander.ca/designing-class-wordpress-api-client/
- [Designing a class to generate HTML content in WordPress
			

			

				As WordPress developers, we often have to generate HTML content for our plugins. (And, if you’re building a theme, that’s pretty much mandatory!) But generating HTML inside a function or method is messy. You have to close your PHP tag, write your HTML, reopen your PHP tag and so on.
This combination of HTML and code isn’t ideal. You’ve coupled your templating to your code in a way that often doesn’t scale well. That’s why it’s common to see such functions or methods grow out of proportion.
The common cause of that is adding conditional logic into the HTML code. This increases the complexity of the code and reduces its readability. So we’d like to avoid that if possible.
It’s worth pointing out that mixing HTML and PHP isn’t bad per se. After all, PHP is also a templating language. We just want to create a proper delimitation between what is regular PHP code and what is PHP template code.
So let’s find a solution to this problem! The twist (well it’s not really a twist for this site…) is that we’re going to use object-oriented programming to do it. We’ll design a class that generates HTML using PHP template.

A shortcode example](designing-class-generate-wordpress-html-content.md) — https://carlalexander.ca/designing-class-generate-wordpress-html-content/
- [Designing classes for the WordPress options API
			

			

				Much like the plugin API, it’s almost impossible to build a plugin without using the options API. This can be a problem if you’re trying to learn object-oriented programming with WordPress. You need a way to build a class around it.
Lucky for us, this is a lot less complicated to do than with the plugin API. The options API is really nothing more than an API around a data store. Our job as designers is simple. We need to design a class that mirrors this API.
That said, we don’t have to limit ourselves to just copying the options API as is. We can also push things further by adding some extra functionality around it. This is what makes designing a class around the options API so interesting.

Review options API](designing-classes-wordpress-options-api.md) — https://carlalexander.ca/designing-classes-wordpress-options-api/
- [Designing a class to create complex WordPress queries
			

			

				Alright, it’s time to continue our journey building our awesome WP_Query_Builder class! So far, we’ve only designed it to build simple WordPress queries. But not all WordPress queries are simple or easy to model using just a cascading method.
It’s even possible that you’ve run into the limits of the WP_Query_Builder already. The class that we created then wasn’t a complete solution. It had some serious limitations if you were a WP_Query expert. You couldn’t use it to perform complex WordPress queries.
What do we mean by complex WordPress queries? We mean queries that use a complex WP_Query query parameters. At the moment, there are three of them: date_query, meta_query and tax_query.
So, for this article, we’re going to back to our WP_Query_Builder class. We’ll add support for one of these complex WP_Query query parameters. We won’t go over all three due to how complex they are. But you can apply what you’ve seen for this one query parameter to design a fluent interface for the other two.

The story so far…](designing-class-complex-wordpress-queries.md) — https://carlalexander.ca/designing-class-complex-wordpress-queries/
- [Designing a class to build simple WordPress queries
			

			

				In a previous article, we looked at how you could create a class to manage WordPress posts. We ended creating a class who’s job it was to interact with the WordPress database. And it did that quite well!
As part of its job, our class also had to be able to query the WordPress database. To do that, we made it easier to reuse code around the WP_Query class. We achieved that by creating methods that used predefined query arguments.
But have you ever looked at the codex page for WP_Query? Holy Moley, there are a lot of query parameters in there! It’s pretty intimidating and not always easy to use in practice.
That’s the problem that we’re going to look at in this article. We’ll design a class to simplify how we build WP_Query objects. It’ll handle all the complexity around WP_Query query parameters for you. The result should be an easier way for you for you to create WordPress queries.

How do you make WordPress queries easier?](designing-class-build-simple-wordpress-queries.md) — https://carlalexander.ca/designing-class-build-simple-wordpress-queries/
- [Introduction to WordPress unit testing
			

			

				I gave a talk at WordCamp Toronto 2015 on WordPress unit testing. This is the companion article that I wrote for it. If you’re just looking for the slides, click here.
“But this worked the other day!”
I don’t know about you, but reading that sentence just frustrates me! Don’t you hate when things worked one day and it doesn’t the next. It’s the stuff of (developer) nightmares.
What if there was a way to ward yourself against that evil? Well, you’re in luck because that’s the goal of software testing! It prevents this situation from happening over and over again. On top of that, it helps you improve the quality of the code you write. Awesome!
Now, software testing is a HUGE field. You have a ton of different types of testing. Each with its own purpose (and, sometimes, philosophy). Today, we’re going to focus on just one type of testing. It’s called unit testing.

So what is unit testing?](introduction-wordpress-unit-testing.md) — https://carlalexander.ca/introduction-wordpress-unit-testing/
- [How do you start unit testing existing WordPress code?
			

			

				A lot of us have heard about unit testing. Out of all the different types of testing (and there are a few!), it’s probably the better-known one. It’s also the most common form of testing used with WordPress.
In the past, we’ve looked at how unit testing works with WordPress. That said, knowing how unit testing works is one thing. This knowledge doesn’t necessarily make it any easier to get started with it in your projects.
Some of us work with existing code bases. It could be a plugin, a theme or a whole WordPress site. How do you take the fundamentals of unit testing and apply them in that context?
This is a tricky question to answer, but it’s also an important one. Most of us will not start using unit testing in a vacuum. We’re going to start using it with one of those existing code bases.
This brings with it its own unique sets of challenges. It also means that you need to have a strategy for them. This will help make this transition smoother for you.

Your code probably isn’t ready for unit tests](how-to-start-unit-testing-wordpress-code.md) — https://carlalexander.ca/how-to-start-unit-testing-wordpress-code/
- [Introduction to WordPress acceptance testing
			

			

				As a WordPress developer, the topic of testing isn’t something that we hear about that often. And, if we do hear about it, it’s more often than not just one specific type of testing: unit testing. (That’s even the one that I’ve thought first!) In fact, it’s not uncommon to associate testing with unit testing because of this.
But software testing is an enormous field. There are a lot of different types of testing. While they might not all be as useful as unit testing, they still all serve a specific purpose.
That said, there are other types of testing that are as useful (or almost as useful!) as unit testing. Acceptance testing is one of them. It’s especially useful if you’re a plugin or theme developer.

Defining acceptance testing](introduction-wordpress-acceptance-testing.md) — https://carlalexander.ca/introduction-wordpress-acceptance-testing/
- [WordPress for the adventurous: Loading
			

			

				I’m sure you woke up thinking “I wish I knew more about WordPress loading.”. Ok… maybe not (it’s just me isn’t it?). It’s just not something you deal with every day.
No, plugins and themes make up your days. That’s what you use to build your custom WordPress solutions. There’s no need to know about the internal process that starts up WordPress.
Yet you can’t ignore it once you start building complex WordPress solutions. Or if you plan on distributing a plugin or theme. That changes the dynamic of things.
Your little world with the plugins and themes you know is gone. You’re in the larger (and messier) WordPress world now. That means you have to play nice with everyone else (damn).

That’s why loading is important](wordpress-adventurous-loading.md) — https://carlalexander.ca/wordpress-adventurous-loading/
- [WordPress for the adventurous: Entry points
			

			

				To master WordPress, you have to be able to look at it from unusual perspectives. It’s exploring these perspectives that gives you that next level understanding. You’re able to view problems from another angle. This can give you unique insights that affect how you approach problems and design solutions for WordPress.
The angle we’re going to explore in this article is the concept of the entry point. Let’s take a look at how WordPress handles it.

What is an entry point?](wordpress-adventurous-entry-points.md) — https://carlalexander.ca/wordpress-adventurous-entry-points/
- [WordPress for the adventurous: Plugin API
			

			

				Let’s say that you ran a poll through the WordPress developer community. It asked the following question: “What defines WordPress?”. The odds are that the plugin API would come up near the top.
From a developer’s perspective (and for the sake of my introduction), there’s nothing that defines WordPress like it. It’s the workhorse of the WordPress ecosystem. You use to build anything that you want with WordPress.
There are plenty of articles out there that show you how to use it, but little on how it works. That makes it a bit misunderstood and lonely (APIs have feelings you know).
It’s time we showed some love for this hard worker.

Actions vs Filters](wordpress-adventurous-plugin-api.md) — https://carlalexander.ca/wordpress-adventurous-plugin-api/
- [WordPress for the adventurous: Rewrite API
			

			

				The story behind rewrite API plays out almost like a Disney movie. You have WordPress and the human (played by you!). Two different worlds. Two different languages.
WordPress is a machine and only understands if you talk to it as such. You need to use a cold language of numbers and code so that it can understand you. Do you need to see a WordPress post? You need to ask him using query variables like p=123.
On the other hand, humans are friendly and talkative. They expect to talk to someone using words. They want to see URLs with the post-title and not query variables.
The rewrite API is the translator that brought these two unlikely friends together. Rewrite rules convert your post-title into the p=123 query variable WordPress wants. Both sides get their happy ending (yay!).

How does the rewrite API do this?](wordpress-adventurous-rewrite-api.md) — https://carlalexander.ca/wordpress-adventurous-rewrite-api/
- [WordPress for the adventurous: WP_Query class
			

			

				It’s not too far-fetched to see WordPress as a library. You write a post and publish it. Meanwhile, WordPress classifies it and puts it away on its shelves.
But how do you find your post again after WordPress shelved it away? You need someone to help you navigate this huge library and find what you’re looking for. You need a librarian!
That’s the job of the WP_Query class in a nutshell. It’s the librarian of the WordPress database. You talk to it when you want to search through the WordPress database. It’ll help you find the information that you need!
It does this without requiring that you know how WordPress stores that information. That means that you don’t have to know how to write MySQL queries. WP_Query takes care of all that for you. (Yay!) It’ll transform your search request into a safe MySQL query and process it for you.
But how does the WP_Query class do this? That’s what we’re going to look at today. We’re going to explore how it works and what it can do for you. This will help you leverage it to the maximum in the future.

What problem does WP_Query solve?](wordpress-adventurous-wp-query-class.md) — https://carlalexander.ca/wordpress-adventurous-wp-query-class/
- [WordPress for the adventurous: Options API
			

			

				As WordPress developers, we often need a way to store and retrieve data. The most common reason for that is that we need to store and retrieve settings for our plugin or theme. But the reality is that there are countless of other reasons why you’d need to store and retrieve data.
So how do we do it? Well, the primary tool that we have at our disposal to do this is the options API. It’s an API that offers a way for us to store and retrieve data from the WordPress database.
It’s pretty much as indispensable as the plugin API. We often can’t build anything in WordPress without it. That’s why it’s worth looking a bit deeper at how it works.

The wp_options table](wordpress-adventurous-options-api.md) — https://carlalexander.ca/wordpress-adventurous-options-api/
- [Diving into WordPress errors](diving-into-wordpress-errors.md) — https://carlalexander.ca/diving-into-wordpress-errors/
- [WordPress core as a gateway to better coding](wordpress-core-as-a-gateway-to-better-coding.md) — https://carlalexander.ca/wordpress-core-as-a-gateway-to-better-coding/
- [How to use the static keyword with WordPress
			

			

				This site has a lot of object-oriented programming articles. Most of them focus on solving WordPress problems using object-oriented programming. This is great when you’re comfortable with object-oriented programming.
But most WordPress developers aren’t that comfortable with it. (You’d think there’d be a book on that or something.) It’s one thing to read about basic concepts like encapsulation and inheritance. It’s another to put them in practice. There are a lot of obstacles that you have to overcome.
One of these obstacles is the proper use of the static keyword. Static methods are a great object-oriented tool to use. But, like all good things, we can also abuse it if we’re not careful.
This happens a lot more in the WordPress development world than anywhere else. And there are good reasons for that. We’ll look at why that is and what you can do about it.

What is the static keyword?](static-keyword-wordpress.md) — https://carlalexander.ca/static-keyword-wordpress/
- [How to use placeholders for WordPress translations
			

			

				Have you ever worked on localization with other web frameworks? If so, you might be familiar with the idea of using keys to identify translation strings. These keys are how your translation system finds the localized text to use inside your application.
If you’ve been doing localization with WordPress, you know that it doesn’t work that way. With WordPress, you use the original (usually English) content string as your translation key. This can be convenient because you always know what the original string was.
That said, it’s still possible to do WordPress localization using keys instead content strings. This can be useful if you come from these different programming backgrounds. You might like to keep working the way you’re used to. Let’s look at how you can do that!

Why would use keys for translations?](placeholders-wordpress-translations.md) — https://carlalexander.ca/placeholders-wordpress-translations/
- [Polymorphism and WordPress: Interfaces
			

			

				Let’s talk about interfaces. As a WordPress developer, how can they be useful to you and your projects? It’s going to be a tough sell because WordPress core doesn’t use them and we’ll see why this is an issue a bit later. That said, you’ll still find this article useful if you’re looking to:

Learn more about PHP and not just WordPress
Build strong and extensible PHP code
Reduce bugs in your open source plugins
Use open source PHP frameworks

Like the article on abstract classes, you’ll get a detailed example to help you with the topic. It’ll explain how interfaces work and how you can use them. You’ll also get a good idea of the design decisions that warrant the use of an interface.

Reviewing interfaces](polymorphism-wordpress-interfaces.md) — https://carlalexander.ca/polymorphism-wordpress-interfaces/
- [Polymorphism and WordPress: Abstract classes
			

			

				When we covered inheritance, there were some questions about interfaces and abstract classes.

What can you use them for?
What are the advantages?
When should you use them?

These are all great questions that are worth exploring. As the title suggests, “Polymorphism” is the object-oriented feature that helps answer these questions. It’s not an easy feature to grasp.
That’s why most of the article will be about an in-depth example. You’ll see the thought process involved with using it. This will help you understand it better so you can apply it to your own projects.

Many forms. Such polymorphism. Wow.](polymorphism-wordpress-abstract-classes.md) — https://carlalexander.ca/polymorphism-wordpress-abstract-classes/
- [Using inheritance with WordPress
			

			

				As a WordPress developer, you’re always looking for ways to better reuse your code between projects. Your time is valuable and you don’t want to reinvent the wheel each time you start a new project.
Object-oriented programming can help you with that. In a previous post, I covered why you should learn it. Now it’s time to take things further by going over the main feature for code reuse. You’ve probably heard about it before. It’s called “inheritance“.

Inheritance, what’s that?](using-inheritance-wordpress.md) — https://carlalexander.ca/using-inheritance-wordpress/
- [Organizing your files in an object-oriented WordPress plugin
			

			

				So you’ve made the plunge to the world of PHP object-oriented programming. You want to use that knowledge to build a plugin or convert your plugin to using objects. That’s great!
We’re going to talk about one of the first hurdles you might face when trying to work with PHP objects. That’s organizing your files. It’s an important topic with no general consensus in the WordPress community.
So why is file organization important? Well, let’s look at the code samples on this site to give you an idea. In general, each code sample tends to have a couple of classes and/or interfaces. They’re also small and only cover one specific WordPress problem.
But once you start building a real plugin, you’ll have to solve a lot of problems. That means that you’ll end up with a lot more classes. It can leave you feeling frustrated and looking for answers to questions like:

What do you do with them?
How do you structure my files and folders to accommodate them?
How do you load all the files containing them?

These are all questions that you’ll get an answer to in this article. So let’s get to it!

The importance of having standards](organizing-files-object-oriented-wordpress-plugin.md) — https://carlalexander.ca/organizing-files-object-oriented-wordpress-plugin/
- [How to troubleshoot WordPress performance
			

			

				I spoke at WordCamp Halifax 2017 on how to troubleshoot the performance of a WordPress site. This is the companion article that I wrote for it. If you’re just looking for the slides, click here.
Have you ever had a client come up to you and ask why a WordPress page was slow to load? We’ve all had that happen at some point or another. Especially nowadays with the increased importance of page load times! (Everything has to be fast fast fast!)
But what do you do when someone asks you to fix such an issue? It can feel like you’re looking for a needle in a haystack. The issue could be anywhere. (It really can!)
So what can you do about it? Well, there are a lot of tools at your disposal. They can help you figure out what’s going on with the performance of your WordPress site.
That said, it’s one thing to know that these tools exist. It’s another one to be able to use them and interpret what they’re telling you. The problem is that it’s what you need to get to the root of a WordPress performance issue.

What’s a WordPress performance issue?](troubleshoot-wordpress-performance.md) — https://carlalexander.ca/troubleshoot-wordpress-performance/
- [PHP reflection API fundamentals
			

			

				Do you ever take the time to read the code of your favourite PHP framework or library? If you have, there’s a good chance that you might have seen them use PHP’s reflection API. And, if you don’t read other people’s code, you should start doing it! (It’s a great learning tool.)
Now, let’s get back to the reflection API. This is an API that gets used quite a lot by framework and library developers. But the funny thing is that it’s almost never talked about when you’re looking at resources to learn PHP. (Or even advanced PHP resources for that matter.)
This is unfortunate. That’s because PHP’s reflection API serves a unique and important purpose. That’s why developers that build our frameworks and libraries use it so much.

What’s a reflection?](php-reflection-api-fundamentals.md) — https://carlalexander.ca/php-reflection-api-fundamentals/
- [Thoughts on WordPress and the MVC pattern
			

			

				Getting proficient with object-oriented programming can feel like falling down a rabbit hole. You break down problems into more and more classes. You feel like it’s neverending and that you could go on forever. You need guidance to make sense of it all.
This is where architectural patterns come in. They’re similar to software design patterns which you use to solve a specific problem. In contrast, you use an architectural pattern to address a set of them at once.
This confers certain benefits to architectural patterns. You get a higher level view of how your classes interact with each other. You then have an easier time piecing everything together.
This is why it’s not uncommon for developers to skip over software design patterns. Instead, they start looking into architectural patterns right away. This is even something I’m guilty of doing (insert audience gasp).
One of the most important architectural patterns is the “model-view-controller” (known as MVC). It’s used by most modern frameworks from Rails to Angular. But does it have a place in WordPress?

So what is the MVC pattern?](thoughts-wordpress-and-mvc-pattern.md) — https://carlalexander.ca/thoughts-wordpress-and-mvc-pattern/
- [Keeping Your WordPress Safe
			

			

				The Montréal WordPress community held an event this month on WordPress security. The event had a talk followed by a “show and tell” segment. This is the companion article for that talk.
This is an important topic for everyone. Not just for WordPress experts. So it’s great to have a chance to teach the community about it.
The goal of the talk was to give everyone an overview of WordPress security. That includes basic concepts and some recommendations. The recommendations themselves target WordPress users of all skill levels. If you’re an advanced WordPress user, you might not learn as much.

Slides](keeping-your-wordpress-safe.md) — https://carlalexander.ca/keeping-your-wordpress-safe/
- [Give your WordPress client an Apple experience
			

			

				Hosting your WordPress site is an annoying problem. You can’t go far to see a discussion about it. Every week, someone asks who’s the best host. And each week, you never know if you’ll see conflicting answers or a consensus.
It’s not like you can live without hosting either. That puts you at the mercy of hosting providers. This isn’t to say that hosting providers are evil. I think a lot of them are good and mean well.
It’s just that, regardless of their intentions, it doesn’t change things for you. Hosting is a critical part of your client’s experience with your service. They’ll call you if their site is slow, down or even hacked. They’ll question the quality of your work because of it.
But it’s more often than not a result of their decision. Clients skimp on hosting all the time. It’s one of the aspects of a project that your client tends to neglect the most. You know this. You’ve lived it many times.
Your client thinks: “Why should I pay $50/month (or $100/month with SSL!!) for premium hosting? I can get something for half or a quarter of the price.” Of course, it sounds great to them.
Except you’re left holding the bag when things go wrong.

You need your Apple experience](give-wordpress-an-apple-experience.md) — https://carlalexander.ca/give-wordpress-an-apple-experience/
- [How does a PHP application work?
			

			

				Most of us are familiar with how a web application works. We know that when we enter an URL in our browser, it’ll contact a web server who’ll return some HTML. The browser will then make follow-up requests and then render the web page. (This is a simplification! But that’s the main idea.)
But what’s happening on the web server returning HTML? How is the web server getting the HTML that it returns to our browser? And, to be even more specific, how does this happen in PHP?
This isn’t something that most of us know how to answer. We know (or at least should know!) how to build a PHP website. But what happens between our PHP code and the browser is a bit of a mystery.
There’s a good chance that you’re thinking, “Well, my site loads. Why should I think twice about this?” And that’s true! But the truth is that knowing how a PHP application works can be useful.
It can affect how you design your PHP application. But it’s also important if you’re looking to improve its performance. For example, it’s hard to understand PHP application caching if you don’t understand how a PHP application works.

The life of a PHP request](php-application.md) — https://carlalexander.ca/php-application/
- [Mastering the use of PHP conditionals
			

			

				No set of control structures is more pervasive in programming than if, elseif and else. With a few exceptions, you’ll use at least one per function or method that you write. There’s just no way around it.
But conditionals (that’s what we call these control structures) fit in the “easy to learn, hard to master” category. In fact, they’re so easy to use that you can develop some bad habits around them. (This is also a problem with loops.) This can lead to code that’s complex and hard to read or even test.
That said, it’s possible to develop good programming habits with conditionals. This is what this article will try to help you with. We’ll go over some programming techniques that can help make conditionals more manageable.

How does PHP evaluate multiple conditionals?](mastering-php-conditionals.md) — https://carlalexander.ca/mastering-php-conditionals/
- [The first thing you should learn from object-oriented programming
			

			

				You’ve decided to learn object-oriented programming, but you don’t know where to start. Object-oriented programming has so many concepts and features. The whole thing can feel overwhelming at times. Let’s help you get started on the right foot.
What’s a great place to start? With the feature that you’ll associate the most with object-oriented programming. It’s called encapsulation. Most modern programming languages support encapsulation using classes.

Why should you learn about it first?](first-thing-learn-object-oriented-programming.md) — https://carlalexander.ca/first-thing-learn-object-oriented-programming/
- [Why it is only PHP](why-it-is-only-php.md) — https://carlalexander.ca/why-it-is-only-php/
- [The one tool I wish I had in PHP](the-one-tool-i-wish-i-had-in-php.md) — https://carlalexander.ca/the-one-tool-i-wish-i-had-in-php/
- [Making you proud](making-you-proud.md) — https://carlalexander.ca/making-you-proud/
- [PHP App Challenge](php-app-challenge.md) — https://carlalexander.ca/php-app-challenge/
- [A plugin for a rainy day](plugin-rainy-day.md) — https://carlalexander.ca/plugin-rainy-day/
- [Helping WordPress make friends with the decorator pattern
			

			

				In some plugin circles (also know as the “cool kids club”), the coolest kid on the block is the wpdb class. Plugins go out of their way to be his friend. Lucky guy (or class)!
One plugin that has to be friends with wpdb is HyperDB. If plugins could talk, it would sound a lot like a scene from kindergarden.

HyperDB: Hey WPDB, wanna be friends? I’ll make you the strongest database class there is!

WPDB: Woah, that sounds awesome. I’m in!

HyperDB: There’s only one catch. You can’t be friends with anyone else.

WPDB: Oh ok. *sad face*
HyperDB uses the proxy pattern to give wpdb his new powers. The HyperDB class achieves that by extending the wpdb class. This is also a limitation of the proxy pattern.
A class can only extend one class. This means that it can only have one proxy (in practice). Creating a proxy prevents others from creating one. This leaves other plugins like Query Monitor in the wind.
Query Monitor: Hey WPDB, how would you like to know when you’re sick?

WPDB: I’d love to! I hate being sick.

Query Monitor: Great! All you need to do is become my friend and I’ll help you with that.

WPDB: Sorry Query Monitor, I’m already friends with HyperDB…
This situation is unfortunate for wpdb. HyperDB could use the diagnostic powers that Query Monitor provides. The proxy pattern won’t have it though. It limits these relationships to one or the other.
How can wpdb have as many friends as he wants?
The smart proxy](wordpress-decorator-pattern.md) — https://carlalexander.ca/wordpress-decorator-pattern/
- [How I marketed and published a niche WordPress book
			

			

				A few weeks ago, I released my first book “Discover object-oriented programming using WordPress“. The book had $11,040 in sales during its launch week. This went above and beyond the expectations that I had for how well the book would do. (I would’ve been ecstatic if it’d made even half of that.)
But before I go any further, I want to do a small preface. What I am going to talk about isn’t anything that I really figured out myself. All that I did was read a lot of what others had done and then tried to do it myself in my own authentic way. (That last part is super important though!)
I’m especially thankful to Nathan Barry and his book “Authority“. (Sadly, he doesn’t sell just the book anymore.) I’m also super grateful to Paul Jarvis who’s inspired me to have my own quirky voice through his newsletter. He and Justin Jackson (not the basketball player!) taught me that marketing didn’t have to be this slimy thing if you were authentic about it. (Justin has a course on marketing for developers.)
That’s also why I’m taking the time to write down all my thoughts about this experience while everything is still fresh. (Much like my year in reviews.) I was only successful because other people shared how they approached marketing and self-publishing a book. I want to do the same by sharing as much information as I can for anyone interested in marketing and publishing their own book.

Having a newsletter](marketing-and-publishing-niche-wordpress-book.md) — https://carlalexander.ca/marketing-and-publishing-niche-wordpress-book/
- [PHP strings and how to format them
			

			

				Strings have always been an integral part of the programming world. We use them so much because they do something that’s almost impossible to do with other data types. They allow our code to communicate with others.
The definition of “others” is quite wide in this context. Others can be as straightforward as someone using your WordPress plugin. But it can also be more abstract like a browser reading HTML code generated by PHP. They are both a third party who interacts with strings generated by your code.
Sometimes, these strings are simple and used as is. But more often than not, these strings need to be dynamic. They need to adapt to what’s going on inside your code.
This latter one is why it’s important to have a good understanding of what you can do with strings in PHP. That’s because there are countless ways that you might want to alter a string. For example, you could have a string change based on certain conditions. Or you could insert one or more variables into it.
For this article, we’re going to focus on how you can format a string. There are a lot of built-in helper functions for strings in PHP. We’ll look at the ones that can help you achieve that goal.

The string data type](php-string-formatting.md) — https://carlalexander.ca/php-string-formatting/
