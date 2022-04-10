from portal.models import *
from django.contrib.auth.models import User

# Создать двух пользователей (с помощью метода User.objects.create_user('username')).
# Создать два объекта модели Author, связанные с пользователями.
# python3 manage.py shell
# from news.models import *

victor_user = User.objects.create_user('victor')
jack_user = User.objects.create_user('jack')

victor = Author.objects.create(user=victor_user)
jack = Author.objects.create(user=jack_user)

# Добавить 4 категории в модель Category.

cat_anime = Category.objects.create(name='Аниме')
cat_kino = Category.objects.create(name='Кино')
cat_music = Category.objects.create(name='Музыка')
cat_game = Category.objects.create(name='Игры')

# Добавить 2 статьи и 1 новость.

text1 = "Статья про аниме и кино"
text2 = "Статья про музыку"
text3 = "Новости про игры"

a1 = Post.objects.create(author=victor, post_type=Post.article, title="Статья1", text=text1)
a2 = Post.objects.create(author=victor, post_type=Post.article, title="Статья2", text=text2)
a3 = Post.objects.create(author=jack, post_type=Post.news, title="Новости", text=text3)

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

PostCategory.objects.create(post = a1, category = cat_anime)
PostCategory.objects.create(post = a1, category = cat_kino)
PostCategory.objects.create(post = a2, category = cat_music)
PostCategory.objects.create(post = a3, category = cat_game)

# Создать как минимум 4 комментария к разным объектам модели Post
# (в каждом объекте должен быть как минимум один комментарий).

comment1 = Comment.objects.create(post = a1, user = victor.user, text = "Комментарий1")
comment2 = Comment.objects.create(post = a2, user = victor.user, text = "Комментарий2")
comment3 = Comment.objects.create(post = a3, user = jack.user, text = "Комментарий3")
comment4 = Comment.objects.create(post = a1, user = jack.user, text = "Комментарий4")

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.

comment1.like()
comment2.like()
comment2.like()
comment3.dislike()

# Обновить рейтинги пользователей.

victor.update_rating()
jack.update_rating()
jack.update_rating()
