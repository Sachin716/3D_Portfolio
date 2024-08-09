from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("" , Home , name="Home" ),
    path("Log" , login_page , name="login"),
    path('admin_home' , admin_page , name="admin"),
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)