# Generated by Django 4.2.6 on 2023-12-10 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capital2',
            fields=[
                ('capitalID', models.IntegerField()),
                ('c_name', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Country2',
            fields=[
                ('countryID', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.AddField(
            model_name='capital2',
            name='countryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.country2'),
        ),
    ]
