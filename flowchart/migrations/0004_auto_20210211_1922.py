# Generated by Django 3.1.6 on 2021-02-12 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowchart', '0003_auto_20210209_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flowchart',
            name='summary',
        ),
        migrations.AddField(
            model_name='flowchart',
            name='team',
            field=models.CharField(default='teams', max_length=40),
            preserve_default=False,
        ),
    ]