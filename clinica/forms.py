from django import forms
from clinica.models import Medico, Paciente

# Formulario para Médico
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'especialidad', 'telefono', 'foto']
        labels = {
            'foto': 'Foto del Médico',
            'telefono': 'Teléfono de Contacto',
        }
        
# Formulario para Paciente
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        # Incluye 'medico' como campo para la clave foránea
        fields = ['medico', 'nombre', 'apellido', 'edad', 'historial', 'foto']
        labels = {
            'foto': 'Foto del Paciente',
            'medico': 'Médico Asignado',
        }