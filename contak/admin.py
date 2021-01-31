from django.contrib import admin

from contak.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "id",
        "user",
        "note",
        "created",
        "modified",
    ]

    list_filter = [
        "user",
    ]

    search_fields = [
        "first_name",
        "last_name",
        "note",
    ]


admin.site.register(Contact, ContactAdmin)
