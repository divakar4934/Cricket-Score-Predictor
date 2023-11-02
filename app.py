
import streamlit as st
import pickle
import pandas as pd
import numpy as np


pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['India',
 'Australia',
 'England',
 'West Indies',
 'Sri Lanka',
 'South Africa',
 'New Zealand',
 'Bangladesh',
 'Afghanistan',
 'Pakistan',
 'Netherlands']

cities =  ['London',
 'Colombo',
 'Mirpur',
 'Abu Dhabi',
 'Sydney',
 'Melbourne',
 'Rangiri',
 'Adelaide',
 'Centurion',
 'Dubai',
 'Harare',
 'Perth',
 'Sharjah',
 'Johannesburg',
 'Pallekele',
 'Brisbane',
 'Southampton',
 'Birmingham',
 'Manchester',
 'Port Elizabeth',
 'Guyana',
 'Durban',
 'Cape Town',
 'Nottingham',
 'Leeds',
 'Antigua',
 'Bulawayo',
 'St Lucia',
 'Cardiff',
 'Jamaica',
 'Auckland',
 'Chandigarh',
 'Karachi',
 'Trinidad',
 'Wellington',
 'Barbados',
 'Hambantota',
 'Mumbai',
 'Chester-le-Street',
 'Delhi',
 'St Kitts',
 'Nagpur',
 'Ahmedabad',
 'Hobart',
 'Napier',
 'Jaipur',
 'Chennai',
 'Bristol',
 'Lahore',
 'Visakhapatnam',
 'Grenada',
 'Hamilton',
 'Rajkot',
 'St Vincent',
 'Belfast',
 'Christchurch',
 'Bangalore',
 'Kolkata',
 'Bloemfontein',
 'Hyderabad',
 'Cuttack']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
 batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
 bowling_team = st.selectbox('select bowling team',sorted(teams))

city = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
 current_score = st.number_input('current score')
with col4:
 overs = st.number_input('Overs done(work for over>10)')
 with col5:
  wickets = st.number_input('Wicket out')
  last_ten = st.number_input('Runs scored in last 10 overs')

  if st.button('Predict Score'):
   balls_left = 300 - (overs*6)
   wickets_left = 10 - wickets
   crr = current_score/overs

   input_df = pd.DataFrame(
    {'batting_team': [batting_team], 'current_score' : [current_score],
     'bowling_team' :[bowling_team], 'ball': [balls_left], 'wicket_left':[wickets],
     'crr': [crr], 'last_ten':[last_ten]}
   )
   result = pipe.predict(input_df)
   st.header("Predicted Score" + str(int(result[0])))