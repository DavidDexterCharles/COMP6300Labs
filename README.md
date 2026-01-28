# Python Local App Setup (with `main.py`)

This document is a quick-start guide for setting up a small Python application locally using a `main.py` file and a virtual environment. It follows a similar numbered, step-by-step style to the Git guide.

We will cover:

- Creating a virtual environment (`venv`)
- Activating and deactivating the virtual environment
- Installing libraries (for example, **NumPy** and **Matplotlib**)
- Creating a `requirements.txt` file
- Recreating the same environment on another machine or directory

---

## 1. First: Create a project folder and `main.py`

1. Create a new folder for your project (for example, `MyPythonApp`).
2. Inside that folder, create a file named `main.py`.

Example minimal `main.py`:

```python
def main():
    print("Hello from main.py!")


if __name__ == "__main__":
    main()
```

Run this once python is installed on your system:

```bash
python main.py
```

_(On some systems you may use `python3` instead of `python`.)_

---

## 2. Second: Create a virtual environment (`venv`)

A **virtual environment** keeps your project’s Python packages isolated from the rest of your system, so different projects can use different versions of libraries without conflicts.

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

You should **activate** the virtual environment before installing packages or running your app, so everything is installed into `venv`.

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

## 4. Fourth: Install libraries (NumPy, Matplotlib, etc.)

With the virtual environment **activated**, you can install libraries using `pip`.

For example, to install **NumPy** and **Matplotlib**:

```bash
pip install numpy matplotlib
```

Once installed, you can import and use them in `main2.py`. Example:

```python
import numpy as np
import matplotlib.pyplot as plt


def main():
    # Simple NumPy example
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Simple Matplotlib example
    plt.plot(x, y)
    plt.title("Sine Wave Example")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.show()


if __name__ == "__main__":
    main()
```

Run your app (with `venv` active):

```bash
python main2.py
```

---

## 5. Fifth: Create a `requirements.txt` file

The `requirements.txt` file lists the packages your project depends on, usually with version numbers. This is extremely useful when:

- You move the project to another machine.
- A teammate wants to set up the project.
- You want a consistent, repeatable environment.

With your virtual environment still **activated**, run:

```bash
pip freeze > requirements.txt
```

This creates a `requirements.txt` file in your project folder containing lines like:

```text
matplotlib==<some-version>
numpy==<some-version>
```

(There will usually be more packages listed, depending on your environment.)

You should commit `requirements.txt` to your Git repository so others can use it.

---

## 6. Sixth: Recreate the environment from `requirements.txt` (new machine or new directory)

If you **clone** the same project into another folder or on another machine, you will typically see:

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
python main.py
```

and expect the application to behave the same way on this new machine or in this new directory.

---

## 7. Seventh: Summary of the basic workflow

1. **Create project folder and `main.py`.**
2. **Create a virtual environment**: `python -m venv venv`.
3. **Activate the environment**:
   - Windows PowerShell: `.\venv\Scripts\Activate.ps1`
   - Windows cmd: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. **Install packages** with `pip install ...` (for example, `pip install numpy matplotlib`).
5. **Run your app**: `python main.py`.
6. **Generate `requirements.txt`**: `pip freeze > requirements.txt`.
7. **On another machine or folder**:
   - Create a new `venv` (`python -m venv venv`),
   - Activate it,
   - Then run `pip install -r requirements.txt`.

Following this pattern will give you a clean, repeatable setup process for small Python applications using `main.py` and virtual environments.
