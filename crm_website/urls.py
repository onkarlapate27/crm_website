from django.urls import path
from .views import user_view, home_view

urlpatterns = [
    path('', view=home_view.home, name='home'),
    path('login/', view=user_view.login_user, name='login'),
    path('logout/', view=user_view.logout_user, name='logout'),
    path('register/', view=user_view.register_user, name='register'),
]