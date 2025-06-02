# Опис таблиць бази даних

## Table: users

| Поле           | Тип       | Опис                                        |
|----------------|-----------|---------------------------------------------|
| user_id        | int (PK)  | Унікальний ідентифікатор користувача       |
| username       | varchar   | Унікальне ім’я користувача                  |
| email          | varchar   | Електронна пошта користувача                |
| password_hash  | varchar   | Хешований пароль                            |
| full_name      | varchar   | Повне ім’я                                  |
| phone_number   | varchar   | Телефонний номер                            |
| role           | varchar   | Роль користувача: `user`, `admin`          |
| created_at     | datetime  | Дата та час створення акаунту               |

## Table: products

| Поле           | Тип       | Опис                                        |
|----------------|-----------|---------------------------------------------|
| product_id     | int (PK)  | Унікальний ідентифікатор товару             |
| name           | varchar   | Назва товару                                |
| description    | text      | Опис товару                                 |
| price          | decimal   | Ціна товару                                 |
| stock_quantity | int       | Кількість на складі                         |
| category_id    | int       | Категорія (FK)                              |
| brand_id       | int       | Бренд (FK)                                  |
| is_active      | bool      | Чи активний товар                           |
| created_at     | datetime  | Дата створення                              |

## Table: product_images

| Поле       | Тип       | Опис                                 |
|------------|-----------|--------------------------------------|
| image_id   | int (PK)  | Унікальний ідентифікатор зображення |
| product_id | int       | Товар (FK)                           |
| image_url  | varchar   | Посилання на зображення              |
| is_main    | bool      | Основне зображення товару            |

## Table: orders

| Поле               | Тип       | Опис                                         |
|--------------------|-----------|----------------------------------------------|
| order_id           | int (PK)  | Унікальний ідентифікатор замовлення          |
| user_id            | int       | Користувач (FK)                              |
| order_date         | datetime  | Дата замовлення                              |
| status             | varchar   | Статус: `pending`, `paid`, `shipped` тощо    |
| total_price        | decimal   | Загальна сума                                |
| payment_method     | varchar   | Метод оплати: `card`, `cash`                 |
| shipping_method    | varchar   | Метод доставки                               |
| shipping_address_id| int       | Адреса доставки (FK)                         |
| tracking_number    | varchar   | Номер відстеження                            |

## Table: order_items

| Поле           | Тип       | Опис                                     |
|----------------|-----------|------------------------------------------|
| order_item_id  | int (PK)  | Унікальний ідентифікатор позиції         |
| order_id       | int       | Замовлення (FK)                          |
| product_id     | int       | Товар (FK)                               |
| quantity       | int       | Кількість                                |
| price_per_item | decimal   | Ціна за одиницю на момент покупки        |

## Table: payments

| Поле            | Тип       | Опис                                      |
|-----------------|-----------|-------------------------------------------|
| payment_id      | int (PK)  | Унікальний ідентифікатор платежу          |
| order_id        | int       | Замовлення (FK)                           |
| payment_date    | datetime  | Дата платежу                              |
| payment_status  | varchar   | Статус платежу                            |
| payment_method  | varchar   | Метод оплати                              |
| transaction_id  | varchar   | Ідентифікатор транзакції                  |

## Table: shipping

| Поле            | Тип       | Опис                                  |
|-----------------|-----------|---------------------------------------|
| shipping_id     | int (PK)  | Унікальний ідентифікатор доставки    |
| order_id        | int       | Замовлення (FK)                       |
| carrier         | varchar   | Перевізник                            |
| tracking_number | varchar   | Номер відстеження                     |
| shipped_date    | datetime  | Дата відправлення                     |
| delivery_date   | datetime  | Дата доставки                         |
| status          | varchar   | Статус доставки                       |

## Table: categories

| Поле       | Тип       | Опис                                  |
|------------|-----------|---------------------------------------|
| category_id| int (PK)  | Унікальний ідентифікатор категорії    |
| name       | varchar   | Назва категорії                       |
| parent_id  | int       | Батьківська категорія (FK)            |
| description| varchar   | Опис категорії                        |

## Table: brands

| Поле       | Тип       | Опис                                  |
|------------|-----------|---------------------------------------|
| brand_id   | int (PK)  | Унікальний ідентифікатор бренду      |
| name       | varchar   | Назва бренду                          |
| logo_url   | varchar   | URL логотипу                          |
| description| varchar   | Опис бренду                           |

## Table: reviews

| Поле       | Тип       | Опис                                   |
|------------|-----------|----------------------------------------|
| review_id  | int (PK)  | Унікальний ідентифікатор відгуку       |
| product_id | int       | Товар (FK)                              |
| user_id    | int       | Користувач (FK)                         |
| rating     | int       | Оцінка (1-5)                            |
| comment    | text      | Текст коментаря                         |
| review_date| datetime  | Дата відгуку                            |

## Table: addresses

| Поле             | Тип       | Опис                          |
|------------------|-----------|-------------------------------|
| address_id       | int (PK)  | Унікальний ідентифікатор     |
| user_id          | int       | Користувач (FK)              |
| city             | varchar   | Місто                        |
| region           | varchar   | Регіон                       |
| postal_code      | varchar   | Поштовий індекс              |
| street           | varchar   | Вулиця                       |
| house_number     | varchar   | Номер будинку                |
| apartment_number | varchar   | Номер квартири               |

## Table: audit_log

| Поле     | Тип       | Опис                                    |
|----------|-----------|-----------------------------------------|
| log_id   | int (PK)  | Унікальний ідентифікатор запису         |
| user_id  | int       | Користувач (FK)                         |
| action   | varchar   | Опис дії (create/update/delete тощо)    |
| entity   | varchar   | Об’єкт (order, product, user тощо)      |
| timestamp| datetime  | Дата та час дії                         |
