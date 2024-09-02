from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView


from app.config import settings
# from app import models, schema
from .models import db_session
from .schema import schema, Department

# db: SQLAlchemy = SQLAlchemy()

def create_app(config_class=settings):
    app = Flask(__name__)


    # app.config.from_object(config_class)


    # db.init_app(app)



    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True # for having the GraphiQL interface
        )
    )



    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
