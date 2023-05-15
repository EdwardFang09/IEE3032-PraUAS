import pandas as pd
from sklearn import linear_model
#import sklearn
import sqlite3
import numpy as np
import warnings
warnings.filterwarnings('ignore', category=UserWarning, append=True)

# Create a SQL connection to our SQLite database
def machine_learning():
    con = sqlite3.connect("db.sqlite3")

    cur = con.cursor()
    # The result of a "cursor.execute" can be iterated over by row
    df = pd.read_csv("uts/training.csv", sep = ';')
    
    X1 = df[['temp1', 'temp2', 'temp1']]
    y1 = df['aktuator1_1']

    X2 = df[['temp4', 'temp5', 'temp6']]
    y2 = df['aktuator1_2']

    X3 = df[['temp7', 'temp8', 'temp9']]
    y3 = df['aktuator1_3']

    X4 = df[['frik1', 'frik2', 'frik3']]
    y4 = df['aktuator2_1']

    X5 = df[['frik4', 'frik5', 'frik6']]
    y5 = df['aktuator2_2']

    X6 = df[['frik7', 'frik8', 'frik9']]
    y6 = df['aktuator2_3']

    X7 = df[['dl1', 'dl2', 'dl3']]
    y7 = df['aktuator3_1']

    X8 = df[['dl4', 'dl5', 'dl6']]
    y8 = df['aktuator3_2']

    X9 = df[['dl7', 'dl8', 'dl9']]
    y9 = df['aktuator3_3']

    X10 = df[['aktuator1_1', 'aktuator1_2', 'aktuator1_3']]
    y10 = df['aktuator_semifinale_1']

    X11 = df[['aktuator2_1', 'aktuator2_2', 'aktuator2_3']]
    y11 = df['aktuator_semifinale_2']

    X12 = df[['aktuator3_1', 'aktuator3_2', 'aktuator3_3']]
    y12 = df['aktuator_semifinale_3']

    X13 = df[['aktuator_semifinale_1', 'aktuator_semifinale_2', 'aktuator_semifinale_3']]
    y13 = df['aktuator_finale']

    regr1 = linear_model.LinearRegression()
    regr1.fit(X1, y1)

    regr2 = linear_model.LinearRegression()
    regr2.fit(X2, y2)

    regr3 = linear_model.LinearRegression()
    regr3.fit(X3, y3)

    regr4 = linear_model.LinearRegression()
    regr4.fit(X4, y4)

    regr5 = linear_model.LinearRegression()
    regr5.fit(X5, y5)

    regr6 = linear_model.LinearRegression()
    regr6.fit(X6, y6)

    regr7 = linear_model.LinearRegression()
    regr7.fit(X7, y7)

    regr8 = linear_model.LinearRegression()
    regr8.fit(X8, y8)

    regr9 = linear_model.LinearRegression()
    regr9.fit(X9, y9)

    regr10 = linear_model.LinearRegression()
    regr10.fit(X10, y10)

    regr11 = linear_model.LinearRegression()
    regr11.fit(X11, y11)

    regr12 = linear_model.LinearRegression()
    regr12.fit(X12, y12)

    regr13 = linear_model.LinearRegression()
    regr13.fit(X13, y13)

    df_newest_sen1 = pd.read_sql_query("SELECT * from uts_sistem1", con)
    df_newest_sen2 = pd.read_sql_query("SELECT * from uts_sistem2", con)
    df_newest_sen3 = pd.read_sql_query("SELECT * from uts_sistem3", con)
    df_newest_akt1= pd.read_sql_query("SELECT * from uts_aktuator_1", con)
    df_newest_akt2= pd.read_sql_query("SELECT * from uts_aktuator_2", con)
    df_newest_akt3= pd.read_sql_query("SELECT * from uts_aktuator_3", con)
    df_newest_akt4= pd.read_sql_query("SELECT * from uts_aktuatorfinal", con)

    df_newest_temp1 = df_newest_sen1[df_newest_sen1.name == 'temp1']
    df_newest_frik1 = df_newest_sen2[df_newest_sen2.name == 'frik1']
    df_newest_dl1 = df_newest_sen3[df_newest_sen3.name == 'dl1']

    df_newest_temp2 = df_newest_sen1[df_newest_sen1.name == 'temp2']
    df_newest_frik2 = df_newest_sen2[df_newest_sen2.name == 'frik2']
    df_newest_dl2 = df_newest_sen3[df_newest_sen3.name == 'dl2']

    df_newest_temp3 = df_newest_sen1[df_newest_sen1.name == 'temp3']
    df_newest_frik3 = df_newest_sen2[df_newest_sen2.name == 'frik3']
    df_newest_dl3 = df_newest_sen3[df_newest_sen3.name == 'dl3']

    df_newest_temp4 = df_newest_sen1[df_newest_sen1.name == 'temp4']
    df_newest_temp5 = df_newest_sen1[df_newest_sen1.name == 'temp5']
    df_newest_temp6 = df_newest_sen1[df_newest_sen1.name == 'temp6']
    df_newest_temp7 = df_newest_sen1[df_newest_sen1.name == 'temp7']
    df_newest_temp8 = df_newest_sen1[df_newest_sen1.name == 'temp8']
    df_newest_temp9 = df_newest_sen1[df_newest_sen1.name == 'temp9']

    df_newest_frik4 = df_newest_sen2[df_newest_sen2.name == 'frik4']
    df_newest_frik5 = df_newest_sen2[df_newest_sen2.name == 'frik5']
    df_newest_frik6 = df_newest_sen2[df_newest_sen2.name == 'frik6']
    df_newest_frik7 = df_newest_sen2[df_newest_sen2.name == 'frik7']
    df_newest_frik8 = df_newest_sen2[df_newest_sen2.name == 'frik8']
    df_newest_frik9 = df_newest_sen2[df_newest_sen2.name == 'frik9']

    df_newest_dl4 = df_newest_sen3[df_newest_sen3.name == 'dl4']
    df_newest_dl5 = df_newest_sen3[df_newest_sen3.name == 'dl5']
    df_newest_dl6 = df_newest_sen3[df_newest_sen3.name == 'dl6']
    df_newest_dl7 = df_newest_sen3[df_newest_sen3.name == 'dl7']
    df_newest_dl8 = df_newest_sen3[df_newest_sen3.name == 'dl8']
    df_newest_dl9 = df_newest_sen3[df_newest_sen3.name == 'dl9']

    df_akt_new1= df_newest_akt1[df_newest_akt1.name == 'aktuator1_1']
    df_akt_new2= df_newest_akt1[df_newest_akt1.name == 'aktuator1_2']
    df_akt_new3= df_newest_akt1[df_newest_akt1.name == 'aktuator1_3']
    df_akt_new4= df_newest_akt2[df_newest_akt2.name == 'aktuator2_1']
    df_akt_new5= df_newest_akt2[df_newest_akt2.name == 'aktuator2_2']
    df_akt_new6= df_newest_akt2[df_newest_akt2.name == 'aktuator2_3']
    df_akt_new7= df_newest_akt3[df_newest_akt3.name == 'aktuator3_1']
    df_akt_new8= df_newest_akt3[df_newest_akt3.name == 'aktuator3_2']
    df_akt_new9= df_newest_akt3[df_newest_akt3.name == 'aktuator3_3']

    df_akt_sem_new1= df_newest_akt1[df_newest_akt1.name == 'aktuator_1_finale']
    df_akt_sem_new2= df_newest_akt2[df_newest_akt2.name == 'aktuator_2_finale']
    df_akt_sem_new3= df_newest_akt3[df_newest_akt3.name == 'aktuator_3_finale']

    akt_sem_new1 = int(df_akt_sem_new1['value'].values[0])
    akt_sem_new2 = int(df_akt_sem_new2['value'].values[0])
    akt_sem_new3 = int(df_akt_sem_new3['value'].values[0])

    akt1_new = int(df_akt_new1['value'].values[0])
    akt2_new = int(df_akt_new2['value'].values[0])
    akt3_new = int(df_akt_new3['value'].values[0])
    akt4_new = int(df_akt_new4['value'].values[0])
    akt5_new = int(df_akt_new5['value'].values[0])
    akt6_new = int(df_akt_new6['value'].values[0])
    akt7_new = int(df_akt_new7['value'].values[0])
    akt8_new = int(df_akt_new8['value'].values[0])
    akt9_new = int(df_akt_new9['value'].values[0])

    temp1_new = int(df_newest_temp1['value'].values[0])
    temp2_new = int(df_newest_temp2['value'].values[0])
    temp3_new = int(df_newest_temp3['value'].values[0])
    temp4_new = int(df_newest_temp4['value'].values[0])
    temp5_new = int(df_newest_temp5['value'].values[0])
    temp6_new = int(df_newest_temp6['value'].values[0])
    temp7_new = int(df_newest_temp7['value'].values[0])
    temp8_new = int(df_newest_temp8['value'].values[0])
    temp9_new = int(df_newest_temp9['value'].values[0])

    frik1_new = int(df_newest_frik1['value'].values[0])
    frik2_new = int(df_newest_frik2['value'].values[0])
    frik3_new = int(df_newest_frik3['value'].values[0])
    frik4_new = int(df_newest_frik4['value'].values[0])
    frik5_new = int(df_newest_frik5['value'].values[0])
    frik6_new = int(df_newest_frik6['value'].values[0])
    frik7_new = int(df_newest_frik7['value'].values[0])
    frik8_new = int(df_newest_frik8['value'].values[0])
    frik9_new = int(df_newest_frik9['value'].values[0])

    dl1_new = int(df_newest_dl1['value'].values[0])
    dl2_new = int(df_newest_dl2['value'].values[0])
    dl3_new = int(df_newest_dl3['value'].values[0])
    dl4_new = int(df_newest_dl4['value'].values[0])
    dl5_new = int(df_newest_dl5['value'].values[0])
    dl6_new = int(df_newest_dl6['value'].values[0])
    dl7_new = int(df_newest_dl7['value'].values[0])
    dl8_new = int(df_newest_dl8['value'].values[0])
    dl9_new = int(df_newest_dl9['value'].values[0])

    a=  [temp1_new, temp2_new, temp3_new, temp4_new, temp5_new, temp6_new, temp7_new, temp8_new, temp9_new,
          frik1_new, frik2_new, frik3_new, frik4_new, frik5_new, frik6_new, frik7_new, frik8_new, frik9_new,
            dl1_new, dl2_new, dl3_new, dl4_new, dl5_new, dl6_new, dl7_new, dl8_new, dl9_new,
              akt1_new, akt2_new, akt3_new, akt4_new, akt5_new, akt6_new, akt7_new, akt8_new, akt9_new,
               akt_sem_new1, akt_sem_new2, akt_sem_new3]
    
    b = np.array(a, dtype=int)
    c = [int(i) for i in a]

    predicted_akt1_1 = regr1.predict([[c[0], c[1], c[2]]])
    predicted_akt1_2 = regr2.predict([[c[3], c[4], c[5]]])
    predicted_akt1_3 = regr3.predict([[c[6], c[7], c[8]]])
    predicted_akt2_1 = regr4.predict([[c[9], c[10], c[11]]])
    predicted_akt2_2 = regr5.predict([[c[12], c[13], c[14]]])
    predicted_akt2_3 = regr6.predict([[c[15], c[16], c[17]]])
    predicted_akt3_1 = regr7.predict([[c[18], c[19], c[20]]])
    predicted_akt3_2 = regr8.predict([[c[21], c[22], c[23]]])
    predicted_akt3_3 = regr9.predict([[c[24], c[25], c[26]]])

    predicted_akt_sem_1 = regr10.predict([[c[27], c[28], c[29]]])
    predicted_akt_sem_2 = regr11.predict([[c[30], c[31], c[32]]])
    predicted_akt_sem_3 = regr12.predict([[c[33], c[34], c[35]]])

    predicted_akt_finale = regr13.predict([[c[36], c[37], c[38]]])
    con.close()
    d = [predicted_akt1_1, predicted_akt1_2, predicted_akt1_3, predicted_akt2_1, predicted_akt2_2, predicted_akt2_3, predicted_akt3_1, predicted_akt3_2, predicted_akt3_3, predicted_akt_sem_1, predicted_akt_sem_2, predicted_akt_sem_3, predicted_akt_finale]
    e = np.array(d, dtype=int)
    f = [int(i) for i in d]
    return f
# predictedCO2 = regr.predict([[999, 950, 350]])

# print(predictedCO2)