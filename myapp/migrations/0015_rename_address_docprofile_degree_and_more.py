# Generated by Django 4.1.2 on 2022-12-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_rename_name_docprofile_address_docprofile_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docprofile',
            old_name='address',
            new_name='degree',
        ),
        migrations.RenameField(
            model_name='docprofile',
            old_name='password',
            new_name='email',
        ),
        migrations.AddField(
            model_name='docprofile',
            name='fees',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='gender',
            field=models.CharField(default='j', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docprofile',
            name='institute',
            field=models.CharField(default='hs', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docprofile',
            name='name',
            field=models.CharField(default='hsa', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docprofile',
            name='specialist',
            field=models.CharField(default='jd', max_length=100),
            preserve_default=False,
        ),
    ]
