# Generated by Django 3.2 on 2021-05-30 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_lectures_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectures',
            name='lecture_plan',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
