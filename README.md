# Python-Sql-Intro

This project loads data about **students and rooms** into a **PostgreSQL (or MySQL)** database and performs analytical queries:

1. Number of students in each room
2. Five rooms with the **lowest average student age**
3. Five rooms with the **highest age difference between students**
4. Rooms where **students of different nationalities (or genders)** live

The results can be **exported to JSON or XML**.

---

## Requirements

Make sure you have:

- **Python 3.11** — the programming language for this project
- **PostgreSQL 15** _(or MySQL 8 if using MySQL branch)_
- **Docker & docker-compose** _(for database deployment)_

Verify installation:

```bash
python --version
docker --version
docker-compose --version
```
