import numpy as np
import pickle
import streamlit as st
import sklearn

FOLDER_PATH=""
STUDENT_TRAINED_MODEL_FILENAME = r"C:\Users\GOUTHAMI\OneDrive\Diabetes project\model_diabetes.pickle"
file_path=STUDENT_TRAINED_MODEL_FILENAME 
with open(file_path,'rb') as readfile:
    loaded_model=pickle.load(readfile)
    
def make_pred(ip_data):
    ip_num=np.array(ip_data).reshape(1,-1)
    pred=loaded_model.predict(ip_num)
    print(pred)
    if pred==1:
         st.success('Person has diabetes :thumbsdown:\n Consume nutritious food and prioritize maintaining your health.')
    else:
        st.success('Person does not have diabtes:thumbsup:\n Ensure to undergo the recommended tests and adhere to prescribed health maintenance guidelines.')

        
def main():
    st.title("Diabetes Prediction :honey_pot:")
    age=st.slider("Choose age (0-100) (>45 years is risk factor for diabetes) ",0,100)
    preg=st.slider("Choose pregnancies (0-17) (higher the number of pregnancies risk of having pregnancies high)",0,20)
    glucose=st.number_input("glucose level (0-199) (>140mg/dL is risk factor for diabetes) ")
    bp=st.number_input("Blood Pressure (0-122) (>80mm Hg is risk factor for diabetes)")
    skin_thickness=st.slider("Skin Thickness (0-99)(>20-30mm is risk factor for diabetes)",0,100)
    insulin=st.number_input("Insulin level (0-846) (>200mu U/ml is risk factor for diabetes)")
    bmi=st.number_input("BMI (0-67.1) (>30is riskfactor for diabetes)")
    DiabetesPedigreeFunction=st.number_input("Diabetes Pedigree Function (0.078-2.42) (>0.5 is risk factor for diabetes)")
    
    res=''
    if st.button('Check Results'):
        res=make_pred([preg,glucose,bp,skin_thickness,insulin,bmi,DiabetesPedigreeFunction,age])
        
    
if __name__=='__main__':
    main()
# Define symptoms and weights
symptoms = ["Increased thirst", "Frequent urination", "Fatigue", "Blurred vision", "Slow healing", "Tingling hands/feet", "Recurring skin, gum, or bladder infections", "Fluctuations in blood pressure", "Dark, velvety skin patches", "Erectile dysfunction"]
weights = [4, 3, 2, 3, 2, 3, 2, 2, 2, 1]

# Symptoms checker section
st.header("Symptoms Checker")
symptoms_selected = []
for i, symptom in enumerate(symptoms):
    if st.checkbox(symptom, key=f"symptom-{i}"):
        symptoms_selected.append(symptom)


# Calculate symptom score
score = sum([weights[symptoms.index(s)] for s in symptoms_selected])

# Define risk levels and thresholds
risk_levels = ["Low", "Moderate", "High"]
thresholds = [0, 6, 10]

# Map score to risk level
risk_level = risk_levels[0]
for i, threshold in enumerate(thresholds):
    if score >= threshold:
        risk_level = risk_levels[i]

# Display result
st.write(f"Your risk level: **{risk_level}**")

# Additional guidance based on risk level
if risk_level == "High":
    st.markdown("You are at high risk of having diabetes. Please consult a doctor immediately.")
elif risk_level == "Moderate":
    st.markdown("You are at moderate risk of having diabetes. Monitor your symptoms and consult a doctor if they worsen.")
else:
    st.markdown("You are at low risk of having diabetes. Keep monitoring your symptoms and stay healthy!")


