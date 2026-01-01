



from flask import Blueprint, render_template

auth_bp = Blueprint("auth",__name__, static_folder="static", template_folder="templates")

@auth_bp.route('/login')
def auth():
    return render_template('auth.html')