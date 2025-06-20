# Generated by Django 5.2.2 on 2025-06-13 10:35

from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        "to-do": "Work to be completed",
        "in-progress": "Work currently being completed",
        "complete": "Work that is finished"
    }
    Status = apps.get_model("issues", "Status")
    for key, value in entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]
