import streamlit as st
import numpy as np
import pandas as pd

from utils.utils import *

def create_tab_corsi(tab_corsi):
    col1,col2= st.columns(2)
    info_corsi= execute_query(st.session_state["connection"], "SELECT Count(DISTINCT(CodC)) AS 'Numero Corsi' FROM CORSI;")
    tipo_corsi = execute_query(st.session_state["connection"], "SELECT COUNT(DISTINCT(Tipo)) AS 'Tipo Corsi' FROM CORSI")
    info_corsi_struct= [dict(zip(info_corsi.keys(),result)) for result in info_corsi ]
    numero_corsi_struct = [dict(zip(tipo_corsi.keys(),result)) for result in tipo_corsi ]

    col1.metric(label = 'Numero Corsi',value = info_corsi_struct[0].get('Numero Corsi'))
    col2.metric(label = 'Tipi di Corsi', value =numero_corsi_struct[0].get('Tipo Corsi'))
    
    option1 = st.selectbox(
    '### Seleziona un tipo di corso per cui vuoi informazioni',
    ('Spinning','Attività musicale', 'Yoga', 'Piscina'))

    option2 = st.selectbox(
    'Seleziona un livello',
    (1,2,3,4))

    info_c = info_corso_per_tipo(option1,option2,'corsi')

    if  info_c ==  []:
        st.markdown('#        ')
        st.markdown('#        ')
        st.warning('### Non ci sono opzioni disponibili ')
        
    else: 
    
        for i in range (0, len(info_c)):
            a = info_c[i].get('Tipo')
            b = info_c[i].get('CodC')
            c = info_c[i].get('Nome')
            d = info_c[i].get('Livello')
            
            st.markdown('#        ')
            st.markdown('### :red[Tipo Corso:] 'f'{a}')
            st.markdown('##### :green[Codice Corso:] 'f'{b}' )
            st.markdown('##### :green[Nome Corso:] 'f'{c}')
            st.markdown('##### :green[Livello Corso:] 'f'{d}')
            st.markdown('#        ')


        expander = st.expander(f'{option1}')   
        expander.write(programmazione_corso(option1)) 
    
    
     
    


#def create_tab_programmi(tab_programmi):
    #col1= tab_programmi.columns(1)
    #info_programmi= execute_query(st.session_state["connection"], "SELECT Tipo FROM CORSI;")
    #info_programmi_struct= [dict(zip(info_programmi.keys(),result)) for result in info_programmi ]
    #tab_programmi.write(info_programmi_struct)


#def create_tab_livello(tab_livello):
    #col1= tab_livello.columns(1)
   # info_livello= execute_query(st.session_state["connection"], "SELECT Livello FROM CORSI;")
   # info_livello_struct= [dict(zip(info_livello.keys(),result)) for result in info_livello ]
    #tab_livello.write(info_livello_struct)


if __name__ == "__main__":
    st.set_page_config(
    page_title="Corsi",
    layout="wide",
    
    )
    st.title("Corsi")

    tab_corsi =st.tabs(["Corsi"])

    if check_connection():
        create_tab_corsi(tab_corsi)
        #create_tab_programmi(tab_programmi)
        #create_tab_livello(tab_livello)
       

