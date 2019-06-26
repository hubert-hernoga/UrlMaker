# Generated by Django 2.0.5 on 2019-06-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0003_auto_20190626_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, null=True)),
                ('short_url', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Url',
        ),
    ]
