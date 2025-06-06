import streamlit as sl

sl.write("Hello from Streamlit!")
sl.title("Welcome to My Streamlit App")
sl.header("This is a header")
sl.subheader("This is a subheader")
sl.text("This is a simple text message.")
sl.markdown("This is **bold** text and *italic* text.")
sl.code("print('Hello, World!')", language='python')
sl.latex(r"""
    E = mc^2
""")
sl.json({"name": "Streamlit", "version": "1.0.0"})
sl.dataframe({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})
sl.table({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})
sl.image("https://via.placeholder.com/150")
sl.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
sl.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
sl.checkbox("Check me!")
sl.radio("Choose an option:", options=["Option 1", "Option 2", "Option 3"])
sl.selectbox("Select an option:", options=["Option A", "Option B", "Option C"])
sl.multiselect("Select multiple options:", options=["Option X", "Option Y", "Option Z"])
sl.slider("Slide me!", min_value=0, max_value=100, value=50)
sl.number_input("Enter a number:", min_value=0, max_value=100, value=50)
sl.text_input("Type something:")
sl.text_area("Type a longer text:")
sl.date_input("Select a date:")
sl.time_input("Select a time:")
sl.file_uploader("Upload a file", type=["csv", "txt", "pdf"])
sl.button("Click me!")
sl.download_button("Download data", data="Sample data to download", file_name="sample.txt")
sl.progress(50)  # Progress bar at 50%
sl.spinner("Loading...")
sl.balloons()  # Show balloons animation
sl.sidebar.title("Sidebar Title")
sl.sidebar.write("This is a sidebar.")
sl.sidebar.checkbox("Sidebar checkbox")
sl.sidebar.radio("Sidebar radio:", options=["Option 1", "Option 2"])
sl.sidebar.selectbox("Sidebar selectbox:", options=["Option A", "Option B"])
sl.sidebar.slider("Sidebar slider", min_value=0, max_value=100, value=50)
sl.sidebar.text_input("Sidebar text input:")
sl.sidebar.text_area("Sidebar text area:")
sl.sidebar.file_uploader("Sidebar file uploader", type=["csv", "txt", "pdf"])
sl.sidebar.button("Sidebar button")
sl.sidebar.download_button("Sidebar download", data="Sample sidebar data", file_name="sidebar_sample.txt")
sl.sidebar.progress(75)  # Sidebar progress bar at 75%
with sl.spinner("Sidebar loading..."):
    # Place the sidebar code inside here
    sl.sidebar.write("Something in the sidebar")
sl.sidebar.balloons()  # Show sidebar balloons animation
