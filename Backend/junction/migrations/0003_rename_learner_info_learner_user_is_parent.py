# Generated by Django 4.2.6 on 2023-10-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junction', '0002_learner_info'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='learner_info',
            new_name='learner',
        ),
        migrations.AddField(
            model_name='user',
            name='is_parent',
            field=models.BooleanField(default=False),
        ),
    ]