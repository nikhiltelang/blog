from django.contrib import admin

# Register your models here.
from . models import contact,customer,Blog, BlogComment , userprofile
from .models import Following , Liked
admin.site.register(contact)
admin.site.register(customer)
# admin.site.register(Blog)
admin.site.register((Blog,BlogComment))
admin.site.register(userprofile)
admin.site.register(Following)
admin.site.register(Liked)