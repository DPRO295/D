import pymongo
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.models import User

def login(request, username, password):
    user = User.objects.filter(username=username).first()
    if user is not None and user.check_password(password):
        s = SessionStore()
        s['user_id'] = str(user.id)
        s.create()
        request.session = s
        return True
    else:
        return False