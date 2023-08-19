import logging
from flask.cli import FlaskGroup
from apps import init_app

app = init_app(db=None)
cli = FlaskGroup(app)
app.logger.setLevel(logging.INFO)



if __name__ == "__main__":
    cli()
