from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crypto/<slug:slug>', get_by_slug, name='get_by_slug'),
    path('comments', get_comments, name='get_comments'),
    # path('comments/create', create_comment, name='create_comment'),
    path('comments/<int:comment_id>/', get_comment, name='get_comment'),
    path('comments/delete/<int:comment_id>', delete_comment, name='delete_comment'),
    path('comments/create', add_and_save, name='add_comment'),
    path('comments/save', add_and_save, name='add_save'),
    path('index_view', index_view, name='index_view'),
    path('index_view2', index_view2, name='index_view2'),
    path('index_view3', index_view3, name='index_view3'),
    path('detail/<int:id>/', detail, name='detail'),
    path('json/', json_response_view, name='json_response_view'),
    path('redirect/', redirect_view, name='redirect_view'),
    path('only_get/', only_get_view, name='only_get_view'),
]
