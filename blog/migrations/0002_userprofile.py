# Generated by Django 2.2.5 on 2020-10-12 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('gender', models.CharField(default='', max_length=100)),
                ('relationship', models.CharField(default='', max_length=100)),
                ('mobile', models.IntegerField(default='', max_length=13)),
                ('hometown', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
