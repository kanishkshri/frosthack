# -*- coding: utf-8 -*-
"""
Created on Sat May 21 19:44:02 2022

@author: hp
"""
import pandas as pd
import numpy as np
import streamlit as st
import pickle
import requests
from bokeh.models.widgets import Div
import urllib



#data= pd.read_csv("clean_data_sample.csv")
#pickle.dump(data.to_dict(),open('books.pkl','wb'))

book_dict= pickle.load(open('C:/Users/hp/Downloads/Frosthack/books.pkl','rb'))
booklist=pd.DataFrame(book_dict)

similarity = pickle.load(open('C:/Users/hp/Downloads/Frosthack/similarity.pkl','rb'))

def fetch_poster(book):
    pic= booklist[booklist["title"]==book]['image-url'].tolist()[0]
    
    return pic

def get_desc(book):
    disc= booklist[booklist["title"]==book]['description'].tolist()[0]
    
    return disc

def recommend(book):
    index = booklist[booklist['title'] == book].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_book = []
    recommended_book_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        
        recommended_book_posters.append(fetch_poster(booklist.iloc[i[0]].title))
        recommended_book.append(booklist.iloc[i[0]].title)

    return recommended_book, recommended_book_posters



st.title("Book Recommendation System")

option= st.selectbox('Choose a book', booklist['title'].values)

# if st.button('Show Recommendation'):
#     recommended_book,recommended_book_posters = recommend(option)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_book[0])
#         st.image(recommended_book_posters[0])
#     with col2:
#         st.text(recommended_book[1])
#         st.image(recommended_book_posters[1])

#     with col3:
#         st.text(recommended_book[2])
#         st.image(recommended_book_posters[2])
#     with col4:
#         st.text(recommended_book[3])
#         st.image(recommended_book_posters[3])
#     with col5:
#         st.text(recommended_book[4])
#         st.image(recommended_book_posters[4])

if st.button('Show Recommendation'):
    recommended_book,recommended_book_posters = recommend(option)
    
    st.subheader(recommended_book[0])
    col1,col2=st.columns(2)
    with col1:
        st.image(recommended_book_posters[0],width=200)
    with col2:
        st.components.v1.html(get_desc(recommended_book[0]), width=None, height=200, scrolling=True)
        
        
        link= booklist[booklist["title"]==recommended_book[0]]['url'].tolist()[0]
        
        rec_link= "https://bookdepository.com" + link
        
        
        st.write(f'''
            <a target="_blank" href={rec_link}>
                <button>
                    Buy Now
                </button>
            </a>
            ''',
            unsafe_allow_html=True
        )
            
            
            
            
    st.subheader(recommended_book[1])
    col1,col2=st.columns(2)
    with col1:
        st.image(recommended_book_posters[1],width=200)
    with col2:
        st.components.v1.html(get_desc(recommended_book[1]), width=None, height=200, scrolling=True)
        
        
        link= booklist[booklist["title"]==recommended_book[1]]['url'].tolist()[0]
        
        rec_link= "https://bookdepository.com" + link
        
        
        st.write(f'''
            <a target="_blank" href={rec_link}>
                <button>
                    Buy Now
                </button>
            </a>
            ''',
            unsafe_allow_html=True
        )
    
    st.subheader(recommended_book[2])
    col1,col2=st.columns(2)
    with col1:
        st.image(recommended_book_posters[2],width=200)
    with col2:
        st.components.v1.html(get_desc(recommended_book[2]), width=None, height=200, scrolling=True)
        
        
        link= booklist[booklist["title"]==recommended_book[2]]['url'].tolist()[0]
        
        rec_link= "https://bookdepository.com" + link
        
        
        st.write(f'''
            <a target="_blank" href={rec_link}>
                <button>
                    Buy Now
                </button>
            </a>
            ''',
            unsafe_allow_html=True
        )
    
    st.subheader(recommended_book[3])
    col1,col2=st.columns(2)
    with col1:
        st.image(recommended_book_posters[3],width=200)
    with col2:
        st.components.v1.html(get_desc(recommended_book[3]), width=None, height=200, scrolling=True)
        
        
        link= booklist[booklist["title"]==recommended_book[3]]['url'].tolist()[0]
        
        rec_link= "https://bookdepository.com" + link
        
        
        st.write(f'''
            <a target="_blank" href={rec_link}>
                <button>
                    Buy Now
                </button>
            </a>
            ''',
            unsafe_allow_html=True
        )
    
    st.subheader(recommended_book[4])
    col1,col2=st.columns(2)
    with col1:
        st.image(recommended_book_posters[4],width=200)
    with col2:
        st.components.v1.html(get_desc(recommended_book[4]), width=None, height=200, scrolling=True)
        
        
        link= booklist[booklist["title"]==recommended_book[3]]['url'].tolist()[0]
        
        rec_link= "https://bookdepository.com" + link
        
        
        st.write(f'''
            <a target="_blank" href={rec_link}>
                <button>
                    Buy Now
                </button>
                
                
            </a>
            ''',
            unsafe_allow_html=True
        )
    
            
    

    
    