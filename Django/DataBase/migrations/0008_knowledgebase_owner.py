# Generated by Django 5.1 on 2024-09-05 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DataBase", "0007_alter_user_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="knowledgebase",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="DataBase.user",
                verbose_name="知识库创建者",
            ),
        ),
    ]
