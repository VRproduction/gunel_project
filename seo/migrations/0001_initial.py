# Generated by Django 3.2.15 on 2022-12-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('keyword', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Qəbula yazıl SEO',
                'verbose_name_plural': 'Qəbula yazıl SEO',
            },
        ),
        migrations.CreateModel(
            name='BlogSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('keyword', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Bloq SEO',
                'verbose_name_plural': 'Bloq SEO',
            },
        ),
        migrations.CreateModel(
            name='ConferenceSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('keyword', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Konfrans SEO',
                'verbose_name_plural': 'Konfrans SEO',
            },
        ),
        migrations.CreateModel(
            name='ContactSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('keyword', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Əlaqə SEO',
                'verbose_name_plural': 'Əlaqə SEO',
            },
        ),
        migrations.CreateModel(
            name='HomeSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('keyword', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Ana səhifə SEO',
                'verbose_name_plural': 'Ana səhifə SEO',
            },
        ),
        migrations.CreateModel(
            name='MediaSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('keyword', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Media SEO',
                'verbose_name_plural': 'Media SEO',
            },
        ),
        migrations.CreateModel(
            name='ServiceSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('keyword', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Xidmətlər SEO',
                'verbose_name_plural': 'Xidmətlər SEO',
            },
        ),
    ]
