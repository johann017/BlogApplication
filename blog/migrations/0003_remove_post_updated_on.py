# Generated by Django 3.2.8 on 2021-11-03 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211103_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
    ]
