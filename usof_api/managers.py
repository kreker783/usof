from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Username must be set")
        user = self.model(login=username, **extra_fields)
        user.set_password(password)
        user.full_name = extra_fields.get("full_name")
        user.email = extra_fields.get("email")
        user.picture = extra_fields.get("picture")
        user.rating = extra_fields.get("rating")
        user.save()
        return user

    def create_admin(self, username, password, **extra_fileds):
        extra_fileds.setdefault("is_superuser", True)
        if extra_fileds.get("is_superuser") is not True:
            raise ValueError("Admin must have is_superuser=True.")
        return self.create_user(username, password, **extra_fileds)
