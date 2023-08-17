import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stat
import warnings
warnings.filterwarnings('ignore')

data1 = pd.read_csv("data.csv")

def CI_VehiclePrice(confidence, brand, model, data=data1.copy(), round=0):
    vehicle_data = data.query(f'vehicle_brand=="{brand}" and vehicle_model=="{model}"')["vehicle_price"].tolist()
    lower_mean, upper_mean = stat.t.interval(confidence,
                                          df=len(vehicle_data)-1, loc=np.mean(vehicle_data),
                                          scale=stat.sem(vehicle_data))
    lower_mean = np.round(lower_mean, round)
    upper_mean = np.round(upper_mean, round)
    average = np.round(np.mean(vehicle_data))
    return lower_mean, upper_mean, average

st.set_page_config(page_title="Vehicles Data & Distribution",
                   layout="wide", page_icon=":1234:")

st.markdown("<h3 style='text-align: center'>Confidence Interval Estimation of Vehicle Price</h3>", unsafe_allow_html=True)
brand = data1["vehicle_brand"].unique().tolist()
brand = st.selectbox("Brand", brand)
model = data1.query(f'vehicle_brand=="{brand}"')["vehicle_model"].unique().tolist()
model = st.selectbox("Model", model)
confidence = st.slider("Confidence", 0.9, 0.99, 0.95, 0.01)
st.divider()
lm, um, avg = CI_VehiclePrice(confidence, brand, model)
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<h5 style='text-align: left'>{brand} - {model} - Average Price in UAE Market</h5>", unsafe_allow_html=True)
    st.markdown(f'Lower Average : :red[**AED {lm}**]')
    st.write(f'Upper Average : :red[**AED {um}**]')
    st.write(f'Sample Statistic : :orange[**AED {avg}**]')
    st.write(f'Confidence Interval Width :  :violet[**AED {um - lm}**]')
with col2:
    st.markdown(f"<h5 style='text-align: center'>Business Insights</h5>",
                unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align: justify'>As we can see from the statistical results(left), the average vehicle prices of \
    brand <mark style = 'background-color:#C5E8EC;color:black;font-weight:bold'>{brand.lower()}</mark> and model \
    <mark style = 'background-color:#C5E8EC;color:black;font-weight:bold'>{model.lower()}</mark> \
    in UAE market would range between <mark style = 'background-color:#C5E8EC;color:red;font-weight:bold'>AED {lm}</mark> and \
    <mark style = 'background-color:#C5E8EC;color:red;font-weight:bold'>AED {um}</mark>. It means, if we take a sample of \
    <mark style = 'background-color:#C5E8EC;color:black;font-weight:bold'>{model.lower()}</mark> models, we can say that with \
    <mark style = 'background-color:#C5E8EC;color:black;font-weight:bold'>{confidence*100}%</mark> confidence/probablity, the average price of {model.lower()} \
    in UAE market would range between above prices. We can get the different price range when we change the confidecnce level. But as we described in inferential \
    statistics, by increasing the confidence level, width of confidence interval will also increase. Therefore we always prefer confidence values as 0.95</h6>",
                unsafe_allow_html=True)