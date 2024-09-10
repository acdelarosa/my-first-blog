# Generated by Django 5.1 on 2024-09-09 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image_alter_post_author_alter_post_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(blank=True, help_text='Ingrese la dirección completa', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='color',
            field=models.CharField(blank=True, help_text='Ingrese el color en formato hex (#RRGGBB)', max_length=7),
        ),
        migrations.AddField(
            model_name='post',
            name='image_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='reference',
            field=models.TextField(blank=True, help_text='Ingrese cualquier referencia adicional de donde vio al can o fue encontrado'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
