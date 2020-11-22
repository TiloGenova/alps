from django.contrib import admin
from .models import Activity
from .models import Contact



# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('category',)


admin.site.register(Activity)
admin.site.register(Contact)
