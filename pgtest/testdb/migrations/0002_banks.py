# Generated by Django 4.2.1 on 2023-05-04 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.SmallIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('geom', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'banks',
                'managed': False,
            },
        ),
    ]
