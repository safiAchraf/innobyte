# Generated by Django 4.2.6 on 2023-10-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junction', '0005_child_learner_last_achievement_course_acheivement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child_learner',
            name='child_level',
            field=models.IntegerField(default=0),
        ),
    ]