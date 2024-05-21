import streamlit as st
import toml

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
tab1, tab2, tab3, tab4 = st.tabs(["Home", "Applegenerator", "Gallery"])

with tab1:
   st.header("Home")
   st.image("https://oekastatic.orf.at/static/images/site/oeka/20170936/apfel.5650847.jpg", width=200)

with tab2:
   st.header("Apple image generator")
   st.image("https://oekastatic.orf.at/static/images/site/oeka/20170936/apfel.5650847.jpg", width=200)
   st.radio("Choose your Apple", ["Normal", "Rot", "Scab"], help='Select an Apple out of 3 choices')
with tab3:
   st.header("Gallery")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
st.title('AppleGenerator')

with tab4:
   st.header("About Us")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
st.title('AppleGenerator')
st.write("[![Star](https://img.shields.io/github/stars/tamertinkci/ML4B-Team-7.svg?logo=github&style=social)](https://gitHub.com/tamertinkci/ML4B-Team-7)")
   st.image('https://i.gifer.com/7kvq.gif', width=200)
 




