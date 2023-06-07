from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(
        self,
        username,
        first_name,
        last_name,
        email,
        password,
        **extrafields,
    ):
        if not username:
            raise ValueError(_("Users must have a username"))
        if not first_name:
            raise ValueError(_("Users must have a first_name"))
        if not last_name:
            raise ValueError(_("Users must have a last_name"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("BaseUserManager: email address is required"))

        user = self.model(
            username,
            first_name,
            last_name,
            **extrafields,
        )
        user.set_password(password)
        extrafields.setdefault("is_staff", False)
        extrafields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        username,
        first_name,
        last_name,
        email,
        password,
        **extrafields,
    ):
        extrafields.setdefault("is_staff", True)
        extrafields.setdefault("is_superuser", True)
        extrafields.setdefault("is_active", True)

        if extrafields.get("is_staff") is not True:
            raise ValueError(_("super_User must have is_staff=True "))

        if extrafields.get("is_superuser") is not True:
            raise ValueError(_("super_User must have is_superuser=True "))

        if not password:
            raise ValueError(_("Super_User must have a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("SuperUser Manager: a valid email address is required"))

        user = self.create_user(
            username, first_name, last_name, email, password, **extrafields
        )
        user.save(using=self._db)
        return user
