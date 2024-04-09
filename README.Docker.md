# How to run this application in container environment?

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [docker compose](https://docs.docker.com/compose/install/)

## Getting started

To run this application, make sure your docker is running, then run the following command:

```bash
docker compose up --build --force-recreate --no-deps
```

Now you can access the application at [localhost:8000](http://localhost:8000).

To stop the application, run the following command:

```bash
docker compose down
```

### First time Setup

If you are running this application for the first time, there are some additional steps you need to follow:

1. Create a `.env` file in the root directory of the project and copy the content from `.env.scaffold` file.
2. Fill in the database configuration in the `.env` file.
3. Run the application.
4. Run the following command to access the command line interface of the application server:

```bash
docker compose exec server bash
```

5. Run the following command to create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the following command to exit the command line interface:

```bash
exit
```

### Upload the data

To upload the data from the CSV file, you first need to have the CSV file under the `HLOCData/` directory in the root directory of the project.

Then, run the following command to upload the data to the container's file system:

```bash 
docker cp HLOCData/. <container_id>:/app/HLOCData
```

> You can get the container ID by running `docker ps`.

Now, run the following command to access the command line interface of the application server:

```bash
docker compose exec server bash
```

Run the following command to import the data:

```bash
python import_data.py
```

## Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

## References
* [Docker's Python guide](https://docs.docker.com/language/python/)