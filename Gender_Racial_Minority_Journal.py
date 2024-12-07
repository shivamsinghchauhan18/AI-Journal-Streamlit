import streamlit as st
import json
import pandas as pd

# Load JSON data
with open("Journal-Info/Gender_Racial_Minority_Journal_Data.json", "r") as file:
    gender_racial_minority_journal_data = json.load(file)

# App Title
st.title(gender_racial_minority_journal_data["literature_review"]["basic_information"]["title"])

# Authors Section
# Display Authors with Images
authors = gender_racial_minority_journal_data["literature_review"]["basic_information"]["authors"]

for author_data in authors:
    affiliations = author_data["affiliations"]  # Access the affiliations list
    cols = st.columns(len(affiliations))  # Create columns for affiliations
    for idx, affiliation in enumerate(affiliations):
        with cols[idx]:
            st.image(affiliation["photo"], width=150, caption=affiliation["name"])
            st.write(f"**Affiliation:** {affiliation['affiliation']}")

# Journal Information
st.header("Journal Information")
st.write(f"**Year of Publication:** {gender_racial_minority_journal_data['literature_review']['basic_information']['year_of_publication']}")
st.write(f"**Journal Name:** {gender_racial_minority_journal_data['literature_review']['basic_information']['journal']['name']}")
st.write(f"**Publisher:** {gender_racial_minority_journal_data['literature_review']['basic_information']['journal']['publisher']}")
st.write(f"**DOI:** [Link]({gender_racial_minority_journal_data['literature_review']['basic_information']['doi_link']})")

# Abstract
st.header("Abstract")
st.write(gender_racial_minority_journal_data["literature_review"]["details"]["abstract"])

# Theory Section
st.header("Theory and Theoretical Basis")
st.subheader("Conceptual Framework")
for theory in gender_racial_minority_journal_data["literature_review"]["details"]["theory_and_theoretical_basis"]["conceptual_framework"]:
    st.write(f"- {theory}")

st.subheader("Key Theoretical Insights")
for insight in gender_racial_minority_journal_data["literature_review"]["details"]["theory_and_theoretical_basis"]["key_theoretical_insights"]:
    st.write(f"- {insight}")

st.write(f"**Central Argument:** {gender_racial_minority_journal_data['literature_review']['details']['theory_and_theoretical_basis']['central_argument']}")

st.header("Hypotheses")
for hypothesis in gender_racial_minority_journal_data["literature_review"]["details"]["hypotheses"]:
    # Extract hypothesis ID (H1, H2, H3) and its text
    hypothesis_id = next(key for key in hypothesis.keys() if key != "rationale")
    hypothesis_statement = hypothesis[hypothesis_id]
    rationale = hypothesis.get("rationale", "No rationale provided.")

    # Display hypothesis and rationale
    st.write(f"**{hypothesis_id}**: {hypothesis_statement}")
    st.write(f"Rationale: {rationale}")

# Key Variables Section
st.header("Key Variables")
variables_data = {
    "Variable Type": ["Independent Variables", "Dependent Variables", "Moderators"],
    "Details": [
        ", ".join(gender_racial_minority_journal_data["literature_review"]["details"]["key_variables"]["independent_variables"]),
        ", ".join(gender_racial_minority_journal_data["literature_review"]["details"]["key_variables"]["dependent_variables"]),
        ", ".join(gender_racial_minority_journal_data["literature_review"]["details"]["key_variables"]["moderators"]),
    ],
}
st.dataframe(pd.DataFrame(variables_data))

# Method Section
st.header("Method: Statistical Method")
st.subheader("Research Design")
for design in gender_racial_minority_journal_data["literature_review"]["details"]["method_statistical_method"]["research_design"]:
    st.write(f"- {design}")

st.subheader("Key Measures")
for key, value in gender_racial_minority_journal_data["literature_review"]["details"]["method_statistical_method"]["key_measures"].items():
    st.write(f"- **{key}:** {value}")

st.subheader("Analytical Tools")
for tool in gender_racial_minority_journal_data["literature_review"]["details"]["method_statistical_method"]["analytical_tools"]:
    st.write(f"- {tool}")

st.subheader("Control Variables")
for variable in gender_racial_minority_journal_data["literature_review"]["details"]["method_statistical_method"]["control_variables"]:
    st.write(f"- {variable}")

st.subheader("Robustness Checks")
for check in gender_racial_minority_journal_data["literature_review"]["details"]["method_statistical_method"]["robustness_checks"]:
    st.write(f"- {check}")

# Sample and Data Sources
st.header("Sample & Data Sources")
st.write(f"**Sample:** {gender_racial_minority_journal_data['literature_review']['details']['sample_and_data_sources']['sample']}")
st.write("**Data Sources:**")
for source in gender_racial_minority_journal_data["literature_review"]["details"]["sample_and_data_sources"]["data_sources"]:
    st.write(f"- {source}")
# Results and Conclusions
st.header("Results and Conclusions")

# Key Observations
st.subheader("Key Observations")
for observation in gender_racial_minority_journal_data["literature_review"]["details"]["results_and_conclusions"]["key_observations"]:
    st.write(f"### {observation['observation']}")
    for detail_key, detail_values in observation["details"].items():
        st.markdown(f"**{detail_key.replace('_', ' ').capitalize()}:**")
        for detail in detail_values:
            st.write(f"- {detail}")

# Conclusion
st.subheader("Conclusion")
for conclusion in gender_racial_minority_journal_data["literature_review"]["details"]["results_and_conclusions"]["conclusion"]:
    st.write(f"- {conclusion}")

# Criticism and Future Research
st.header("Criticism and Future Research")
st.subheader("Criticism")
for criticism in gender_racial_minority_journal_data["literature_review"]["details"]["criticism_and_future_research"]["criticism"]:
    st.write(f"- {criticism}")

st.subheader("Future Research Directions")
for direction in gender_racial_minority_journal_data["literature_review"]["details"]["criticism_and_future_research"]["future_research_directions"]:
    st.write(f"- {direction}")

# Footer
st.markdown("---")
