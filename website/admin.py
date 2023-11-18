from django.contrib import admin
from .models import Record

# Register your models here.

# show only firstname and lastname (check models.py def __str__)
# admin.site.register(Record)


# showing depend list display
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'address', 'created_at']
