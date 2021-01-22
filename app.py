import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
# import matplotlib.pyplot as plt
# import geopandas as gpd
# import folium
# from streamlit_folium import folium_static
import warnings
warnings.filterwarnings("ignore")

title = "Sprint 1 | Team No Breaks!"
st.set_page_config(page_title=title, page_icon=":school:", layout="wide", initial_sidebar_state="auto")

intro = "Introduction"
bground = "Background and Context"
dataInfo = "The Data We Used"
method = "Our Pipeline"
eda = "EDA"
cluster = "Cluster Results"
conclusion = "Conclusion"
recomm = "Recommendations"
team = "The Team"
page = st.sidebar.radio("Page Navigation", [intro, bground, dataInfo, method, eda, cluster, conclusion, recomm, team])

def insertBlankLines(num_of_blank_lines):
  for i in range(num_of_blank_lines):
    st.markdown("")

def writeText(text, align="center"):
  st.write("<h3 style='text-align: " + align + ";'>" + text + "</h3>", unsafe_allow_html=True)

if page == intro:
  col1, col2 = st.beta_columns(2)
  with col1:
    insertBlankLines(15)
    st.title("Status of school MOOE budget allocation in the Philippines in 2015")
  with col2:
    # Photo by Rasy Nak from Pexels (https://www.pexels.com/photo/close-up-photo-of-girl-holding-paper-893924/)
    image = Image.open("assets/intro1.jpg")
    st.image(image, use_column_width=True)

elif page == bground:
  col1, col2 = st.beta_columns(2)
  with col1:
    # Photo by Mikechie Esparagoza from Pexels (https://www.pexels.com/photo/photo-of-man-holding-paper-1660613/)
    image = Image.open("assets/bground1.jpg")
    st.image(image, use_column_width=True)
  with col2:
    insertBlankLines(15)
    st.subheader(bground)
    st.title("What is the question that we want to answer?")

elif page == dataInfo:
  st.title(dataInfo)
  insertBlankLines(10)

  col1, col2, col3, col4, col5, col6, col7 = st.beta_columns(7)
  with col1:
    # <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    image = Image.open("assets/school.png")
    st.image(image, use_column_width=True)
    writeText("Masterlist of Schools.csv")
  with col3:
    image = Image.open("assets/mooe.png")
    st.image(image, use_column_width=True)
    writeText("MOOE data.csv")
  with col5:
    image = Image.open("assets/room.png")
    st.image(image, use_column_width=True)
    writeText("Rooms data.csv")
  with col7:
    # <div>Icons made by <a href="" title="Vectors Market">Vectors Market</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    image = Image.open("assets/teacher.png")
    st.image(image, use_column_width=True)
    writeText("Teachers data.csv")

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

