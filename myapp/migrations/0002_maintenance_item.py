# Generated by Django 5.2.1 on 2025-05-31 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='item',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
