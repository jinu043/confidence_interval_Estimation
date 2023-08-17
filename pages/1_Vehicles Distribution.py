import numpy as np
import streamlit as st
import pandas as pd
pd.set_option("display.max_rows", None)
import plotly.express as px


data1 = pd.read_csv("data.csv")

vehicle_brands = data1["vehicle_brand"].unique().tolist()
vehicle_brand = []
data_points = []
vehicle_model = []
for brand in vehicle_brands:
    df = data1[data1["vehicle_brand"] == f'{brand}']
    for model in df["vehicle_model"].unique().tolist():
        df_model = df[df["vehicle_model"] == f'{model}']
        vehicle_brand.append(f'{brand}')
        data_points.append(df_model.shape[0])
        vehicle_model.append(f'{model}')

model_datapoints = pd.DataFrame(
    {
        "vehicle_brand": vehicle_brand,
        "vehicle_model": vehicle_model,
        "data_points": data_points
    })
modelscount = pd.DataFrame(model_datapoints["vehicle_brand"].value_counts()).reset_index().rename(
    columns={"index": "vehicle_brand",
             "vehicle_brand": "count"})
modelscount["vehicle_brand"] = modelscount["vehicle_brand"].apply(lambda x: x.strip())

fig = px.pie(modelscount, values="count", names="vehicle_brand",
            labels={"count":"Models", "vehicle_brand":"Brand"})

def descriptive_statistics(data, brand, model):
    df = data.copy()
    df = df[df["vehicle_brand"]==f"{brand}"]
    df = df[df["vehicle_model"]==f'{model}']
    statistics = df["vehicle_price"].describe()
    statistics = pd.DataFrame(np.round(statistics.loc[["max", "mean", "min"]],0))
    mileage = df["mileage"].describe()
    mileage = pd.DataFrame(np.round(mileage.loc[["max", "mean", "min"]],0))
    return statistics, mileage

st.set_page_config(page_title="Vehicles Data & Distribution",
                   layout="wide", page_icon=":1234:")

col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown("<h2 style='text-align: center'>Data Sample</h2>", unsafe_allow_html=True)
    st.dataframe(data1.sample(5), use_container_width=True, hide_index=True)
    cl1, cl2 = st.columns(2)
    with cl1:
        st.markdown("<h5 style='text-align: center'>Descriptive Statistics</h5>", unsafe_allow_html=True)
        veh_brand = st.selectbox("Brand",options = data1["vehicle_brand"].unique().tolist())
        veh_model = st.selectbox("Model", options = data1[data1["vehicle_brand"]==f"{veh_brand}"]["vehicle_model"].unique().tolist())
        stats, mil = descriptive_statistics(data1, veh_brand, veh_model)
        st.dataframe(pd.concat([stats, mil], axis=1))
    with cl2:
        st.markdown("<h5 style='text-align: center'>Available Model Years</h5>", unsafe_allow_html=True)
        Model_years = data1.query(f'vehicle_brand=="{veh_brand}" and vehicle_model=="{veh_model}"')["model_year"].unique().tolist()
        Model_Years = np.sort(np.array(Model_years))
        for i in Model_Years:
            st.markdown(f"<h6 style='text-align: center'>{i}</h6>", unsafe_allow_html=True)


with col2:
    st.markdown("<h2 style='text-align: center'>Models Distribution by Brand</h2>", unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
