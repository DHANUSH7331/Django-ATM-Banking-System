from django.contrib import admin
from .models import Gender, RelationShip, Acc_type , State
# Register your models here.
admin.site.register(Gender)
admin.site.register(State)
admin.site.register(Acc_type)
admin.site.register(RelationShip)
