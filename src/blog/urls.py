from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('articles/<int:pk>/', views.article_details, name='details')
]