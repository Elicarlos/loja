# Generated by Django 4.2.4 on 2023-08-30 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_produto_is_best_seller_produto_is_featured_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='is_best_seller',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='is_featured',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='is_hot_trend',
        ),
        migrations.CreateModel(
            name='ItemEspecial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=50)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
    ]