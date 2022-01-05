from django.db import models

# Create your models here.
class DataBreach(models.Model):
    """
        Create a Model for the data breach with the set of fields.
    """
    name = models.CharField(max_length=100, help_text='Name of Covered Entity')
    state = models.CharField(max_length=50, help_text='State of Covered Entity')
    covered_entity_type = models.CharField(max_length=50, help_text='Covered Entity Type')
    individuals_affected = models.CharField(max_length=50, help_text='Individuals Affected')
    breach_submission_date = models.DateField(help_text='Breach Submission Date')
    type_of_breach = models.CharField(max_length=50, help_text='Type of Breach')
    location_of_breach_information = models.CharField(max_length=50,
        help_text='Location of Breached Information')
