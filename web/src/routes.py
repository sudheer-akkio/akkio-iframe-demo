import json
import os

from flask import (
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.utils import secure_filename

from src import app, db
from src.forms import LoginForm, RegisterForm, SetupForm
from src.models import User


@app.route("/")  # Decorator -- what URL should I navigate and display the HTML code?
@app.route("/home")  # This is how we can handle multiple routes for the same request
def home_page():
    active_tab = "home"
    return render_template("home.html", active_tab=active_tab)


@app.route("/setup", methods=["GET", "POST"])
def setup_page():
    form = SetupForm()

    if current_user.is_authenticated:
        if form.validate_on_submit():
            # store endpoints in session object to be used to render in separate routes
            session["chat_endpoint"] = form.chat_explore.data
            session["dashboard_endpoint"] = form.dashboard.data
            session["insights_report_endpoint"] = form.insights_report.data

            flash(
                "Endpoints Set! This does not guarantee the endpoints will render.",
                category="success",
            )
    else:
        flash("Please login first.", category="danger")

        return redirect(url_for("login_page"))

    # Check if session values are set and update form data
    if "chat_endpoint" in session:
        form.chat_explore.data = session["chat_endpoint"]
    if "dashboard_endpoint" in session:
        form.dashboard.data = session["dashboard_endpoint"]
    if "insights_report_endpoint" in session:
        form.insights_report.data = session["insights_report_endpoint"]

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(
                f"There was an error with setting endpoints: {err_msg}",
                category="danger",
            )

    active_tab = "setup"
    return render_template("setup.html", form=form, active_tab=active_tab)


@app.route("/analyze", methods=["GET", "POST"])
def analyze_page():
    chat_endpoint = session.get("chat_endpoint", None)

    if not chat_endpoint:
        form = SetupForm()
        chat_endpoint = form.chat_explore.data

    active_tab = "analyze"
    return render_template(
        "analyze.html",
        chat_endpoint=chat_endpoint,
        active_tab=active_tab,
    )


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard_page():
    dashboard_endpoint = session.get("dashboard_endpoint", None)

    if not dashboard_endpoint:
        form = SetupForm()
        dashboard_endpoint = form.dashboard.data

    active_tab = "dashboard"
    return render_template(
        "dashboard.html",
        dashboard_endpoint=dashboard_endpoint,
        active_tab=active_tab,
    )


@app.route("/insights", methods=["GET", "POST"])
def insights_page():
    insights_report_endpoint = session.get("insights_report_endpoint", None)

    if not insights_report_endpoint:
        form = SetupForm()
        insights_report_endpoint = form.insights_report.data

    active_tab = "insights"
    return render_template(
        "insights.html",
        insights_report_endpoint=insights_report_endpoint,
        active_tab=active_tab,
    )


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if (
        form.validate_on_submit()
    ):  # validate_on_submit will automatically run the validation specified in RegisterForm class and only create user if all validations are successful
        user_to_create = User(
            username=form.username.data,
            password=form.password1.data,
        )

        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(
            f"Account created successfully! You are now logged in as {user_to_create.username}",
            category="success",
        )

        return redirect(
            url_for("setup_page")
        )  # make sure to import these methods from flask

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(
                f"There was an error with creating a user: {err_msg}", category="danger"
            )

    active_tab = "register"
    return render_template("register.html", form=form, active_tab=active_tab)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(
                f"Success! You are logged in as: {form.username.data}",
                category="success",
            )

            return redirect(url_for("setup_page"))

        else:
            flash(
                "Username and password are not match! Please try again",
                category="danger",
            )

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error with logging in: {err_msg}", category="danger")

    active_tab = "login"
    return render_template("login.html", form=form, active_tab=active_tab)


@app.route("/logout")
def logout_page():
    # Remove connection object from session, which will be a logout
    # session.pop("snowflake_obj", None)
    logout_user()
    flash("You have been logged out!", category="info")
    return redirect(url_for("home_page"))
