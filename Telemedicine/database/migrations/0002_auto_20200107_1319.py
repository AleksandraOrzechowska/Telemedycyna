# Generated by Django 2.2.6 on 2020-01-07 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conferences',
            fields=[
                ('conference_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_surname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('pesel', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_surname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('result_text', models.TextField()),
                ('result_image', models.BinaryField()),
                ('comment_image', models.BinaryField()),
                ('comment_text', models.TextField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Doctors')),
                ('pesel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Patients')),
            ],
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.AddField(
            model_name='conferences',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.Doctors'),
        ),
        migrations.AddField(
            model_name='conferences',
            name='pesel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Patients'),
        ),
    ]
