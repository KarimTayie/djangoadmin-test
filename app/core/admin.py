from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class AppAdmin(AdminSite):
    stat = {
        "value": "5269",
        "title": "Units Sold",
        "subtitle": "Avg. 351 per week",
        "label": "-12%",
    }

    chart = {
        "series": '{"labels": ["1", "2", "3"], "datasets": [{"data": [1, 2, 3]}]}',  # JSON object
        "height": 360,  # Optional
        "value": "5269",
        "title": "Units Sold",
        "subtitle": "Avg. 351 per week",
        "label": "-12%",
    }

    def index(self, request, extra_context=chart):
        # Update extra_context with new variables
        print("I Was here")
        return super().index(request, extra_context)


# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )


admin = AppAdmin(name="Test")

admin.register(models.User, UserAdmin)
admin.register(models.Wall)
