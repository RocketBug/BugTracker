# Generated by Django 2.2.6 on 2020-01-01 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0008_auto_20200102_0050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bugitem',
            old_name='project_id',
            new_name='project',
        ),
    ]
