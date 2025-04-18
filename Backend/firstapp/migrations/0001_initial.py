# Generated by Django 4.2 on 2025-04-18 07:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.CharField(max_length=255)),
                ('votes', models.IntegerField(default=0)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='firstapp.poll')),
            ],
        ),
    ]
