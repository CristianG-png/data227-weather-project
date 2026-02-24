import streamlit as st
from PIL import Image

st.set_page_config(page_title="Analysis of Weather Patterns in Seattle:", layout="wide")

st.title("Analysis of Weather Patterns in Seattle")
st.write(Image.open('images/SeattleNeighborhoodMap.jpg'))
st.write("This project will serve as a demonstration of a Narrative Visualization project with charts\
         designed using Altair. This project is deployed using Streamlit.\n")
st.write(
    "To explore this visual data story, please navigate it through the pages in the sidebar:\n"
    "- **Story**: The central narrative, beginning with taking into account daily weather patterns over time.\n"
    "- **Explore**: For a closer reader-driven exploration of the data, we provide a few interactive designs.\n"
    "- **Methods**: We lay down some key details about our data and limitations to our analysis.\n"
)
st.info("Dataset: `vega_datasets.data.seattle_weather()`")
