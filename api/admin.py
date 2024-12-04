from django.contrib import admin
from .models import programmer
# Register your models here.
#aqui se crea los modelos (las tablas o coleciones)
admin.site.register(programmer) #aca se registra el modelo para poder ver lo en el panel de administracion
