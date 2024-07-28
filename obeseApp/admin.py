from django.contrib import admin
from .models import MyFormData  
@admin.register(MyFormData)
class FormDataAdmin(admin.ModelAdmin):
    list_display = ('age', 'gender', 'location', 'occupation', 'encounter_obese', 'profession_of_obese', 'primary_causes_of_obesity', 'junk_food_main_cause', 'used_fitness_app', 'fitness_apps_used', 'reasons_for_app_failure', 'effective_features', 'barriers_to_adherence', 'additional_comments')
    search_fields = ('location', 'occupation', 'profession_of_obese', 'additional_comments')
