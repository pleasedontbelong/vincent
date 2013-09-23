from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.contrib.messages import api as messages_api
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import curry



class SuccessURLRedirectDetailMixin(object):
    """
    Inspired on SuccessURLRedirectListMixin mixin on ``braces``.
    It's used basically with the create and edit CBV
    and it will redirect to the detail view of the element.
    """
    success_detail_url = None
    success_detail_kwarg = None
    success_detail_attribute = None

    def get_success_url(self):
        # Return the reversed success url.
        if None in (self.success_detail_url, self.success_detail_kwarg, self.success_detail_attribute):
            raise ImproperlyConfigured(
                "%(cls)s is missing a class setting "
                "to reverse and redirect. Define "
                "%(cls)s.success_detail_url, success_detail_kwarg and success_detail_attribute"
                "or override %(cls)s.get_success_url()"
                "." % {"cls": self.__class__.__name__})
        return reverse(self.success_detail_url, kwargs={
            self.success_detail_kwarg: getattr(self.object, self.success_detail_attribute)
        })


class MessageWrapper(object):
    """Wrap the django.contrib.messages.api module to automatically pass a given
    request object as the first parameter of function calls.
    """
    def __init__(self, request):
        self.request = request

    def __getattr__(self, attr):
        """Retrieve the function in the messages api and curry it with the
        instance's request.
        """
        fn = getattr(messages_api, attr)
        return curry(fn, self.request)


class MessageMixin(object):
    """Add a `messages` attribute on the view instance that wraps
    `django.contrib .messages`, automatically passing the current request object.
    """
    def dispatch(self, request, *args, **kwargs):
        self.messages = MessageWrapper(request)
        return super(MessageMixin, self).dispatch(request, *args, **kwargs)


class FormMessageMixin(MessageMixin):
    """Add contrib.messages support in views that use FormMixin."""
    form_valid_message = _("Your information has been saved successfully.")
    form_invalid_message = _("Please correct the errors in the form then re-submit.")

    def form_valid(self, form):
        response = super(FormMessageMixin, self).form_valid(form)
        if self.form_valid_message:
            self.messages.success(self.form_valid_message)
        return response

    def form_invalid(self, form):
        response = super(FormMessageMixin, self).form_invalid(form)
        if self.form_invalid_message:
            self.messages.error(self.form_invalid_message)
        return response


class DeleteMessageMixin(MessageMixin):
    """Provide message support to generic.DeleteView."""

    @property
    def delete_message(self):
        msg = _("The %(object_name)s has been deleted.")
        return msg % {'object_name': self.model._meta.verbose_name}

    def delete(self, request, *args, **kwargs):
        response = super(DeleteMessageMixin, self).delete(request, *args, **kwargs)
        self.messages.success(self.delete_message)
        return response
