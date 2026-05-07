# =========================
# FILE: app/modules/auth/routes.py
# =========================

from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import user
from app.models.user import User
from app.core.extensions import db

auth_bp = Blueprint('auth', __name__)

# REGISTER (TALENT)
@auth_bp.route("/register/talent", methods=["GET", "POST"])
def register_talent():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "User already exists"

        user = User(name=name, email=email, role="talent")
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("auth/register_talent.html")


# =========================
# LOGIN (FIXED)
# =========================

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session["user_id"] = user.id
            session["role"] = user.role

            if user.role == "admin":
                return redirect("/admin")

            elif user.role == "talent":
                return redirect("/talent/dashboard")

            elif user.role == "client":
                return redirect("/client/dashboard")

        return "Invalid credentials"

    return render_template("auth/login.html")

# LOGOUT
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("public.home"))

# =========================
# ADD THIS TO EXISTING FILE
# =========================

@auth_bp.route("/register/client", methods=["GET", "POST"])
def register_client():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "User already exists"

        user = User(name=name, email=email, role="client")
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("auth/register_client.html")