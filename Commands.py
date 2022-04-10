import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsPaper.settings")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsPaper.settings")
# os.environ.setdefault("TEAMVAULT_CONFIG_FILE", "/etc/teamvault.cfg")

import django
django.setup()


from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment


import random


def todo():
    # Команда для входа в Django Shell (python3 manage.py shell)
    # from news.models import *
    # удалять объекты
    User.objects.all().delete()
    Category.objects.all().delete()

    # создание пользователей
    jack_user = User.objects.create_user(username='jack', email='jack@mail.ru', password='jack_password')
    richard_user = User.objects.create_user(username='richard', email='richard@mail.ru', password='richard_password')

    # создание объектов авторов
    jack = Author.objects.create(user=jack_user)
    richard = Author.objects.create(user=richard_user)

    # создание категорий
    cat_games = Category.objects.create(name="Игры")
    cat_music = Category.objects.create(name="Музыка")
    cat_cinema = Category.objects.create(name="Кино")
    cat_IT = Category.objects.create(name="IT")

    # создание текстов статей/новостей
    text_article_games_cinema = """статья_игры_кино_Джека__статья_игры_кино_Джека__статья_игры_кино_Джека_
                                   _статья_игры_кино_Джека__статья_игры_кино_Джека__"""

    text_article_music = """статья_музыка_Ричарда__статья_музыка_Ричарда__статья_музыка_Ричарда_
                            _статья_музыка_Ричарда__статья_музыка_Ричарда__"""

    text_news_IT = """новость_IT_Ричарда__новость_IT_Ричарда__новость_IT_Ричарда__новость_IT_Ричарда__
                    новость_IT_Ричарда__новость_IT_Ричарда__новость_IT_Ричарда__новость_IT_Ричарда__"""

    # создание двух статей и новости
    article_jack = Post.objects.create(author=jack, post_type=Post.article, title="статья_игры_кино_Джека",
                                        text=text_article_games_cinema)
    article_richard = Post.objects.create(author=richard, post_type=Post.article, title="статья_музыка_Ричарда",
                                        text=text_article_music)
    news_richard = Post.objects.create(author=richard, post_type=Post.news, title="новость_IT_Ричарда", text=text_news_IT)

    # присваивание категорий этим объектам
    PostCategory.objects.create(post=article_jack, category=cat_games)
    PostCategory.objects.create(post=article_jack, category=cat_cinema)
    PostCategory.objects.create(post=article_richard, category=cat_music)
    PostCategory.objects.create(post=news_richard, category=cat_IT)

    # создание комментариев
    comment1 = Comment.objects.create(post=article_jack, user=richard.user, text="коммент Ричарда №1 к статье Джека")
    comment2 = Comment.objects.create(post=article_richard, user=jack.user, text="коммент Джека №2 к статье Ричарда")
    comment3 = Comment.objects.create(post=news_richard, user=richard.user, text="коммент Ричарда №3 к новости Ричарда")
    comment4 = Comment.objects.create(post=news_richard, user=jack.user, text="коммент Джека №4 к новости Ричарда")

    # список всех объектов, которые можно лайкать
    list_for_like = [article_jack,
                     article_richard,
                     news_richard,
                     comment1,
                     comment2,
                     comment3,
                     comment4]

    # 100 рандомных лайков/дислайков (по четности счетчика)
    for i in range(100):
        random_obj = random.choice(list_for_like)
        if i % 2:
            random_obj.like()
        else:
            random_obj.dislike()

    # подсчет рейтинга Джека
    rating_jack = (sum([post.rating * 3 for post in Post.objects.filter(author=jack)])
                    + sum([comment.rating for comment in Comment.objects.filter(user=jack.user)])
                    + sum([comment.rating for comment in Comment.objects.filter(post__author=jack)]))
    jack.update_rating(rating_jack)  # и обновление

    # подсчет рейтинга Ричарда
    rating_richard = (sum([post.rating * 3 for post in Post.objects.filter(author=richard)])
                    + sum([comment.rating for comment in Comment.objects.filter(user=richard.user)])
                    + sum([comment.rating for comment in Comment.objects.filter(post__author=richard)]))
    richard.update_rating(rating_richard)  # и обновление

    # лучший автор
    best_author = Author.objects.all().order_by('-rating')[0]

    print("Лучший автор")
    print("username:", best_author.user.username)
    print("Рейтинг:", best_author.rating)
    print("")

    # лучшая статья
    best_article = Post.objects.filter(post_type=Post.article).order_by('-rating')[0]
    print("Лучшая статья")
    print("Дата:", best_article.created)
    print("Автор:", best_article.author.user.username)
    print("Рейтинг:", best_article.rating)
    print("Заголовок:", best_article.title)
    print("Превью:", best_article.preview())
    print("")

    # печать комментариев к ней
    print("Комментарии к ней")
    for comment in Comment.objects.filter(post=best_article):
        print("Дата:", comment.created)
        print("Автор:", comment.user.username)
        print("Рейтинг:", comment.rating)
        print("Комментарий:", comment.text)
        print("")