from django.contrib import admin
from api.models import Freelancers, Brand

# Customizing the display and search fields for the Freelancers model in the admin interface
class FreelancersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone_number', 'last_name', 'followers', 'brand')
    search_fields = ('first_name', 'email', 'phone_number', 'last_name', 'followers', 'brand')

# Customizing the display and filter options for the Brand model in the admin interface
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_id', 'brand_name', 'about', 'freelancers')
    list_filter = ('brand_name',)

# Registering the models and their respective admin customization

# Register the Freelancers model with the FreelancersAdmin customization
admin.site.register(Freelancers, FreelancersAdmin)

# Register the Brand model with the BrandAdmin customization
admin.site.register(Brand, BrandAdmin)
