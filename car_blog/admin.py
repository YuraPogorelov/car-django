from django.contrib import admin

# Register your models here.

from car_blog.models import Transmission, Body_type, Brend, Engine, Characteristics

admin.site.register(Transmission)
admin.site.register(Body_type)
admin.site.register(Brend)
admin.site.register(Engine)
admin.site.register(Characteristics)
