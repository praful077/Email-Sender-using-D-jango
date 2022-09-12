from django.contrib import admin

from customer.models import EmailInfo

# Register your models here.


# @admin.register(Register)
class EmailInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name','email')


admin.site.register(EmailInfo,EmailInfoAdmin)
admin.site.site_header = "Email Sender"
admin.site.index_title = "Email From Admin"
