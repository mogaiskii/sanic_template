from db.models import User
from library.auth import get_password_hash, generate_user_tokens
from library.db.manager import Manager


class UsersManager(Manager):
    __model__ = User

    def set_user_password_hash(self, user: User, password: str) -> User:
        """
        sets User `password_hash` field value as a hashed password
        NOTE: this function does not flush user to database, just sets value to entity
        """
        user.password_hash = get_password_hash(self._settings.PASSWORD_SALT, password)
        return user

    async def get_auth_user(self, login: str, password: str) -> User:
        password_hash = get_password_hash(self._settings.PASSWORD_SALT, password)

        return await self.get_exact_one(User.login==login, User.password_hash==password_hash)

    def create_tokens(self, user):
        tokens = generate_user_tokens(
            user.id, self._settings.JWT_SECRET, self._settings.TOKEN_LIFESPAN_SEC, self._settings.REFRESH_LIFESPAN_SEC
        )
        return tokens
