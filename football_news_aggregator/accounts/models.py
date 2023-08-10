from django.core.validators import MinLengthValidator
from django_countries.fields import CountryField
from football_news_aggregator.accounts.managers import FootballUserManager
from football_news_aggregator.common.validators import validate_only_letters
from django.db import models
from django.contrib.auth import models as auth_models


class FootballNewsUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = 'username'
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = FootballUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 3
    LAST_NAME_MIN_LENGTH = 3
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LENGTH),
                    validate_only_letters),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(LAST_NAME_MIN_LENGTH),
                    validate_only_letters),
    )

    email = models.EmailField(
        null=True,
        blank=True,
        unique=True,
    )

    country = CountryField()

    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='pictures/',
    )

    favourite_team = models.CharField(
        max_length=30,
        validators=(MinLengthValidator(2),
                    ))

    user = models.OneToOneField(
        FootballNewsUser,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def delete(self, *args, **kwargs):
        self.user.delete()
        super().delete(*args, **kwargs)


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        FootballNewsUser,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    user = models.ForeignKey(
        FootballNewsUser,
        on_delete=models.CASCADE,
    )

    timestamp = models.DateTimeField(auto_now_add=True)
