from django.contrib import admin

from .models import Organization, OrganizationDomains, Fundraise, Payment, Tokens

# Register your models here.
admin.site.register(Organization)
admin.site.register(OrganizationDomains)
admin.site.register(Fundraise)
admin.site.register(Payment)
admin.site.register(Tokens)