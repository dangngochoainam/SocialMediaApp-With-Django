# Generated by Django 4.0.4 on 2022-05-08 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialmediaapp', '0018_alter_posts_hagtags'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='like',
            name='notification',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like', to='socialmediaapp.notification'),
        ),
    ]
