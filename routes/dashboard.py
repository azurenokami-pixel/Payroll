from flask import Blueprint, render_template

dashboard_bp = Blueprint("dashboard",__name__, static_folder="static", template_folder="templates")

@dashboard_bp.route('/dashboard/')
def show_dashboard():
    return render_template('dashboard.html')