# Generated by Django 4.0.10 on 2024-02-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0004_alter_experience_category_alter_experience_host_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='pet_friendly',
            field=models.BooleanField(default=True),
        ),
    ]