# Generated by Django 2.1.5 on 2019-01-24 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apptwo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='web',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=121, unique=True)),
                ('t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptwo.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptwo.web'),
        ),
    ]