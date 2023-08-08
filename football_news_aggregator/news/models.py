from django.db import models


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'accounts.FootballNewsUser',
        on_delete=models.CASCADE,
        related_name='authored_articles',
    )

    def __str__(self):
        return self.title


class NewsSource(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    description = models.TextField()
    article = models.ForeignKey(
        NewsArticle,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class NewsCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    article = models.ForeignKey(
        NewsArticle,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
