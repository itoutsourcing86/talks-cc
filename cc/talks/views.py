from django.views import generic
from braces import views
from . import models
from . import forms
from django.shortcuts import redirect
from django.db.models import Count

# Create your views here.


class RestrictToUserMixin(views.LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class TalkDetailView(RestrictToUserMixin, generic.DetailView):
    form_class = forms.TalkForm
    http_method_names = ['get', 'post']
    model = models.TalkList
    template_name = 'talks_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TalkDetailView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = self.get_object()
            talk = form.save(commit=False)
            talk.talk_list = obj
            talk.save()
        else:
            return self.get(request, *args, **kwargs)
        return redirect(obj)


class TalkListView(RestrictToUserMixin, generic.ListView):
    model = models.TalkList
    template_name = 'talks_list.html'
    context_object_name = 'lists'

    def get_queryset(self):
        queryset = super(TalkListView, self).get_queryset()
        queryset = queryset.annotate(talk_count=Count('talks'))
        return queryset


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
