# Generated by Django 4.2.1 on 2023-11-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_alter_women_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0),
        ),
    ]
