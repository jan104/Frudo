# Generated by Django 2.0.4 on 2018-04-17 09:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_comment_comment_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='importance',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
