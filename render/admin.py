from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Journal)
admin.site.register(Todo)
admin.site.register(Journal_Prompts)
admin.site.register(BlogPost)
admin.site.register(YoutubeContent)