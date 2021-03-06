# Generated by Django 3.2.5 on 2022-02-04 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Categories', '0004_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='Product_Images')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Categories.categories')),
            ],
        ),
    ]
