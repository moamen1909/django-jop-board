# Generated by Django 4.2.1 on 2023-05-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jop_jop_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='descriptions',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
