
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path, include

from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
<<<<<<< HEAD
    path('home/', views.home2, name='home2'),
    path('logout/', views.user_logout, name='logout'),
=======
    path('home2/', views.home2, name='home2'),
    path('logout/', views.logout, name='logout'),
>>>>>>> origin/main
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
