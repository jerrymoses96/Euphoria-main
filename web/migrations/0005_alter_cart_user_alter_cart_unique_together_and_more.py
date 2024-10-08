# Generated by Django 5.0.6 on 2024-09-03 10:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_customuser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'product')},
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
