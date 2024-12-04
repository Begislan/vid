from django.urls import path, include
from .views import (
    adminka_view, feedback_list,
    user_create, user_delete, user_list, user_detail, user_update,
    video_update, video_create, video_delete, video_detail, cat_list,
    cat_detail, cat_update, cat_delete, cat_create
)

urlpatterns = [
    path('', adminka_view, name='adminka'),
    path('video_create/', video_create, name='video_create'),
    path('video/<int:id>/', video_detail, name='video_detail'),
    path('video_update/<int:id>', video_update, name='video_update'),
    path('video_delete/<int:id>', video_delete, name='video_delete'),

    path('user_list/', user_list, name='user_list'),
    path('user_create/', user_create, name='user_create'),
    path('user_detail/<int:id>/', user_detail, name='user_admin_detail'),
    path('user_update/<int:id>/', user_update, name='user_admin_update'),
    path('user_delete/<int:id>/', user_delete, name='user_admin_delete'),

    path('feedback/', feedback_list, name='feedback_list'),

    path('cat_list/', cat_list, name='cat_list'),
    path('cat_detail/<int:id>/', cat_detail, name='cat_detail'),
    path('cat_update/<int:id>/', cat_update, name='cat_update'),
    path('cat_delete/<int:id>/', cat_delete, name='cat_delete'),
    path('cat_create/', cat_create, name='cat_create'),
]
