# Generated by Django 4.1.7 on 2023-03-01 08:25

from django.db import migrations


def transfer_tags(apps, schema_editor):
    Issue = apps.get_model('issue_tracker.Issue')

    for issue in Issue.objects.all():
        issue.tags.set(issue.tags_old.all())


def rollback_transfer(apps, schema_editor):
    Issue = apps.get_model('issue_tracker.Issue')

    for issue in Issue.objects.all():
        issue.tags_old.set(issue.tags.all())


class Migration(migrations.Migration):
    dependencies = [
        ("issue_tracker", "0002_rename_type_issue_type_old"),
    ]


operations = [

    migrations.RunPython(transfer_tags, rollback_transfer)

]
