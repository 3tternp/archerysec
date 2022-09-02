# Generated by Django 3.2.15 on 2022-08-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_alter_monthdb_critical'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdb',
            name='critical_cloud',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectdb',
            name='high_cloud',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectdb',
            name='low_cloud',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectdb',
            name='medium_cloud',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectdb',
            name='total_cloud',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
