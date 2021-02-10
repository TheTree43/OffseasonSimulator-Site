

from django.contrib import admin
from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('about', views.about, name='about' ),
    path('Packers', views.Packers, name='Packers' ),
    path('Bears', views.Bears, name='Bears' ),
    path('Vikings', views.Vikings, name='Vikings' ),
    path('Lions', views.Lions, name='Lions' )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
