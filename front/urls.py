from django.urls import path
from .views import *

urlpatterns = [
    path('', front_core, name="core"),
    path('thank/', feedback_success, name="feedback_success"),
    path('videos/', full_videos, name='videos'),
    path('videos/<int:id>', video_details, name='video_details'),
    path('users/', users, name='users'),
    path('users/<int:id>/', user_detail, name='user_detail'),
    path('cats/', category_list, name='cats'),
    path('cats/<int:pk>/', category_details, name='category_details'),


]