# Generated by Django 3.2.5 on 2021-07-27 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
