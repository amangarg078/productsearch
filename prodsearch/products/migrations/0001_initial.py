# Generated by Django 3.2.7 on 2021-09-22 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('price', models.FloatField()),
                ('discount', models.FloatField(blank=True, null=True)),
                ('currency_code', models.CharField(max_length=3)),
                ('colour', models.CharField(blank=True, max_length=20, null=True)),
                ('imgs_src', models.URLField()),
                ('stock', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('checksum', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=512)),
                ('position', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='products.ProductCategory'),
        ),
    ]
