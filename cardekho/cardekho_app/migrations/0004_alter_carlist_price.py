# Generated by Django 4.2.17 on 2024-12-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardekho_app', '0003_alter_carlist_chassisnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlist',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
