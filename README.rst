DummyWeb
========

Dummy Meuporg web frontend

Installation
------------

Setup with:

.. code-block:: bash

    pip install -e .

Set environment variables:

.. code-block:: bash

    FLASK_APP=dummyweb
    SQLALCHEMY_DATABASE_URI=sqlite:////path/to/database.db"


Run the server with:

.. code-block:: bash

    FLASK_APP=dummyweb python -m flask run