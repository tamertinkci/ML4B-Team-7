import streamlit as st
from streamlit_option_menu import option_menu
import toml
from generate_image import generate_and_plot
# import time

st.set_page_config(layout="wide")


def load_config(file_path):
    with open(file_path, 'r') as file:
        config = toml.load(file)
    return config


config = load_config('.streamlit/config.toml')

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'],
                           icons=['house', 'gear'], menu_icon="cast", default_index=1)

if selected == 'Home':
    st.title("The Applegenerator")

    selected2 = option_menu(None, ["Home", "Ai Image Generator", "Gallery", 'About Us'],
                            icons=['house', 'alexa', "border-all", 'exclamation-circle'],
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
        with open('css/styles.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        st.title("Generate your own Apple")
        if st.button("Generate :magic_wand:"):
            # with st.spinner('Wait for it...'):
            # time.sleep(2)
            image = generate_and_plot()
            st.image(image, caption="An Apple")

    if selected2 == 'Gallery':
        st.title('Gallery')
        st.write("In this gallery, you'll find generated Apple images from the community.")

    if selected2 == 'About Us':
        st.title("About Us")
        st.image('https://i.gifer.com/7kvq.gif', width=200)
        st.write(
            "[![Star](https://img.shields.io/github/stars/tamertinkci/ML4B-Team-7.svg?logo=github&style=social)](https://gitHub.com/tamertinkci/ML4B-Team-7)")

if selected == 'Settings':
    st.title('Settings')
    selected3 = option_menu(None, ["Theme", "Generator", "Gallery", 'About Us'],
                            menu_icon="cast", default_index=0, orientation="horizontal")

    if selected3 == "Theme":
        theme_choice = st.radio("Choose Theme", ["Darkmode", "Lightmode"])
        if theme_choice == "Lightmode":
            st.write('Lightmode')
        elif theme_choice == "Darkmode":
            st.write('Darkmode')
