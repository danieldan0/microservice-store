# Online Shop System - C4 Context Diagram

This diagram shows the high-level view of the Online Shop System and its interactions with external users and systems.

```mermaid
graph TB
    %% Define nodes
    Guest["Guest<br/>[Person]<br/>Browses products without account"]
    Customer["Customer<br/>[Person]<br/>Shops and manages orders"]
    Vendor["Vendor<br/>[Person]<br/>Manages products and inventory"]
    Admin["Admin<br/>[Person]<br/>Manages marketplace and users"]
    
    OnlineShop["Online Shop System<br/>[Software System]<br/>E-commerce marketplace for<br/>browsing, ordering, and<br/>managing products"]
    
    PaymentGateway["Payment Gateway<br/>[External System]<br/>Processes payments"]
    
    %% Define relationships
    Guest -->|Browses products| OnlineShop
    Customer -->|Shops and orders| OnlineShop
    Vendor -->|Manages products| OnlineShop
    Admin -->|Manages system| OnlineShop
    
    OnlineShop -->|Processes payments via| PaymentGateway
```

# Online Shop System - Container Diagram

This diagram shows the high-level containers (applications and data stores) that make up the Online Shop System.

```mermaid
graph TB
    subgraph "Online Shop System"
        %% Frontend
        WebApp["Web Application<br/>[Container: Svelte]<br/>Provides UI for all users"]
        
        %% API Gateway
        APIGateway["API Gateway<br/>[Container: Python/Flask]<br/>Routes requests, handles auth"]
        
        %% Microservices
        UserService["User Service<br/>[Container: Python/Flask]<br/>Manages authentication and users"]
        ProductService["Product Service<br/>[Container: Python/Flask]<br/>Manages products and reviews"]
        OrderService["Order Service<br/>[Container: Python/Flask]<br/>Handles orders and cart"]
        AdminService["Admin Service<br/>[Container: Python/Flask]<br/>System administration"]
        
        %% Data Stores
        PostgreSQL["PostgreSQL Database<br/>[Container: PostgreSQL]<br/>Stores all application data"]
        Redis["Redis Cache<br/>[Container: Redis]<br/>Session and cache storage"]
        Kafka["Message Broker<br/>[Container: Kafka]<br/>Event streaming"]
        FileStorage["File Storage<br/>[Container: MinIO/Local]<br/>Product images"]
    end
    
    %% External Systems
    PaymentGateway["Payment Gateway<br/>[External System]"]
    
    %% Users
    User["User<br/>[Person]<br/>All user types"]
    
    %% Relationships
    User --> WebApp
    WebApp --> APIGateway
    
    APIGateway --> UserService
    APIGateway --> ProductService
    APIGateway --> OrderService
    APIGateway --> AdminService
    
    UserService --> PostgreSQL
    UserService --> Redis
    ProductService --> PostgreSQL
    ProductService --> FileStorage
    OrderService --> PostgreSQL
    AdminService --> PostgreSQL
    
    UserService --> Kafka
    ProductService --> Kafka
    OrderService --> Kafka
    AdminService --> Kafka
    
    OrderService --> PaymentGateway
```
