import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config (page_title='analysis')

st.title('Analytics')
st.header('Price per sqft Geomap')

new_df= pd.read_csv('datasets_app/data_viz1.csv')
feature_text= pickle.load(open('datasets_app/feature_text.pkl','rb'))

group_df = new_df.groupby('sector')[[
    'price','price_per_sqft','built_up_area','latitude','longitude'
]].mean(numeric_only=True)

fig= px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200, height=700)

st.plotly_chart(fig,use_container_width=True)

st.header('features WordCloud')
plt.rcParams["font.family"] = "Arial"

wordcloud = WordCloud(
    width=800, 
    height=800, 
    background_color='white', 
    stopwords=set(['s']),
    min_font_size=10
).generate(feature_text)

# ✅ Create figure properly
fig, ax = plt.subplots(figsize=(8, 8))

ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")

# ✅ Pass figure to Streamlit
st.pyplot(fig)

st.header('Area vs Price ')
property_type=st.selectbox('Select Property Type',['flat','house'])
if property_type =='house':

  fig1= px.scatter(new_df[new_df['property_type']=='house'],  x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

  st.plotly_chart(fig1,use_container_width=True)
else:
  fig1= px.scatter(new_df[new_df['property_type']=='flat'],  x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

  st.plotly_chart(fig1,use_container_width=True)

st.header('BHK Pie Chart')
sector_operations=new_df['sector'].unique().tolist()
sector_operations.insert(0,'overall')
selected_sectors=st.selectbox('Select sector',sector_operations)

if selected_sectors=='overall':
  fig2= px.pie(new_df, names='bedRoom')

  st.plotly_chart(fig2,use_container_width=True)
else:
  fig2= px.pie(new_df[new_df['sector']==selected_sectors], names='bedRoom')

  st.plotly_chart(fig2,use_container_width=True) 

st.header('Side by Side BHK price comparision')
fig3= px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3,use_container_width=True)

st.header('Side by Side Displot for property type')
fig4, ax = plt.subplots(figsize=(10, 4))

sns.histplot(
    data=new_df,
    x='price',
    hue='property_type',   
    kde=True,
    stat="density",
    common_norm=False,
    alpha=0.4,
    ax=ax
)

st.pyplot(fig4)
