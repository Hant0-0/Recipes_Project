from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    #Auth
    path('login/', views.loginuser, name='loginuser'),
    path('signin/', views.signinuser, name='signinuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    #Recipes
    path('current/', views.currentrecipes, name='currentrecipes'),
    path('create/', views.createrecipes, name="createrecipes"),
    path('viewsrecipes/<int:rec_pk>', views.viewsrecipes, name="viewsrecipes"),
    path('delete/<int:rec_pk>', views.deleterecipes, name="deleterecipes")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)