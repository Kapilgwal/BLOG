# Blog API (Django REST Framework)

A simple **Blog API** built with Django REST Framework (DRF), supporting CRUD operations for **Authors**, **Articles**, and **Comments**.  
Includes **pagination** support for listing endpoints.

---

## 🚀 Features

- **Authors API** – Create, read, update, and delete authors.
- **Articles API** – Manage articles with CRUD operations.
- **Comments API** – Add and list comments for articles.
- **Pagination** – Server-side pagination using DRF’s `PageNumberPagination`.
- **Browsable API** – Explore endpoints easily via DRF’s built-in browsable UI.

---

## 📂 API Endpoints

| Resource         | Method | Endpoint                                      | Description                          |
|------------------|--------|-----------------------------------------------|--------------------------------------|
| Authors          | GET    | `/api/authors/`                               | List all authors (paginated)         |
| Authors          | GET    | `/api/authors/{id}/`                          | Retrieve author by ID                |
| Authors          | POST   | `/api/authors/`                               | Create a new author                  |
| Authors          | PUT    | `/api/authors/`                               | Update author (ID in request body)   |
| Authors          | DELETE | `/api/authors/`                               | Delete author (ID in request body)   |
| Articles         | GET    | `/api/articles/`                              | List all articles (paginated)        |
| Articles         | GET    | `/api/articles/{id}/`                         | Retrieve article by ID               |
| Articles         | POST   | `/api/articles/`                              | Create a new article                 |
| Articles         | PUT    | `/api/articles/{id}/`                         | Update article by ID                 |
| Articles         | DELETE | `/api/articles/{id}/`                         | Delete article by ID                 |
| Comments         | GET    | `/api/articles/{article_id}/comments/`        | List all comments for an article     |
| Comments         | POST   | `/api/articles/{article_id}/comments/`        | Add comment to an article            |

---

## 🔄 Pagination Usage

This project uses a custom `AuthorPagination` (and similar for other views) that extends DRF’s `PageNumberPagination`.

**Query Parameters:**
- `page` – The page number (default: 1)
- `page_size` – Number of items per page (default: 4, max: 100)

**Example:**
