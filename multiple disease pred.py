import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading saved models

heart_disease_model = pickle.load(open("C:/Users/kesav/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("C:/Users/kesav/Desktop/Multiple Disease Prediction System/saved models/parkinsons_model.sav", 'rb'))


#navigation sidebar

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons = ['heart', 'person'],
                           default_index = 0)
    
    
#prediction page
if (selected == 'Heart Disease Prediction'):
    #page title
    st.title ('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex (1 = male; 0 = female)')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)

if (selected == 'Parkinsons Prediction'):
    #page title
    st.title ('Parkinsons Prediction using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP RAP')
        
    with col2:
        PPQ = st.text_input('MDVP PPQ')
        
    with col3:
        DDP = st.text_input('Jitter DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer APQ5')
        
    with col3:
        APQ = st.text_input('MDVP APQ')
        
    with col4:
        DDA = st.text_input('Shimmer DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)