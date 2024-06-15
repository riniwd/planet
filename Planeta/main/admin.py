from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Articles)
admin.site.register(Data)
admin.site.register(TimeTable)
admin.site.register(Gallery)

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель планетария СГУГиТ'
