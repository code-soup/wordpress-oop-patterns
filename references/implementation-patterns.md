## AI Implementation Instructions

This section contains extracted patterns and code examples for AI assistants to implement.

### Pattern: Entity (Domain Model)

**Rule:** Entities contain business logic, not persistence logic. They never know about the database.

**AI Instructions:**
- Create entity classes that represent business concepts (Product, Order, Customer)
- Put business validation in entity methods, not in save/retrieve logic
- Use class constants for post types
- Implement PostTypeInterface for persistence mapping
- Never extend WP_Post class (it's final and designed as data transfer object)

**Code Example:**
```php
class Product {
    const POST_TYPE = 'shop_product';

    private string $name;
    private float $price;
    private bool $available;

    /**
     * Business logic: Change price with validation
     */
    public function change_price( float $new_price ): void {
        if ( $new_price < 0 ) {
            throw new \InvalidArgumentException( 'Price cannot be negative' );
        }

        // Ensure 2 decimal precision
        $this->price = (float) number_format( $new_price, 2, '.', '' );
    }

    /**
     * Map to wp_posts table
     */
    public function get_post_data(): array {
        return [
            'post_type'      => self::POST_TYPE,
            'post_title'     => $this->name,
            'post_name'      => sanitize_title( $this->name ),
            'post_status'    => $this->available ? 'publish' : 'draft',
            'comment_status' => 'closed',
        ];
    }

    /**
     * Map to wp_postmeta table
     */
    public function get_post_meta(): array {
        return [
            '_product_price' => $this->price,
        ];
    }
}
```

---

### Pattern: Repository

**Rule:** Repository acts as in-memory collection of domain objects. It abstracts WP_Query and database operations.

**AI Instructions:**
- Inject WP_Query via constructor (don't create inside methods)
- Provide collection-like methods: find(), save(), remove()
- Hide WP_Query complexity behind semantic method names
- Use private find() and find_one() as base methods
- Reuse WP_Query instance with ->query() method (resets state)
- Always use performance optimizations (no_found_rows, update_post_meta_cache)

**Code Example:**
```php
class Job_Repository {
    private WP_Query $query;

    public function __construct( WP_Query $query ) {
        $this->query = $query;
    }

    public static function create(): self {
        return new self( new WP_Query() );
    }

    /**
     * Save creates or updates based on ID presence
     */
    public function save( array $post_data ): int|WP_Error {
        if ( ! empty( $post_data['ID'] ) ) {
            return wp_update_post( $post_data, true );
        }
        return wp_insert_post( $post_data, true );
    }

    /**
     * Find by ID - uses find_one() base method
     */
    public function find_by_id( int $id ): ?WP_Post {
        return $this->find_one( [ 'p' => $id ] );
    }

    /**
     * Find active jobs
     */
    public function find_active(): array {
        return $this->find( [
            'post_status'    => 'publish',
            'posts_per_page' => -1,
        ] );
    }

    /**
     * Base method for multiple results
     */
    private function find( array $query_args ): array {
        $defaults = [
            'post_type'              => 'link_panther_jobs',
            'no_found_rows'          => true,
            'update_post_meta_cache' => false,
            'update_post_term_cache' => false,
        ];

        return $this->query->query( array_merge( $defaults, $query_args ) );
    }

    /**
     * Base method for single result
     */
    private function find_one( array $query_args ): ?WP_Post {
        $query_args['posts_per_page'] = 1;
        $posts = $this->find( $query_args );

        return $posts[0] ?? null;
    }

    public function remove( WP_Post $post, bool $force = false ): void {
        wp_delete_post( $post->ID, $force );
    }
}
```

---

### Pattern: Dependency Injection

**Rule:** Inject dependencies via constructor. Never use global state or create dependencies inside classes.

**AI Instructions:**
- Pass dependencies as constructor parameters
- Use type hints for all dependencies
- Create factory methods (create(), init()) for simple instantiation
- Use DI container for complex dependency graphs
- Prefer constructor injection over setter injection

**Code Example:**
```php
// BAD: Creates tight coupling
class Scanner {
    public function scan( string $url ) {
        $client = new GuzzleHttp\Client(); // ❌ Bad!
        return $client->get( $url );
    }
}

// GOOD: Dependency injection
class Scanner {
    public function __construct(
        private ClientInterface $http_client,
        private Logger $logger,
        private Config $config
    ) {}

    public function scan( string $url ): Response {
        $this->logger->info( "Scanning: {$url}" );

        return $this->http_client->request( 'GET', $url, [
            'timeout' => $this->config->get_timeout(),
        ] );
    }
}

// Usage
$scanner = new Scanner(
    new GuzzleHttp\Client(),
    Logger::get_instance(),
    new Config()
);
```

---

### Pattern: Hook Encapsulation

**Rule:** Encapsulate WordPress hooks in dedicated class. Separate hook registration from business logic.

**AI Instructions:**
- Create Hooker/EventManager class to centralize add_action/add_filter
- Register all hooks in single register_hooks() method
- Use object methods as callbacks (not static methods or closures)
- Keep callback methods public for WordPress to call them
- Use priority and accepted_args parameters explicitly

**Code Example:**
```php
class Scan_Handler {
    public function __construct(
        private Hooker $hooker,
        private Scanner $scanner
    ) {}

    public function register_hooks(): void {
        $this->hooker->add_action(
            'link_panther_run_scan',
            $this,
            'handle_scan',
            10,
            2
        );

        $this->hooker->add_filter(
            'link_panther_scan_url',
            $this,
            'modify_scan_url'
        );
    }

    /**
     * Action callback - must be public
     */
    public function handle_scan( int $job_id, int $offset ): void {
        // Business logic here
        $this->scanner->scan_job( $job_id, $offset );
    }

    /**
     * Filter callback - must be public
     */
    public function modify_scan_url( string $url ): string {
        return trailingslashit( $url );
    }
}

// Hooker utility class
class Hooker {
    public function add_action( string $hook, object $object, string $method, int $priority = 10, int $args = 1 ): void {
        add_action( $hook, [ $object, $method ], $priority, $args );
    }

    public function add_filter( string $hook, object $object, string $method, int $priority = 10, int $args = 1 ): void {
        add_filter( $hook, [ $object, $method ], $priority, $args );
    }
}
```

---

## License & Attribution

All article content © Carl Alexander (https://carlalexander.ca)
This guide compiled for educational purposes and references only.
Please visit original articles for full content and code examples.
