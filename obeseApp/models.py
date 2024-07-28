from django.db import models

class MyFormData(models.Model):
    # Basic fields
    age = models.IntegerField()  # Expecting an integer value
    gender = models.CharField(max_length=20)  # Expecting a short string (e.g., "Male", "Female")
    location = models.CharField(max_length=255)  # Expecting a string for location
    occupation = models.CharField(max_length=255)  # Expecting a string for occupation

    # Observational fields
    encounter_obese = models.CharField(max_length=3)  # Expects values like "Yes" or "No"
    profession_of_obese = models.CharField(max_length=255)  # Expecting a comma-separated string
    primary_causes_of_obesity = models.CharField(max_length=255)  # Expecting a comma-separated string

    # Perception fields
    junk_food_main_cause = models.CharField(max_length=3)  # Expects values like "Yes" or "No"

    # Fitness Apps and Programs fields
    used_fitness_app = models.CharField(max_length=3)  # Expects values like "Yes" or "No"
    fitness_apps_used = models.CharField(max_length=255)  # Expecting a comma-separated string
    reasons_for_app_failure = models.CharField(max_length=255)  # Expecting a comma-separated string

    # Needs and Preferences fields
    effective_features = models.CharField(max_length=255)  # Expecting a comma-separated string
    barriers_to_adherence = models.CharField(max_length=255)  # Expecting a comma-separated string

    # Additional comments
    additional_comments = models.TextField()  # Expecting a longer text

    def __str__(self):
        return f'{self.age} - {self.gender} - {self.location}'
