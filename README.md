Using Celery with Flask For Picture Galerry
=======================

[Using Celery with Flask](http://celeryproject.org).

The application provides two examples of background tasks using Celery:

- Example 1 grab pictures asynchronously.
- Example 2 launches one or more asynchronous jobs and shows progress updates in the web page.

Here is a screenshot of this application:


Quick Setup
-----------

1. Clone this repository.
2. Create a virtualenv and install the requirements.
3. Open a second terminal window and start a local Redis server (if you are on Linux or Mac, execute `run-redis.sh` to install and launch a private copy).
celery --loglevel=info`.
4. Start the Flask application on your original terminal window: `flask run`.
5. Go to `http://localhost:5000/` and enjoy this application!


