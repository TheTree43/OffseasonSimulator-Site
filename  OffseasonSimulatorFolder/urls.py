

from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('', views.home, name='home' ),
    path('about', views.about, name='about' ),
    path('Packers', views.Packers, name='Packers' ),
    path('Bears', views.Bears, name='Bears' ),
    path('Vikings', views.Vikings, name='Vikings' ),
    path('Lions', views.Lions, name='Lions' ),

]
