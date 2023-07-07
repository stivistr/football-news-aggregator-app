from django.contrib import admin
from football_news_aggregator.accounts.models import FootballNewsUser, Profile


@admin.register(FootballNewsUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_superuser')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
