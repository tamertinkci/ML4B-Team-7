import streamlit as st
from streamlit_option_menu import option_menu
import toml
from generate_image import generate_and_plot

st.set_page_config(layout="wide")

with open("css/styles.css") as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = toml.load(file)
    return config

config = load_config('.Streamlit/config.toml')

if 'themes' not in st.session_state:
        st.session_state.themes = {
            "current_theme": "light",
            "refreshed": True,
            "light": {
                "theme.base": "light",
                "theme.backgroundColor": "white",
                "theme.primaryColor": "#5591f5",
                "theme.secondaryBackgroundColor": "#82E1D7",
                "theme.textColor": "#0a1464",
                "button_face": "Darkmode🌜"
            },
            "dark": {
                "theme.base": "dark",
                "theme.backgroundColor": "#000000",
                "theme.primaryColor": "#660000",
                "theme.secondaryBackgroundColor": "#2F2F2F",
                "theme.textColor": "#FFFFFF",
                "button_face": "Lightmode🌞"
            }
        }
    
st.markdown('<h1 class="bruno-ace-unique">The Applegenerator</h1>', unsafe_allow_html=True)

selected = option_menu(None, ["Home", "Ai Image Generator", "History"],
                        icons=['house', 'alexa', "border-all"],
                        menu_icon="cast", default_index=0, orientation="horizontal")

if selected == 'Home':
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("")

    current_theme = st.session_state.themes["current_theme"]
    if current_theme == "light":
        image_url = 'https://i2.wp.com/blog.indiefolio.com/wp-content/uploads/2015/07/SW_AF_AppleFizz_new.gif?resize=1024%2C633&ssl=1'
    else:
        image_url = 'https://raw.githubusercontent.com/tamertinkci/ML4B-Team-7/2963a33d77d69539a55e1445c60a8305edd12d72/assets/applelogolight.gif'

    assert isinstance(image_url, str), f"Expected image_url to be a string, but got {type(image_url)}"

    with col2:
        st.image(image_url, use_column_width=True)
    with col3:
        st.write("")

    st.title('Create your own apple with just 1 Click!')

    ms = st.session_state
    if "themes" not in ms:
        ms.themes = {
            "current_theme": "dark",
            "refreshed": True,
            "light": {
                "theme.base": "light",
                "theme.backgroundColor": "white",
                "theme.primaryColor": "#5591f5",
                "theme.secondaryBackgroundColor": "#82E1D7",
                "theme.textColor": "#0a1464",
                "button_face": "Darkmode🌜"
            },
            "dark": {
                "theme.base": "dark",
                "theme.backgroundColor": "#000000",
                "theme.primaryColor": "#660000",
                "theme.secondaryBackgroundColor": "#2F2F2F",
                "theme.textColor": "#FFFFFF",
                "button_face": "Lightmode🌞"
            },
        }


    def ChangeTheme():
        previous_theme = ms.themes["current_theme"]
        tdict = ms.themes["light"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]
        for vkey, vval in tdict.items():
            if vkey.startswith("theme"):
                st._config.set_option(vkey, vval)

        ms.themes["refreshed"] = False
        if previous_theme == "dark":
            ms.themes["current_theme"] = "light"
        elif previous_theme == "light":
            ms.themes["current_theme"] = "dark"

    btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("")
    with col2:
        st.write("")
    with col3:
        st.button(btn_face, on_click=ChangeTheme)

    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown("""
        <div style="color: grey;">
            An App created by Stephen Nkwelle, Sabrin Souilah, Yamen Mohamad and Tamer Tinkci 
            <a href="https://gitHub.com/tamertinkci/ML4B-Team-7">
                <img src="https://img.shields.io/github/stars/tamertinkci/ML4B-Team-7.svg?logo=github&style=social" alt="Star on GitHub" style="vertical-align: middle;">
            </a>
        </div>
        """, unsafe_allow_html=True)
    if ms.themes["refreshed"] == False:
        ms.themes["refreshed"] = True
        st.rerun()

if selected == 'Ai Image Generator':
    st.title("Generate your own Apple")
    if st.button("Generate :magic_wand:"):
        # with st.spinner('Wait for it...'):
        # time.sleep(2)
        image = generate_and_plot()
        st.image(image, caption="An Apple")

if selected == 'History':
    st.title('History of Generated Apples')
    st.write("Here you will find your recently created images of apples")
