# Generated by Django 4.1.5 on 2023-03-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_scholarship_host_alter_scholarship_last_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='location',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
