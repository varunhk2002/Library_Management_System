# Generated by Django 5.0.2 on 2024-03-02 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, null=True)),
                ('author', models.CharField(max_length=35, null=True)),
                ('isbn', models.BigIntegerField(null=True)),
                ('publisher', models.CharField(max_length=35, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.BigIntegerField()),
                ('fees', models.IntegerField(null=True)),
                ('holding', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='lib_manage.books')),
            ],
        ),
    ]
