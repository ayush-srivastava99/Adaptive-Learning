# Generated by Django 3.1.2 on 2020-10-23 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20201019_1257'),
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createassignment',
            name='info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
