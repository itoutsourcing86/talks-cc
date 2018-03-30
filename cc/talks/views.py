from django.views import generic
from braces import views
from . import models

# Create your views here.


class TalkDetailView(generic.DetailView):
    model = models.TalkList
    template_name = 'talks_detail.html'

    def get_queryset(self):
        queryset = super(TalkDetailView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class TalkListView(views.LoginRequiredMixin, generic.ListView):
    model = models.TalkList
    template_name = 'talks_list.html'
    context_object_name = 'lists'

    def get_queryset(self):
        return self.request.user.lists.all()
