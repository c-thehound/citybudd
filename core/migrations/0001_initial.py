# Generated by Django 3.0.3 on 2020-02-18 21:31

import core.managers.user_managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authentication.user',),
            managers=[
                ('objects', core.managers.user_managers.MenteeManager()),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authentication.user',),
            managers=[
                ('objects', core.managers.user_managers.MentorManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300)),
                ('units', models.ManyToManyField(to='core.Unit')),
            ],
        ),
    ]
