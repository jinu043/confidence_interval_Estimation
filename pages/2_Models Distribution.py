import pandas as pd
import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
import random
import plotly.express as px
import streamlit as st

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

def vehicles_distribution(brand, data=model_datapoints):
    vehicle = model_datapoints.query(f'vehicle_brand=="{brand}"').sort_values(by="data_points")
    values = vehicle["data_points"].values
    labels = vehicle["vehicle_model"].values
    colors = sns.color_palette('bright')[0:len(values)]
    sns.set_theme(font_scale=0.8, font="serif")
    plt.rcParams["font.size"] = 5
    sns.set(rc={'axes.facecolor':'cornflowerblue', 'figure.facecolor':'#C5E8EC'})
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, colors=colors, autopct='%.0f%%', startangle=180, textprops={'family':'serif', 'fontsize':8, 'fontweight':'bold'})
    centre_circle = plt.Circle((0,0), 0.7, fc="white")
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    return fig

def random_color_generator():
    color = random.choice(list(mcolors.CSS4_COLORS.keys()))
    return color

def model_price_distribution(brand, model, data=data1.copy()):
    df = data.query(f'vehicle_brand=="{brand}"')
    df = df.query(f"vehicle_model=='{model}'")["vehicle_price"]
    fig = px.histogram(df, nbins=20, color_discrete_sequence=[f'{random_color_generator()}'], title=f"Price Distribution - {model}")
    fig.update_layout(bargap=0.01, showlegend=False, xaxis_title="Vehicle Price", yaxis_title="Count")
    fig.update_yaxes(tickfont_family="Arial Black")
    fig.update_xaxes(tickfont_family="Arial Black")
    return fig

st.set_page_config(page_title="Vehicles Data & Distribution",
                   layout="wide", page_icon=":1234:")

col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 style='text-align: center'>Vehicle Model Distribution</h3>", unsafe_allow_html=True)
    brand = data1["vehicle_brand"].unique().tolist()
    brand = st.selectbox("Brand", brand)
    brand_total = data1[data1["vehicle_brand"]==f"{brand}"]
    st.markdown(f"<h5 style='text-align: center'>Total Number of available {brand} vehicles with models sample size \
    greater than 7 are {len(brand_total)} </h5>", unsafe_allow_html=True)
    st.pyplot(vehicles_distribution(f"{brand}"), use_container_width=True)


with col2:
    st.markdown("<h3 style='text-align: center'>Model Price DIstribution</h3>", unsafe_allow_html=True)
    model = data1.query(f'vehicle_brand=="{brand}"')["vehicle_model"].unique().tolist()
    model = st.selectbox("Model", model)
    fig = model_price_distribution(brand, model)
    st.plotly_chart(fig, use_container_width=True)
    model_total = data1.query(f'vehicle_brand=="{brand}" and vehicle_model=="{model}"')
    st.markdown(f"<h6 style='text-align: center'>Total {model} vehicles - {len(model_total)}</h6>", unsafe_allow_html=True)
