from django.urls import path
from .views import showPost, showPostById

app_name="blog"

urlpatterns = [
    path('', showPost, name='posts'),
    path('<int:post_id>', showPostById, name='post_detail'),

]