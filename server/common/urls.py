from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.EachUser.as_view()),
    path('message/', views.MessageSend.as_view()),
    path('signup/', views.signup),
]

urlpatterns = format_suffix_patterns(urlpatterns)
