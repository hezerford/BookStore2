# Generated by Django 5.1.4 on 2025-01-01 18:15

import django.core.validators
import django.db.models.deletion
import user_profile.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0005_rename_email_subscription'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('street', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('postal_code', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Пожалуйста, введите действительный номер телефона, состоящий не менее чем из 10 цифр.', regex='^\\+?1?\\d{10,15}$')])),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=user_profile.models.user_profile_path)),
                ('is_active', models.BooleanField(default=True)),
                ('favorite_books', models.ManyToManyField(blank=True, related_name='favorited_by', to='store.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
