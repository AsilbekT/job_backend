# Generated by Django 4.2.3 on 2023-07-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
