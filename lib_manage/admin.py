from django.contrib import admin
from .models import Books, Member, Transaction

# Register your models here.

admin.site.register(Member)
admin.site.register(Books)
admin.site.register(Transaction)
