# Generated by Django 3.2.5 on 2021-07-29 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionComment',
        ),
    ]
