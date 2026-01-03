

import os
from flask import Flask, render_template
from database import db  # Import from new file

app = Flask(__name__)

# 1. Setup path
db_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(db_folder, 'Auth.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 2. Initialize the db with the app
db.init_app(app)

# 3. Create Tables (Import User here)
with app.app_context():
    from models.user import User
    db.create_all()

# 4. Register Blueprints
from routes.dashboard import dashboard_bp
from routes.auth import auth_bp
app.register_blueprint(dashboard_bp)
app.register_blueprint(auth_bp)

@app.route("/")
def landing():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
