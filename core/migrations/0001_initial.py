# Generated by Django 4.1.6 on 2023-02-16 20:06

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Atualizado em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('role', models.CharField(max_length=35, verbose_name='Função')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Atualizado em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('name', models.CharField(max_length=50, verbose_name='Serviço')),
                ('description', models.CharField(max_length=150, verbose_name='Descrição')),
                ('logo', models.CharField(choices=[('lni-cog', 'Gear'), ('lni-stats-up', 'Graph'), ('lni-users', 'User'), ('lni-layers', 'Designs'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Rocket')], max_length=12, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Teammate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Atualizado em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('name', models.CharField(max_length=35, verbose_name='Nome')),
                ('bio', models.CharField(max_length=150, verbose_name='Biografia')),
                ('avatar', stdimage.models.StdImageField(force_min_size=True, upload_to='teammate', variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Avatar')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.role', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Membro',
                'verbose_name_plural': 'Membros',
            },
        ),
    ]
