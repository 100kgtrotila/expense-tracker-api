# 💰 Expense Tracker API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-316192?style=for-the-badge&logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge&logo=sqlalchemy)

A high-performance, asynchronous REST API for tracking personal expenses. Built with **FastAPI**, **SQLAlchemy (Async)**, and **PostgreSQL**. Features include secure JWT authentication, pagination with metadata, and search capabilities.

---

## 🔗 Project URL


https://roadmap.sh/projects/expense-tracker-api

> This repository contains the solution for the Expense Tracker API project.

---

## ✨ Key Features

* **⚡ Asynchronous Architecture:** Built on top of `asyncpg` and `asyncio` for high concurrency.
* **🔐 Secure Authentication:** User registration and login using **OAuth2** with **JWT** (JSON Web Tokens) and Argon2 password hashing.
* **📂 Category Management:** Create, read, update, and delete expense categories.
* **💸 Expense Tracking:**
    * Add expenses linked to categories.
    * **Smart Pagination:** Returns data along with `page`, `limit`, and `total` count for frontend integration.
    * **Search & Filtering:** Find expenses by name.
* **🛡️ Robust Error Handling:** Standardized error responses (401, 404, 409, 422).
* **📑 Auto-Documentation:** Interactive API docs via Swagger UI and ReDoc.

---

## 🛠️ Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy (Async)
* **Migrations:** Alembic
* **Validation:** Pydantic v2
* **Authentication:** PyJWT, pwdlib
* **Server:** Uvicorn

---

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites

* Python 3.10 or higher
* PostgreSQL database (local or cloud, e.g., Supabase)

### 1. Clone the repository

```bash
git clone [https://github.com/100kgtrotila/expense-tracker-api.git](https://github.com/100kgtrotila/expense-tracker-api.git)
cd expense-tracker-api