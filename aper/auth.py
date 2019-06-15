from aper import login_manager
from .models import User


@login_manager.request_loader
def load_user(request):
    token = request.headers.get('Authorization')

    if token is not None:
        username, password = token.split(":")  # naive token
        print(username)
        user_entry = User.get(username)
        if (user_entry is not None):
            user = User(user_entry[0], user_entry[1])
            if (user.password == password):
                return user
    return None