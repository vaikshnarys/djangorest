from django.contrib import admin
from .models import Workservis,Category


@admin.register(Workservis)
class WorkservisAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_at'
    fields = ['title','description','is_published','cat','price']
    list_display = ['title','description','is_published','cat','price']
    search_fields = ['title__startswith']
    ordering = ['-create_at']
    actions = ['activate_post']

    @admin.action(description='Activate posts')
    def activate_post(modeladmin, request, queryset):
        queryset.update(kind=Workservis.ACTIVE)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']