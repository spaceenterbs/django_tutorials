from django.urls import path
from .views import UserNameFeeds

urlpatterns = [
    path("<str:username>", UserNameFeeds.as_view()),  # 특정 유저가 작성한 게시글만 가져옴
]
