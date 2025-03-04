import numpy as np
import pickle
import streamlit as st

# Load the trained model
loader_model = pickle.load(open('trained_model.sav', 'rb'))

def asd(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loader_model.predict(input_data_reshaped)
    if prediction == 0:
        return 'Patient is ASD'
    else:
        return 'Patient is non-ASD'

def main():
    # Add background image
    def add_bg_from_url():
        st.markdown(
            """
            <style>
            .stApp {
                background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRu_KYZhfsUNpCDDrdk-BGINsbdKP33kzY4mw&s");
                background-attachment: fixed;
                background-size: cover;
                font-family: 'Arial', sans-serif;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    add_bg_from_url()

    # App title and description
    st.markdown(
        """
        <h1 style="font-family: 'Comic Sans MS', cursive; color: #ff5733; text-align: center; 
        text-shadow: 2px 2px 4px #000000;">Autism Spectrum Disorder Prediction Tool</h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <div style="font-family: 'Verdana', sans-serif; color: #1a1a1a; font-size: 1.1rem; text-align: justify; background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
    This tool uses a machine learning model to predict whether a child may have Autism Spectrum Disorder (ASD) based on behavioral patterns. Please note that this prediction is based on the information provided and is not a definitive diagnosis.
    </div>
    """,
    unsafe_allow_html=True
)


    # Collect input from the user with explanations for each question
    st.markdown("### Behavioral and Developmental Questions:")

    questions = [
        ("1. Does your child look at you when you call his/her name?", "Children with ASD may often avoid or fail to respond to their names when called."),
        ("2. Is it easy for you to get eye contact with your child?", "Difficulty in maintaining eye contact is a common trait observed in children with ASD."),
        ("3. Does your child point to indicate that she/he wants something?", "Pointing is a significant developmental milestone; lack of this can be a red flag for ASD."),
        ("4. Does your child point to share interest with you?", "Joint attention, such as pointing to share interest, is often absent in children with ASD."),
        ("5. Does your child pretend? (e.g., care for dolls, talk on a toy phone)", "Pretend play shows imagination and social interaction; a lack can indicate ASD."),
        ("6. Does your child follow where you’re looking?", "Following someone's gaze demonstrates an understanding of attention and shared focus."),
        ("7. If someone in the family is visibly upset, does your child try to comfort them?", "Children with ASD may show reduced empathy or awareness of others' emotions."),
        ("8. Would you describe your child’s first words as delayed?", "Delayed speech is a frequent developmental concern in children with ASD."),
        ("9. Does your child use simple gestures? (e.g., wave goodbye)", "Gestures like waving are vital social cues, often underdeveloped in ASD."),
        ("10. Does your child stare at nothing with no apparent purpose?", "Repetitive or purposeless staring can be indicative of ASD traits."),
    ]

    inputs = []
    for idx, (question, explanation) in enumerate(questions, start=1):
        st.markdown(f"**{question}**")
        st.write(explanation)
        response = st.selectbox("", ["", "YES", "NO"], key=f"q{idx}")
        inputs.append(1 if response == "YES" else 0)

    st.markdown("### Additional Information:")
    age = st.slider("Age (in months)", 12, 36)
    inputs.append(age)

    gender = st.selectbox("Gender", ["", "Male", "Female"], key="gender")
    inputs.append(1 if gender == "Male" else 0)

    ethnicity = st.selectbox("Ethnicity", ["", "Middle Eastern", "White European", "Hispanic", "Asian", "South Asian", "Native Indian", "Black", "Latino", "Mixed", "Pacifica", "Others"], key="ethnicity")
    inputs.append(["Middle Eastern", "White European", "Hispanic", "Asian", "South Asian", "Native Indian", "Black", "Latino", "Mixed", "Pacifica", "Others"].index(ethnicity) if ethnicity else -1)

    jaundice = st.selectbox("Jaundice", ["", "YES", "NO"], key="jaundice")
    inputs.append(1 if jaundice == "YES" else 0)

    family_member_asd = st.selectbox("Family member with ASD", ["", "YES", "NO"], key="family_asd")
    inputs.append(1 if family_member_asd == "YES" else 0)

    who_test = st.selectbox("Who completed the test?", ["", "Family member", "Health Care Professional", "Self", "Others"], key="who_test")
    inputs.append(["Family member", "Health Care Professional", "Self", "Others"].index(who_test) if who_test else -1)

    if st.button("ASD Test Result"):
        diagnosis = asd(inputs)
        st.markdown(f"<h3 style='color: #1d3557; text-shadow: 1px 1px 2px #000;'>Result: {diagnosis}</h3>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
