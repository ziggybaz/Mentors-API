import click
import logging
import csv
from flask.cli import FlaskGroup
from jparser.parser import ParseRows, ParseRow
from sqlalchemy import text
from apps import init_app
from models import db, MentorCheck


app = create_app = init_app(db=db)
cli = FlaskGroup(app)
app.logger.setLevel(logging.INFO)


@cli.command("create_db")
def create_db():
    # TODO :remove dropping data on prod
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("read")
@click.argument("source")
def read_data(source):
    """
    Read data from source eg csv
    """
    with open(source) as f:
        app.logger.info("Running cron job..")
        input_rows = csv.DictReader(f)
        scanner = ParseRows(input_rows)
        cme_t, drill_t = scanner.compute_cme_and_drill_topics()
        cme_drill_topics_db_ids_temp = {}

        # Store CME topics
        # TODO :Fix code smell
        for item in cme_t:
            # TODO :optimize
            sql = text(
                "INSERT INTO cme_topics(topic) VALUES(:val) ON CONFLICT (topic) DO UPDATE SET updated_at=NOW() RETURNING id"
            )
            item_id = db.session.execute(
                sql,
                {"val": item},
            )
            db.session.commit()
            cme_drill_topics_db_ids_temp.update(
                {f"cme_topic_{item}_id": item_id.fetchone()[0]}
            )
        # Store Drill topics
        for item in drill_t:
            # TODO :optimize
            sql = text(
                "INSERT INTO drill_topics(topic) VALUES(:val) ON CONFLICT (topic) DO UPDATE SET updated_at=NOW() RETURNING id"
            )
            item_id = db.session.execute(
                sql,
                {"val": item},
            )
            cme_drill_topics_db_ids_temp.update(
                {f"drill_topic_{item}_id": item_id.fetchone()[0]}
            )
            db.session.commit()
        f.seek(0)
        input_rows = csv.DictReader(f)

        for item in input_rows:
            processor = ParseRow(item)
            cleaned_data = processor.match_particpant_and_topics_to_rows()
            for row in cleaned_data:
                # TODO :Fix code smell
                row.update(
                    {
                        "cme_unique_id": cme_drill_topics_db_ids_temp[
                            f"cme_topic_{row.get('cme_topic','null')}_id"
                        ],
                        "drill_unique_id": cme_drill_topics_db_ids_temp[
                            f"drill_topic_{row.get('drill_topic','null')}_id"
                        ],
                    }
                )

        db.session.bulk_insert_mappings(MentorCheck, cleaned_data)
        db.session.commit()


if __name__ == "__main__":
    cli()
