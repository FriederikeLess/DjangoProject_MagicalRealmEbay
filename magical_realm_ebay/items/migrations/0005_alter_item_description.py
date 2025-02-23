# Generated by Django 5.1.4 on 2025-01-08 13:45

import profanity.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0004_alter_itemcategory_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.TextField(
                default="No description available",
                validators=[profanity.validators.validate_is_profane],
            ),
        ),
    ]
