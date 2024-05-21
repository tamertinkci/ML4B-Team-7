import streamlit as st
import toml
import time

st.set_page_config(layout="wide")

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = toml.load(file)
    return config

config = load_config('.streamlit/config.toml')

print(config['theme']['primaryColor'])
print(config['theme']['backgroundColor'])


# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose your Apple",
        ("Normal Apple", "Rotten Apple", "Scab Apple", "Blotch Apple")
    )
tab1, tab2, tab3, tab4 = st.tabs(["Home", "Ai image generator", "Gallery", "About Us"])

with tab1:
   st.title("Home")
   st.image("https://oekastatic.orf.at/static/images/site/oeka/20170936/apfel.5650847.jpg", width=200)

with tab2:
   st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Grüne Hintergrundfarbe */
        color: white; /* Textfarbe */
        border: none; 
        padding: 15px 32px; 
        text-align: center; 
        text-decoration: none; /* Keine Unterstreichung */
        display: inline-block; /* Inline-Blockelement */
        font-size: 30px; /* Schriftgröße */
        margin: 4px 2px; /* Rand */
        cursor: pointer; /* Cursor ändert sich bei Hover */
        border-radius: 12px; /* Abgerundete Ecken */
    }
    .stButton>button:hover {
        background-color: #45a049; /* Dunklere grüne Hintergrundfarbe bei Hover */
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Apple image generator")
st.image("https://oekastatic.orf.at/static/images/site/oeka/20170936/apfel.5650847.jpg", width=200)
if st.button("Generate :magic_wand:"):
   with st.spinner('Wait for it...'):
    time.sleep(5)

with tab3:
   st.title("Gallery")
   

with tab4:
   st.title("About Us")
   st.image('https://i.gifer.com/7kvq.gif', width=200)
   st.write("[![Star](https://img.shields.io/github/stars/tamertinkci/ML4B-Team-7.svg?logo=github&style=social)](https://gitHub.com/tamertinkci/ML4B-Team-7)")
  
 




