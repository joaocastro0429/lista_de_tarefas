# Generated by Django 5.2 on 2025-05-05 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
