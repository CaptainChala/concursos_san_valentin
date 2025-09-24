from django.urls import path
from .views import RegistroParticipanteView, VerificarCorreoView, ListaParticipantesAdminView, SorteoGanadorView, SetPasswordView, AdminLoginView

urlpatterns = [
    path("registro/", RegistroParticipanteView.as_view(), name="registro"),
    path("verificar/", VerificarCorreoView.as_view(), name="verificar"),
    path("admin/participantes/", ListaParticipantesAdminView.as_view(), name="participantes"),
    path("admin/sorteo/", SorteoGanadorView.as_view(), name="sorteo"),
    path("set-password/", SetPasswordView.as_view(), name="set-password"),
    path("admin/login/", AdminLoginView.as_view(), name="admin-login"),
]
