# Generated by Django 4.2.7 on 2024-03-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_otboys_otboysinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.RenameField(
            model_name='otboysinfo',
            old_name='fid',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='otboysinfo',
            name='views',
        ),
        migrations.AddField(
            model_name='otboysinfo',
            name='views',
            field=models.ManyToManyField(related_name='otboys_info', to='test1.imagemodel'),
        ),
    ]
