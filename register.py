import streamlit as st
import db
import login

def register_clicked(user_id,password):
    # var=Authenticate(user_id,password)
    register()

def register():
    _, col2, _ = st.columns([1, 2, 1])
    if st.register_state==False:
            with col2:
                markdown = """
                        Register"""
                st.markdown(markdown)
                with st.form('register'):
                    _,name,age,address,_ = st.columns([1,5,2,5,1])
                    name=st.text_input(label="Name",value="",placeholder="Name") 
                    # dob = st.date() 
                    age=st.number_input(label="Age",value="",placeholder="age")
                    address = st.text_input(label="",value="",placeholder="Address")
                    st.form_submit_button("Register",on_click=db.execute,args=(name,age,address))
                    st.register_state=True
                    login.login()

