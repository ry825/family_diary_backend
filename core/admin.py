from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models as coreModels


# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('personal Info'), {'fields': ()}),
        (
            _('permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (_('important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(coreModels.User, UserAdmin,)
admin.site.register(coreModels.Diary)
admin.site.register(coreModels.schedule)
admin.site.register(coreModels.Video)
admin.site.register(coreModels.Picture)
