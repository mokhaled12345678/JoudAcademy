# Generated by Django 4.2.5 on 2023-10-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserView', '0010_course_price_course_price_ar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist', models.TextField(blank=True)),
                ('frist_ar', models.TextField(blank=True)),
                ('second', models.TextField(blank=True)),
                ('second_ar', models.TextField(blank=True)),
            ],
        ),
    ]
