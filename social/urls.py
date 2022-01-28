from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import *

from app import views
from app.api.api import RegisterUser, StatusView, UserView



 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('logout/', views.Logout, name='logout'),
    path('check/<str:user>/', views.check_username, name='check'),
    path('follow/<int:id>/', views.follow, name='follow'),
    path('unfollow/<int:id>/', views.unfollow, name='unfollow'),
    path('feeds/', views.feed, name="feeds"),
    path('post_status/', views.post_status, name='post_status'),
    path('update/', views.update_profile, name='update'),
    
    path('api/', include([
        path('userview/', UserView.as_view()),
        path('register/', RegisterUser.as_view()),
        path('status/', StatusView.as_view()),
        
    ]))
    ,   
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'app.error_handling.bad_request'
handler403 = 'app.error_handling.permission_denied'
handler404 = 'app.error_handling.page_not_found'
handler500 = 'app.error_handling.server_error'