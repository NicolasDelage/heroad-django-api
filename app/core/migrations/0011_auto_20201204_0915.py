# Generated by Django 3.1.3 on 2020-12-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_masterrun_runs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterrun',
            name='comments',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]