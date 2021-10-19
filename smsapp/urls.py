from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('new',views.new,name='new'),
    path('newlogin',views.fnnewlogin,name='newlogin'),
    path('newhome',views.fnnewhome,name='newhome'),
    path('grid',views.grid,name='grid'),
    path('home',views.fnhome,name='home'),
    path('about',views.fnabout,name='about'),
    path('new1',views.fnnew1,name='new1'),
    path('demo',views.fndemo,name='demo'),
    path('ajax',views.fnajax,name='ajax'),
    path('delete',views.fndelete,name='delete'),
    path('apidemo',views.fnapidemo,name='apidemo'),
    path('apidemoget',views.fnapidemoget,name='apidemoget'),
    path('apidemodelete/<int:id>/',views.fnapidemodelete,name='apidemodelete'),
    path('apidemoupdate/<int:id>/',views.fnapidemoupdate,name='apidemoupdate'),
    path('profile',views.fnprofile,name='profile'),
    path('register',views.fnregister,name='register'),
    path('display',views.display,name='display')

]
