# Generated by Django 5.0.7 on 2024-08-09 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Thumbnail', models.ImageField(upload_to='staticfiles/Images/Category_Thumbnails')),
                ('Description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Renders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('render', models.ImageField(upload_to='App/Renders')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=1000)),
                ('time_taken', models.CharField(max_length=1000)),
                ('model', models.FileField(upload_to='App/3D_Models')),
                ('thumbnail', models.ImageField(upload_to='App/Maps/Thumbnails')),
                ('Custom_Three_File', models.FileField(blank=True, null=True, upload_to='staticfiles/ThreeJSFiles')),
                ('Metal_Maps', models.ImageField(blank=True, null=True, upload_to='App/Maps/Metal_Maps')),
                ('Ambeint_Occlusion_Maps', models.ImageField(blank=True, null=True, upload_to='App/Maps/AmbientO_Maps')),
                ('Emmission_Maps', models.ImageField(blank=True, null=True, upload_to='App/Maps/Emmission_Maps')),
                ('Height_Maps', models.ImageField(blank=True, null=True, upload_to='App/Maps/Height_Maps')),
                ('Colour_Maps', models.ImageField(blank=True, null=True, upload_to='App/Maps/Colour_Maps')),
                ('Roughness_Maps', models.ImageField(blank=True, null=True, upload_to='App/Maps/Roughness_Maps')),
                ('Normal_Map', models.ImageField(blank=True, null=True, upload_to='App/Maps/Normal_Maps')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Belongs_To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.category')),
            ],
        ),
    ]
