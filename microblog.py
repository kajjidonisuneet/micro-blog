""" to define the Flask application instance """

from app import create_app, db, cli
from app.models import User, Post, Message, Notification, Task

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    ''' this function is added for the "flask shell" command to avoid importing all the required models every time while running python in interperter mode
    the return line maps the key to the object note: only the key will be availabe in the flask shell'''
    return {'db': db, 'User':User, 'Post':Post, 'message':Message, 'notification':Notification, 'task':Task}