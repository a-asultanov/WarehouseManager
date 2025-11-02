# Warehouse & Procurement Manager

## Описание (RU)

**Warehouse & Procurement Manager** — backend-система на Flask и PostgreSQL для управления поставщиками, товарами, заказами и складскими остатками.

Проект реализует базовую логику закупок: оформление заказов у поставщиков, приёмка товаров и автоматическое обновление остатков на складе.  
Система состоит из REST API, админ-панели на Flask-Admin и Docker-окружения для развёртывания.

### Технологии
- Python 3.11  
- Flask — REST API  
- SQLAlchemy — ORM  
- PostgreSQL — база данных  
- Flask-Admin — веб-интерфейс для управления  
- Docker & Docker Compose

### Запуск через Docker
```bash
git clone https://github.com/a-asultanov/WarehouseManager.git
cd WarehouseManager
docker compose up --build
```

После запуска:
- API: http://localhost:5000/api/status  
- Админ-панель: http://localhost:5000/admin  

### Основные эндпоинты API

| Метод | Эндпоинт          | Назначение                  |
|--------|-------------------|-----------------------------|
| GET    | `/api/suppliers`  | Получить список поставщиков |
| POST   | `/api/suppliers`  | Добавить поставщика         |
| GET    | `/api/products`   | Получить список товаров     |
| POST   | `/api/products`   | Добавить товар              |
| GET    | `/api/orders`     | Получить список заказов     |
| POST   | `/api/orders`     | Создать заказ               |
| GET    | `/api/stocks`     | Получить остатки на складе  |

### Логика работы
1. Создаётся поставщик и товар.  
2. Формируется заказ, где указывается поставщик, товар и количество.  
3. После изменения статуса заказа на `received` остатки автоматически увеличиваются.  

### Админ-панель
В проекте используется Flask-Admin для управления данными через веб-интерфейс.  
Панель находится в разработке и может выглядеть упрощённо. Основной функционал добавления и редактирования заказов доступен.

---

## Description (EN)

**Warehouse & Procurement Manager** is a backend system built with Flask and PostgreSQL for managing suppliers, products, purchase orders, and warehouse stock.

It implements basic procurement logic: creating purchase orders, receiving goods, and automatically updating warehouse inventory.  
The project includes a REST API, a Flask-Admin dashboard, and a Docker environment for deployment.

### Tech Stack
- Python 3.11  
- Flask — REST API  
- SQLAlchemy — ORM  
- PostgreSQL — database  
- Flask-Admin — web interface for management  
- Docker & Docker Compose

### Run with Docker
```bash
git clone https://github.com/a-asultanov/WarehouseManager.git
cd WarehouseManager
docker compose up --build
```

After launch:
- API: http://localhost:5000/api/status  
- Admin panel: http://localhost:5000/admin  

### Main API Endpoints

| Method | Endpoint         | Description              |
|---------|------------------|--------------------------|
| GET     | `/api/suppliers` | Get all suppliers        |
| POST    | `/api/suppliers` | Add supplier             |
| GET     | `/api/products`  | Get all products         |
| POST    | `/api/products`  | Add product              |
| GET     | `/api/orders`    | Get all purchase orders  |
| POST    | `/api/orders`    | Create purchase order    |
| GET     | `/api/stocks`    | Get warehouse stock      |

### Logic
1. A supplier and product are created.  
2. A purchase order is placed specifying supplier, product, and quantity.  
3. When the order status changes to `received`, stock levels are automatically updated.

### Admin Panel
The project uses Flask-Admin for database management via a web interface.  
The admin dashboard is under development and may appear minimal. Core functionality for creating and updating orders is supported.

---
