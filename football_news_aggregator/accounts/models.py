from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models, get_user_model
from django_countries.fields import CountryField
from football_news_aggregator.news.models import NewsArticle
from football_news_aggregator.common.validators import NameContainsOnlyLettersValidator, FirstCharMustBeLetterValidator
from football_news_aggregator.accounts.managers import FootballUserManager

UserModel = get_user_model()


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
        validators=[(MinLengthValidator(FIRST_NAME_MIN_LENGTH),
                     FirstCharMustBeLetterValidator,
                     NameContainsOnlyLettersValidator)]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[(MinLengthValidator(LAST_NAME_MIN_LENGTH),
                     FirstCharMustBeLetterValidator,
                     NameContainsOnlyLettersValidator)]
    )

    email = models.EmailField(
        null=True,
        blank=True,
        unique=True,
    )

    profile_picture = models.ImageField()

    country = CountryField()

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Bookmark(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    news_article = models.ForeignKey(
        NewsArticle,
        on_delete=models.CASCADE,
    )

    timestamp = models.DateTimeField(auto_now_add=True)
