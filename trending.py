import streamlit as st
from firebase_admin import auth

def app():
    #st.header(' MWANACHUO PLATFORM!! ')
    
    header1, header2 = st.columns([0.75,3])
    with header1:
        container1 = st.container(border=True)   
        container1.image('logo.png', width=100)

    
    st.header(' :green[Getting Started!!]')
    col1, col2 = st.columns([2,3])
    col1.video('simu.mp4')  
    col2.markdown(' **The best platform for all campus news and updates. Spreading the word quick and fast across the community** ')
    col2.markdown('''Mwanachuo makes it easier to transfer information to the receiving end of the students community.''')
    col2.markdown('''Aunthenticity, Honesty and an Unwavering dedication to our users are our core values MWANACHUO is geared to become the number one news outlet source in the university.''')
    
    col2.write('[Learn More](https://wa.link/p7ke9l)')


    with col2:
        col5, col6 = st.columns(2)
        col5.button(' :green[**Sign Up**]', use_container_width=True)
        


    st.write(' ### ')
    st.write(' ### ')
    st.write(' ### ')
    mid1, mid2, mid3 = st.columns([4,2,4])
    mid2.subheader('Explore')
    mid6, mid7, mid8 = st.columns([0.5,15,0.5])
    mid7.write('**Get to know the limitless potentials MWANACHUO brings to the univeristy community.**')

    mid4, mid5 = st.columns([3,4])
    st.video('MWANACHUO.mp4')
    st.caption("DISCLAIMER: Photo was taken from twitter acc UDSM ICON")


    st.write(' ### ')
    container = st.container(border=True)
    with container:
        col1, col2 = st.columns([4,2])
        col1.subheader(':green[**Subscribe to our newsletter**] ')
        col1.write('**Get our real time updates**')
        col2.text_input(label='', placeholder='Your Email')
        col2.button("Subscribe")


    st.write(' ### ')
    st.markdown(''' MWANACHUO as an information portal facilitates the flow of information from top to bottom
    guarranteeing safest and fastest information flow, auntheniticity and reliability on both ends. ''')    
        

    st.write(' ### ')
    st.write(' ### ')
    st.write(' ### ')
    st.write(' ### ')
    col1, col2, col3, col4 = st.columns([2,6,2,2])
    col1.caption('mwanachuo.app')
    col3.caption(' [Privacy Policy]()')
    col4.caption( ' [Terms of Use]() ')

    