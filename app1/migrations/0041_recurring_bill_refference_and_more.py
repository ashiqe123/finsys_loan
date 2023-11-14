# Generated by Django 4.2.5 on 2023-11-14 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0040_alter_recurring_bill_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring_bill',
            name='refference',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recurring_bill',
            name='profile_name',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
    ]
