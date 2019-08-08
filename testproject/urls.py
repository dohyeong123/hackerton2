from django.contrib import admin
from django.urls import path, include
import testapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', testapp.views.home, name='home'),
    path('login/', testapp.views.login, name='login'),
    path('logout/', testapp.views.logout, name='logout'),
    path('signup/', testapp.views.signup, name='signup'),
    path('cate_trend/', testapp.views.cate_trend, name='cate_trend'),
    path('accounts/', include('allauth.urls')),
]
