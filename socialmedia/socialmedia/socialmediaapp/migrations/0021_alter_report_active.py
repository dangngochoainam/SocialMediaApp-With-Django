# Generated by Django 4.0.4 on 2022-05-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmediaapp', '0020_alter_auctionsdetails_active_alter_posts_hagtags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]