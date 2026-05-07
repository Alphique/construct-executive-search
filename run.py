# FILE: run.py
from app import create_app
from app.core.extensions import db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        # This will now work because create_app() has finished
        db.create_all()
    app.run(debug=True)