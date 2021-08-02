from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import TaskSerializer,UserSerializer,PostSerializer
from .models import Task,Post


# ユーザー作成用のエンドポイント
class CreateUserView(generics.CreateAPIView):
    serializer_class =UserSerializer
    #　新しくユーザーができるタイミングはユーザーが存在しないのでJWTは誰でもアクセスできるようにしている
    permission_classes =(AllowAny,)



#ブログの投稿データのエンドポイント
class PostListView(generics.ListAPIView):
    queryset =Post.objects.all()
    serializer_class =PostSerializer
    permission_classes =(AllowAny,)


# 特定のブログのデータを取得するためのエンドポイント
class PostDetailView(generics.RetrieveAPIView):
    queryset =Post.objects.all()
    serializer_class =PostSerializer
    permission_classes =(AllowAny,)


class TaskListView(generics.ListAPIView):
    queryset =Task.objects.all()
    serializer_class =TaskSerializer
    permission_classes =(AllowAny,)


class TaskDatailView(generics.RetrieveAPIView):
    queryset =Task.objects.all()
    serializer_class =TaskSerializer
    permission_classes =(AllowAny,)

#　taskの新規作成購入のやつ
class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class =TaskSerializer