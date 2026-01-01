import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 1. Setup path
db_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(db_folder, 'Auth.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 2. CREATE DB OBJECT HERE
db = SQLAlchemy(app) 

# 3. NOW IMPORT MODELS
from models.user import User

with app.app_context():
    db.create_all()

# 4. NOW REGISTER BLUEPRINTS
from routes.dashboard import dashboard_bp
from routes.auth import auth_bp
app.register_blueprint(dashboard_bp)
app.register_blueprint(auth_bp)

@app.route("/")
def landing():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
