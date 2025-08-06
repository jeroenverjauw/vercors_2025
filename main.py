import streamlit as st

st.sidebar.image("data/egeltje.jpeg", use_container_width =True)

Home = st.Page("pages/Home.py",title="Home")
Dagboek = st.Page("pages/Dagboek.py", title="Dagboek", )
Proclamatie = st.Page("pages/Proclamatie.py", title="Proclamatie", )
Muziek = st.Page("pages/Muziek.py", title="Muziek", )

Jeroen = st.Page("pages/Jeroen.py", title="Jeroen", )
Siel = st.Page("pages/Siel.py", title="Siel", )
Jakob = st.Page("pages/Jakob.py", title="Jakob", )
Gerout = st.Page("pages/Gerout.py", title="Gerout", )
Muziek = st.Page("pages/Muziek.py", title="Muziek", )
Souvenirs = st.Page("pages/Souvenirs.py", title="Des Petits Souvenirs", )

pg = st.navigation(
        {
            "": [Home,],
            "Secties": [Dagboek,Proclamatie, Muziek, Souvenirs],
            "Individuele media": [Jeroen, Siel,Jakob, Gerout]
        }
    )

pg.run()