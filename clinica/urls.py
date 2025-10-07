from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio
    path('', views.medico_list, name='inicio'),

    # CRUD Médico
    path('medicos/', views.medico_list, name='medico_list'),
    path('medicos/<int:pk>/', views.medico_detail, name='medico_detail'),
    path('medicos/nuevo/', views.medico_create, name='medico_create'),
    path('medicos/<int:pk>/editar/', views.medico_update, name='medico_update'),
    path('medicos/<int:pk>/eliminar/', views.medico_delete, name='medico_delete'),

    # CRUD Paciente
    path('pacientes/', views.paciente_list, name='paciente_list'),
    path('pacientes/<int:pk>/', views.paciente_detail, name='paciente_detail'),
    path('pacientes/nuevo/', views.paciente_create, name='paciente_create'),
    path('pacientes/<int:pk>/editar/', views.paciente_update, name='paciente_update'),
    path('pacientes/<int:pk>/eliminar/', views.paciente_delete, name='paciente_delete'),
]
