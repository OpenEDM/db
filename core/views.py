from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, CreateView, TemplateView
from openpyxl.writer.excel import save_virtual_workbook

from core.forms import LoadForm
from core.utils import Exporter


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'


class LoadView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'core/load.html'
    form_class = LoadForm
    permission_required = 'can_load'

    def get_initial(self):
        return {
            'user': self.request.user
        }

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('load')


class ExportView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'can_export'

    def get(self, request):
        wb = Exporter().export()
        response = HttpResponse(content=save_virtual_workbook(wb),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=myexport.xlsx'
        return response
