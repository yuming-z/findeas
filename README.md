# FINDEAS Backend

## Pre-requisites

- [Python 3.10+](https://www.python.org/downloads/)
- [MySQL 8.0+](https://dev.mysql.com/downloads/mysql/)

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

6. Create a MySQL database.

Access the MySQL server by opening `mysql.exe` (Windows user), or access via the command line:

```bash
mysql -u root
```

> If you install MySQL via Homebrew, you need to run the `mysql` services first;
> 
> ```bash
> brew services start mysql
> ```

Execute the following statements in the MySQL command line to set up the database:

```sql
CREATE DATABASE knowyourpartner;
CREATE USER 'group12'@'localhost' IDENTIFIED BY 'group12';
GRANT ALL PRIVILEGES ON knowyourpartner.* TO 'group12'@'localhost';
FLUSH PRIVILEGES;
```

Create a database:

```sql
CREATE DATABASE findeas;
```

It is a recommended practice to create a separate user for the database. You can create a new user with the following command:

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
-- username and password are placeholders
GRANT ALL PRIVILEGES ON findeas.* TO 'username'@'localhost';
FLUSH PRIVILEGES;
```

Connect the database:

```sql
CONNECT findeas;
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
