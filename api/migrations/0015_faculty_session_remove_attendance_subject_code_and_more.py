# Generated by Django 4.1.12 on 2023-11-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('employee_id', models.IntegerField()),
                ('branch', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=500, null=True)),
                ('subjects', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.BigIntegerField()),
                ('faculty_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('subject_name', models.CharField(max_length=150, null=True)),
                ('ip', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='subject_code',
        ),
        migrations.AddField(
            model_name='attendance',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
