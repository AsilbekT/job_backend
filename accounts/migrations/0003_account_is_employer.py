# Generated by Django 4.2.3 on 2023-07-20 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_employer',
            field=models.BooleanField(default=False),
        ),
    ]
