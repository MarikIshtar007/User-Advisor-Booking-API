from django.urls import path, include

from users import views


urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('register/', views.UserRegisterApiView.as_view()),
]
