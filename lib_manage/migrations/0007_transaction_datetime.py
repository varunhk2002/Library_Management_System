# Generated by Django 5.0.2 on 2024-03-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_manage', '0006_alter_books_holder_alter_member_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
