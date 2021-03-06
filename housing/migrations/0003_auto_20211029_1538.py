# Generated by Django 3.2.8 on 2021-10-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_alter_studenthousing_disttogrounds'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studenthousing',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='studenthousing',
            name='noiseLevel',
        ),
        migrations.AddField(
            model_name='studenthousing',
            name='location',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studenthousing',
            name='maxCost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studenthousing',
            name='minCost',
            field=models.IntegerField(default=0),
        ),
    ]
