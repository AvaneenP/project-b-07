# Generated by Django 3.2.9 on 2021-12-03 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0022_auto_20211128_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestedlistings',
            old_name='listingAddress',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='suggestedlistings',
            old_name='listingName',
            new_name='Name',
        ),
    ]
