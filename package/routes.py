from sqlalchemy.orm import session
from wtforms.form import Form
from package import app
from flask import render_template,redirect,url_for,flash
from package.models import user
from package.forms import RegisterForm,LogInForm
from package import db
from flask_login import login_user,logout_user


@app.route('/')

@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/settings')
def settings_page():
    return render_template('settings.html')

@app.route('/register',methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create=user(username=form.username.data,
                email_address=form.email_address.data,
                password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('login_page'))

    if form.errors!={}:
        for err_msg in form.errors.values():
            flash(f'There was an Error {err_msg}',category='danger')

    return render_template('register.html',form=form)
  
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form=LogInForm()
    if form.validate_on_submit():
        attempted_user = user.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('settings_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You are logged out",category='info')
    return redirect(url_for("home_page"))