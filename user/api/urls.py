from django.urls import include, path
from .views import ListUsers ,RegisterUser ,Login


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('list-users', ListUsers.as_view(), name='list-users'),
    path('register', RegisterUser.as_view(), name='register-user'),
    path('login', Login.as_view(), name='login-user'),
    
]
