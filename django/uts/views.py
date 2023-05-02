from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
import paho.mqtt.client as mqtt

from .serializers import SensorSerializer
from .models import Sensor
from uts import ml

import sqlite3
import pandas as pd
DATABASE_FILE = 'db.sqlite3'

def webview(request):
    """A view of all bands."""
    view = Sensor.objects.all().values()
    return render(request, 'webview.html', {'views': view})

class SensorDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()
    def retrieve(self, request, *args, **kwargs):
        temp1 = Sensor.objects.get(name="temp1")
        frik1 = Sensor.objects.get(name="getar1")
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
    temp = Sensor.objects.get(name='temp1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Gas data ', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp1', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 

def on_message_temp2(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    temp = Sensor.objects.get(name='temp2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Suhu data ', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp2', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 

def on_message_temp3(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    temp = Sensor.objects.get(name='temp3')
    data = {
        'value': msg.payload.decode('utf-8')
    }

    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new pH data ', msg.payload.decode('utf-8'))    
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('temp3', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')}) 


def on_message_frik(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sensor.objects.get(name='frik1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Volume data ', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik1', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_frik2(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sensor.objects.get(name='frik2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Berat data ', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik2', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_frik3(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    frik = Sensor.objects.get(name='frik3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Kelembaban data ', msg.payload.decode('utf-8'))   
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('frik3', msg.payload.decode('utf-8')))
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sensor.objects.get(name='dl1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Musim data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl1', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl2(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sensor.objects.get(name='dl2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Sales data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl2', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_dl3(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sensor.objects.get(name='dl3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Jumlah Pengunjung data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('dl3', msg.payload.decode('utf-8')))  
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
    dl = Sensor.objects.get(name='aktuator1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator 1 data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator1', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator2(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sensor.objects.get(name='aktuator2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator 2 data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator2', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aktuator3(client, userdata, msg):
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sensor.objects.get(name='aktuator3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aktuator 3 data ', msg.payload.decode('utf-8'))  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator3', msg.payload.decode('utf-8')))  
        db_conn.commit()
        cursor.close()
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_ml(client, userdata, msg):
    pred = ml.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sensor.objects.get(name='aktuator_ml')
    data = {
        'value': pred[3]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction Final: ', pred[3])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator_ml', pred[3]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[3]})

def on_message_ml1(client, userdata, msg):
    pred = ml.machine_learning()
    print(pred)
    print(pred[0])
    print(pred[0][0])
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sensor.objects.get(name='aktuator_ml1')
    data = {
        'value': pred[0][0]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction 1: ', pred[0][0])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator_ml1', pred[0][0]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[0][0]})

def on_message_ml2(client, userdata, msg):
    pred = ml.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sensor.objects.get(name='aktuator_ml2')
    data = {
        'value': pred[1][0]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction 2: ', pred[1][0])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator_ml2', pred[1][0]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[1][0]})

def on_message_ml3(client, userdata, msg):
    pred = ml.machine_learning()
    db_conn = userdata['db_conn']
    cursor = db_conn.cursor()
    dl = Sensor.objects.get(name='aktuator_ml3')
    data = {
        'value': pred[2][0]
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('Prediction 3: ', pred[2][0])  
        cursor.execute('INSERT INTO uts_sensordata (name, value) VALUES (?,?)', ('aktuator_ml3', pred[2][0]))  
        db_conn.commit()
        cursor.close()
    return Response({"value": pred[2][0]})

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

#client.message_callback_add('uts/aktuator', on_message_aktuator)
client.message_callback_add('uts/akt1', on_message_aktuator1)
client.message_callback_add('uts/akt2', on_message_aktuator2)
client.message_callback_add('uts/akt3', on_message_aktuator3)

# client.message_callback_add('uts/aktuator_ml', on_message_ml)
client.message_callback_add('uts/akt_ml1', on_message_ml1)
client.message_callback_add('uts/akt_ml2', on_message_ml2)
client.message_callback_add('uts/akt_ml3', on_message_ml3)

client.connect('localhost', 1883)
client.loop_start()
client.subscribe('uts/#')


    