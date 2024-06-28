# Generated by Django 5.0.4 on 2024-04-30 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='图书标题')),
                ('author', models.CharField(max_length=128, verbose_name='作者')),
                ('image', models.CharField(max_length=128, verbose_name='封面图')),
                ('price', models.IntegerField(verbose_name='价格(分)')),
            ],
        ),
        migrations.AlterField(
            model_name='admin',
            name='avatar',
            field=models.CharField(default='/media/avatar/default.jpg', max_length=64, verbose_name='头像'),
        ),
    ]
