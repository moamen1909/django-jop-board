# Generated by Django 4.2.1 on 2023-05-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_jop_published_at_jop_vacancy_jop_experiense_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jop',
            name='Vacancy',
            field=models.IntegerField(default=1),
        ),
    ]
