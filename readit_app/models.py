from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    category = models.CharField(max_length=70)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=70)

    def __str__(self):
        return self.tag


class Article(Timestamp):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/')
    content = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)

    def get_absolute_url(self):
        return reverse("readit:article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(Timestamp):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='article/comment_author', null=True, blank=True)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.author.username

