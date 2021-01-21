import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import geopandas as gpd
# import folium
# from streamlit_folium import folium_static
import warnings
warnings.filterwarnings('ignore')

intro = 'Introduction'
bground = 'Background'
dataInfo = 'Meet Our Data'
method = 'Our Pipeline'
eda = 'EDA'
cluster = 'Cluster Results'
conclusion = 'Conclusion'
recomm = 'Recommendations'
team = 'The Team'
page = st.sidebar.radio('Page Navigation', [intro, bground, dataInfo, method, eda, cluster, conclusion, recomm, team])

if page == intro:
    st.header("Put title of presentation here")
    st.subheader("Put subtitle here")

elif page == bground:
    st.header("Background and Context")
    st.subheader("Put subtitle here")

elif page == dataInfo:
    st.header(dataInfo)
    st.subheader("Put subtitle here")

elif page == method:
    st.header(method)
    st.subheader("Put subtitle here")

elif page == eda:
    st.header(eda)
    st.subheader("Put subtitle here")

elif page == cluster:
    st.header(cluster)
    st.subheader("Put subtitle here")

elif page == conclusion:
    st.header(conclusion)
    st.subheader("Put subtitle here")

elif page == recomm:
    st.header(recomm)
    st.subheader("Put subtitle here")

elif page == team:
    st.header(team)
    st.subheader("Put subtitle here")