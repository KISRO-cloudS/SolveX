# Generated by Django 3.1.7 on 2022-09-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_brief_Discription', models.TextField(default='Tell Your Condition ...', max_length=1000)),
                ('clip', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
            ],
        ),
        migrations.DeleteModel(
            name='Dashboards',
        ),
    ]