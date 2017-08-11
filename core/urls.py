from django.conf.urls import url

from core.views import IndexView, LoadView, ExportView

urlpatterns = [
    url('^$', IndexView.as_view()),
    url(r'^load/', LoadView.as_view(), name='load'),
    url(r'^export/', ExportView.as_view(), name='export'),
]
