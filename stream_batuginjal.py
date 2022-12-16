
import pickle
import streamlit as st

#Membaca Model
ginjal_model = pickle.load(open('penyakit_batu_ginjal.sav', 'rb'))

#Judul Web
st.title('PREDIKSI BATU GINJAL')



#membagi kolom 
col1, col2 = st.columns(2)

with col1 :
       Gravity = st.number_input('Input Nilai Gravity')

with col2 :
       Ph = st.number_input('Input Nilai Ph')

with col1 :
       Osmo = st.number_input('Input Nilai Osmo')

with col2 :
       Cond = st.number_input('Input Nilai Cond')

with col1 :
       Urea = st.number_input('Input Nilai Urea')

with col2 :
       Calc = st.number_input('Input Nilai Calc')

#code untuk prediksi
ginjal_diagnosis = ''

#membuat tombol
if st.button('Test') :
    ginjal_prediction = ginjal_model.predict([[Gravity, Ph, Osmo, Cond, Urea, Calc]])
    
    if  (ginjal_prediction[0] == 1):
           ginjal_diagnosis = 'Pasien terkena Batu Ginjal'
    else :
           ginjal_diagnosis = ' Pasien tidak terkena Batu Ginjal'

    st.success(ginjal_diagnosis)  