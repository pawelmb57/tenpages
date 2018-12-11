from django.contrib import admin
from main.models import Books, UserBooks, LogPages, Activity, Profile

admin.site.register(Books)
admin.site.register(UserBooks)
admin.site.register(LogPages)
admin.site.register(Activity)
admin.site.register(Profile)
