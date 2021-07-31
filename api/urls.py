from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>', views.QuestionDetail.as_view()),

    path('questions/comments/', views.QuestionCommentList.as_view()),
    path('questions/comments/<int:pk>', views.QuestionCommentDetail.as_view()),

    path('questions/answers/', views.AnswerList.as_view()),
    path('questions/answers/<int:pk>', views.AnswerDetail.as_view()),

    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>', views.TagDetail.as_view())
]