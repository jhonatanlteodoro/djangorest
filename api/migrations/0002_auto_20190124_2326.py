# Generated by Django 2.1.5 on 2019-01-24 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='create_on',
            new_name='created_on',
        ),
    ]
