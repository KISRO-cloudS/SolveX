# Generated by Django 3.1.7 on 2022-03-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Have', models.CharField(choices=[('h', ' problems'), ('h', 'Health problems'), ('h', 'Health problems'), ('h', 'Health problems')], max_length=1000)),
            ],
        ),
    ]
