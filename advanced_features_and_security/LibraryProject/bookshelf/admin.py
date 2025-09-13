from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser, Book


# ------------------------
# Custom User Admin
# ------------------------
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_superuser", "profile_thumbnail")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

    def profile_thumbnail(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" width="40" height="40" style="border-radius:50%;" />', obj.profile_photo.url)
        return "-"
    profile_thumbnail.short_description = "Profile Photo"


# ------------------------
# Book Admin
# ------------------------
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("author", "publication_year")
    search_fields = ("title", "author")
    ordering = ("title",)


# Register Models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)
