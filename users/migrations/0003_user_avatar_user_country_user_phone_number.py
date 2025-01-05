# Generated by Django 4.2.2 on 2025-01-05 20:31

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите изображение",
                null=True,
                upload_to="users/avatars/",
                verbose_name="Аватар",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="country",
            field=models.CharField(
                blank=True,
                help_text="Введите страну",
                max_length=50,
                null=True,
                verbose_name="Страна",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                help_text="Введите номер телефона",
                max_length=128,
                region=None,
                verbose_name="Телефон",
            ),
        ),
    ]
