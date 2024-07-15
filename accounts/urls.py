from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.view_login, name='login'),
    path('logout/', views.logout_view, name='logout')
]
