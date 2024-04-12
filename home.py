import streamlit as st
from firebase_admin import firestore


def app():
    cols4, cols5, cols6 = st.columns([3,8,3])
    cols5.subheader('NEWS AND ANNOUNCEMENTS')
    news1, news2 = st.columns([2,3])
    news1.markdown('''Share news, updates and announcements directly to the community.''')
    news1.markdown(''' MWANACHUO offers a safe space for leaders to engage with their
    students by posting announcements and news''')  
    news2.image('news.PNG')
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db=firestore.client()
    st.session_state.db=db
    # st.title('  :violet[Pondering]  :sunglasses:')
    
    ph = ''
    if st.session_state.username=='':
        ph = 'Login to be able to post!!'
    else:
        ph='Post your thought'   
    st.subheader(' :green[+ RESERVED FOR LEADERS ONLY +] ', help='includes CRs, DARUSO Leaders etc')       
    post=st.text_area(label=' :orange[>>>] ', placeholder=ph, height=None, max_chars=500)


    if st.button('Post',use_container_width=20):
        if post!='':
                    
            info = db.collection('Posts').document(st.session_state.username).get()
            if info.exists:
                info = info.to_dict()
                if 'Content' in info.keys():
                
                    pos=db.collection('Posts').document(st.session_state.username)
                    pos.update({u'Content': firestore.ArrayUnion([u'{}'.format(post)])})
                    # st.write('Post uploaded!!')
                else:
                    
                    data={"Content":[post],'Username':st.session_state.username}
                    db.collection('Posts').document(st.session_state.username).set(data)    
            else:
                    
                data={"Content":[post],'Username':st.session_state.username}
                db.collection('Posts').document(st.session_state.username).set(data)

            st.success('Post uploaded!!')
    expander1 = st.expander('NEWS AND ANNOUNCEMENTS')
    with expander1:
       st.header(' :orange[Latest Posts] ')
    
    
       docs = db.collection('Posts').get()
            
       for doc in docs:
            d=doc.to_dict()
            try:
                container = st.container(border=True)
            #container.image(image, caption=':green[Posted by:] '+':orange[{}]'.format(d['Username']), value=d['Content'][-1])
                st.text_area(label=':green[Posted by:] '+':orange[{}]'.format(d['Username']),value=d['Content'][-1],height=20)
            except: pass

    st.write(' ### ')
    st.write(' ### ')
    
    #####----###################--------#############------------###########
    cols1, cols2, cols3 = st.columns([4,5,4])
    cols2.subheader(' LOST AND FOUND')
    cols4, cols5 = st.columns([3,2])
    cols4.markdown('''If you loose something while on campus don't panick, 
    MWANACHUO offers a solution where you can ask around the community and get immediate response from
    the community. Post a description of what you have lost when found you will be notified in a moments notice''')
    cols5.image('lost.png')
    
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db=firestore.client()
    st.session_state.db=db
    # st.title('  :violet[Pondering]  :sunglasses:')
    
    ph = ''
    if st.session_state.username=='':
        ph = 'Login to be able to post!!'
    else:
        ph='Explain what you have lost in details'   
    #st.subheader(' :green[+ FOR ALL STUDENT] ')       
    post=st.text_area(label=' :green[POST WHAT YOU HAVE LOST/FOUND HERE] ', placeholder=ph, height=None, max_chars=500)


    if st.button('Upload',use_container_width=20):
        if post!='':
                    
            info = db.collection('Posts').document(st.session_state.username).get()
            if info.exists:
                info = info.to_dict()
                if 'Content' in info.keys():
                
                    pos=db.collection('Posts').document(st.session_state.username)
                    pos.update({u'Content': firestore.ArrayUnion([u'{}'.format(post)])})
                    # st.write('Post uploaded!!')
                else:
                    
                    data={"Content":[post],'Username':st.session_state.username}
                    db.collection('Posts').document(st.session_state.username).set(data)    
            else:
                    
                data={"Content":[post],'Username':st.session_state.username}
                db.collection('Posts').document(st.session_state.username).set(data)

            st.success('Post uploaded!!')
    
    expander = st.expander('NEW UPLOADS')
    with expander:
      st.header(':orange[NEW UPLOADS]')    
      docs = db.collection('Posts').get()
            
      for doc in docs:
        d=doc.to_dict()
        try:
            container1 = st.container(border=True)
            #container.image(image, caption=':green[Posted by:] '+':orange[{}]'.format(d['Username']), value=d['Content'][-1])
            st.text_area(label=':green[From Lost & Found by:] '+':orange[{}]'.format(d['Username']),value=d['Content'][-1], height=20)
        except: pass
        
         
    



    st.write(' ### ')
    col1, col2, col3, col4 = st.columns([2,6,2,2])
    col1.caption('mwanachuo.app')
    col3.caption(' [Privacy Policy]()')
    col4.caption( ' [Terms of Use]() ')    
