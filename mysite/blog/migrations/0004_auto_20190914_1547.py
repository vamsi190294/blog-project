# Generated by Django 2.2.1 on 2019-09-14 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='acive',
            new_name='active',
        ),
    ]