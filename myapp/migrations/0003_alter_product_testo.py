# Generated by Django 4.1.1 on 2022-10-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_product11_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='testo',
            field=models.CharField(blank=True, choices=[('Традиционное тесто', 'Традиционное тесто'), ('Тонкое тесто', 'Тонкое тесто')], max_length=100, null=True),
        ),
    ]
