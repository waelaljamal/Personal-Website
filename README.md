# Personal Website

Personal Website By Using **Django** Framework & Integrate it with **Tailwindcss** & **Unpoly** js Libraries.

![Home Page Screenshot](https://github.com/alnuaimi94/Personal-Website/raw/main/static/images/screenshots/desktop-home.png)

![Blog Page Screenshot](https://github.com/alnuaimi94/Personal-Website/raw/main/static/images/screenshots/desktop-blog.png)

## Installation:

- Clone the project:

  ```bash
  git clone https://github.com/alnuaimi94/Personal-Blog
  ```

- Change directory & Create virtualenv called **env**:
  ```bash
  cd Personal-Blog
  ```
  ```bash
  python3 -m venv env
  ```
- Activate virtualenv & Install dependencies:
  - for Windows System:
    ```bash
      env/Scripts/activate
    ```
  - for Linux System:
    ```bash
      source ./env/bin/activate
    ```
  ```bash
  pip install -r requirements-dev.txt
  ```
- Create .env file in the root of the project when manage.py is found & add this lines inside it:

  ```bash
  SECRET_KEY=YOUR_SECRET_KEY
  DATABASE_URL=sqlite:///db.sqlite3
  ```

  > **_NOTE:_** you can generate Django SECRET_KEY by using this command line:

  ```cmd
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```

- Collectstatic & Runserver:
  ```bash
  python manage.py collectstatic
  ```
  ```bash
  python manage.py runserver
  ```
- Finally open the localhost in the browser:
  ```bash
    http://127.0.0.1:8000/
  ```

## Usage:

### Django Silk:

You can access the debug information by visit this link:

```bash
  http://127.0.0.1:8000/silk/
```

Silk primarily consists of:

- Middleware for intercepting Requests/Responses
- A wrapper around SQL execution for profiling of database queries
- A context manager/decorator for profiling blocks of code and functions either manually or dynamically.
- A user interface for inspection and visualisation of the above.

### Tailwind & Unpoly with Webpack:

> **_NOTE:_** Use Tailwind and unpoly with Webpack Cli makes files small and compressed by dispensing with other codes in these libraries that we do not need in our project.

I used **Tailwind** because it's best framework to design anything you want.
it give you freedom to customize every pixel in the web screen like Flutter.

I want to make my blog fast, light and portable, so I used the **Unpoly** Js Library.
**Unpoly** enables fast and flexible frontends while keeping rendering logic on the server.
It has no dependencies and plays nice with existing code.

## License:

Copyright (c) 2021-present Abdullah Alnuaimi under the **MIT License**.
