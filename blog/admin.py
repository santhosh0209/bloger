from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('no', 'category')  
    list_filter = ( 'category_filter','category_filter2') 


admin.site.register(Post,PostAdmin)  

