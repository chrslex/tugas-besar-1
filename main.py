import streamlit as st
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# READ DATA
df = pd.read_csv("./od_mangga.csv", index_col="id")

# Nama kabupaten atau kota 
nama_kabupaten_kota = df.loc[:, "nama_kabupaten_kota"]

# Mengambil nama kota unik dari dataframe
nama_kabupate_kota_choice = np.unique(np.array(nama_kabupaten_kota))


# STREAMLIT DATAFRAME
if st.checkbox('Tunjukkan dataframe'):
    df


# SELECT BOX STREAMLIT
a = st.selectbox("Pilih kabupaten/kota untuk diketahui perkembangan produksi mangga", nama_kabupate_kota_choice)

# PLOT LINE CHART
df_filter = df[(df["nama_kabupaten_kota"] == a)]

d = {}
st.line_chart(
    data=df_filter,
    x = "tahun",
    y = "jumlah_produksi"
)

# LINEAR MODEL PREDICTION 
st.write("PREDICTED FOR NEXT 5 YEARS")

linmodel = linear_model.LinearRegression(fit_intercept=True)
linmodel.fit(X= np.array(df_filter["tahun"]).reshape(-1,1), y=df_filter["jumlah_produksi"])

X_test = np.array([2019,2020,2021,2022,2023])
y_pred = linmodel.predict(X_test.reshape(-1,1))
# fig = plt.scatter(X_test, y_pred, color ='b')

# st.pyplot(fig)
st.line_chart(
    pd.DataFrame(
        y_pred,
        X_test
    )
)