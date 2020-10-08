# Generated by Django 3.1.2 on 2020-10-08 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20201007_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='username',
        ),
        migrations.AddField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_teacher',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('class_present', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=2)),
                ('is_student', models.BooleanField(default=True, editable=False)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.teacher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
