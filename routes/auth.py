from flask import Blueprint, render_template, request, redirect, url_for
from database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def auth():
    from models.user import User  # Local import to stay safe
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            return redirect(url_for('dashboard.show_dashboard'))
        else:
            return render_template('auth.html', error="Invalid credentials")

    return render_template('auth.html')
