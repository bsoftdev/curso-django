from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.show_posts, name='posts'),
    path('post/<int:post_id>/', views.single_post,name='single_post')
]
