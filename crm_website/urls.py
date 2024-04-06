from django.urls import path
from .views import user_view, home_view, customers_view

urlpatterns = [
    path('', view=home_view.home, name='home'),
    path('login/', view=user_view.login_user, name='login'),
    path('logout/', view=user_view.logout_user, name='logout'),
    path('register/', view=user_view.register_user, name='register'),
    path('customers/', view=customers_view.list_customers, name='customers'),
    path('customers/add/', view=customers_view.add_customer, name='add'),
    path('customers/update/<int:customer_id>', view=customers_view.update_customer, name='update'),
    path('customers/delete/<int:customer_id>', view=customers_view.delete_customer, name='delete'),
]