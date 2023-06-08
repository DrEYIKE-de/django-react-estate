from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampUUIDModel
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Gender(models.TextChoices):
    Male = "Male", _("Male")
    Female = "Female", _("Female")
    Other = "Other", _("Other")


class Profile(TimeStampUUIDModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"),
        max_length=30,
        default="+237690407052",
    )
    about_me = models.TextField(
        verbose_name=_("About Me"),
        default="Tells us more about you",
    )
    license = models.CharField(
        verbose_name=_("Real estate license"),
        max_length=255,
        blank=True,
        null=True,
    )
    gender = models.CharField(
        verbose_name=_("gender of user"),
        max_length=20,
        choices=Gender.choices,
        default=Gender.Other,
    )
    profile_photo = models.ImageField(
        verbose_name=_(" user avatar"), default="/profile.png"
    )
    country = CountryField(
        default="CMR",
        verbose_name=_("User Country"),
        help_text=_("the country of this user"),
    )
    city = models.CharField(
        max_length=200,
        verbose_name=_("city of the user"),
        default="Douala",
    )
    is_buyer = models.CharField(
        default=False,
        verbose_name=_("Buyer"),
        help_text=_("Are you looking for buying houses"),
    )
    is_agent = models.BooleanField(
        default=False,
        verbose_name=_("Agent"),
        help_text=_("Are you looking for selling houses"),
    )
    top_agent = models.BooleanField(
        default=False, verbose_name=_("Top Agent"), help_text=_("Are you a top agent")
    )
    ratings = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    num_reviews = models.IntegerField(verbose_name=_("number of reviews"), default=0)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return f"{self.user.username} 's profile"
