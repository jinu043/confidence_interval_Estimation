import streamlit as st

st.set_page_config(page_title="Confidence Interval Estimation",
                   layout="wide", page_icon=":1234:")


st.markdown("<h1 style='text-align: center'>Confidence Interval Estimation</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: justify'>Confidence interval estimation is a technique from inferential statistics method for calculating the \
 population parameters values such as range of average mean, range of average variance and range of proportion etc. My intention is to calculate the average price and average mileage \
 of used cars located in united arab emirates. I have collected data from various web sites of established automobile dealers in UAE market \
 by using python web scrapping method (used Selenium library).</h5>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: justify'>Since we have available with sample datas, we would able to calculate only \
sample statistics such as sample standard deviation, sample mean etc from the collected samples. Therefore we have to use t-distribution to calculate the \
corresponding population parameters. We can come up with some confidence level that the average price and mileage of used cars in UAE market would be within \
a particular range which would be determined by t-distribution.</h5>", unsafe_allow_html=True)

st.markdown("### Formula to calculate average price of used cars")

st.latex(r'''\overline{x} - t_{\alpha/2, {n-1}}\left(s/\sqrt{n}\right)\quad 
                                    \underline {<} \quad \mu \quad \underline {<} \quad \overline{x}  + t_{\alpha/2, {n-1}}\left(s/\sqrt{n}\right)''')

st.markdown("<h5 style='text-align: justify'>We normally use alpha values between 0.9 and 0.99. When you increase the value of alpha, width of confidence interval \
would become large which may not give a good business insights. When you decrease the value of alpha, then the confidence interval width would become too low which may \
lead to misinterpets the actual population value. Therefore we normally use alpha as 0.95 for calculating the confidence interval of population parameters such as averages \
or porportions.</h5>", unsafe_allow_html=True)
st.balloons()
