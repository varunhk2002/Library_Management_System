# Generated by Django 5.0.2 on 2024-03-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_manage', '0002_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='holder',
            field=models.IntegerField(null=True),
        ),
    ]
