

from django.contrib import admin
from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static
import flowchart.views
import thumbnail.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home' ),
    path('simulator', views.simulator, name='simulator' ),

    path('about', thumbnail.views.about, name='about' ),

    path('Packers', flowchart.views.Packers, name='Packers' ),
    path('Bears', flowchart.views.Bears, name='Bears' ),
    path('Vikings', flowchart.views.Vikings, name='Vikings' ),
    path('Lions', flowchart.views.Lions, name='Lions' ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
