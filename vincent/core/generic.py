from django.views import generic
from .mixins import FormMessageMixin, DeleteMessageMixin, MessageMixin


class DetailView(MessageMixin, generic.DetailView):
    """
    Extending django's generic view to add MessageMixin's functionality
    """


class ListView(MessageMixin, generic.ListView):
    """
    Extending django's generic view to add MessageMixin's functionality
    """


class CreateView(FormMessageMixin, generic.CreateView):
    """
    Extending django's generic view to add FormMessageMixin's functionality
    """


class UpdateView(FormMessageMixin, generic.UpdateView):
    """
    Extending django's generic view to add FormMessageMixin's functionality
    """


class DeleteView(DeleteMessageMixin, generic.DeleteView):
    """
    Extending django's generic view to add DeleteMessageMixin's functionality
    """
