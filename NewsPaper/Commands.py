import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsPaper.settings")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsPaper.settings")
# os.environ.setdefault("TEAMVAULT_CONFIG_FILE", "/etc/teamvault.cfg")

import django
django.setup()


from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment


import random


