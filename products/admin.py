from django.contrib import admin

from .models import Product, Comment


class CommentsInline(admin.StackedInline):
    model = Comment
    fields = ['author', 'active', 'body', 'starts',]
    extra = 1


# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'datetime_created', 'active',]

    inlines = [
        CommentsInline,
    ]


# admin.site.register(Comment)
@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['author', 'product','datetime_created', 'active', 'body', 'starts']

