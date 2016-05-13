from django.contrib import admin
from mysm.models import Screen, Link, Location, MediaType, ScreenLink, Category

# Register your models here.
class ScreenLinkInline(admin.TabularInline):
    model = ScreenLink
    ordering = ('position',)
    fields = ('position', 'sl_link', 'display_time')
    view_on_site = False


class ScreenAdmin(admin.ModelAdmin):
    view_on_site = False
    list_per_page = 10

    list_display = ('id', 'location', 'brand', 'model')
    list_filter = ('location',)
    inlines = [ScreenLinkInline,]


class LinkAdmin(admin.ModelAdmin):
    view_on_site = False
    list_per_page = 10
    #exclude = ('url',)

    list_display = ('url', 'link_type', 'id', 'category')
    list_display_links = ('url',)
    list_editable = ('link_type', 'category')

    # def get_readonly_fields(self, request, obj=None):
    #     if obj is None:
    #         return ['url ']
    #     return []
    # class Meta:
    #     abstract = True


class ScreenLinkAdmin(admin.ModelAdmin):
    view_on_site = False
    list_per_page = 10

    list_display = ('id', 'sl_screen', 'Screen_Location','sl_link', 'display_time', 'position')
    list_display_links = ('sl_link',)
    list_editable = ('display_time','position')
    list_filter = ('sl_screen','sl_link', "sl_screen__location")
    search_fields = ('sl_link__url','sl_screen__brand')

    def Screen_Location(self, obj):
        return obj.sl_screen.location


admin.site.register(Screen, ScreenAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Location)
#admin.site.register(Category)
admin.site.register(MediaType)
admin.site.register(ScreenLink, ScreenLinkAdmin)
