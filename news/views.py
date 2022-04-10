from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
# импортируем класс, который говорит нам о том, что в этом представлении
# мы будем выводить список объектов из БД
from .models import Post, Category
from django.shortcuts import render
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import ProductForm

class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'post.html'
# указываем имя шаблона, где будет лежать HTML, в котором будут все инструкции о том,
    # как именно пользователю должны вывестись наши объекты
    context_object_name = 'post'
# это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться
    # к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')

    ordering = ['title']
    paginate_by = 1


class PostsList2(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'
# указываем имя шаблона, где будет лежать HTML, в котором будут все инструкции о том,
    # как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'
# это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться
    # к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')
    paginate_by = 1
    ordering = ['title']


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        return context

class PostsList3(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'post3.html'
# указываем имя шаблона, где будет лежать HTML, в котором будут все инструкции о том,
    # как именно пользователю должны вывестись наши объекты
    context_object_name = 'post3'
# это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться
    # к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')
    paginate_by = 1
    ordering = ['title']


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        return context



class PostDetailView(DetailView):
    template_name = 'flatpages/post_detail.html'
    queryset = Post.objects.all()

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните.
# Остальное он сделает за вас
class PostCreateView(CreateView):
    template_name = 'flatpages/post_create.html'
    form_class = ProductForm


class PostUpdateView(UpdateView):
    template_name = 'flatpages/post_create.html'
    form_class = ProductForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте,
    # который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'flatpages/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'