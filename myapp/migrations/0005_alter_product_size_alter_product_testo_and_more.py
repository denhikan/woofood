# Generated by Django 4.1.1 on 2022-10-02 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_product_size_alter_product_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.size', verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='testo',
            field=models.CharField(blank=True, choices=[('Традиционное тесто', 'Традиционное тесто'), ('Тонкое тесто', 'Тонкое тесто')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.weight', verbose_name='Вес'),
        ),
    ]
