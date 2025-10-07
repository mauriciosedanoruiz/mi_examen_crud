from django.contrib import admin
from clinica.models import Medico, Paciente

# Registra tus modelos aquí.
# Esto hace que las tablas 'Medico' y 'Paciente' sean visibles y
# editables en http://localhost:8000/admin/
admin.site.register(Medico)
admin.site.register(Paciente)