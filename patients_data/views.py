from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm  # Import the form we will create


# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")


def home(request):
    return render(request, "home.html")



def patient_list(request):
    patients = Patient.objects.all()  # Fetch all patients
    return render(request, 'patients_data/patient_list.html', {'patients': patients})

def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('patient_list')
            except Exception as e:
                # Add error message to form context
                return render(request, 'patients_data/patient_form.html', {
                    'form': form,
                    'error_message': f"Error saving patient: {str(e)}"
                })
        else:
            # Add form errors to context
            return render(request, 'patients_data/patient_form.html', {
                'form': form,
                'form_errors': form.errors
            })
    else:
        form = PatientForm()
    return render(request, 'patients_data/patient_form.html', {
        'form': form,
        'form_errors': None,
        'error_message': None
    })


def patient_update(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            try:
                form.save()
                return redirect('patient_list')
            except Exception as e:
                return render(request, 'patients_data/patient_form.html', {
                    'form': form,
                    'error_message': f"Error updating patient: {str(e)}"
                })
        else:
            return render(request, 'patients_data/patient_form.html', {
                'form': form,
                'form_errors': form.errors
            })
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients_data/patient_form.html', {
        'form': form,
        'form_errors': None,
        'error_message': None
    })



def patient_delete(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == "POST":
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patients_data/patient_confirm_delete.html', {'patient': patient})

def about(request):
    """Render the about page"""
    return render(request, 'patients_data/about.html')

def contact(request):
    """Render the contact page"""
    return render(request, 'patients_data/contact.html')
