# Generated by Django 2.2.2 on 2020-01-23 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='new_link',
            field=models.URLField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]