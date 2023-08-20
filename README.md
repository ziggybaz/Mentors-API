Mentors API

## Structure

```bash


├── apps
│   ├── api
│   │   ├── api_v1.py
│   │   ├── __init__.py
│   │   └── views
│   │       ├── mentor.py
│   │       └── ping.py
│   ├── docs
│   │   └── docs.yml
│   └── __init__.py
├── conf
│   ├── config.py
│   └── __init__.py
├── cronfile-dev
├── cronfile-prod
├── data-source
│   ├── sample-2.csv
│   └── sample.csv
├── docker-compose.yml
├── Dockerfile
├── Dockerfile.dev
├── heroku.yml
├── init-dev.sh
├── init-prod.sh
├── jparser
│   ├── __init__.py
│   └── parser.py
├── Makefile
├── manage.py
├── models
│   ├── cme.py
│   ├── drill.py
│   ├── __init__.py
│   ├── mentor.py
│   └── mixin.py
├── pytest.ini
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── stubs
    │   └── output.json
    ├── test_config.py
    ├── test_endpoints.py
    ├── test_models.py
    └── test_pasrer.py


```

### API Endpoints

| METHOD |      ENDPOINT      |                          DESCRIPTION |
| ------ | :----------------: | -----------------------------------: |
| GET    |    /api/v1/ping    |           Ping to check if API is up |
| GET    | /api/v1/metorships |            Get a list of mentorships |
| GET    |      /apidocs      | The swagger documentaion for the api |

## Heroku

The API is hosted on heroku

> **_NOTE:_** The datbase has data from processing the case on sheet 3 (EXAMPLE OUTPUT FROM A SINGLE CASE)

The swagger docs can be found on https://jparser-api-7097118d0ae3.herokuapp.com/apidocs which can be used for testing the api

> **_NOTE:_** - The API runs on [Free Heroku Dyno](https://devcenter.heroku.com/articles/dyno-types) with 512MB RAM and sleeps periodically

## Local set up

Ensure the following ports are not in use

- 8003
- 8078 (adminer web interface to manage postgres)

[The docker-compose file](docker-compose.yml) contains the components needed to the services.
In the root project directory, boot up the services in the docker compose file using

```shell
docker-compose up
```

**_NOTE:_** The swagger docs can be found on https://jparser-api-7097118d0ae3.herokuapp.com/ which can be used for testing the api

The cron is set up to run every minure for test purposes and can be modified here

#### Running Tests on local

Python 3.8 + is required\
While still in the root directory of the project. You can create a virtual environment in the folder using

```shell
 python{PYTHON_VERSION} -m venv mentors
```

You can activate the environment using

```shell
source mentors/bin/activate
```

To install dependencies.

```shell
(venv) make init
```

To run unit tests

```shell
(venv)  make unit_tests
```

To run all tests with coverage report .

```shell
(venv)  make test_coverage
```

### Checking the database on local

A web interface(while docker-compose services running) to check the database can be found on

- http://localhost:8078/?pgsql=mentors-db&username=postgres&db=mentors
- password is `postgres`

### Triger cron on local

To run cron ensure all the services are running `docker-compose up`

Set the required environmental variables using

```shell
(venv)  source .env-cli
```

Run the cron via

```shell
(venv)  export FLASK_APP=manage.py && python manage.py read "./data-source/sample-2.csv"
```

### Assumptions

- The file sheet to extracted can be uploaded to the server as csv or the csv will publicly acessible on providers like s3 etc

### TODO

- Set up cron for on heroku
- Improve code comments and remove code smells
- Improve swagger docs
