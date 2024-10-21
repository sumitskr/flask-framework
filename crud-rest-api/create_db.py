from app import db, create_app
from models import *  # Import your models

# Create an app context
app = create_app()

with app.app_context():
    db.create_all()  # This will create the tables in the database
    print("Tables created successfully!")
