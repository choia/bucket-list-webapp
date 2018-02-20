from django.contrib import admin
from .models import Post, Category


admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'category')

admin.site.register(Post, PostAdmin)