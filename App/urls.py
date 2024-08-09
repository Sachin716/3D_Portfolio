from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("" , Home , name="Home" ),
    path("Log" , login_page , name="login"),
    path('admin_home' , admin_page , name="admin"),
    path('admin_items/<str:category_item>' , Admin_Multiple_items , name="Categories"),
    path('edit_item/<int:id>', Admin_Single_item , name="item" ),
    path('Register' , register_user , name="Register")
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)