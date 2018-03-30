from django.views import generic
from braces import views
from . import models
from . import forms

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


class TalkCreateView(views.LoginRequiredMixin, generic.CreateView):
    model = models.TalkList
    template_name = 'talks_create.html'
    form_class = forms.TalkListForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(TalkCreateView, self).form_valid(form)


class TalksUpdateView(RestrictToUserMixin, generic.UpdateView):
    model = models.TalkList
    form_class = forms.TalkListForm
