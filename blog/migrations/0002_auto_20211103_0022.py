# Generated by Django 3.2.8 on 2021-11-03 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_on']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
