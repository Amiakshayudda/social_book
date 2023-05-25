from django.urls import path

from . import views
from excelpd.views import WriteExcelToDb

urlpatterns = [
    path("createexcel", views.export_data_to_excel, name="createexcel"),
    path("writeexceltodb", WriteExcelToDb.as_view(), name="writeexceltodb"),
]