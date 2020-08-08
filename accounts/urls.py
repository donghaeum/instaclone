from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('siginup/', signup, name='signup'),
    path('login/', login_check, name='login'),
    path('logout/', logout, name='logout'),
]