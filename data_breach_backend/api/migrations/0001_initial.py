# Generated by Django 3.2.9 on 2022-01-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBreach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of Covered Entity', max_length=100)),
                ('state', models.CharField(help_text='State of Covered Entity', max_length=50)),
                ('covered_entity_type', models.CharField(help_text='Covered Entity Type', max_length=50)),
                ('individuals_affected', models.CharField(help_text='Individuals Affected', max_length=50)),
                ('breach_submission_date', models.DateField(help_text='Breach Submission Date')),
                ('type_of_breach', models.CharField(help_text='Type of Breach', max_length=50)),
                ('location_of_breach_information', models.CharField(help_text='Location of Breached Information', max_length=50)),
            ],
        ),
    ]
