from django.urls import path
from . import views



urlpatterns=[
    path('register', views.registration, name= 'registration')
    # path('user_login',views.registration, name= 'registration'),
    # path('register', views.add_user , name = 'add')  #2nd process
]

