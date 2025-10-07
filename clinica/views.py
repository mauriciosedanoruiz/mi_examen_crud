from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from clinica.models import Medico, Paciente
from clinica.forms import MedicoForm, PacienteForm 
from django.db.models import Count

# ----------------- Vistas CRUD para MÉDICO -----------------

def medico_list(request):
    # Cuenta cuántos pacientes tiene cada médico
    medicos = Medico.objects.annotate(num_pacientes=Count('paciente')).order_by('apellido')
    return render(request, 'clinica/medico_list.html', {'medicos': medicos, 'title': 'Listado de Médicos'})

def medico_detail(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    pacientes = medico.paciente_set.all() # Accede a los pacientes relacionados
    return render(request, 'clinica/medico_detail.html', {'medico': medico, 'pacientes': pacientes, 'title': 'Detalle del Médico'})

def medico_create(request):
    if request.method == 'POST':
        # request.FILES es esencial para la subida de imágenes
        form = MedicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm()
    return render(request, 'clinica/medico_form.html', {'form': form, 'accion': 'Crear Nuevo Médico', 'title': 'Crear Médico'})

def medico_update(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        # request.FILES es esencial para la actualización de imágenes
        form = MedicoForm(request.POST, request.FILES, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medico_detail', pk=medico.pk)
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'clinica/medico_form.html', {'form': form, 'accion': f'Editar a {medico.nombre}', 'title': 'Editar Médico'})

def medico_delete(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.delete()
        return redirect('medico_list')
    return render(request, 'clinica/medico_confirm_delete.html', {'medico': medico, 'title': 'Eliminar Médico'})


# ----------------- Vistas CRUD para PACIENTE -----------------

def paciente_list(request):
    # El select_related optimiza la consulta para obtener el nombre del médico
    pacientes = Paciente.objects.select_related('medico').order_by('apellido')
    return render(request, 'clinica/paciente_list.html', {'pacientes': pacientes, 'title': 'Listado de Pacientes'})

def paciente_detail(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'clinica/paciente_detail.html', {'paciente': paciente, 'title': 'Detalle del Paciente'})

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST, request.FILES)
        if form.is_valid():
            paciente = form.save()
            # Redirige al detalle del paciente recién creado
            return redirect('paciente_detail', pk=paciente.pk) 
    else:
        form = PacienteForm()
    return render(request, 'clinica/paciente_form.html', {'form': form, 'accion': 'Registrar Nuevo Paciente', 'title': 'Registrar Paciente'})

def paciente_update(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, request.FILES, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_detail', pk=paciente.pk)
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'clinica/paciente_form.html', {'form': form, 'accion': f'Editar a {paciente.nombre}', 'title': 'Editar Paciente'})

def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente_list')
    return render(request, 'clinica/paciente_confirm_delete.html', {'paciente': paciente, 'title': 'Eliminar Paciente'})