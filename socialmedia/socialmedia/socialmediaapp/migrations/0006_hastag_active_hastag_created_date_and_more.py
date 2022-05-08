# Generated by Django 4.0.4 on 2022-05-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmediaapp', '0005_notification_comment_notification_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='hastag',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hastag',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='hastag',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='auctionsdetails',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
