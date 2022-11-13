# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-25 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookdetails',
            fields=[
                ('bid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=37)),
                ('bauthor', models.CharField(max_length=37)),
                ('avail', models.CharField(max_length=27)),
            ],
        ),
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('brname', models.CharField(max_length=37)),
            ],
        ),
        migrations.CreateModel(
            name='takenbooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.bookdetails')),
            ],
        ),
        migrations.CreateModel(
            name='uregister',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=107)),
                ('passcode', models.CharField(max_length=37)),
                ('role', models.CharField(max_length=37)),
                ('fname', models.CharField(max_length=37)),
                ('lanme', models.CharField(max_length=37)),
                ('phoneno', models.IntegerField()),
                ('email', models.EmailField(max_length=37)),
            ],
        ),
        migrations.AddField(
            model_name='takenbooks',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.uregister'),
        ),
        migrations.AddField(
            model_name='bookdetails',
            name='branchid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.branch'),
        ),
    ]
