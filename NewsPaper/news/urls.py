from django.urls import path
from .views import PostsList2, PostDetailView, PostCreateView, \
                    PostUpdateView, PostDeleteView,PostsList, PostsList3




urlpatterns = [ path('search/', PostsList2.as_view()),
                path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Ссылка на детали товара
                path('create/', PostCreateView.as_view(), name='post_create'),
                path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
                path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
                path('', PostsList.as_view()),
                path('post3/', PostsList3.as_view())
                ]