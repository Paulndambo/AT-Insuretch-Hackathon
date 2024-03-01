# Generated by Django 5.0 on 2024-03-01 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_brokerage_broker_salesagent_brokerage"),
    ]

    operations = [
        migrations.AddField(
            model_name="brokerage",
            name="broker",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.broker",
            ),
        ),
    ]