# Generated by Django 4.0.5 on 2023-01-11 01:13

from django.db import migrations, models
import django.db.models.deletion
import metering_billing.utils.utils


class Migration(migrations.Migration):
    dependencies = [
        (
            "metering_billing",
            "0146_usagealert_alter_webhooktrigger_trigger_name_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="historicalorganization",
            old_name="company_name",
            new_name="organization_name",
        ),
        migrations.RenameField(
            model_name="organization",
            old_name="company_name",
            new_name="organization_name",
        ),
        migrations.AlterField(
            model_name="historicalplan",
            name="created_on",
            field=models.DateTimeField(
                default=metering_billing.utils.utils.now_utc, null=True
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="created_on",
            field=models.DateTimeField(
                default=metering_billing.utils.utils.now_utc, null=True
            ),
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag_name", models.CharField(max_length=50)),
                (
                    "tag_group",
                    models.CharField(choices=[("plan", "Plan")], max_length=15),
                ),
                ("tag_hex", models.CharField(max_length=7, null=True)),
                ("tag_color", models.CharField(max_length=20, null=True)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tags",
                        to="metering_billing.organization",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="plan",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="plans", to="metering_billing.tag"
            ),
        ),
    ]
