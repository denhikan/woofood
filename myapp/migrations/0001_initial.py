# Generated by Django 4.1.1 on 2022-09-30 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название товара')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Вес',
                'verbose_name_plural': 'Вес',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название товара')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('descriprion', models.TextField(max_length=5000, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение в списке')),
                ('testo', models.CharField(choices=[('Традиционное тесто', 'Традиционное тесто'), ('Тонкое тесто', 'Тонкое тесто')], max_length=100, null=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.category', verbose_name='Категория')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.size', verbose_name='Размер')),
                ('weight', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.weight', verbose_name='Вес')),
            ],
        ),
    ]
