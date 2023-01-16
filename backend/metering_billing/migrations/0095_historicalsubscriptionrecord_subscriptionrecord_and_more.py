# Generated by Django 4.0.5 on 2022-12-03 16:09

from decimal import Decimal

import django.db.models.deletion
import metering_billing.utils.utils
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0094_alter_historicalplanversion_day_anchor_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalSubscriptionRecord",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("start_date", models.DateTimeField()),
                ("next_billing_date", models.DateTimeField(blank=True, null=True)),
                ("last_billing_date", models.DateTimeField(blank=True, null=True)),
                ("end_date", models.DateTimeField()),
                ("scheduled_end_date", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("ended", "Ended"),
                            ("not_started", "Not Started"),
                        ],
                        default="not_started",
                        max_length=20,
                    ),
                ),
                ("auto_renew", models.BooleanField(default=True)),
                ("is_new", models.BooleanField(default=True)),
                (
                    "subscription_id",
                    models.CharField(
                        blank=True,
                        default=metering_billing.utils.utils.subscription_uuid,
                        max_length=100,
                    ),
                ),
                (
                    "prorated_flat_costs_dict",
                    models.JSONField(blank=True, default=dict, null=True),
                ),
                (
                    "flat_fee_already_billed",
                    models.DecimalField(
                        decimal_places=10, default=Decimal("0"), max_digits=20
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="metering_billing.customer",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="metering_billing.organization",
                    ),
                ),
                (
                    "plan_version",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        related_query_name="subscription_record",
                        to="metering_billing.planversion",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical subscription record",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="SubscriptionRecord",
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
                ("start_date", models.DateTimeField()),
                ("next_billing_date", models.DateTimeField(blank=True, null=True)),
                ("last_billing_date", models.DateTimeField(blank=True, null=True)),
                ("end_date", models.DateTimeField()),
                ("scheduled_end_date", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("ended", "Ended"),
                            ("not_started", "Not Started"),
                        ],
                        default="not_started",
                        max_length=20,
                    ),
                ),
                ("auto_renew", models.BooleanField(default=True)),
                ("is_new", models.BooleanField(default=True)),
                (
                    "subscription_id",
                    models.CharField(
                        blank=True,
                        default=metering_billing.utils.utils.subscription_uuid,
                        max_length=100,
                    ),
                ),
                (
                    "prorated_flat_costs_dict",
                    models.JSONField(blank=True, default=dict, null=True),
                ),
                (
                    "flat_fee_already_billed",
                    models.DecimalField(
                        decimal_places=10, default=Decimal("0"), max_digits=20
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscription_records",
                        to="metering_billing.customer",
                    ),
                ),
                (
                    "filters",
                    models.ManyToManyField(
                        blank=True, to="metering_billing.categoricalfilter"
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscription_records",
                        to="metering_billing.organization",
                    ),
                ),
                (
                    "plan_version",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscription_records",
                        related_query_name="subscription_record",
                        to="metering_billing.planversion",
                    ),
                ),
            ],
            options={
                "unique_together": {("organization", "subscription_id")},
            },
        ),
        migrations.AlterUniqueTogether(
            name="subscription",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="billing_plan",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="filters",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="organization",
        ),
        migrations.DeleteModel(
            name="HistoricalSubscription",
        ),
        migrations.AlterField(
            model_name="historicalinvoice",
            name="subscription",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="metering_billing.subscriptionrecord",
            ),
        ),
        migrations.RemoveField(
            model_name="invoice",
            name="subscription",
        ),
        migrations.AddField(
            model_name="invoice",
            name="subscription",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invoices",
                to="metering_billing.subscriptionrecord",
            ),
        ),
        migrations.DeleteModel(
            name="Subscription",
        ),
    ]
