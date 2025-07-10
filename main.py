import streamlit as st

st.sidebar.image("pages/egeltje.jpeg", use_container_width =True)
# from streamlit_extras.app_logo import add_logo

# # image has 200x200 pixels size
# add_logo("pages/egeltje.jpeg", height=20000)

Home = st.Page("pages/Home.py",title="Home")
Dagboek = st.Page("pages/Dagboek.py", title="Dagboek", )

pg = st.navigation(
        {
            "": [Home,],
            "Sectie 1": [Dagboek,],
        }
    )


pg.run()