from django.forms import ModelForm, BooleanField
from .models import Post


# Создаём модельную форму
class ProductForm(ModelForm):
    check_box = BooleanField(label='Подтвердить')
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'cats', 'check_box']