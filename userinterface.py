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

add_selectbox = st.sidebar.selectbox(
    "Test",
    ("option 1", "option 2", "option 3")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose your Apple",
        ("Normal Apple", "Rotten Apple", "Scab Apple", "Blotch Apple")
    )
st.title('AppleGenerator')
st.image('https://i.gifer.com/7kvq.gif', width=100)  
st.radio("Choose your Apple", ["Normal", "Rot", "Scab"], help='Select an Apple out of 3 choices')

st.write("[![Star](https://img.shields.io/github/stars/tamertinkci/ML4B-Team-7.svg?logo=github&style=social)](https://gitHub.com/tamertinkci/ML4B-Team-7)")
