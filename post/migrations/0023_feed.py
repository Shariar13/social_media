# Generated by Django 3.1.2 on 2021-02-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_remove_post_post_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
