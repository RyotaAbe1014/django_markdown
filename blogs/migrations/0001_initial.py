# Generated by Django 3.1 on 2022-04-15 15:22

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='言語')),
            ],
            options={
                'db_table': 'technologies',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', mdeditor.fields.MDTextField()),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.technologies')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]