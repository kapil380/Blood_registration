# Generated by Django 3.0.6 on 2020-05-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Address',
            field=models.TextField(),
        ),
    ]
