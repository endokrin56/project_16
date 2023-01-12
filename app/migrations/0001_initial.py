# Generated by Django 4.1.3 on 2023-01-10 16:28

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('text', ckeditor.fields.RichTextField()),
                ('category', models.CharField(choices=[('Tanks', 'Танк'), ('Hily', 'Хилы'), ('DD', 'ДД'), ('Merchants', 'Торговцы'), ('Guild_Masters', 'Гилдмастеры'), ('Quest_Givers', 'Квестгиверы'), ('Blacksmiths', 'Кузнецы'), ('Tanners', 'Кожевники'), ('Potion_Makers', 'Зельевары'), ('Spell Masters', 'Мастера_заклинаний')], default='Tanks', max_length=13)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usersresponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.advertisements')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
