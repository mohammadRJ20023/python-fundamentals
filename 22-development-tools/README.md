# Chapter 22: Development Tools

## 📖 English

This chapter introduces useful development tools and practices that every Python developer should know.

---

## Virtual Environment (venv)

A virtual environment creates an isolated Python environment for each project.

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate (Windows)

```bash
.venv\Scripts\activate
```

### Activate (Linux / macOS)

```bash
source .venv/bin/activate
```

---

## Installing Packages

```bash
pip install requests
```

---

## Export Installed Packages

```bash
pip freeze > requirements.txt
```

---

## Install Packages From requirements.txt

```bash
pip install -r requirements.txt
```

---

## Type Hinting

Type hints improve code readability and help IDEs detect errors.

```python
def greet(name: str) -> None:
    print(f"Hello {name}")
```

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## .gitignore

Never upload these files to GitHub:

```text
.venv/
__pycache__/
*.pyc
```

---

## Requirements

- Python 3.10+

---

## 📖 فارسی

در این فصل با ابزارها و نکات مهم توسعه پروژه‌های پایتون آشنا می‌شوید.

---

## محیط مجازی (Virtual Environment)

برای هر پروژه بهتر است یک محیط مجازی جداگانه ایجاد کنید.

### ساخت محیط مجازی

```bash
python -m venv .venv
```

### فعال‌سازی در ویندوز

```bash
.venv\Scripts\activate
```

### فعال‌سازی در لینوکس و مک

```bash
source .venv/bin/activate
```

---

## نصب کتابخانه

```bash
pip install requests
```

---

## ساخت فایل requirements.txt

```bash
pip freeze > requirements.txt
```

---

## نصب از روی requirements.txt

```bash
pip install -r requirements.txt
```

---

## Type Hinting

برای خواناتر شدن کد و تشخیص بهتر خطاها توسط IDE استفاده می‌شود.

```python
def greet(name: str) -> None:
    print(f"Hello {name}")
```

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## فایل .gitignore

فایل‌های زیر را در GitHub قرار ندهید:

```text
.venv/
__pycache__/
*.pyc
```

---

