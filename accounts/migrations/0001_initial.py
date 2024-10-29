# Generated by Django 5.1.2 on 2024-10-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='Not Available', max_length=100)),
                ('first_name', models.CharField(default='Not Available', max_length=100)),
                ('last_name', models.CharField(default='Not Available', max_length=100)),
                ('email', models.EmailField(default='example@email.com', max_length=254)),
                ('codechef', models.CharField(default='Not Available', max_length=100)),
                ('codeforces', models.CharField(default='Not Available', max_length=100)),
                ('leetcode', models.CharField(default='Not Available', max_length=100)),
                ('email_verified', models.BooleanField(default='False')),
                ('leetcode_token', models.CharField(default='Not Available', max_length=100)),
                ('codechef_token', models.CharField(default='Not Available', max_length=100)),
                ('codeforces_token', models.CharField(default='Not Available', max_length=100)),
                ('token', models.CharField(default='Not Available', max_length=100)),
                ('leetcode_verified', models.BooleanField(default='False')),
                ('codechef_verified', models.BooleanField(default='False')),
                ('codeforces_verified', models.BooleanField(default='False')),
                ('institute', models.CharField(default='@ Not Available', max_length=100)),
                ('friends', models.JSONField(default=dict)),
                ('followers', models.IntegerField(default=0)),
            ],
        ),
    ]