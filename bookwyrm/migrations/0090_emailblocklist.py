# Generated by Django 3.2.4 on 2021-09-08 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0089_user_show_suggested_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailBlocklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('domain', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]
