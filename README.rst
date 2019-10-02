DummyWeb
========

Dummy Meuporg web frontend.

Installation for Linux
----------------------

Setup with:

.. code-block:: bash

    pip install -e .


Create a directory which will contain all the accounts' data. Assume this
directory will be ``/path/to/accounts_directory`` here. This path will be
the value of the ``DUMMY_ACCOUNT_DIR`` environment variable.

Set environment variables:

.. code-block:: bash

    FLASK_APP=dummyweb
    SQLALCHEMY_DATABASE_URI=sqlite:////path/to/database.db
    DUMMY_ACCOUNT_DIR=/path/to/accounts_directory


Run the server with:

.. code-block:: bash

    python -m flask run
	
Installation for Windows
------------------------

install Python (python-3.7.0) ;

make a virtual environment from windows cmd :

.. code-block:: bash

	pip install virtualenvwrapper-win
	mkvirtualenv dummyweb

"Envs" folder has been created in your personal user's folder with your new
virtual environment.

In order to deactivate it:

.. code-block:: bash

	deactivate

In order to activate it:
	
.. code-block:: bash

	workon dummyweb

Activate the virtual environment

Clone our project https://github.com/dummymeuporg/dummyweb.git

Install the project in editable mode (i.e. setuptools "develop mode")

.. code-block:: bash

	pip install -e .
    
Create a directory which will contain all the accounts' data. Assume this
directory will be ``%USERPROFILE%\\dummyaccounts`` here (where %USERPROFILE%
refers to your home directory on Windows, e.g. C:\Users\Geoffrey). This path will
be the value of the ``DUMMY_ACCOUNT_DIR`` environment variable.
    
Set the following environment variables:


.. code-block:: bash

	set "FLASK_APP=dummyweb"
	set "SQLALCHEMY_DATABASE_URI=sqlite:///D:\\Git\\dummyweb\\test.db"
	set "DUMMY_ACCOUNT_DIR=%USERPROFILE%\\dummyaccounts"


Make a db with python cmd

.. code-block:: bash

	dummyctl create-bd

Now you should have a ``test.db`` file created at the root directory.

Run the server with:

.. code-block:: bash

	python -m flask run

From the browser try to access:
http://127.0.0.1:5000

If it works, well played!
