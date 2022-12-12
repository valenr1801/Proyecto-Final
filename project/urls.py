"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import index
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, monstrar_familiares, 
                            BuscarFamiliar, AltaFamiliar, 
                            ActualizarFamiliar, BorrarFamiliar)
urlpatterns = [
      path('admin/', admin.site.urls),
      path('saludar/', index),
      path('mi-familia/', monstrar_familiares), # nueva vista
      path('mi-familia/buscar', BuscarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
      path('mi-familia/alta', AltaFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
      path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()) ,
      path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view())
       ]
