# Generated by Django 4.1.2 on 2022-12-18 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='password2',
        ),
    ]