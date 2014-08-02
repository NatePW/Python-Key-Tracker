from django.contrib import admin
from Keys.models import Key, Checkout, People

# Register your models here.
admin.site.register(Key)
admin.site.register(Checkout)
admin.site.register(People)