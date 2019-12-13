from django.urls import path

from wall import views


app_name = 'wall'

urlpatterns = [
    path('list/', views.ListWallPostsView.as_view(), name='list'),
    path('create/', views.CreateWallPostsView.as_view(), name='create'),
]
