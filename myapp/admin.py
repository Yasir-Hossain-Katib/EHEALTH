from django.contrib import admin
from myapp.models import patient
from myapp.models import doctor
from myapp.models import Data
from myapp.models import DocProfile
from myapp.models import Payment



# Register your models here.
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(Data)
admin.site.register(Payment)


class DocProfileAdmin(admin.ModelAdmin):
    list_display=("name","email","degree","gender","institute","specialist","fees")

admin.site.register(DocProfile,DocProfileAdmin)