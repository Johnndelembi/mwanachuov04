import streamlit as st
import numpy as np
import pandas as pd

def app():    
    st.header('A :green[STUDY] ON UNIVERSITY INFORMATION OUTLETS')
    st.subheader('**PROJECT SUMMARY**')
    st.markdown('''This project proposes a mobile and online platform to improve information flow within the university. 
            Students and faculty will receive personalized and timely updates, announcements, and event details. 
            Additionally, a user-friendly system that is developed to help students report and track lost belongings on campus, 
            reducing stress and promoting a more organized environment.''')
    st.markdown('**A study conducted in the University of Dar es Salaam on information outlets, the results are as follows** ')
    

    result_container = st.container(border=True)
    with result_container:
        id1 = pd.read_csv('identity_kpi.csv')
        id2 = pd.read_csv('possible_reasons_kpi.csv')
        id3 = pd.read_csv('willingness_kpi.csv')
        st.subheader("**KPI's**")

        st.write("(a) *89.6% of respondents were normal students were normal students as opposed to 10% who were leaders.* ")
        st.dataframe(id1, hide_index=True, use_container_width=True)

        st.markdown(''' (b) *72.4% of respondents said the main reason for getting/sending late, 
            unreliable or outdated information was due to 'Inconveniences such as bundle and networks
            while 10.34% said otherwise*''')
        st.dataframe(id2, hide_index=True, use_container_width=True)

        st.write(" (c) *86% of the respondents agreed to a better solution that would help them alleviate the problems they face towards getting updated and reliable information*")
        st.dataframe(id3, hide_index=True, use_container_width=True)


        st.caption("KPI means KEY PERFOMANCE INDICATOR")





    st.subheader('SHORT SUMMARY REPORT')
    result_container1 = st.container(border=True)
    with result_container1:  
        result1,  result2 = st.columns(2)
        result1.markdown(''' According to the research conducted about 72.4% agreed to incoveniences like
            bundle and network issues being the major problem hindering their access to up-to-date information while 27.6% distributed almost equally among
            "information sent late", "post being less detailed", and "sheer lazyness to make regular check ups for information".
            With Mwanachuo app student will be able to solve the problem of late information, and having to deal with less-detailed post.
            all the informations and updates from Mwanachuo app are authentic and true to the university community        
            ''')
        result2.image('5.PNG', caption='A pie chart displaying research findings on the reasons as to why university student encounter unauthentic/unreliable information')
        st.write( "___ ")

    result_container2 = st.container(border=True)
    with result_container1:
        result3, result4 = st.columns(2)
        result3.markdown(''' About 41% both normal students and leaders agreed on the fact that information credibility, 
            reliability and authenticity means to your socio-academic well-being while on campus
            and that it matters when the information outlets thrive to uphold truth, and panctuality, a good information discharge from top to bottom ''')
        result3.markdown('''This means that students relly on sending/receiving information in their run-of-the-mill day-to-day university life''')
        result4.image('7.PNG', caption='A histogram showing how much quality information and how and when they get the information means to students socio-academic well life on campus  ')





    st.write(' ### ')
    st.write(' ### ')

    st.subheader('Team')
    bottom1, bottom2, bottom3 = st.columns(3, gap='small')
    bot1, bot2, bot3 = st.columns([3.5,3,3]) 
    with bottom1:  
       container1 = st.container(border=True) 
       container1.image('profile-pic-3.png', width=150)
       container1.markdown('**Martha Kidumbuyo**')

    with bottom2:
        container2 = st.container(border=True)   
        container2.image('profile-pic.png', width=150)
        container2.markdown('  **[John Ndelembi](https://t.ly/uecuB)**')

    with bottom3:
        container3 = st.container(border=True)    
        container3.image('profile-pic-2.png', width=150)
        container3.markdown('**Dadila Seddy**')

    container = st.container(border=True)
    with container:
        cols1, cols2 = st.columns([7,2])
        cols2.image('logo.png', width=150)    
        cols1.subheader(':green[Chat with Us]')
        cols1.markdown('Contact via: [Whatsapp](https://wa.link/p7ke9l)')
        cols1.markdown('Contact via: [E-mail](https://williamjohnie61@gmail.com)')
    
    
    col1, col2, col3, col4 = st.columns([2,6,2,2])
    col1.caption('mwanachuo.app')
    col3.caption(' [Privacy Policy]()')
    col4.caption( ' [Terms of Use]() ')



        
