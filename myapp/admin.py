from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Maintenance)
admin.site.register(Suggestion)