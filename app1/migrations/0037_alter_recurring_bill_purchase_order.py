# Generated by Django 4.2.5 on 2023-11-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0036_alter_recurring_bill_purchase_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurring_bill',
            name='purchase_order',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
