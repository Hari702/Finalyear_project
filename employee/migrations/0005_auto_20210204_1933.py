# Generated by Django 2.2.5 on 2021-02-04 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20210131_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='UPLOAD_MRI_IMAGE',
            new_name='UPLOAD_ROAD_IMAGE',
        ),
    ]
