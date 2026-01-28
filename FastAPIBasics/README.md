# FastAPI Local App Setup (with `main.py`)

This document is a quick-start guide for setting up and running a small **FastAPI** application locally using a `main.py` file and a virtual environment.

We will cover:

- Creating a project and `main.py` FastAPI app
- Creating and activating a virtual environment (`venv`)
- Installing FastAPI and Uvicorn
- Running the FastAPI server locally
- Using the interactive API docs
- Creating and reusing a `requirements.txt` file
- Ensuring `venv` is excluded from Git

---

## 1. First: Create a project folder and FastAPI `main.py`

1. Create a new folder for your project called `FastAPIApp` (for example, inside this `FastAPIBasics` folder).

2. Inside `FastAPIApp`, create a file named `main.py`.

Example minimal `main.py` for FastAPI:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

We will run this app later using Uvicorn (an ASGI server).

---

## 2. Second: Create a virtual environment (`venv`)

It is recommended to use a **virtual environment** so that the FastAPI and related packages are isolated from the rest of your system.

From inside your project folder, run:

```bash
python -m venv venv
```

This creates a new folder called `venv` that contains an isolated Python environment.

If your system uses `python3` instead, you would run:

```bash
python3 -m venv venv
```

---

## 3. Third: Activate and deactivate the virtual environment

You should **activate** the virtual environment before installing FastAPI or running your app, so that everything is installed into `venv`.

### 3.1 Activate on Windows

- **PowerShell**:

  ```bash
  .\venv\Scripts\Activate.ps1
  ```

- **Command Prompt (cmd.exe)**:

  ```bash
  venv\Scripts\activate
  ```

You should see something like `(venv)` appear at the start of your terminal prompt, indicating that the virtual environment is active.

### 3.2 Activate on macOS / Linux

```bash
source venv/bin/activate
```

Again, you should see `(venv)` at the beginning of your prompt.

### 3.3 Deactivate the virtual environment (all platforms)

To deactivate (go back to the system Python), simply run:

```bash
deactivate
```

After this, the `(venv)` prefix will disappear from your prompt.

---

## 4. Fourth: Install FastAPI and Uvicorn

With the virtual environment **activated**, install the packages you need to run FastAPI:

```bash
pip install fastapi "uvicorn[standard]"
```

This installs:

- `fastapi` – the web framework
- `uvicorn` – the ASGI server that will host your FastAPI app

You can check installed packages with:

```bash
pip list
```

---

## 5. Fifth: Run the FastAPI application

Assuming your app is in `main.py` and the FastAPI instance is called `app` (as in the earlier example), you can start the server with:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Explanation:

- `main` refers to the filename `main.py` (without the `.py`).
- `app` is the FastAPI instance inside that file.
- `--reload` automatically restarts the server when you save code changes (useful in development).
- `--host 0.0.0.0` listens on all available network interfaces (optional; for local development you can omit it).
- `--port 8000` sets the port; by default Uvicorn uses `8000`.

Once the server is running, you should see log output in the terminal, and you can open:

- `http://127.0.0.1:8000/` (root endpoint)
- `http://127.0.0.1:8000/items/123?q=test` (example parameterized endpoint)

Press `Ctrl + C` in the terminal to stop the server.

---

## 6. Sixth: Use the interactive API docs

FastAPI automatically generates interactive API documentation.

With the server running, open these URLs in your browser:

- Swagger UI docs (interactive API explorer):
  - `http://127.0.0.1:8000/docs`

- ReDoc docs (alternative documentation style):
  - `http://127.0.0.1:8000/redoc`

You can use these pages to see available endpoints, test them, and understand request/response models.

---

## 7. Seventh: Create a `requirements.txt` file

The `requirements.txt` file lists the packages your FastAPI project depends on, usually with specific versions. This is extremely useful when:

- You move the project to another machine.
- A teammate wants to set up the project.
- You want a consistent, repeatable environment.

With your virtual environment still **activated**, run:

```bash
pip freeze > requirements.txt
```

This creates a `requirements.txt` file in your project folder containing lines like:

```text
fastapi==<some-version>
uvicorn==<some-version>
```

(There will usually be more packages listed, depending on your environment.)

You should commit `requirements.txt` to your Git repository so others can use it.

---

## 8. Eighth: Recreate the environment from `requirements.txt` (new machine or new directory)

If you **clone** the same FastAPI project into another folder or on another machine, you will typically see:

- The source files (including `main.py`)
- The `requirements.txt` file
- But **no** `venv` folder yet (it should not be committed to Git)

To set everything up again:

1. **Clone the repository** (or copy the project folder).
2. **Create a new virtual environment** in the cloned folder.
3. **Activate** the virtual environment.
4. **Install dependencies from `requirements.txt`**.

Example sequence (inside the newly cloned project folder):

```bash
python -m venv venv
```

Activate it (Windows PowerShell example):

```bash
.\venv\Scripts\Activate.ps1
```

Then install all required packages:

```bash
pip install -r requirements.txt
```

This reads all the listed dependencies and installs matching versions into your new `venv`, recreating the same environment as the original project (as closely as possible).

You can now run:

```bash
uvicorn main:app --reload --port 8000
```

and expect the application to behave the same way on this new machine or in this new directory.

---

## 9. Ninth: Exclude `venv` from Git commits

You normally **do not want** to commit your virtual environment folder (`venv`) to Git, because it can be large and is easy to recreate from `requirements.txt`.

To tell Git to ignore `venv` (and `.venv` if you use that name), add the following lines to your `.gitignore` file in the root of your project:

```gitignore
# Python virtual environments
venv/
.venv/
```

After this, Git will stop tracking those folders, and they will not be included in future commits or pushes.

---

## 10. Tenth: Summary of the FastAPI workflow

1. **Create project folder and `main.py` with a FastAPI app.**
2. **Create a virtual environment**: `python -m venv venv`.
3. **Activate the environment**:
   - Windows PowerShell: `.\venv\Scripts\Activate.ps1`
   - Windows cmd: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. **Install FastAPI and Uvicorn**: `pip install fastapi "uvicorn[standard]"`.
5. **Run the server**: `uvicorn main:app --reload --port 8000`.
6. **Use the docs** at `/docs` or `/redoc` to explore and test your API.
7. **Generate `requirements.txt`**: `pip freeze > requirements.txt`.
8. **On another machine or folder**:
   - Create a new `venv` (`python -m venv venv`),
   - Activate it,
   - Then run `pip install -r requirements.txt`,
   - Finally start the server again with `uvicorn main:app --reload --port 8000`.

Following this pattern will give you a clean, repeatable setup process for small FastAPI applications using `main.py` and virtual environments.
