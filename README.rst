DummyWeb
========

Dummy Meuporg web frontend.

Installation
------------

Setup with:

.. code-block:: bash

    pip install -e .

Set environment variables:

.. code-block:: bash

    FLASK_APP=dummyweb
    SQLALCHEMY_DATABASE_URI=sqlite:////path/to/database.db"
    DUMMY_ACCOUNT_DIR=/path/to/accounts_directory


Run the server with:

.. code-block:: bash

    python -m flask run
	
Installation for Windows
------------

install Python (python-3.7.0) ;

make a virtual environment from windows cmd :

.. code-block:: bash

	>pip install virtualenvwrapper-win
	>mkvirtualenv dummyweb

“Envs” folder has been created in your personal user’s folder with your new virtual environment.

For deactivate it:

.. code-block:: bash

	>deactivate

For activate it:
	
.. code-block:: bash

	>workon dummyweb

Activate the virtual environment

Clone our project https://github.com/dummymeuporg/dummyweb.git

Install the project in editable mode (i.e. setuptools "develop mode")

.. code-block:: bash

	\Git\dummyweb>pip install -e .


Make a db with python cmd

.. code-block:: bash

	Git\dummyweb>python
	>>> from dummyweb import db
	>>> db.create_all()
	ctrl + z (for leave python cmd)
	cmd \Git\dummyweb>dir

you have to see test.db

Connect test.db to our virtual environment:
open Envs\dummyweb\Scripts\activate.bat with a text editor
add this lines at the end:

.. code-block:: bash

	set "FLASK_APP=dummyweb"
	set "SQLALCHEMY_DATABASE_URI=sqlite:///D:\\Git\\dummyweb\\test.db"
	set "DUMMY_ACCOUNT_DIR=%USERPROFILE%\\dummyaccounts"


Run the server with:

.. code-block:: bash

	>python -m flask run

From the browser try to access:
http://127.0.0.1:5000

If it’s work well played!
