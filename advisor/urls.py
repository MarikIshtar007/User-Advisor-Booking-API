from django.urls import path, include

from advisor import views


urlpatterns = [
    path('', views.AdvisorAddView.as_view())
]
