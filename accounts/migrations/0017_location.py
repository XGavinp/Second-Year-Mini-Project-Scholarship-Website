# Generated by Django 4.1.5 on 2023-03-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_remove_scholarship_location_delete_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(max_length=30)),
            ],
        ),
    ]
