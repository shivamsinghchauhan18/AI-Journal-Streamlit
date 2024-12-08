import os
import nltk
import streamlit as st
import pandas as pd
import json


# Load Custom CSS
def load_css(css_file_path):
    with open("/Users/shivamsingh/PycharmProjects/Strategic Management/Styling/Genereal-Styling.css", "r") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Embed the CSS
css_path = os.path.join(os.path.dirname(__file__), "style.css")
load_css(css_path)

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

# Title and Basic Information
st.title(AI_Journal_data["literature_review"]["basic_information"]["title"])

# Authors Section
st.header("Authors")
authors = AI_Journal_data["literature_review"]["basic_information"]["authors"]
cols = st.columns(len(authors))

for idx, author in enumerate(authors):
    with cols[idx]:
        st.image(author["photo"], caption=author["name"], use_container_width=True)
        st.markdown(f"<p><b>Name:</b> {author['name']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><b>Affiliation:</b> {author['affiliation']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><b>Expertise:</b> {author['expertise']}</p>", unsafe_allow_html=True)

# Year of Publication and Journal
st.markdown(f"<p><b>Year of Publication:</b> {AI_Journal_data['literature_review']['basic_information']['year_of_publication']}</p>", unsafe_allow_html=True)
journal_info = AI_Journal_data["literature_review"]["basic_information"]["journal"]
st.markdown(f"<p><b>Journal:</b> {journal_info['name']} ({journal_info['publisher']})</p>", unsafe_allow_html=True)
st.markdown(f"<p><b>Impact:</b> {journal_info['impact']}</p>", unsafe_allow_html=True)
st.markdown(f"<p><a href='{AI_Journal_data['literature_review']['basic_information']['doi']}'><b>DOI:</b> {AI_Journal_data['literature_review']['basic_information']['doi']}</a></p>", unsafe_allow_html=True)

# Abstract Section
st.header("Abstract")
st.write(AI_Journal_data["literature_review"]["abstract"]["summary"])

# Theory and Theoretical Basis
st.header("Theory and Theoretical Basis")
theories = AI_Journal_data["literature_review"]["details"]["theory_and_theoretical_basis"]["core_theories"]
for theory in theories:
    st.markdown(f"<p><b>{theory['name']}:</b> {theory['description']}</p>", unsafe_allow_html=True)
st.markdown("**Supporting Frameworks:**", unsafe_allow_html=True)
frameworks = AI_Journal_data["literature_review"]["details"]["theory_and_theoretical_basis"]["supporting_frameworks"]
for framework in frameworks:
    st.markdown(f"<li>{framework}</li>", unsafe_allow_html=True)
st.markdown("**Key Insights:**", unsafe_allow_html=True)
key_insights = AI_Journal_data["literature_review"]["details"]["theory_and_theoretical_basis"]["key_insights"]
for insight in key_insights:
    st.markdown(f"<li>{insight}</li>", unsafe_allow_html=True)

# Hypotheses Section
st.header("Hypotheses")
hypotheses = AI_Journal_data["literature_review"]["details"]["hypotheses"]
for hypothesis in hypotheses:
    for key, value in hypothesis.items():
        st.markdown(f"<p><b>{key}:</b> {value}</p>", unsafe_allow_html=True)

# Key Variables
st.header("Key Variables")
st.subheader("Independent Variables")
for variable in AI_Journal_data["literature_review"]["details"]["key_variables"]["independent_variables"]:
    st.markdown(f"<li>{variable}</li>", unsafe_allow_html=True)
st.subheader("Dependent Variables")
for variable in AI_Journal_data["literature_review"]["details"]["key_variables"]["dependent_variables"]:
    st.markdown(f"<li>{variable}</li>", unsafe_allow_html=True)
st.subheader("Moderators")
for moderator in AI_Journal_data["literature_review"]["details"]["key_variables"]["moderators"]:
    st.markdown(f"<p><b>{moderator['name']}:</b> {moderator['description']}</p>", unsafe_allow_html=True)

# Statistical Method
st.header("Method: Statistical Method")
method = AI_Journal_data["literature_review"]["details"]["method_statistical_method"]
st.markdown(f"<p><b>Research Design:</b> {method['research_design']}</p>", unsafe_allow_html=True)
st.markdown("**Measures:**", unsafe_allow_html=True)
for measure in method["measures"]:
    st.markdown(f"<p><b>{measure['name']}:</b> {measure['description']}</p>", unsafe_allow_html=True)
st.markdown("**Analysis Techniques:**", unsafe_allow_html=True)
for technique in method["analysis_techniques"]:
    st.markdown(f"<li>{technique}</li>", unsafe_allow_html=True)
st.markdown("**Control Variables:**", unsafe_allow_html=True)
for control in method["control_variables"]:
    st.markdown(f"<li>{control}</li>", unsafe_allow_html=True)
st.markdown("**Robustness Checks:**", unsafe_allow_html=True)
for check in method["robustness_checks"]:
    st.markdown(f"<li>{check}</li>", unsafe_allow_html=True)

# Sample and Data Sources
st.header("Sample and Data Sources")
sample_info = AI_Journal_data["literature_review"]["details"]["sample_and_data_sources"]
st.markdown(f"<p><b>Sample:</b> {sample_info['sample']}</p>", unsafe_allow_html=True)
st.markdown("**Industries:**", unsafe_allow_html=True)
for industry in sample_info["industries"]:
    st.markdown(f"<li>{industry}</li>", unsafe_allow_html=True)
st.markdown("**Data Sources:**", unsafe_allow_html=True)
for source in sample_info["data_sources"]:
    st.markdown(f"<li>{source}</li>", unsafe_allow_html=True)


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
st.dataframe(table_1_df,hide_index=True)

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

st.dataframe(new_table_df,hide_index=True)

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
st.dataframe(new_table_df3,hide_index=True)

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

st.dataframe(table_3_df,hide_index=True)

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




