# Generated by Django 2.2.6 on 2020-01-01 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0007_bugitem_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bugitem',
            old_name='project',
            new_name='project_id',
        ),
    ]
