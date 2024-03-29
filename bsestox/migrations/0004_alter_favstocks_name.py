# Generated by Django 5.0.1 on 2024-01-25 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bsestox", "0003_remove_favstocks_id_remove_stockscurrval_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favstocks",
            name="name",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="bsestox.stocks",
            ),
        ),
    ]
