# Generated by Django 4.1.7 on 2023-05-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0008_order_admin_order_oid_order_price_order_status_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Order",),
    ]
