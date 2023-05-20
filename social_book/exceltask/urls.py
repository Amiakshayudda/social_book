from django.urls import path

from exceltask.views import ReadExcelView, GetTopBook, ReadNewExcelView, SimpleReadExcelView

urlpatterns = [
    path("uploadexcel", ReadExcelView.as_view(), name="uploadexcel"),
    path("gettopbook", GetTopBook.as_view(), name="gettopbook"),
    path("uploadnewexcel", ReadNewExcelView.as_view(), name="uploadnewexcel"),
    path('fetchall', SimpleReadExcelView.as_view(), name='fetchall')
    # path("generateexcel", CreateExcelDFView, name="generateexcel")
]
