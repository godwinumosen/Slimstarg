# Generated by Django 4.1.4 on 2023-03-14 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StargEntertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, unique=True)),
                ('slug', models.SlugField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('options', models.CharField(choices=[('publish', 'Publish'), ('draft', 'Draft')], default='draft', max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]