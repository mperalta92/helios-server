from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView
from django.views.generic import TemplateView

import helios
from helios.models import Election
from helios.views import get_election_govote_url
from helios_auth.security import get_user
from signbook.forms.verify_form import VerifyForm


class IndexView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        election = Election.objects.first()
        url = get_election_govote_url(election)
        if get_user(request):
            # pass
            return redirect(url)
        else:
            return redirect("http://localhost:8000/auth/password/login")


class MerkleView(FormView):
    form_class = VerifyForm
    template_name = "verify.html"
    success_url = "merkle_result"

    def form_valid(self, form):
        # form.instance here would be == SomeModel.objects.get(pk=pk_from_kwargs)
        return super(MerkleView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(MerkleView, self).get_context_data(**kwargs)
        context['TEMPLATE_BASE'] = helios.TEMPLATE_BASE
        context['result'] = False
        return context

class MerkleResultView(TemplateView):
    template_name = "verified.html"

    def get_context_data(self, **kwargs):
        context = super(MerkleResultView, self).get_context_data(**kwargs)
        context['TEMPLATE_BASE'] = helios.TEMPLATE_BASE
        return context
