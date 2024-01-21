# Generated by Django 3.2.15 on 2024-01-21 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0008_team_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_in', models.DateTimeField(blank=True, null=True)),
                ('lunch1', models.DateTimeField(blank=True, null=True)),
                ('dinner1', models.DateTimeField(blank=True, null=True)),
                ('breakfast2', models.DateTimeField(blank=True, null=True)),
                ('lunch2', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
