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

st.title('AppleGenerator')
st.image("https://oekastatic.orf.at/static/images/site/oeka/20170936/apfel.5650847.jpg", width=100)
st.video('https://i.gifer.com/7kvq.gif', loop=true, autoplay=true, muted=true)
st.radio("Choose your Apple", ["Normal", "Rot", "Scab"], help='Select an Apple out of 3 choices')

st.write("[![Star](https://img.shields.io/github/stars/tamertinkci/ML4B-Team-7.svg?logo=github&style=social)](https://gitHub.com/tamertinkci/ML4B-Team-7)")
