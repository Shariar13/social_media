# Generated by Django 3.1.2 on 2021-02-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_remove_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_view',
            field=models.IntegerField(default=0),
        ),
    ]
