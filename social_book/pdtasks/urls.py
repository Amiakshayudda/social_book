from django.urls import path

from pdtasks.views import PdExcelTask

urlpatterns = [
    path("pdexceltask", PdExcelTask.as_view(), name="pdexceltask")
]
