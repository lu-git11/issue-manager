
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)

from .models import Issue, Status
from django.urls import reverse_lazy 


class IssueListView(ListView):
    template_name = "issues/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_issues"] = Issue.objects.filter(status="1").order_by('-created_on')
        context["in_progress"] =Issue.objects.filter(status="2")
        context["complete"] = Issue.objects.filter(status="3")
        return context
        #to_do = Status.objects.get(name="to-do")
     #   context["title"] = "To-Do"
      #  context["issue_list"] = (
      #      Issue.objects
      #      .filter(status=to-do)
      #      .order_by("created_on").reverse()
      #  )
      #  return context

   # def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
      #  working = Status.objects.get(name="in-progress")
      #  context["title"] = "In-progress"
      #  context["issue_list"] = (
     #       Issue.objects
    #        .filter(status=in_progress)
     #       .order_by("created_on").reverse()
     #   )
     #   return context

    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
    #    complete = Status.objects.get(name="complete")
     #   context["title"] = "Complete"
     #   context["issue_list"] = (
     #       Issue.objects
      #      .filter(status=complete)
       #     .order_by("created_on").reverse()
      #  )
      #  return context

class IssueDetailView(DetailView):
    template_name = "issues/issue.html"
    model = Issue

class IssueCreateView(CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = [
        "title", "description", "status"
    ]
    success_url = reverse_lazy("list") 


class IssueDeleteView(DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("list")   

class IssueUpdateView(UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = [
        "status"
    ]
    success_url = reverse_lazy("list") 
    
       #* sire to be redirected after 


                      

