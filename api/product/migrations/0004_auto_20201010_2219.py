# Generated by Django 3.1.2 on 2020-10-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201010_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
