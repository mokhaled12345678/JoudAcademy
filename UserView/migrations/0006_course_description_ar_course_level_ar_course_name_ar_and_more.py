# Generated by Django 4.2.5 on 2023-09-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserView', '0005_remove_course_requirements_course_age_course_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description_ar',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='level_ar',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='course',
            name='name_ar',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='period_ar',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='tutor_ar',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='course',
            name='type_ar',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='objectives',
            name='description',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='objectives',
            name='description_ar',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='tutor',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='objectives',
            name='name',
            field=models.CharField(default='', max_length=90),
        ),
    ]