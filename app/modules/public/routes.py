# =========================
# FILE: app/modules/public/routes.py
# =========================

from flask import Blueprint, render_template

public_bp = Blueprint('public', __name__)

@public_bp.route("/")
def home():
    return render_template(
        "public/home.html",
        title="Executive Search Zambia",
        description="Construct Executive Search helps companies find top executives in Zambia."
    )

@public_bp.route("/about")
def about():
    return render_template(
        "public/about.html",
        title="About CES",
        description="Learn about Construct Executive Search"
    )