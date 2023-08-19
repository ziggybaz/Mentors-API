FROM  python:3.10.5-slim-bullseye


# set work directory
WORKDIR /usr/src/app


# install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    bash netcat cron

COPY ./requirements.txt .
RUN pip install --no-cache-dir -U -r requirements.txt

# copy project
COPY . .

RUN chmod +x init.sh
ENTRYPOINT ["sh", "./init.sh" ]
