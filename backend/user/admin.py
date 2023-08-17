# from django.contrib import admin

# from .models import User

# # Register your models here.
# admin.site.register(User)

from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone", "get_balance")

    def get_balance(self, obj):
        return obj.balance

    get_balance.short_description = "Balance"


admin.site.register(User, UserAdmin)
