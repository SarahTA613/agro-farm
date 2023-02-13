# Generated by Django 4.1.6 on 2023-02-12 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_address', models.CharField(max_length=255)),
                ('business_size', models.PositiveBigIntegerField(default=5)),
                ('adv', models.FileField(upload_to='media/adv')),
                ('business_doc', models.FileField(upload_to='media/documents', verbose_name='Business Documents')),
                ('nid_front', models.ImageField(upload_to='media/nid_front')),
                ('nid_back', models.ImageField(upload_to='media/nid_back')),
                ('nationality', django_countries.fields.CountryField(default='BD', max_length=2)),
                ('date_at', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
