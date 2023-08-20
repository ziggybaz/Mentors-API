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


COPY cronfile-prod /etc/cron.d/cronfile

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cronfile

# Apply the cron job
RUN crontab /etc/cron.d/cronfile

RUN  crontab -l






ENTRYPOINT ["sh", "./init-prod.sh" ]

