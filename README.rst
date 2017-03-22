Hello World App
================

Dev
----

- prepare:

  ::

    $ python3 -m venv .venv
    
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    $ pip install -r test_requirements.txt

- Run:

  :: 

    $ python main.py
    $ PYTHONPATH=. FLASK_APP=hello_world flask run

- Tests:

  ::

    $ PYTHONPATH=. py.test
    $ PYTHONPATH=. py.test  --verbose -s
