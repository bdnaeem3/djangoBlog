from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    publish_date = models.DateField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='blogImages', null=True)

    def __str__(self):
        return self.title

# CRUD = Create Read Update Delete
# Image, Title, User, Publish Date, Content, Slug, Comment
