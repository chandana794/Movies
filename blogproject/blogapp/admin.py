from django.contrib import admin
from blogapp.models import Post,Comments



class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title','author')}
admin.site.register(Post,PostAdmin)

class CommentsAdmin(admin.ModelAdmin):
  list_display=['name','email','post','body','created','updated','active']#can be tuple also
  list_filter=('active','created','updated')#on which basis filter should be applied those fileds we can mention here
  search_fields=('name','email','body')
admin.site.register(Comments,CommentsAdmin)











# Register your models here.
