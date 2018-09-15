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