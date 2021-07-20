Flask Task
----------

this is simple flask application for purpose of recruitment process.


Acceptance criteria as follows:
===============================

## I. A login functionality exists
- a user can be mocked, but registration is out of scope
- there should be a signifier to display the logged in user&#39;s name - users not logged in are redirected to
the login screen and should not be allowed to access anything else

### II. Money Movements view
- a list view to show money movements
- a money movement item has a modified date, a money amount with currency, a originator person and
a clickable link to show other details

### III. Details view
- the Details view can be reached by clicking a money movement in the Money Movements view (II).
- The details displayed are at least the same as in (II)
- Additionally a receiver person is shown
- A text input field exists to write notes

### IV. The flask app includes setup and start instructions - The app should be
startable on Ubuntu 20.04 LTS
- Any packaging / dependency management can be used, if instructions to install it are provided




Installation guide (for Ubuntu 20.04 LTS):

Clone the repository::

    $ git clone https://github.com/felonx/flasking
    $ cd flasking

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ source venv/bin/activate

Install requirements::

    $ pip install requirements.txt

Set environmental variables::

    $ export FLASK_APP=project/app.py
    $ export FLASK_ENV=development

Run flask application::

    $ flask run

Open http://127.0.0.1:5000 in a browser


About the app
=============

Per acceptance criteria, app lists all Transactions (renamed from 'money movements' for clarity),
with option to see detail of each transaction, and option to edit notes for each of transaction.

User login functionality is implemented with session object storing the name of the user under 'user' key,
and the simple decorator which routes unlogged user to a login page.

Additionally, app offers a script to generate some sample data and populate into database.

App is covered by tests using pytest library, with some fixtures set up in conftest.py

Potential development that could be suggested for next iterations may include:
 - enhancing login functionality, including registration and authentication
 - css styling for the templates