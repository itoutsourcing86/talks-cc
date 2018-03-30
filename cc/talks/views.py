from django.views import generic
from braces import views
from . import models

# Create your views here.


class RestrictToUserMixin(views.LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class TalkDetailView(RestrictToUserMixin, generic.DetailView):
    model = models.TalkList
    template_name = 'talks_detail.html'


class TalkListView(RestrictToUserMixin, generic.ListView):
    model = models.TalkList
    template_name = 'talks_list.html'
    context_object_name = 'lists'
