# agr hamien apna data ui pe show krna to pandas hamien bht se methods provide krta hai
# pandas is a python library used for data manipulation and analysis


import base64
import streamlit as st # web interface
import pandas as pd # For data manupilation
import datetime # datetime
import csv # For reading and writting CSV files
import os  # operating syystem for doing system level things

MOOD_FILE =  "mood_log.csv"  # capital mien is lye likha hai k is file mein mojod daat change hoga lekin file change nh ogi

#we make two fiunction one is for delete the data and other one is for adding data
def load_mood_data(): # second return for function and frist return for if condition
    if not os.path.exists(MOOD_FILE):
        # Create initial DataFrame with proper column names
        return pd.DataFrame(columns=["Date", "Mood"])
    
    # Read CSV and ensure column names match
    df = pd.read_csv(MOOD_FILE)
    df.columns = df.columns.str.strip()  # Remove any whitespace from column names
    return df

def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline='') as file:  # Add newline='' to prevent extra blank lines
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Function to encode local fox image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string

# Adding fox image as background (LEFT SIDE)
fox_image_base64 = get_base64_image("background.webp")  # Use uploaded file

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{fox_image_base64}") no-repeat left center;
        background-size: cover; /* Ensures full screen */
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <style>
    h1, h2, h3, h4, h5, h6 {{
        color: black !important;  /* Only headings will be black */
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# st.title("Mood Tracker")
# today = datetime.date.today()
# st.subheader("How are you feeling Today?")

# mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Nuetral"])
# if st.button("Log Mood"):
#    save_mood_data(today, mood)
#    st.info("Mood logged successfully!")
#    st.balloons() # balloon to show the success message
# data= load_mood_data()

# if not data.empty():
#    st.subheader("Mood Trends Over Time")
#    data["Date"] = pd.to_datetime(data["Date"])

#    mood_count= data.groupby("Mood").count()["Date"] # count the number of mods
#    st.bar_chart(mood_count) # plot the bar chart


#  Streamlit app title
st.title("Mood Tracker😃")

# Get today's date
today = datetime.date.today()

# Create subheader for mood input
st.subheader("🤔 How are you feeling today?")

# Create dropdown for mood selection
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Create button to save mood
if st.button("Log Mood"):
    
    # Save mood when button is clicked
    save_mood_data(today, mood)
    st.info("Mood logged successfully!😃")
    st.balloons() # balloon to show the success message

    # Show success message


# Load existing mood data
data = load_mood_data()

# If there is data to display
if not data.empty:
    # Create section for Visualization 
    st.subheader("Mood Trends Over Time 📈😊📉😢")

    try:
        # Convert date strings to datetime objects
        data["Date"] = pd.to_datetime(data["Date"])

        # Count frequency of each mood
        mood_counts = data.groupby("Mood", observed=True).count()["Date"]

        # Display bar chart of mood frequencies
        st.bar_chart(mood_counts)
    except Exception as e:
        st.error(f"Error processing mood data: {str(e)}")
        st.write("Current data columns:", list(data.columns))

    # Build with love by Asharib Ali
    st.write("Build with ❤️ by [Ayesha Faisal](https://github.com/ayesha-offical)")



