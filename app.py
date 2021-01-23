import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
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
method = "Methodology"
cluster = "Visualizing the Clusters"
conclusion = "Conclusion and Recommendations"
team = "The Team"
page = st.sidebar.radio("Page Navigation", [intro, bground, dataInfo, method, cluster, conclusion, team])

def insertBlankLines(num_of_blank_lines):
  for i in range(num_of_blank_lines):
    st.markdown("")

def writeText(text, align="center"):
  st.write("<h3 style='text-align: " + align + ";'>" + text + "</h3>", unsafe_allow_html=True)

def boxPlot(scaled_df, showfliers=True):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18,7))

    #sns.boxplot(x="Cluster_Labels", y="", data=scaled_df, ax=axes[0,0])
    #axes[0,0].set_title("Enrolment", fontsize=16)

    sns.boxplot(x=scaled_df.Cluster_Labels, y=scaled_df["mooe.student"], ax=axes[0], showfliers=showfliers)
    axes[0].set_title("MOOE per student", fontsize=22)
    axes[0].set_ylabel("value", fontsize=18)
    axes[0].set_xlabel("cluster label", fontsize=18)
    axes[0].tick_params(axis='x', labelsize=16)
    axes[0].tick_params(axis='y', labelsize=14)

    sns.boxplot(x=scaled_df.Cluster_Labels, y=scaled_df["teacher.mooe"], ax=axes[1], showfliers=showfliers)
    axes[1].set_title("MOOE per teacher", fontsize=22)
    axes[1].set_ylabel("value", fontsize=18)
    axes[1].set_xlabel("cluster label", fontsize=18)
    axes[1].tick_params(axis='x', labelsize=16)
    axes[1].tick_params(axis='y', labelsize=14)

    sns.boxplot(x=scaled_df.Cluster_Labels, y=scaled_df["rooms.mooe"], ax=axes[2], showfliers=showfliers)
    axes[2].set_title("MOOE per room", fontsize=22)
    axes[2].set_ylabel("value", fontsize=18)
    axes[2].set_xlabel("cluster label", fontsize=18)
    axes[2].tick_params(axis='x', labelsize=16)
    axes[2].tick_params(axis='y', labelsize=14)

    plt.tight_layout()
    plt.show()
    st.pyplot(fig)

if page == intro:
  col1, col2 = st.beta_columns(2)
  with col1:
    insertBlankLines(20)
    st.title("K-means Clustering of MOOE Ratios to classify Philippine Public Schools in 2015")
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
    insertBlankLines(20)
    st.subheader(bground)
    st.title("What ratios could the government use to better classify public schools to prioritize those that are in need?")

elif page == dataInfo:
  st.title(dataInfo)
  insertBlankLines(10)

  col1, col2, col3, col4, col5, col6, col7 = st.beta_columns(7)
  with col1:
    # <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    image = Image.open("assets/school.png")
    st.image(image, use_column_width=True)
    writeText("Masterlist of Schools.csv")
    st.markdown("* school.id")
  with col3:
    image = Image.open("assets/mooe.png")
    st.image(image, use_column_width=True)
    writeText("MOOE data.csv")
    st.markdown("* school.enrollment\n* school.mooe")
  with col5:
    image = Image.open("assets/room.png")
    st.image(image, use_column_width=True)
    writeText("Rooms data.csv")
    st.markdown("* rooms.standard.academic")
  with col7:
    # <div>Icons made by <a href="" title="Vectors Market">Vectors Market</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    image = Image.open("assets/teacher.png")
    st.image(image, use_column_width=True)
    writeText("Teachers data.csv")
    st.markdown("* teachers.regular")

elif page == method:
  st.title(method)
  st.subheader("Exploratory Data Analysis")
  st.markdown("- Determining the ratios that we want to focus on")
  st.subheader("Cleaning the Data Set")
  st.markdown("- Paring down the rows from 46,603 down to 41,271 removing unusable values such as NaN and inf")
  st.subheader("Feature engineering")
  st.markdown("- Student-to-teacher ratio\n- Student-to-room ratio\n- MOOE-to-student ratio\n- MOOE-to-room ratio\n- MOOE-to-teacher ratio")
  insertBlankLines(1)
  st.header("K-means clustering to develop a segmentation of the schools based on the ratios")
  st.markdown("- Iterating through different pair and trio combinations among the ratios\n- Identifying a subset among the pairings with discernible elbow\n- Obtaining silhouettes for the chosen subset")
  insertBlankLines(1)
  st.subheader("Visualizing the clusters")

elif page == cluster:
  st.title(cluster)
  st.header("Ratio of MOOE vs students, teachers, rooms")
  three_clusters = pd.read_csv('dataset/viz1.csv')
  four_clusters = pd.read_csv('dataset/viz2.csv')

  st.subheader("3 Clusters with silhouette score of 0.582639")
  st.write(three_clusters['Cluster_Labels'].value_counts().to_frame())
  insertBlankLines(8)
  st.subheader("4 Clusters with silhouette score of 0.565403")
  st.write(four_clusters['Cluster_Labels'].value_counts().to_frame())

  insertBlankLines(20)
  st.header("Visualization of the 4 Clusters")
  boxPlot(four_clusters, False)

  insertBlankLines(20)
  st.header("Visualization of the removal of Cluster 3")
  wo_outliers = four_clusters[four_clusters["Cluster_Labels"] != 3 ]
  boxPlot(wo_outliers, False)

  # Box plot of 4 clusters (MOOE ratios)
  # Box plot without cluster 3

elif page == conclusion:
  st.title(conclusion)
  insertBlankLines(5)
  st.subheader("Education")
  st.header("What strategy would you recommend based on the clusters formed?")
  st.subheader("- Deped should review MOOE budget allocation for schools in Cluster 0")
  st.subheader("- Deped should identify which factors make the MOOE budget high for schools in Cluster 3")
  insertBlankLines(12)
  st.subheader("Machine Learning")
  st.header("How can you improve your analysis?")
  st.subheader("- Try different clustering methods other than k-means (e.g. hierarchical)")
  st.subheader("- Separate non-outliers and outliers from the data set and create models for each set")

elif page == team:
  st.title("Team No Breaks")
  st.header("Mentored by Patrick Juan")
  st.subheader("Gee-R, Nico, Pash, Tim")

