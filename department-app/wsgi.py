"""Application's main module. Creates Flask application."""

from factories import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
