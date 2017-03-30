=========================
Install Instructions Node
=========================

First, make sure you have node and
npm installed (see: https://nodejs.org/).

Then, install dependencies:

.. highlight::shell
    cd ux
    npm install

Run the project:

.. highlight::shell
    npm run dev

Your browser will open in the project url.

=================
Python Side Notes
=================

Python is not really required to run this project,
so, **I didn't use it to complete the task**.

As the probable goal of this test is to see some *mad python skills*,
I created a simple Flask project to consult the Spotify API on demand,
which is, basically, all it is possible to do with python for this
task.

Install Instructions
--------------------

Create and load your virtualenv; then:

.. highlight::shell
    cd web
    pip install -r requirements.txt

Then:

.. highlight::shell
    source .env  # if autoenv does not see it
    flask run

Getting Started
---------------

The route you're looking for is **/spotify/search**.
Start the Flask project and type the following in your browser:

http://localhost:5000/spotify/search
