import datetime
import calendar
import jwt
from helpers.constants import JWT_SECRET, JWT_ALGORITHM
from service.user_service import UserService
from flask import abort


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_by_username(username)

        if user is None:
            raise abort(401)

        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                abort(401)

        data = {
            'username': user.username,
            'role': user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=[JWT_ALGORITHM])

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=[JWT_ALGORITHM])

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, token_approve):
        data = jwt.decode(jwt=token_approve, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = data.get('username')

        return self.generate_tokens(username, None, is_refresh=True)
