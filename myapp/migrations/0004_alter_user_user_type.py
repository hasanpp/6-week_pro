# Generated by Django 5.0.6 on 2024-06-15 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_user_email_alter_user_user_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(default='Admin', max_length=10),
        ),
    ]
