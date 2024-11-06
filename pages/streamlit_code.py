import streamlit as st
st.title("streamlit important code")
st.image("https://eu-images.contentstack.com/v3/assets/blt6b0f74e5591baa03/blt7c0bf7e21d4410b4/6319700b8cc2fa14e223aa27/8895.png?width=1280&auto=webp&quality=95&format=jpg&disable=upscale")
st.header("Title")
st.markdown("""In streamlit we can write titlw of the website.""")
st.code(
    'st.title("Streamlit important code")'
)
st.header("Header")
st.markdown("""In streamlit this code cane b used for headers.""")
st.code(
    'st.header("Header")'
)
st.header("markdown")
st.markdown("""In streamlit this code there have different size of text write in paragraphes.""")
st.subheader("bigest size of text.")
st.code(
    'st.markdown("# bigest size of text")'
)
st.subheader("big size of text.")
st.code(
    'st.markdown("## big size of text")'
)
st.subheader("small size of text.")

st.code(
    'st.markdown("### small size of text")'
)
st.subheader("smallest size of text.")

st.code(
    'st.markdown("#### smallest size of text")'
)
st.subheader("paragrapf size of text.")

st.code(
    'st.markdown(""""paragrapf size of text""")'
)
st.header("Caption")
st.markdown(""""This code can b used to write caption.""")
st.code(
    'st.caption("caption")'
)
st.header("Code")
st.markdown(""""This code can b used to write code.""")
st.code(
    'st.code("code")'
)
st.image("https://images.datacamp.com/image/upload/v1640050216/image34_xrej1c.jpg")
st.header("Images")
st.code(
    'st.image("kid.jpg", caption="A kid playing")'
)
st.header("videos")
st.code(
    'st.video("video.mp4")'
)
st.header("audio")
st.code(
    'st.audio("audio.mp3")'
)
st.image("https://images.datacamp.com/image/upload/v1640050214/image7_hswsm1.png")
st.header("checkbox")
st.markdown("""This code can be used to check boxes""")
st.code(
    'st.checkbox("yes")'
)
st.header("Button")
st.markdown("""This code can be used to create buttons""")

st.code(
    'st.button("Click me!")'
)
st.header("click box")
st.code(
    "st.radio('Pick your gender', ['Male', 'Female'])"
)
st.header("slection box")
st.code(
    "st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])"
)
st.header("Multi slection box")
st.code(
    "st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])"
)
st.header("select slider")
st.code(
    "st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])"
)
st.header("select number slider")
st.code(
    "st.slider('Pick a number', 0, 50)"
)
st.image("https://images.datacamp.com/image/upload/v1640050216/image33_cv7qcf.png")
st.header("Data input")
st.code(
    "st.number_input('Pick a number', 0, 10)"
)
st.code(
"st.text_input('Email address')"
)
st.code(
    "st.date_input('Traveling date')"
)
st.code(
    "st.time_input('School time')"
)
st.code(
    "st.text_area('Description')"
)
st.code(
    "st.file_uploader('Upload a photo')"
)
st.code(
    "st.color_picker('Choose your favorite color')"
)
st.image("https://images.datacamp.com/image/upload/v1640050214/image21_ssdlov.png")