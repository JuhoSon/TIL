from django.db import models

class Article(models.Model):
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#charfield
    title = models.CharField(max_length=10)
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#textfield
    content = models.TextField()
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#datetimefield
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<게시글 제목: {self.title} / 게시글 내용: {self.content}'