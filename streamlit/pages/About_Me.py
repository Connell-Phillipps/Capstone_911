import streamlit as st

st.title("About Me")

col1, col2 = st.columns(2)

with col1:
    st.image('..\misc\headshot.jpg')

with col2:
    st.markdown("""Hello,\n 
I'm Connell Phillipps. Being a mechanical engineer, I've always found joy in deciphering intricate puzzles. 
Yet Lately, I felt an undeniable pull toward data science and computer learning. I find something captivating 
about using my knack for problem-solving to dive into datasets, unveiling hidden truths about our world. 
This transition isn't just about switching gears; it's about merging my engineering roots with a desire 
to confront real-world challenges. Guided by data, I am on a mission to understand the world around us more 
deeply. """)

st.markdown("""     
### **Connect with me:**
- [GitHub](https://github.com/Connell-Phillipps/Connell-Phillipps)
- [LinkedIn](www.linkedin.com/in/connell-phillipps)
""")