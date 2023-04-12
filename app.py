import streamlit as st
import pandas as pd


st.set_page_config(page_title='The ACME Day', page_icon='ACME LOGO(T).png', initial_sidebar_state='expanded')
st.markdown("<h1 style='text-align: center; font-family: monospace; color: #b2d1d4;'>The ACME Day</h1>", unsafe_allow_html=True)
st.write("We, your juniors, cordially invite you to join us on 6th May for our valedictory event. As we near the end of the academic year, we would like to take this opportunity to express our deep gratitude for all that you have done for us.\n\nYour guidance, support, and encouragement have been invaluable to us, and we would like to show our appreciation by celebrating this momentous occasion with you. We have planned an exciting event with a variety of performances and speeches that we hope you will enjoy.\n\nPlease join us at Dasari Auditourim at 12pm on 6th May for an evening filled with love, respect, and memories to cherish for a lifetime. We look forward to seeing you there!\n\n\nWith warm regards,\n\nTeam ACME 2k24")
st.write("❤️")
st.sidebar.image("ACME LOGO(T).png")
rollnum=st.sidebar.text_input("Roll Number",placeholder="Enter RollNo.",max_chars=10)

if len(rollnum)> 0:
    data = pd.read_excel("Book1.xlsx")
    row = data.loc[data["Roll"] == rollnum]

    if len(row) > 0:
        img_pth = row["Location"].iloc[0]
        img = open(img_pth, "rb").read()
        st.image(img)
        st.download_button(":apple: Download",file_name="The Acme day invitation.jpg",data=img)

    else:
        st.warning("Endhi yoo, susukopanley Roll Number tappu kottinav anta chudu", icon="⚠️")




