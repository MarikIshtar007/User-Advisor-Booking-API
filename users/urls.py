from django.urls import path, include

from users import views
from advisor import views as adv_views


urlpatterns = [
    path('user/login/', views.UserLoginApiView.as_view()),
    path('user/register/', views.UserRegisterApiView.as_view()),
    path('user/<user_id>/advisor/', adv_views.ShowAdvisors.as_view(),name='show-advisors'),
    path('user/<int:user_id>/advisor/<int:advisor_id>', adv_views.BookAdvisors.as_view(), name='book-advisors')

]
