from django.contrib import admin
from .models import Sensor
from .models import SensorData
from .models import Aktuator_1
from .models import Aktuator_2
from .models import Aktuator_3
from .models import AktuatorFinal
from .models import Sistem1
from .models import Sistem2
from .models import Sistem3

admin.site.register(Sensor)
admin.site.register(SensorData)
admin.site.register(Aktuator_1)
admin.site.register(Aktuator_2)
admin.site.register(Aktuator_3)
admin.site.register(AktuatorFinal)
admin.site.register(Sistem1)
admin.site.register(Sistem2)
admin.site.register(Sistem3)