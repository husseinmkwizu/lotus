# Generated by Django 4.0.5 on 2022-10-14 19:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0045_alter_billingplan_status_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="backtestsubstitution",
            old_name="old_plan",
            new_name="original_plan",
        ),
        migrations.RenameField(
            model_name="historicalbacktestsubstitution",
            old_name="old_plan",
            new_name="original_plan",
        ),
    ]
