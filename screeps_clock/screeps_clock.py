from flask import Flask, session, redirect, url_for, escape, request, render_template, flash, send_from_directory
from screeps_clock import app
from flask_cors import cross_origin
import screeps_clock.routes.clock



@app.route('/')
def index():
    return redirect(url_for('html_time'))


@app.after_request
def add_header(response):
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'private, no-store, no-cache, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
    return response


# set the secret key.  keep this really secret:
app.secret_key = app.config['SECRET_KEY']