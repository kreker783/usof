from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Username must be set")
        user = self.model(login=username,
                          email=extra_fields.get("email"),
                          full_name=extra_fields.get("full_name"),
                          picture=extra_fields.get("picture"),
                          rating=extra_fields.get("rating"))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(username, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
