# models/user.py
import app # Import the whole module instead of 'from app import db'

class User(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    username = app.db.Column(app.db.String(50), unique=True, nullable=False)
    password = app.db.Column(app.db.String(100), nullable=False)
