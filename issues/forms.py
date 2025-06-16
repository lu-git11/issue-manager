from .models import Issue


class IssueCreationForm(Issue):
    model = Issue
    fields = ("title", "description", "status")
    labels = {
        "title": ("Title"),
        "description": ("Description"),
        "status": ("Status")
    }