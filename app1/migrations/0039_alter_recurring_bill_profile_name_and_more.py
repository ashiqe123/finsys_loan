# Generated by Django 4.2.5 on 2023-11-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0038_alter_recurring_bill_purchase_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurring_bill',
            name='profile_name',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recurring_bill',
            name='purchase_order',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
    ]
