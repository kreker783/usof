from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Username must be set")
        user = self.model(login=username,
                          email=extra_fields.get("email"),
                          full_name=extra_fields.get("full_name"),
                          picture=extra_fields.get("picture"),
                          raiting=extra_fields.get("rating"))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Admin must have is_staff=True.")

        return self.create_user(username, password, **extra_fields)
