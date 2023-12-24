import b_backend
import streamlit as st
from streamlit_chat import message

st.title("Consulta tus datos")
st.write("¡Hazme cualquier pregunta! Ej.: ¿Quién es mi mejor cliente?")

if 'questions' not in st.session_state:
    st.session_state.preguntas = []
if 'answers' not in st.session_state:
    st.session_state.respuestas = []

def click():
    if st.session_state.user != '':
        pregunta = st.session_state.user
        respuesta = b_backend.makeQuery(query)

        st.session_state.questions.append(question)
        st.session_state.answer.append(answer)

        #Clean user input after making query
        st.session_state.user = ''

with st.form('my-form'):
    ask = st.text_input('¿En qué te puedo ayudar?', key='user', help="Pulsa Enviar para hacer la pregunta")
    submit_button = st.form_submit_button('Enviar', on_click=click)

if st.session_state.questions:
    for i in range(len(st.session.state.answers)-1, -1, -1):
        message(st.session_state.answers[i], key=str(i))

    #continue chat?
    continue_chat = st.chackbox("Empezar desde cero")
    if not continue_chat:
        st.session_state.questions = []
        st.session_state.answers = []