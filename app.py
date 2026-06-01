import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="JoSAA College Finder",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_excel("JoSAA.xlsx", engine="openpyxl")

    df = df[~df["Closing Rank"].astype(str).str.endswith("P")]

    df["Closing Rank"] = pd.to_numeric(
        df["Closing Rank"],
        errors="coerce"
    )

    return df


df = load_data()

st.title("JoSAA College Finder")
st.subheader(f"View available colleges to you")
st.markdown("---")
st.sidebar.header("Filters")

gender = st.sidebar.selectbox(
    "Gender",
    sorted(df["Gender"].dropna().unique())
)

category = st.sidebar.selectbox(
    "Category",
    sorted(df["Seat Type"].dropna().unique())
)

quota = st.sidebar.selectbox(
    "Quota",
    sorted(df["Quota"].dropna().unique())
)

rank = st.sidebar.number_input(
    "Your Rank",
    min_value=1,
    value=30000,
    step=1000
)

branch = st.sidebar.selectbox(
    "Preferred Branch",
    ["All", "Computer Science and Engineering", "Electronics and Communication Engineering", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering"]
)

available = df[
    (df["Seat Type"] == category)
    & (df["Quota"] == quota)
    & (df["Gender"] == gender)
    & (df["Closing Rank"] > rank)
]
if branch != "All":
    available = available[available["Academic Program Name"].astype(str).str.contains(branch, na=False)]

st.subheader(f"Available Choices ({len(available)})")

st.dataframe(
    available,
    use_container_width=True,
    height=700
)

csv = available.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Results as CSV",
    data=csv,
    file_name="available_colleges.csv",
    mime="text/csv"
)

st.markdown("---")
st.info(
    """
    **Disclaimer:** This tool uses historical JoSAA cutoff data for prediction purposes only.
    Admission outcomes may vary significantly in the current year due to changes in cutoffs,
    seat availability, applicant preferences, and counseling dynamics. Use these results as
    a reference and not as a guarantee of admission.
    """
)