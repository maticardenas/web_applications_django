# Generated by Django 4.2.2 on 2024-02-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_task_valid_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="due_date",
            field=models.DateField(blank=True, db_comment="The date when the task is due.", null=True),
        ),
        migrations.AddConstraint(
            model_name="task",
            constraint=models.CheckConstraint(
                check=models.Q(("due_date__gt", models.F("created_at"))),
                name="due_date_after_created_at",
            ),
        ),
    ]
