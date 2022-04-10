from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()

    def __str__(self):
        return f'{self.user}'

class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return f'{self.name.title()}'


class Post(models.Model):
    article = 'a'
    news = 'n'

    POST_TYPE = [
        (article, "Статья"),
        (news, "Новость")
    ]

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    post_type = models.CharField(max_length = 1, choices = POST_TYPE, default = article)
    created = models.DateTimeField(auto_now_add = True)
    cats = models.ManyToManyField(Category, through = 'PostCategory')
    title = models.CharField(max_length = 255)
    text = models.TextField()
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


    def __str__(self):
        return f'{self.title}: {self.text[:20]}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/posts/{self.id}'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()