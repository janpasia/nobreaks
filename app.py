import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import geopandas as gpd
# import folium
# from streamlit_folium import folium_static
import warnings
warnings.filterwarnings("ignore")

title = "Sprint 1 | Team No Breaks!"
st.set_page_config(page_title=title, page_icon=":school:", layout="centered", initial_sidebar_state="collapsed")

intro = "Introduction"
bground = "Background"
dataInfo = "Meet Our Data"
method = "Our Pipeline"
eda = "EDA"
cluster = "Cluster Results"
conclusion = "Conclusion"
recomm = "Recommendations"
team = "The Team"
page = st.sidebar.radio("Page Navigation", [intro, bground, dataInfo, method, eda, cluster, conclusion, recomm, team])

if page == intro:
  st.title("Status of school MOOE budget allocation in the Philippines in 2015")
  st.subheader("Put subtitle here")

elif page == bground:
  st.title("Background and Context")
  st.subheader("Put subtitle here")

elif page == dataInfo:
  st.title(dataInfo)
  st.subheader("Put subtitle here")

elif page == method:
  st.title(method)
  st.subheader("Put subtitle here")

elif page == eda:
  st.title("Exploratory Data Analysis")
  st.subheader("Put subtitle here")

elif page == cluster:
  st.title(cluster)
  st.subheader("Put subtitle here")

elif page == conclusion:
  st.title(conclusion)
  st.subheader("Put subtitle here")

elif page == recomm:
  st.title(recomm)
  st.subheader("Put subtitle here")

elif page == team:
  st.title(team)
  st.header("Team No Breaks")
  st.markdown("Mentored by Patrick Juan")
  st.markdown("Gee-R, Nico, Pash, Tim")

