from django.db import models


class NewsArticle(models.Model):
    TOPICS = (
        ('Transfers', 'Transfers'),
        ('Breaking News', 'Breaking News'),
        ('Announcement', 'Announcement'),
        ('Results', 'Results'),
        ('Fixture', 'Fixture'),
        ('Other', 'Other'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    topic = models.CharField(max_length=200, blank=True, null=True, choices=TOPICS)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_text = models.TextField(max_length=300, blank=False, null=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE,)


