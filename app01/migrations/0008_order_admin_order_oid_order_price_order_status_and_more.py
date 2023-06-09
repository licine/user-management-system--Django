# Generated by Django 4.1.7 on 2023-05-09 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0007_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="admin",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="app01.admin",
                verbose_name="管理员",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="oid",
            field=models.CharField(default=11111, max_length=64, verbose_name="订单号"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="price",
            field=models.IntegerField(default=11, verbose_name="价格"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.SmallIntegerField(
                choices=[(1, "待支付"), (2, "已支付")], default=1, verbose_name="状态"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="title",
            field=models.CharField(default=11, max_length=32, verbose_name="名称"),
            preserve_default=False,
        ),
    ]
