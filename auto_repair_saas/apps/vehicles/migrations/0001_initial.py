# Generated by Django 3.1.4 on 2020-12-25 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=15)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='contacts.contact')),
            ],
        ),
    ]
