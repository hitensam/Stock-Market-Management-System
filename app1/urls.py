from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'app1'

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup'),
    path('',RedirectView.as_view(url='user')),
    path('user/', views.User, name='user'),
    path('stocks/', views.stock, name='stock'),
    path('addStock/', views.addStock, name='addStock'),
    path('logout/', views.logout, name='logout')
]