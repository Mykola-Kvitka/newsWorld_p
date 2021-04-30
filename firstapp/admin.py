from django.contrib import admin
from .models import News,News,Topic,Comment


admin.site.site_header = "KVISL"
admin.site.site_title = "KVISL Admin Portal"
admin.site.index_title = "Welcome to KVISL NEWS Portal"

class NewsAdmin(admin.ModelAdmin):
    list_filter = ('writer', 'date')
class TopicAdmin(admin.ModelAdmin):
    list_filter = ('tittle', 'creationDate')
class CommentAdmin(admin.ModelAdmin):   
    list_filter = ('authorName', 'dateTime')




admin.site.register(News,NewsAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Comment,CommentAdmin)
