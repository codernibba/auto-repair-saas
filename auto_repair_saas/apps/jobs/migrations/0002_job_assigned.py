# Generated by Django 3.1.4 on 2020-12-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='assigned',
            field=models.TextField(blank=True, null=True),
        ),
    ]
