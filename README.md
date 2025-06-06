# C4 Architecture Documentation – Online Shop System

### Online Shop System - Context Diagram

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

### Online Shop System - Container Diagram

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

### Online Shop System - Component Diagrams

```mermaid
graph TD
   subgraph "User Service"
       UserCtrl["UserController"]
       UserSvc["UserService"]
       UserRepo["UserRepository"]
       JWT["JWTProvider"]
       UserEntity["User Entity"]
   end
   
   subgraph "Product Service"
       ProductCtrl["ProductController"]
       ProductSvc["ProductService"]
       ProductRepo["ProductRepository"]
       ProductKafka["KafkaProducer"]
       ProductEntity["Product/Category/Review Entity"]
   end
   
   subgraph "Order Service"
       OrderCtrl["OrderController"]
       OrderSvc["OrderService"]
       OrderRepo["OrderRepository"]
       OrderKafka["KafkaProducer"]
       OrderEntity["Order/Cart Entity"]
   end
   
   subgraph "Admin Service"
       AdminCtrl["AdminController"]
       AdminSvc["AdminService"]
       AdminRepo["AdminRepository"]
       AdminKafka["KafkaConsumer"]
       ReportGen["ReportGenerator"]
   end
   
   UserCtrl --> UserSvc
   UserSvc --> UserRepo
   UserSvc --> JWT
   UserRepo --> UserEntity
   
   ProductCtrl --> ProductSvc
   ProductSvc --> ProductRepo
   ProductSvc --> ProductKafka
   ProductRepo --> ProductEntity
   
   OrderCtrl --> OrderSvc
   OrderSvc --> OrderRepo
   OrderSvc --> OrderKafka
   OrderRepo --> OrderEntity
   
   AdminCtrl --> AdminSvc
   AdminSvc --> AdminRepo
   AdminSvc --> AdminKafka
   AdminSvc --> ReportGen
```

### Online Shop System - Deployment Diagram

This diagram shows how the system is deployed using Docker Compose.

```mermaid
graph TD
    subgraph "Docker-Compose"
        subgraph "Application Level"
            WebApp["Svelte Frontend<br/>[Docker Container]"]
            APIGateway["API Gateway<br/>[Docker Container]"]
            UserService["User Service<br/>[Docker Container]"]
            ProductService["Product Service<br/>[Docker Container]"]
            OrderService["Order Service<br/>[Docker Container]"]
            AdminService["Admin Service<br/>[Docker Container]"]
        end
        
        subgraph "Infrastructure Level"
            PostgreSQL["PostgreSQL<br/>[Docker Container]"]
            Redis["Redis<br/>[Docker Container]"]
            Kafka["Kafka + Zookeeper<br/>[Docker Containers]"]
            FileStorage["MinIO/Volume<br/>[Docker Container/Volume]"]
        end
    end
    
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
```

# Behaviors – Online Shop System

## Admin Service

#### AsyncAPI

- [AsyncAPI](https://studio.asyncapi.com/?share=644f05d1-56ba-4882-9b07-e10ee7b22e7d)
- [AsyncApi/AdminService.yaml](https://github.com/danieldan0/microservice-store/blob/main/AsyncApi/AdminService.yaml)

#### OpenAPI

- [OpenApi/AdminService.yaml](https://github.com/danieldan0/microservice-store/blob/main/OpenApi/AdminService.yaml)

![image](https://github.com/user-attachments/assets/45014a91-c2b6-4105-ad42-c06c0233ad72)

## Order Service

#### AsyncAPI

- [AsyncAPI](https://studio.asyncapi.com/?share=78d68da1-58e4-4386-ad0d-d6817340d4cd)
- [AsyncApi/OrderService.yaml](https://github.com/danieldan0/microservice-store/blob/main/AsyncApi/OrderService.yaml)

#### OpenAPI

- [OpenApi/OrderService.yaml](https://github.com/danieldan0/microservice-store/blob/main/OpenApi/OrderService.yaml)

![image](https://github.com/user-attachments/assets/f860b98c-3617-4257-b76e-91a86a61db70)

## Product Service

#### AsyncAPI

- [AsyncAPI](https://studio.asyncapi.com/?share=11d92e5c-03c6-430e-a0a9-2ce09cb26d55)
- [AsyncApi/ProductService.yaml](https://github.com/danieldan0/microservice-store/blob/main/AsyncApi/ProductService.yaml)

#### OpenAPI

- [OpenApi/ProductService.yaml](https://github.com/danieldan0/microservice-store/blob/main/OpenApi/ProductService.yaml)

![image](https://github.com/user-attachments/assets/78996bb1-43bb-4e25-9261-388f9783ef08)

## User Service

#### AsyncAPI

- [AsyncAPI](https://studio.asyncapi.com/?share=695c581f-8238-4d0a-869f-310e46a6a9d6)
- [AsyncApi/UserService.yaml](https://github.com/danieldan0/microservice-store/blob/main/AsyncApi/UserService.yaml)

#### OpenAPI

- [OpenApi/UserService.yaml](https://github.com/danieldan0/microservice-store/blob/main/OpenApi/UserService.yaml)

![image](https://github.com/user-attachments/assets/1388b587-a4c0-4663-97a1-23cae67b98d0)

# Component ERDs - Online Shop System

### Order Service

![image](https://github.com/user-attachments/assets/fac2cd9c-76be-49fb-b520-aa4ecebd7df6)

### Product Service

![image](https://github.com/user-attachments/assets/f486c5e2-83e6-445a-bef3-f097c008b5a3)

### User Service

![image](https://github.com/user-attachments/assets/1c04a38b-b223-4e6b-a874-5bf4a88a8510)

# ERD

![ERD](https://github.com/user-attachments/assets/2254a2f0-9c5d-4e9c-8959-a381ca4a2f42)

