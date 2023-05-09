# Generated by Django 3.2.15 on 2023-05-06 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_management', '0001_initial'),
        ('networkscanners', '0025_networkscanresultsdb_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkscandb',
            name='updated_time',
        ),
        migrations.AddField(
            model_name='networkscandb',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='network_scan_db_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='networkscandb',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='networkscandb',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='networkscandb',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.organization'),
        ),
        migrations.AddField(
            model_name='networkscandb',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='network_scan_db_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='networkscanresultsdb',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='network_scan_result_db_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='networkscanresultsdb',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='networkscanresultsdb',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='networkscanresultsdb',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.organization'),
        ),
        migrations.AddField(
            model_name='networkscanresultsdb',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='network_scan_result_db_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='taskscheduledb',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasksch_scan_result_db_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='taskscheduledb',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='taskscheduledb',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='taskscheduledb',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.organization'),
        ),
        migrations.AddField(
            model_name='taskscheduledb',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasksch_scan_result_db_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]