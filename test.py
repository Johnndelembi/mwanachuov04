import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth, exceptions, credentials, initialize_app
from httpx_oauth.clients.google import GoogleOAuth2

cred = credentials.Certificate("mwanachuo2-7faec-firebase-adminsdk-ddavb-0b8a737a43.json")
try:
    firebase_admin.get_app()
except ValueError as e:
    initialize_app(cred)

def app():
# Usernm = []
    col3, col4, col5 = st.columns([1.3,3,2])
    with col3:
        containerx = st.container(border=True)
        containerx.image('logo.png', width=100)
    

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'regnumber' not in st.session_state:
        st.session_state.regnumber = ''
    if 'college' not in st.session_state:
        st.session_state.college = ''         


    def f(): 
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.regnumber = user.display_name
            
            global Usernm
            Usernm=(user.uid)
            
            st.session_state.signedout = True
            st.session_state.signout = True    
  
            
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''


        
    
        
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
        
    student_type = ('Student', 'Leader', )
        
    
    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        col5.header(' :green[To Get Access] ')
        choice = st.selectbox('Login/Signup',['Login','Sign up'])
        email = st.text_input(label='Email', placeholder='Enter your email address' )   
        password = st.text_input(label='Password', placeholder='Enter your password', type='password', help='write a strong password make it so that its easy to remember')

        

        
        if choice == 'Sign up':
            st.subheader('PROFILE INFORMATION')
            username = st.text_input(label='Username', placeholder="Enter  your unique username", help='please include your position if you are a leader i.e Jackson Temba: BAEST CR, Janet John: DARUSO VP, James June: MT114 Seminar Leader')
            regnumber = st.text_input('Registration number', help='Write your registration number as it shows in your Stident ID')
            college = st.text_input('College/School', help='Write your respective college i.e COSS, CoNAS, UDSE')
            category = st.selectbox('Category', student_type, help='Tell us what you identify as, normal student or Leader')

            if category == 'Leader':
                position = st.text_input(label='*For Leaders Only*', placeholder='Specify your leadership role', help='Leadership role i.e BAGES CR, BAST CR, DARUSO')
            
            if st.button(' :green[**Create my account**]', use_container_width=True):
                user = auth.create_user(email = email, password = password, uid=username, display_name=regnumber)
                
                st.success('Account created successfully!')
                st.info('Please Login using your email and password')
                st.balloons()
        else:
            # st.button('Login', on_click=f)          
            st.button(' :green[**Login**]', on_click=f, use_container_width=True)
                

            
            
    if st.session_state.signout:
                
                st.info(' Successfully signed in as '+st.session_state.username )
                container = st.container(border=True)
                container.text('Email ID: '+st.session_state.useremail)
                container.text('Registration Number :'+st.session_state.regnumber )
                
                st.write(' ### ')
 
                st.subheader(':green[+ NEWS FEED] ')

                container2 = st.container(border=True)
                container2.subheader(''' School Of Economics Charity SEASON-2 😊''')
                container2.image('charity.jpg')
                container2.markdown(''' Our UDSE charity is in full swing, and we're thrilled to have you join us!.
                Today marks the continuation of our contribution activities, we're counting on each and every one of you to lend a hand. We simply can't do this without YOU!.
                Let's come together and bring hope to the little ones at FADHIRA center on April 20th.Your generosity will truly make a difference.
                Be blessed and thank you for making the world brighter✨
                ''')

                st.write(' ### ')
                container4 = st.container(border=True)
                container4.subheader('TAX SYSTEMS TRAINING')
                container4.image('udta.jpg')
                container4.markdown('''Helloooo Everyone😍😍😍😍😍👋🏻👋🏻 This is a Good News🔥🔥💫💫💡💡💡
UDTA in collaboration with Tanzania Revenue Authority (TRA)⚖⚖,, is thrilled to announce a ground breaking TAX PACKAGE TRAINING!!!🔥🔥🚨🚨🚨. In this Training,  participants will have the opportunity to acquire essential skills:- 📌📌📌
1. TAXPAYER PORTAL SYSTEM
    .   E-Filling system (File Tax Returns kama VAT Returns, SDL na PAYEE)
- TIN application 
- Driving License 
- Tax Payments 
- Non resident Returns 
- VFD&EFD error Management Services etc

2. TANCIS SYSTEM (Tanzania Customs Integrated system) 

3. Q&A 

Note : This Training is typically offered at a high cost by various Firms,  BUT we're breaking barriers and bringing it to you for FREE!  that's right _no fee involved for UDTA members.💫💡 and 
5,000/= for non members. 

#FreeTraining#Don'tMissOut#CertificateFromTRA 🎓 ✨✨
''')

                container3 = st.container(border=True)
                container3.image('resultss.jpg')
                container3.write('First semester results on display!! Visit your aris accounts to view your reults')




                st.button(':green[Sign out]', on_click=t, use_container_width=True)
            
                
    

                            
    def ap():
        st.write('Posts')
