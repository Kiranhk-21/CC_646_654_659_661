import streamlit as st
import db
import register

def login_clicked(user_id,password):
    # var=Authenticate(user_id,password)
    var = db.auth_execute(user_id,password)
    if var: 
        st.login_state=True
    else:
        st.login_state=False
        st.error("Invalid User")

def login():
    _, col2, _ = st.columns([1, 2, 1])
    if st.register_state:
        if st.login_state==False:
            with col2:
                markdown = """
                        Login Page """
                st.markdown(markdown)
            with col2: 
                with st.form('login'):
                    user_id=st.text_input(label="",value="",placeholder="User ID")  
                    password=st.text_input(label="",value="",placeholder="Password",type="password")
                    st.form_submit_button("Login",on_click=login_clicked,args=(user_id,password))

    else:
        register.register()
        if st.register_state:
            login()
            
def logout():
    st.login_state = False
    login()
