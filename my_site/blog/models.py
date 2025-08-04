from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.caption}'


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.TextField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='posts')
    image_name = models.CharField(max_length=20, null=True, blank=True)
    publication_date = models.DateField(auto_now_add=True, auto_now=False)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True, primary_key=True)
    content = models.TextField(blank=True)
    tag = models.ManyToManyField(Tag, null=False)

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

