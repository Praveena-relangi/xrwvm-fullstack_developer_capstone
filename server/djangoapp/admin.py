from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class
class CarModelInline(admin.TabularInline):  # Use TabularInline for displaying CarModel in CarMake
    model = CarModel
    extra = 1  # Number of blank CarModel forms to display in CarMake admin

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')  # Fields to display in the admin list view
    list_filter = ('type', 'year')  # Filters for the admin list view
    search_fields = ('name', 'car_make__name')  # Searchable fields

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Include CarModel inline within CarMake admin
    list_display = ('name', 'description')  # Fields to display in the admin list view
    search_fields = ('name',)  # Searchable fields

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)
