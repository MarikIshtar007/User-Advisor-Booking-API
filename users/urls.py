from django.urls import path, include

from users import views


urlpatterns = [
    path('user/login/', views.UserLoginApiView.as_view()),
    path('user/register/', views.UserRegisterApiView.as_view()),
    path('admin/advisor/', views.AdvisorAddView.as_view()),
]
