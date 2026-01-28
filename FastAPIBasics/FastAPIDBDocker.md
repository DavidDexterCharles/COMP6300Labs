# FastAPI + Databases with Docker Compose

This document builds on the basic FastAPI setup and focuses on connecting your FastAPI app to **PostgreSQL** and **MongoDB**, with both databases started using a single `docker-compose.yml` file.

We will cover:

- Creating a `docker-compose.yml` file that runs PostgreSQL and MongoDB
- Starting and stopping the database containers
- Installing the Python libraries needed to talk to the databases
- Example connection code for PostgreSQL and MongoDB from FastAPI
- Typical connection URLs you can reuse in your own code

> This guide assumes you already have a FastAPI project set up in `FastAPIBasics/FastAPIApp` and can run it with Uvicorn as described in the main `README.md`.

---

## 1. First: Prerequisites

Before working with Docker and databases, ensure you have:

1. **Docker and Docker Compose installed** on your machine.
2. A working FastAPI application in `FastAPIBasics/FastAPIApp/main.py`.
3. A Python virtual environment (`venv`) created and activated inside `FastAPIApp`.

From inside `FastAPIApp`:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # On Windows PowerShell
```

Then make sure you can still run your FastAPI app with something like:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

---

## 2. Second: `docker-compose.yml` for PostgreSQL and MongoDB

In the `FastAPIBasics` folder (one level **above** `FastAPIApp`), there is a file called `docker-compose.yml`.

This file defines two services:

- **PostgreSQL** (for relational data)
- **MongoDB** (for document/NoSQL data)

You only need to:

1. Open `FastAPIBasics/docker-compose.yml` to view or adjust usernames/passwords if needed.
2. Remember the default values used (you will need them in your connection strings), for example:
   - Postgres database name: `fastapi_db`
   - Postgres user: `fastapi_user`
   - Postgres password: `fastapi_password`
   - Mongo root user: `fastapi_root`
   - Mongo root password: `fastapi_root_password`

---

## 3. Third: Start PostgreSQL and MongoDB with Docker Compose

From inside the `FastAPIBasics` folder (where `docker-compose.yml` lives), run:

```bash
docker compose up -d
```

This will:

- Pull the Postgres and Mongo images (if not already available).
- Start two containers:
  - `fastapi_postgres` (PostgreSQL on port `5432`)
  - `fastapi_mongo` (MongoDB on port `27017`)

To check that the containers are running:

```bash
docker compose ps
```

To stop the containers later:

```bash
docker compose down
```

While your FastAPI app is running (from `FastAPIApp`) and the Docker containers are up, your app can connect to both databases using `localhost` and the standard ports.

---

## 4. Fourth: Install Python database libraries

Inside your **activated** virtual environment in `FastAPIApp`, install libraries for PostgreSQL and MongoDB:

```bash
pip install sqlalchemy psycopg2-binary pymongo
```

This gives you:

- `sqlalchemy` – higher-level ORM/engine for relational databases.
- `psycopg2-binary` – PostgreSQL driver used by SQLAlchemy.
- `pymongo` – MongoDB driver.

You can later add other tools (for example, an async driver like `motor`) if you wish, but these are enough for basic examples.

---

## 5. Fifth: Connection URLs for PostgreSQL and MongoDB

Assuming you use the default credentials defined in `docker-compose.yml`, the typical **connection URLs** will be:

- **PostgreSQL SQLAlchemy URL**:

  ```text
  postgresql+psycopg2://fastapi_user:fastapi_password@localhost:5432/fastapi_db
  ```

- **MongoDB URL** (pymongo):

  ```text
  mongodb://fastapi_root:fastapi_root_password@localhost:27017
  ```

You can hardcode these while learning, but in real projects you should store them in environment variables or configuration files.

---

## 6. Sixth: Example – Connect FastAPI to PostgreSQL

Below is a very simple example of connecting to PostgreSQL from your FastAPI app using SQLAlchemy. This can go inside `FastAPIApp/main.py` (or in separate modules if you prefer better structure).

```python
from fastapi import FastAPI
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://fastapi_user:fastapi_password@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL, echo=True)

app = FastAPI()


@app.get("/db-check/postgres")
def check_postgres():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1")).scalar()
    return {"postgres_ok": result == 1}
```

Steps to try this:

1. Make sure Docker containers are running (`docker compose up -d` from `FastAPIBasics`).
2. Activate your virtual environment in `FastAPIApp`.
3. Run FastAPI with:

   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

4. Open `http://127.0.0.1:8000/db-check/postgres` in your browser.

If everything is set up correctly, you should get a response like:

```json
{ "postgres_ok": true }
```

---

## 7. Seventh: Example – Connect FastAPI to MongoDB

Here is a basic example using `pymongo` to connect to MongoDB and insert/read a document. Again, this can go into `main.py` or a separate module that you import.

```python
from fastapi import FastAPI
from pymongo import MongoClient

MONGO_URL = "mongodb://fastapi_root:fastapi_root_password@localhost:27017"

mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client["fastapi_db"]      # database name
items_collection = mongo_db["items"]       # collection name

app = FastAPI()


@app.post("/db-check/mongo")
def create_item(name: str):
    result = items_collection.insert_one({"name": name})
    return {"inserted_id": str(result.inserted_id)}


@app.get("/db-check/mongo")
def list_items():
    items = list(items_collection.find({}, {"_id": 0}))
    return {"items": items}
```

Try it with:

1. Docker databases running: `docker compose up -d` from `FastAPIBasics`.
2. FastAPI running: `uvicorn main:app --reload --host 127.0.0.1 --port 8000` from `FastAPIApp`.
3. Use:
   - `POST http://127.0.0.1:8000/db-check/mongo?name=test-item`
   - `GET  http://127.0.0.1:8000/db-check/mongo`

You can also experiment via the interactive docs at `http://127.0.0.1:8000/docs`.

---

## 8. Eighth: Summary workflow (FastAPI + Postgres + Mongo + Docker)

1. **Set up FastAPI app** in `FastAPIApp` (see the main FastAPI README).
2. **Create and activate a virtual environment** inside `FastAPIApp`.
3. **Install dependencies**:
   - `pip install fastapi "uvicorn[standard]" sqlalchemy psycopg2-binary pymongo`
4. **Use the provided `docker-compose.yml` in `FastAPIBasics`** to start databases:
   - `docker compose up -d`
5. **Connect to PostgreSQL** using the SQLAlchemy URL:
   - `postgresql+psycopg2://fastapi_user:fastapi_password@localhost:5432/fastapi_db`
6. **Connect to MongoDB** using the Mongo URL:
   - `mongodb://fastapi_root:fastapi_root_password@localhost:27017`
7. **Run FastAPI**:
   - `uvicorn main:app --reload --host 127.0.0.1 --port 8000`
8. **Test database endpoints** through:
   - Browser/HTTP client (for example, `/db-check/postgres`, `/db-check/mongo`)
   - Interactive docs at `/docs`.

Following these steps will give you a simple but realistic FastAPI setup that talks to both PostgreSQL and MongoDB, with both databases managed by Docker Compose.
