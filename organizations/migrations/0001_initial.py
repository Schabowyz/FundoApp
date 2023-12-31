# Generated by Django 4.2.3 on 2023-07-24 17:16

from django.db import migrations, models
import django.db.models.deletion
import organizations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('webpage', models.URLField(blank=True, max_length=256)),
                ('image', models.ImageField(blank=True, upload_to=organizations.models.path_and_rename_organization)),
                ('currency_code', models.CharField(max_length=3)),
                ('budget', models.IntegerField()),
                ('tokens_per_person', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationDomains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.URLField(max_length=256)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization')),
            ],
        ),
    ]
