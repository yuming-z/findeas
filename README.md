# FINDEAS Backend

## Pre-requisites

- [Python 3.10+](https://www.python.org/downloads/)
- [PostgreSQL 12+](https://www.postgresql.org/download/)

> You also run in container environment. See [README.Docker.md](README.Docker.md) for more information.

## Installation

1. Clone the repository.
2. Create a virtual environment.

```bash
python -m venv venv
```

> If `python` does not work, try using `py` for Windows or `python3` for Mac/Linux.

3. Activate the virtual environment.

Windows:

```powershell
./venv/Scripts/Activate.ps1
```

Mac/Linux:

```bash
source venv/bin/activate
```

> You can use `conda` to create a virtual environment as well.

4. Install the dependencies.

```bash
pip install -r requirements.txt
```

> To install dependencies via `conda`, run `conda install --file requirements.txt`.

5. Create a `.env` file in the root directory of the project and copy all contents from `.env.scaffold` to `.env`.

6. Create a PostgreSQL database.

You should have a default user `postgres` with the password you defined during installation.

Connect to the PostgreSQL server:

```bash
psql --user postgres
```

> You will be prompted to enter the password for the `postgres` user.

Create a database:

```sql
CREATE DATABASE findea;
```

It is a recommended practice to create a separate user for the database. You can create a new user with the following command:

```sql
CREATE USER user WITH PASSWORD 'password'; -- the user name and password can be anything you want
GRANT ALL PRIVILEGES ON DATABASE findea TO user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO user;
```

7. Fill in the database credentials in the `.env` file.

8. Run the migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

9. Load the data into the database.

You should have the dataset stored under `HLOCData/` in the root directory of the project.

```bash
python import_data.py
```

10. Run the server.

```bash
python manage.py runserver
```
