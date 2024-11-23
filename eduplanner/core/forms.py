from django import forms

eventTypes = (
    ("1", "Inicio de Semestre"), 
    ("2", "Fin de Semestre"), 
    ("3", "Inicio de Inscripción de Asignaturas"), 
    ("4", "Fin de Inscripción de Asignaturas"), 
    ("5", "Receso Académico"), 
    ("6", "Inicio de Plazos de Solicitudes Administrativas"),
    ("7", "Fin de Plazos de Solicitudes Administrativas"), 
    ("8", "Inicio de Plazos para la Gestión de Beneficios"), 
    ("9", "Fin de Plazos para la Gestión de Beneficios"), 
    ("10", "Ceremonia de Titulación o Graduación"), 
    ("11", "Reunión de Consejo Académico"), 
    ("12", "Talleres y Charlas"), 
    ("13", "Día de Orientación para Nuevos Estudiantes"), 
    ("14", "Eventos Extracurriculares"), 
    ("15", "Inicio de Clases"), 
    ("16", "Último Día de Clases"), 
    ("17", "Día de Puertas Abiertas"), 
    ("18", "Suspensión de Actividades Completa"), 
    ("19", "Suspensión de Actividades Parcial"), 
)

class testform(forms.Form):
    value = forms.CharField(max_length=64)

class loginform(forms.Form):
    email       = forms.EmailField(max_length=128, widget=forms.TextInput(attrs={'id': "inputEmail", 'class': "form-control", 'aria-describedby': "emailHelp"}))
    password    = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'id': "inputPassword", 'class': "form-control"}))

class registerform(forms.Form):
    name        = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'id': "inputName", 'class': "form-control"}))
    email       = forms.EmailField(max_length=128, widget=forms.TextInput(attrs={'id': "inputEmail", 'class': "form-control", 'aria-describedby': "emailHelp"}))
    password    = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'id': "inputPassword", 'class': "form-control", 'oninput': "validatePassword()"}))
    pass_repeat = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'id': "inputRepeat", 'class': "form-control", 'oninput': "validatePassword()"}))

class eventform(forms.Form):
    name            = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'id': "inputName", 'class': "form-control"}))
    description     = forms.CharField(max_length=2048, widget=forms.Textarea(attrs={'id': "inputComment", 'class': "form-control"}))
    date_start      = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'id': "inputDateStart", 'class': "form-control", 'oninput': "verify()"}))
    date_end        = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'id': "inputDateEnd", 'class': "form-control", 'oninput': "verify()"}))
    forced          = forms.BooleanField()#widget=forms.BooleanField(attrs={'id': "inputForced", 'class': "form-control"}))
    event_type      = forms.ChoiceField(choices=eventTypes)#, widget=forms.ChoiceField(attrs={'id': "inputEventType", 'class': "form-control"}))