import streamlit as st
import pandas as pd
import json

from nltk.app.nemo_app import images

# Load JSON data for the literature review
with open("/Users/shivamsingh/PycharmProjects/pythonProject1/Journal-Info/AI-Journal-Data.json", "r") as file:
    AI_Journal_data = json.load(file)


# Load JSON data for the literature review (new research paper)


# Load JSON data for Table 1
with open("/Users/shivamsingh/PycharmProjects/pythonProject1/Journal-Table/AI-Journal-Table1.json", "r") as file:
    AI_Journal_data_table_1 = json.load(file)

# Load JSON data for the new table
with open("/Users/shivamsingh/PycharmProjects/pythonProject1/Journal-Table/AI-Journal-Table2.json", "r") as file:
    AI_Journal_data_table_2 = json.load(file)

with open("/Users/shivamsingh/PycharmProjects/pythonProject1/Journal-Table/AI-Journal-Table3.json", "r") as file:
    AI_Journal_data_table_3 = json.load(file)

# Load JSON data for Table 3
with open("/Users/shivamsingh/PycharmProjects/pythonProject1/Journal-Table/AI-Journal-Table4.json", "r") as file:
    AI_Journal_data_table_4 = json.load(file)

# App Title and Basic Information
st.title(AI_Journal_data["literature_review"]["basic_information"]["title"])
st.subheader("Authors: " + ", ".join(AI_Journal_data["literature_review"]["basic_information"]["authors"]))
st.write(f"Year: {AI_Journal_data['literature_review']['basic_information']['year']}")
st.write(f"Journal: {AI_Journal_data['literature_review']['basic_information']['journal']}")
st.write(f"[Read the Article]({AI_Journal_data['literature_review']['basic_information']['link']})")


# Add spacing
st.markdown("<br><br>", unsafe_allow_html=True)

# Add Author Photos
st.subheader("Authors")
authors = [
    {"name": "Sebastian Krakowski", "photo": "/Users/shivamsingh/PycharmProjects/pythonProject1/images/images.jpeg", "affiliation": "Stockholm School of Economics"},
    {"name": "Johannes Luger", "photo": "/Users/shivamsingh/PycharmProjects/pythonProject1/images/Johannes-Luger.jpg", "affiliation": "Copenhagen Business School"},
    {"name": "Sebastian Raisch", "photo": "/Users/shivamsingh/PycharmProjects/pythonProject1/images/Sebastian-Raisch.jpg", "affiliation": "University of Geneva"},
]

cols = st.columns(len(authors))
for idx, author in enumerate(authors):
    with cols[idx]:
        st.image(author["photo"], width=150)
        st.subheader(author["name"])
        st.caption(author["affiliation"])


# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Abstract Section
st.header("Abstract")
st.write(AI_Journal_data["literature_review"]["details"]["abstract"])

# Add spacing
st.markdown("<br>", unsafe_allow_html=True)

# Theory Section
st.header("Theory and Theoretical Basis")
st.write("**Basis**: " + AI_Journal_data["literature_review"]["details"]["theory"]["basis"])
st.write("**Key Insights**:")
for insight in AI_Journal_data["literature_review"]["details"]["theory"]["key_insights"]:
    st.write(f"- {insight}")


# Add spacing
st.markdown("<br>", unsafe_allow_html=True)


# Hypotheses Section
st.header("Hypotheses")
for question in AI_Journal_data["literature_review"]["details"]["hypotheses"]["questions_explored"]:
    st.write(f"- {question}")

# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Key Variables Table
st.header("Key Variables")
variables_data = {
    "Variable Type": ["Independent", "Dependent", "Moderator"],
    "Details": [
        ", ".join(AI_Journal_data["literature_review"]["details"]["key_variables"]["independent_variables"]),
        ", ".join(AI_Journal_data["literature_review"]["details"]["key_variables"]["dependent_variables"]),
        ", ".join(AI_Journal_data["literature_review"]["details"]["key_variables"]["moderators"]),
    ],
}
st.dataframe(pd.DataFrame(variables_data))

# Add spacing
st.markdown("<br>", unsafe_allow_html=True)


# Table 1: Effect of Player Capabilities in Different Tournament Formats
st.subheader("Effect of Player Capabilities in Different Tournament Formats")

# Convert JSON data for Table 1 into a DataFrame
variables = AI_Journal_data_table_1["Variables"]
conventional_win = AI_Journal_data_table_1["Conventional"]["Win"]
conventional_loss = AI_Journal_data_table_1["Conventional"]["Loss"]
centaur_win = AI_Journal_data_table_1["Centaur"]["Win"]
centaur_loss = AI_Journal_data_table_1["Centaur"]["Loss"]
engine_win = AI_Journal_data_table_1["Engine"]["Win"]
engine_loss = AI_Journal_data_table_1["Engine"]["Loss"]

# Ensure all arrays have the same length by padding with None where necessary
max_length = max(len(variables), len(conventional_win), len(conventional_loss),
                 len(centaur_win), len(centaur_loss), len(engine_win), len(engine_loss))

def pad_column(column, max_length):
    return column + [None] * (max_length - len(column))

variables = pad_column(variables, max_length)
conventional_win = pad_column(conventional_win, max_length)
conventional_loss = pad_column(conventional_loss, max_length)
centaur_win = pad_column(centaur_win, max_length)
centaur_loss = pad_column(centaur_loss, max_length)
engine_win = pad_column(engine_win, max_length)
engine_loss = pad_column(engine_loss, max_length)

# Create the DataFrame
table_1_df = pd.DataFrame({
    "Variable": variables,
    "Conventional Win": conventional_win,
    "Conventional Loss": conventional_loss,
    "Centaur Win": centaur_win,
    "Centaur Loss": centaur_loss,
    "Engine Win": engine_win,
    "Engine Loss": engine_loss
})

# Display the exact table as it appears
st.dataframe(table_1_df)

# Table 1 Statistics
st.subheader("Statistics for Effect of Player Capabilities in Different Tournament Formats")
st.write(f"**Pseudo R² for Conventional Games**: {AI_Journal_data_table_1['Statistics']['Pseudo R^2']['Conventional']}%")
st.write(f"**Pseudo R² for Centaur Games**: {AI_Journal_data_table_1['Statistics']['Pseudo R^2']['Centaur']}%")
st.write(f"**Pseudo R² for Engine Games**: {AI_Journal_data_table_1['Statistics']['Pseudo R^2']['Engine']}%")
st.write(f"**Number of Observations (N) - Conventional**: {AI_Journal_data_table_1['Statistics']['N']['Conventional']}")
st.write(f"**Number of Observations (N) - Centaur**: {AI_Journal_data_table_1['Statistics']['N']['Centaur']}")
st.write(f"**Number of Observations (N) - Engine**: {AI_Journal_data_table_1['Statistics']['N']['Engine']}")


# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Add New Table: Centaur and Engine Games
st.subheader("Centaur and Engine Games")

# Convert JSON data of new table into a DataFrame
new_table_df = pd.DataFrame({
    "Independent variable": AI_Journal_data_table_2["Table"]["Independent variable"],
    "Centaur Games (Win)": AI_Journal_data_table_2["Table"]["Centaur Games (Win)"],
    "Centaur Games (Loss)": AI_Journal_data_table_2["Table"]["Centaur Games (Loss)"],
    "Engine Games (Win)": AI_Journal_data_table_2["Table"]["Engine Games (Win)"],
    "Engine Games (Loss)": AI_Journal_data_table_2["Table"]["Engine Games (Loss)"]
})

st.dataframe(new_table_df)

# Statistics for the New Table
st.subheader("Statistics for Centaur and Engine Games")
st.write(f"**Pseudo R² for Centaur Games**: {AI_Journal_data_table_2['Table']['Pseudo R²']['Centaur Games']}")
st.write(f"**Pseudo R² for Engine Games**: {AI_Journal_data_table_2['Table']['Pseudo R²']['Engine Games']}")
st.write(f"**Number of Observations (N) - Centaur Games**: {AI_Journal_data_table_2['Table']['N']['Centaur Games']}")
st.write(f"**Number of Observations (N) - Engine Games**: {AI_Journal_data_table_2['Table']['N']['Engine Games']}")

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Effect of human–machine capabilities in the centaur and engine tournament formats")
new_table_df3 = pd.DataFrame({
    "Independent variable": AI_Journal_data_table_3["Table"]["Independent variable"],
    "Centaur Games (Win)": AI_Journal_data_table_3["Table"]["Centaur Games (Win)"],
    "Centaur Games (Loss)": AI_Journal_data_table_3["Table"]["Centaur Games (Loss)"],
    "Engine Games (Win)": AI_Journal_data_table_3["Table"]["Engine Games (Win)"],
    "Engine Games (Loss)": AI_Journal_data_table_3["Table"]["Engine Games (Loss)"]
})
st.dataframe(new_table_df3)

st.subheader("Statistics for Effect of human–machine capabilities in the centaur and engine tournament formats")
st.write(f"**Pseudo R² for Centaur Games**: {AI_Journal_data_table_3['Table']['Pseudo R²']['Centaur Games']}")
st.write(f"**Pseudo R² for Engine Games**: {AI_Journal_data_table_3['Table']['Pseudo R²']['Engine Games']}")
st.write(f"**Number of Observations (N) - Centaur Games**: {AI_Journal_data_table_3['Table']['N']['Centaur Games']}")
st.write(f"**Number of Observations (N) - Engine Games**: {AI_Journal_data_table_3['Table']['N']['Engine Games']}")

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Table 3: Effect of Human–Machine Capabilities in the Centaur and Engine Tournament Formats
st.subheader("Relationship between chess-playing capabilities and human–machine capabilities")

# Convert JSON data of Table 3 into a DataFrame
table_3_df = pd.DataFrame({
    "Dependent variable": AI_Journal_data_table_4["Table"]["Dependent variable"],
    "Human–centaur capabilities": AI_Journal_data_table_4["Table"]["Human–centaur capabilities"],
    "Human–engine capabilities": AI_Journal_data_table_4["Table"]["Human–engine capabilities"]
})

st.dataframe(table_3_df)

# Statistics for Table 3
st.subheader("Statistics for  Relationship between chess-playing capabilities and human–machine capabilities")
st.write(f"**R² (within subjects)**: {AI_Journal_data_table_4['Table']['Statistics']['R² (within subjects)']}")
st.write(f"**Number of Observations (N) - Human–centaur capabilities**: {AI_Journal_data_table_4['Table']['Statistics']['N (Human–centaur capabilities)']}")
st.write(f"**Number of Observations (N) - Human–engine capabilities**: {AI_Journal_data_table_4['Table']['Statistics']['N (Human–engine capabilities)']}")

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Results Section
st.header("Results and Conclusions")
st.subheader("Substitution Dynamics")
for substitution in AI_Journal_data["literature_review"]["details"]["results_and_conclusions"]["substitution_dynamics"]:
    st.write(f"- {substitution}")
# Add spacing
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Complementation Dynamics")
for complementation in AI_Journal_data["literature_review"]["details"]["results_and_conclusions"]["complementation_dynamics"]:
    st.write(f"- {complementation}")
# Add spacing
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Limitations of Machine Capabilities")
for limitation in AI_Journal_data["literature_review"]["details"]["results_and_conclusions"]["limitations_of_machine_capabilities"]:
    st.write(f"- {limitation}")

# Add spacing
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Conclusion")
for conclusion in AI_Journal_data["literature_review"]["details"]["results_and_conclusions"]["conclusion"]:
    st.write(f"- {conclusion}")

# Add spacing
st.markdown("<br>", unsafe_allow_html=True)

st.header("Criticism and Future Research")
st.subheader("Criticism")
for criticism in AI_Journal_data["literature_review"]["details"]["criticism_and_future_research"]["criticism"]:
    st.write(f"- {criticism}")

st.subheader("Future Research Directions")
for future_research in AI_Journal_data["literature_review"]["details"]["criticism_and_future_research"]["future_research_directions"]:
    st.write(f"- {future_research}")


# Final spacing for clean layout
st.markdown("<br><br>", unsafe_allow_html=True)




