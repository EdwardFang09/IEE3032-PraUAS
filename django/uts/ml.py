import pandas as pd
from sklearn import linear_model
#import sklearn
import sqlite3
import numpy as np

# Create a SQL connection to our SQLite database
def machine_learning():
    con = sqlite3.connect("db.sqlite3")

    cur = con.cursor()
    # The result of a "cursor.execute" can be iterated over by row
    df = pd.read_sql_query("SELECT * from uts_sensordata", con)
    df_temp1 = df[df.name == 'temp1']
    df_frik1 = df[df.name == 'frik1']
    df_dl1 = df[df.name == 'dl1']

    df_temp2 = df[df.name == 'temp2']
    df_frik2 = df[df.name == 'frik2']
    df_dl2 = df[df.name == 'dl2']

    df_temp3 = df[df.name == 'temp3']
    df_frik3 = df[df.name == 'frik3']
    df_dl3 = df[df.name == 'dl3']

    df_akt = df[df.name == 'aktuator']
    df_akt1 = df[df.name == 'aktuator1']
    df_akt2 = df[df.name == 'aktuator2']
    df_akt3 = df[df.name == 'aktuator3']

    # Verify that result of SQL query is stored in the dataframe
    #print(df.head())

    temp1 = df_temp1['value'].values
    temp2 = df_temp2['value'].values
    temp3 = df_temp3['value'].values

    frik1 = df_frik1['value'].values
    frik2 = df_frik2['value'].values
    frik3 = df_frik3['value'].values

    dl1 = df_dl1['value'].values
    dl2 = df_dl2['value'].values
    dl3 = df_dl3['value'].values

    akt = df_akt['value'].values
    akt1 = df_akt1['value'].values
    akt2 = df_akt2['value'].values
    akt3 = df_akt3['value'].values

    df_new = pd.DataFrame(list(zip(temp1, temp2, temp3, frik1, frik2, frik3, dl1, dl2, dl3, akt, akt1, akt2, akt3)),
                columns =['Gas', 'Suhu', 'PH', 'Volume', 'Berat', 'Kelembaban', 'Musim', 'Sales', 'Jumlah_pengunjung', 'Aktuator', 'aktuator1', 'aktuator2', 'aktuator3'])

    X1 = df_new[['Gas', 'Suhu', 'PH']]
    y1 = df_new['aktuator1']

    X2 = df_new[['Volume', 'Berat', 'Kelembaban']]
    y2 = df_new['aktuator2']

    X3 = df_new[['Musim', 'Sales', 'Jumlah_pengunjung']]
    y3 = df_new['aktuator3']

    regr1 = linear_model.LinearRegression()
    regr1.fit(X1, y1)

    regr2 = linear_model.LinearRegression()
    regr2.fit(X2, y2)

    regr3 = linear_model.LinearRegression()
    regr3.fit(X3, y3)

    df_newest = pd.read_sql_query("SELECT * from uts_sensor", con)
    df_newest_temp1 = df_newest[df_newest.name == 'temp1']
    df_newest_frik1 = df_newest[df_newest.name == 'frik1']
    df_newest_dl1 = df_newest[df_newest.name == 'dl1']

    df_newest_temp2 = df_newest[df_newest.name == 'temp2']
    df_newest_frik2 = df_newest[df_newest.name == 'frik2']
    df_newest_dl2 = df_newest[df_newest.name == 'dl2']

    df_newest_temp3 = df_newest[df_newest.name == 'temp3']
    df_newest_frik3 = df_newest[df_newest.name == 'frik3']
    df_newest_dl3 = df_newest[df_newest.name == 'dl3']

    df_newest_akt = df_newest[df_newest.name == 'aktuator']
    df_newest_akt1 = df_newest[df_newest.name == 'aktuator1']
    df_newest_akt2 = df_newest[df_newest.name == 'aktuator2']
    df_newest_akt3 = df_newest[df_newest.name == 'aktuator3']

    temp1_new = int(df_newest_temp1['value'].values[0])
    temp2_new = int(df_newest_temp2['value'].values[0])
    temp3_new = int(df_newest_temp3['value'].values[0])

    frik1_new = int(df_newest_frik1['value'].values[0])
    frik2_new = int(df_newest_frik2['value'].values[0])
    frik3_new = int(df_newest_frik3['value'].values[0])

    dl1_new = int(df_newest_dl1['value'].values[0])
    dl2_new = int(df_newest_dl2['value'].values[0])
    dl3_new = int(df_newest_dl3['value'].values[0])

    akt_new= df_newest_akt['value'].values[0]
    akt_new1= df_newest_akt1['value'].values[0]
    akt_new2= df_newest_akt2['value'].values[0]
    akt_new3= df_newest_akt3['value'].values[0]

    a=  [temp1_new, temp2_new, temp3_new, frik1_new, frik2_new, frik3_new, dl1_new, dl2_new, dl3_new, akt_new1, akt_new2, akt_new3]
    b = np.array(a, dtype=int)
    c = [int(i) for i in a]

    predicted_akt1 = regr1.predict([[c[0], c[1], c[2]]])
    predicted_akt2 = regr1.predict([[c[3], c[4], c[5]]])
    predicted_akt3 = regr1.predict([[c[6], c[7], c[8]]])
    # df_akt = pd.DataFrame(list(zip(predicted_akt1, predicted_akt2, predicted_akt3)),
    #             columns =['aktuator1', 'aktuator2', 'aktuator3'])
    
    # X4 = df_akt[['aktuator1', 'aktuator2', 'aktuator3']]
    # y4 = df_new['Aktuator']

    # regr = linear_model.LinearRegression()
    # regr.fit(X4, y4)
    # predicted_akt = regr.predict([[c[9], c[10], c[11]]])
    
    con.close()
    return predicted_akt1, predicted_akt2, predicted_akt3

# predictedCO2 = regr.predict([[999, 950, 350]])

# print(predictedCO2)