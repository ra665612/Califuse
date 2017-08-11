from django.contrib import admin
from cali.models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info',)

    def user_info(self, obj):
        return obj.image

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('image', 'user') #'-image' for reverse order
        return queryset

    user_info.short_description = 'image'

admin.site.register(UserProfile,UserProfileAdmin)
