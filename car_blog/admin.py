from django.contrib import admin

# Register your models here.
from car_blog.models import Color, Transmission, Body_type, Brend

admin.site.register(Color)
admin.site.register(Transmission)
admin.site.register(Body_type)
admin.site.register(Brend)
