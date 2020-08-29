# Generated by Django 2.2 on 2020-08-29 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='text',
            field=models.TextField(max_length=3000, verbose_name='Опрос'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='webapp.Choice', verbose_name='Ответ')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls', to='webapp.Poll', verbose_name='Опрос')),
            ],
        ),
    ]
