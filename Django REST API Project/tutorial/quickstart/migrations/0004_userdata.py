# Generated by Django 2.1.1 on 2018-10-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quickstart', '0003_delete_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=17)),
                ('password', models.CharField(max_length=17)),
                ('email', models.CharField(max_length=17)),
            ],
        ),
    ]