import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config (page_title='price predictor')

with open('df.pkl','rb') as file:
  df=pickle.load(file)


with open('pipeline.pkl','rb') as file:
  pipeline=pickle.load(file)

st.header('enter your inputs')
#property type
property_type= st.selectbox('Property Type',['flat','house'])

#sector
sector= st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

#bedroom
bedroom= float(st.selectbox('Number of bedrooms',sorted(df['bedRoom'].unique().tolist())))

#bathroom
bathroom= float(st.selectbox('Number of bathrooms',sorted(df['bathroom'].unique().tolist())))

#balcony
balcony= st.selectbox('Number of balconies',sorted(df['balcony'].unique().tolist()))

#agepossesion
property_age= st.selectbox('property age',sorted(df['agePossession'].unique().tolist()))

#built_up_area
built_up_area= st.number_input('Bulit up area')

#servant room
servant_room=float(st.selectbox('servant room',[0.0,1.0]))

#store room
store_room=float(st.selectbox('store room',[0.0,1.0]))

#furnishsing type
furnishing_type= st.selectbox('Furnishing type',sorted(df['furnishing_type'].unique().tolist()))

#furnishsing type
luxury_category= st.selectbox('luxury category',sorted(df['luxury_category'].unique().tolist()))

#floor category
floor_category= st.selectbox('floor category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
  #form a dataframe
  data=[property_type,sector,bedroom,bathroom,balcony,property_age,built_up_area,servant_room,store_room,furnishing_type,luxury_category,floor_category]
  columns=['property_type','sector','bedRoom','bathroom','balcony','agePossession','built_up_area','servant room','store room','furnishing_type','luxury_category','floor_category']

  #convert to df
  one_df= pd.DataFrame([data],columns=columns)

  st.dataframe(one_df)

  #predict
  base_price=np.expm1(pipeline.predict(one_df))[0]
  low= base_price - 0.22
  high = base_price + 0.22

  #display
  st.text('the price of the flat is between {} Cr and {} Cr'.format(round(low,2) , round(high,2)))