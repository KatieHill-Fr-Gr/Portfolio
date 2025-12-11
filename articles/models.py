from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    summary = models.CharField(max_length=500)
    body = models.TextField()
    contributors = models.ManyToManyField(
        to='users.User',
        related_name='contributed_projects',
        blank=True
    )
    date_completed = models.DateField(
        blank=True,
        null=True
    )
    is_public = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name
    
class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=500)
    caption = models.CharField(max_length=200, blank=True, null=True)
    is_primary = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_primary', 'uploaded_at']

    def __str__(self):
        return f'Image for {self.article.name}'
