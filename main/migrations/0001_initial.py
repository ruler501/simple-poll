# Generated by Django 2.2.1 on 2019-05-10 00:52

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DistributedPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('timestamp', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('channel', models.CharField(max_length=1000)),
                ('question', models.CharField(max_length=1000)),
                ('options', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), max_length=99, size=None)),
            ],
            options={
                'ordering': ['timestamp'],
                'get_latest_by': 'timestamp',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question', models.CharField(max_length=1000)),
                ('options', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), max_length=100, size=None)),
                ('id', models.CharField(blank=True, default=None, max_length=8, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'name',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.IntegerField()),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Poll')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
            ],
            options={
                'ordering': ['option'],
            },
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['name'], name='main_user_name_d2d935_idx'),
        ),
        migrations.AddField(
            model_name='response',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question'),
        ),
        migrations.AddField(
            model_name='response',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AddField(
            model_name='question',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Block'),
        ),
        migrations.AddField(
            model_name='block',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.DistributedPoll'),
        ),
        migrations.AddIndex(
            model_name='response',
            index=models.Index(fields=['question'], name='main_respon_questio_2f4895_idx'),
        ),
        migrations.AddConstraint(
            model_name='response',
            constraint=models.UniqueConstraint(fields=('question', 'option', 'user'), name='Single Response Copy'),
        ),
        migrations.AddIndex(
            model_name='question',
            index=models.Index(fields=['block'], name='main_questi_block_i_c7c3bc_idx'),
        ),
        migrations.AddIndex(
            model_name='block',
            index=models.Index(fields=['poll'], name='main_block_poll_id_ac8d0f_idx'),
        ),
    ]
