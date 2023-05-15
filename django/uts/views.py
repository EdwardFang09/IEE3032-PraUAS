from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
import paho.mqtt.client as mqtt

from .serializers import SensorSerializer
from .models import Sensor
from .models import AktuatorFinal
from .models import Sistem1
from .models import Sistem2
from .models import Sistem3
from .models import Aktuator_1
from .models import Aktuator_2
from .models import Aktuator_3

from uts import ml_new

import sqlite3
import pandas as pd
DATABASE_FILE = 'db.sqlite3'

def webview(request):
    """A view of all bands."""
    view = Sensor.objects.all().values()
    usaha1 = Sistem1.objects.all().values()
    usaha2 = Sistem2.objects.all().values()
    usaha3 = Sistem3.objects.all().values()
    akt1 = Aktuator_1.objects.all().values()
    akt2 = Aktuator_2.objects.all().values()
    akt3 = Aktuator_3.objects.all().values()
    akt_final = AktuatorFinal.objects.all().values()
    return render(request, 'webview.html', {'views': view, 'usaha1':usaha1, 'usaha2':usaha2, 'usaha3':usaha3, 'akt1':akt1, 'akt2':akt2, 'akt3':akt3, 'akt_final':akt_final})

class SensorDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()
    def retrieve(self, request, *args, **kwargs):
        temp1 = Sensor.objects.get(name="temp1")
        frik1 = Sensor.objects.get(name="frik1")
        dl1 = Sensor.objects.get(name="dl1")

        temp2 = Sensor.objects.get(name="temp2")
        frik2 = Sensor.objects.get(name="frik2")
        dl2 = Sensor.objects.get(name="dl2")

        temp3 = Sensor.objects.get(name="temp3")
        frik3 = Sensor.objects.get(name="frik3")
        dl3 = Sensor.objects.get(name="dl3")

        akt = Sensor.objects.get(name="aktuator")

        sensor_value={"Sensor Temperatur 1": int(temp1.value),
                       "Sensor Friksi 1": int(frik1.value),
                       "Sensor Daya Listrik 1": int(dl1.value),
                       
                       "Sensor Temperatur 2": int(temp2.value),
                       "Sensor Friksi 2": int(frik2.value),
                       "Sensor Daya Listrik 2": int(dl2.value),
                       
                       "Sensor Temperatur 3": int(temp3.value),
                       "Sensor Friksi 3": int(frik3.value),
                       "Sensor Daya Listrik 3": int(dl3.value),

                       "Aktuator": int(akt.value),
                       }
        
        return Response(sensor_value)     


def on_message_temp(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    temp = Sistem1.objects.get(name='temp1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Proksimitas (m):', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp1', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 

def on_message_temp2(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    temp = Sistem1.objects.get(name='temp2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Flex (°):', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp2', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 

def on_message_temp3(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    temp = Sistem1.objects.get(name='temp3')
    data = {
        'value': msg.payload.decode('utf-8')
    }

    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Berat (kg):', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp3', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 

def on_message_temp4(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    temp = Sistem1.objects.get(name='temp4')
    data = {
        'value': msg.payload.decode('utf-8')
    }

    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Suhu (C):', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp4', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 

def on_message_temp5(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    temp = Sistem1.objects.get(name='temp5')
    data = {
        'value': msg.payload.decode('utf-8')
    }

    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Tegangan (V):', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp5', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 

def on_message_temp6(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    temp = Sistem1.objects.get(name='temp6')
    data = {
        'value': msg.payload.decode('utf-8')
    }

    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Arus (A):', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp6', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 

def on_message_temp7(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    temp = Sistem1.objects.get(name='temp7')
    data = {
        'value': msg.payload.decode('utf-8')
    }

    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Tekanan (P):', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp7', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 

def on_message_temp8(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    temp = Sistem1.objects.get(name='temp8')
    data = {
        'value': msg.payload.decode('utf-8')
    }

    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Medan magnet (mT):', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp8', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 

def on_message_temp9(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    temp = Sistem1.objects.get(name='temp9')
    data = {
        'value': msg.payload.decode('utf-8')
    }

    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Radiasi (W/m2):', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp9', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 

def on_message_frik(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sistem2.objects.get(name='frik1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Ultrasonic (cm):', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik1', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_frik2(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sistem2.objects.get(name='frik2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Gas (%):', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik2', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_frik3(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sistem2.objects.get(name='frik3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('pH:', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik3', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_frik4(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sistem2.objects.get(name='frik4')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Motion:', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik4', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_frik5(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sistem2.objects.get(name='frik5')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Tilt (derajat):', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik5', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_frik6(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sistem2.objects.get(name='frik6')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Gaya (N):', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik6', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_frik7(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sistem2.objects.get(name='frik7')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Aliran (ft/s):', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik7', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_frik8(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sistem2.objects.get(name='frik8')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Vibrasi (a/s):', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik8', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_frik9(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sistem2.objects.get(name='frik9')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Warna (array):', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik9', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sistem3.objects.get(name='dl1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('CO2 (ppm):', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl1', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl2(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sistem3.objects.get(name='dl2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Cahaya (LDR):', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl2', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl3(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sistem3.objects.get(name='dl3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Kualitas udara (ppm):', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl3', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl4(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sistem3.objects.get(name='dl4')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Cuaca:', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl4', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl5(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sistem3.objects.get(name='dl5')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Kelembaban (%):', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl5', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl6(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sistem3.objects.get(name='dl6')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Kecepatan angin (m/s):', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl6', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl7(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sistem3.objects.get(name='dl7')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Radiasi (gray):', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl7', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl8(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sistem3.objects.get(name='dl8')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Suara (dB):', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl8', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl9(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sistem3.objects.get(name='dl9')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Oksigen (%):', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl9', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sensor.objects.get(name='aktuator')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator final data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator1(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_1.objects.get(name='aktuator1_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Kalsium (g)', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator1_1', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator2(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_1.objects.get(name='aktuator1_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator 2 data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator1_2', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator3(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_1.objects.get(name='aktuator1_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator 3 data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator1_3', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator4(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_2.objects.get(name='aktuator2_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator 3 data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator2_1', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator5(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_2.objects.get(name='aktuator2_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator 3 data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator2_2', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator6(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_2.objects.get(name='aktuator2_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator 3 data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator2_3', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator7(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_3.objects.get(name='aktuator3_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator 3 data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator3_1', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator8(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_3.objects.get(name='aktuator3_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator 3 data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator3_2', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator9(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_3.objects.get(name='aktuator3_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator 3 data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator3_3', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_ml(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = AktuatorFinal.objects.get(name='aktuator_finale')
    print(pred[12])
    data = {
        'value': pred[12]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Final: ', pred)  
        #cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator_ml', pred[3]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[12]})

def on_message_ml1(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_1.objects.get(name='aktuator1_1')
    data = {
        'value': pred[0]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 1_1: ', pred[0])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator1_1', pred[0]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[0]})

def on_message_ml2(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_1.objects.get(name='aktuator1_2')
    data = {
        'value': pred[1]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 1_2: ', pred[1])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator1_2', pred[1]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[1]})

def on_message_ml3(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_1.objects.get(name='aktuator1_3')
    data = {
        'value': pred[2]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 1_3: ', pred[2])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator1_3', pred[2]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[2]})

def on_message_ml4(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_2.objects.get(name='aktuator2_1')
    data = {
        'value': pred[3]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 2_1: ', pred[3])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator2_1', pred[3]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[3]})

def on_message_ml5(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_2.objects.get(name='aktuator2_2')
    data = {
        'value': pred[4]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 2_2: ', pred[4])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator2_2', pred[4]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[4]})

def on_message_ml6(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_2.objects.get(name='aktuator2_3')
    data = {
        'value': pred[5]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 2_3: ', pred[5])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator2_3', pred[5]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[5]})

def on_message_ml7(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_3.objects.get(name='aktuator3_1')
    data = {
        'value': pred[6]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 3_1: ', pred[6])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator3_1', pred[6]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[6]})

def on_message_ml8(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_3.objects.get(name='aktuator3_2')
    data = {
        'value': pred[7]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 3_2: ', pred[7])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator3_2', pred[7]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[7]})

def on_message_ml9(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_3.objects.get(name='aktuator3_3')
    data = {
        'value': pred[8]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 3_3: ', pred[8])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator3_3', pred[8]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[8]})

def on_message_ml10(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_1.objects.get(name='aktuator_1_finale')
    data = {
        'value': pred[9]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 1: ', pred[9])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator1', pred[9]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[9]})

def on_message_ml11(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_2.objects.get(name='aktuator_2_finale')
    data = {
        'value': pred[10]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 2: ', pred[10])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator2', pred[10]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[10]})

def on_message_ml12(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Aktuator_3.objects.get(name='aktuator_3_finale')
    data = {
        'value': pred[11]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt 3: ', pred[11])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator3', pred[11]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[11]})

def on_message_ml13(client, userdata, msg):
    pred = ml_new.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = AktuatorFinal.objects.get(name='aktuator_finale')
    data = {
        'value': pred[12]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Akt Final: ', pred[12])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator_finale', pred[12]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[12]})

db_conn = sqlite3.connect(DATABASE_FILE, check_same_thread=False)

client = mqtt.Client("uts")
client.user_data_set({'db_conn': db_conn})

client.message_callback_add('uts/temp1', on_message_temp)
client.message_callback_add('uts/frik1', on_message_frik)
client.message_callback_add('uts/dl1', on_message_dl)

client.message_callback_add('uts/temp2', on_message_temp2)
client.message_callback_add('uts/frik2', on_message_frik2)
client.message_callback_add('uts/dl2', on_message_dl2)

client.message_callback_add('uts/temp3', on_message_temp3)
client.message_callback_add('uts/frik3', on_message_frik3)
client.message_callback_add('uts/dl3', on_message_dl3)

client.message_callback_add('uts/temp4', on_message_temp4)
client.message_callback_add('uts/temp5', on_message_temp5)
client.message_callback_add('uts/temp6', on_message_temp6)
client.message_callback_add('uts/temp7', on_message_temp7)
client.message_callback_add('uts/temp8', on_message_temp8)
client.message_callback_add('uts/temp9', on_message_temp9)

client.message_callback_add('uts/frik4', on_message_frik4)
client.message_callback_add('uts/frik5', on_message_frik5)
client.message_callback_add('uts/frik6', on_message_frik6)
client.message_callback_add('uts/frik7', on_message_frik7)
client.message_callback_add('uts/frik8', on_message_frik8)
client.message_callback_add('uts/frik9', on_message_frik9)

client.message_callback_add('uts/dl4', on_message_dl4)
client.message_callback_add('uts/dl5', on_message_dl5)
client.message_callback_add('uts/dl6', on_message_dl6)
client.message_callback_add('uts/dl7', on_message_dl7)
client.message_callback_add('uts/dl8', on_message_dl8)
client.message_callback_add('uts/dl9', on_message_dl9)

#client.message_callback_add('uts/akt10', on_message_ml)
client.message_callback_add('uts/akt1', on_message_ml1)
client.message_callback_add('uts/akt2', on_message_ml2)
client.message_callback_add('uts/akt3', on_message_ml3)
client.message_callback_add('uts/akt4', on_message_ml4)
client.message_callback_add('uts/akt5', on_message_ml5)
client.message_callback_add('uts/akt6', on_message_ml6)
client.message_callback_add('uts/akt7', on_message_ml7)
client.message_callback_add('uts/akt8', on_message_ml8)
client.message_callback_add('uts/akt9', on_message_ml9)
client.message_callback_add('uts/akt10', on_message_ml10)
client.message_callback_add('uts/akt11', on_message_ml11)
client.message_callback_add('uts/akt12', on_message_ml12)
client.message_callback_add('uts/akt13', on_message_ml13)

""" client.message_callback_add('uts/akt2', on_message_aktuator2)
client.message_callback_add('uts/akt3', on_message_aktuator3)
client.message_callback_add('uts/akt4', on_message_aktuator4)
client.message_callback_add('uts/akt5', on_message_aktuator5)
client.message_callback_add('uts/akt6', on_message_aktuator6)
client.message_callback_add('uts/akt7', on_message_aktuator7)
client.message_callback_add('uts/akt8', on_message_aktuator8)
client.message_callback_add('uts/akt9', on_message_aktuator9) """

client.connect('localhost', 1883)
client.loop_start()
client.subscribe('uts/#')


    