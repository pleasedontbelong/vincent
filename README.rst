Vincent
=======

Website for movie recomendations

Installation
============

Ubuntu ::

    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:pitti/postgresql
    sudo apt-get update
    sudo apt-get install postgresql-server-dev-9.2
    sudo add-apt-repository ppa:rwky/redis
    sudo apt-get update
    sudo apt-get install redis-server
    sudo apt-get install git-core


Python dependencies installation
--------------------------------

::

    pip install -r requirements/development.txt


Database installation
---------------------

Then synchronize ::

    python manage.py syncdb
