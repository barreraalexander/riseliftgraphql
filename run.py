from app import create_app
from app.config import settings
from flask import Flask


app: Flask = create_app()

if __name__=='__main__':
    app.run(
        port=5003,
        debug=settings.debug
    )