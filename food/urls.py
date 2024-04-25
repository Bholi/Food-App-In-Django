from django.urls import path
from .views import *
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/',item_detail,name='detail'),
    path('add/',add_item,name='add'),
    path('edit/<int:pk>/',edit,name='edit'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('register/',register,name='register'),
    path('login/',views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',logout_view,name='logout'),
    path('profiel/',profile,name='profile'),
]

urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

