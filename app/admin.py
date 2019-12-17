from django.contrib import admin
from django.utils.html import format_html

from app.models import Recipe, Ingredient, Unit, RecipeIngredientUnit, Tag, RecipeTag


class RecipeIngredientUnitInlineAdmin(admin.TabularInline):
    model = RecipeIngredientUnit
    extra = 0


class RecipeTagInlineAdmin(admin.StackedInline):
    #raw_id_fields = ('tag',)
    model = RecipeTag
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientUnitInlineAdmin, RecipeTagInlineAdmin)

    def detail_start(self, obj):
        if obj.detail is None or obj.detail == '':
            return '? No summary ?'
        if len(obj.detail) < 80:
            return format_html(f'<h2> ID = {obj.id} / </h2>{obj.detail[:80]}')

    detail_start.short_description = "Summary"
    list_display = ('title', 'description', 'detail_start')
    list_display_links = list_display


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientUnit)
admin.site.register(Tag)
admin.site.register(RecipeTag)
