import streamlit as st
from streamlit_option_menu import option_menu
import toml
from generate_image import generate_and_plot
# import time

st.set_page_config(layout="wide")

with open("css/styles.css") as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


def load_config(file_path):
    with open(file_path, 'r') as file:
        config = toml.load(file)
    return config


config = load_config('.Streamlit/config.toml')

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings', 'About Us'],
                           icons=['house', 'gear', 'exclamation-circle'], menu_icon="cast", default_index=0)

if selected == 'Home':
    st.markdown('<h1 class="bruno-ace-unique">The Applegenerator</h1>', unsafe_allow_html=True)

    selected2 = option_menu(None, ["Home", "Ai Image Generator", "Gallery"],
                            icons=['house', 'alexa', "border-all"],
                            menu_icon="cast", default_index=0, orientation="horizontal")

    if selected2 == 'Home':
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("")
        with col2:
            st.image(
                'https://i2.wp.com/blog.indiefolio.com/wp-content/uploads/2015/07/SW_AF_AppleFizz_new.gif?resize=1024%2C633&ssl=1',
                use_column_width=True)
        with col3:
            st.write("")
        st.title('Kurze Einführung')

    if selected2 == 'Ai Image Generator':
        st.title("Generate your own Apple")
        if st.button("Generate :magic_wand:"):
            # with st.spinner('Wait for it...'):
            # time.sleep(2) 
            image = generate_and_plot()
            st.image(image, caption="An Apple")

    if selected2 == 'Gallery':
        st.title('Gallery')
        st.write("In this gallery, you'll find generated Apple images from the community.")

if selected == 'Settings':
    st.title('Settings')
    selected3 = option_menu(None, ["Theme"],
                            menu_icon="cast", default_index=0, orientation="horizontal")

    if selected3 == "Theme":
        ms = st.session_state
        if "themes" not in ms:
            ms.themes = {"current_theme": "light",
                         "refreshed": True,
                         "light": {"theme.base": "dark",
                                   "theme.backgroundColor": "white",
                                   "theme.primaryColor": "#5591f5",
                                   "theme.secondaryBackgroundColor": "#82E1D7",
                                   "theme.textColor": "#0a1464",
                                   "button_face": "Darkmode🌜"},
                         "dark": {"theme.base": "dark",
                                  "theme.backgroundColor": "#000000",
                                  "theme.primaryColor": "#660000",
                                  "theme.secondaryBackgroundColor": "#2F2F2F",
                                  "theme.textColor": "#FFFFFF",
                                  "button_face": "Lightmode🌞"},
                         }

        def ChangeTheme():
            previous_theme = ms.themes["current_theme"]
            tdict = ms.themes["dark"] if ms.themes["current_theme"] == "light" else ms.themes["light"]
            for vkey, vval in tdict.items():
                st._config.set_option(vkey, vval)

            ms.themes["refreshed"] = False
            ms.themes["current_theme"] = "dark" if previous_theme == "light" else "light"

        btn_face = ms.themes["dark"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["light"]["button_face"]
        st.button(btn_face, on_click=ChangeTheme)

        if not ms.themes["refreshed"]:
            ms.themes["refreshed"] = True
            st.experimental_rerun()

if selected == 'About Us':
    st.title("About Us")
    st.image('https://i.gifer.com/7kvq.gif', width=200)
    st.write(
         "[our GitHub! ![Star](https://img.shields.io/github/stars/tamertinkci/ML4B-Team-7.svg?logo=github&style=social)](https://gitHub.com/tamertinkci/ML4B-Team-7)")
