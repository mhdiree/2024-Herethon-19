# Generated by Django 5.0.3 on 2024-07-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_auto_20240706_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='frequency',
            field=models.CharField(default=0, max_length=5),
        ),
    ]