from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet,CreateUserView,TaskListView,TaskDatailView,PostListView,PostDetailView



router =routers.DefaultRouter()
router.register('tasks',TaskViewSet,basename='tasks')

urlpatterns=[
    path('list-post/',PostListView.as_view(),name='list-post'),
    path('detail-post/<str:pk>/',PostListView.as_view(),name='detail-post'),

    path('list-task/',PostListView.as_view(),name='list-task'),
    path('detail-task/<str:pk>/',PostListView.as_view(),name='detail-task'),
    path('register/',CreateUserView.as_view(),name='register'),

    #JWTトークンを取得してくれるパス
    path('auth/',include('djoser.urls.jwt')),
    path('',include(router.urls))
]