# Generated by Django 4.1.12 on 2023-10-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='data',
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.CharField(max_length=10, null=True),
        ),
    ]