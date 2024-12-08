import os
import streamlit as st
import json


# Load Custom CSS
def load_css(css_file_path):
    with open(css_file_path, "r") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Path to the CSS file
css_file_path = "/Users/shivamsingh/PycharmProjects/Strategic Management/Styling/Genereal-Styling.css"
load_css(css_file_path)


# Load JSON data
with open("/Users/shivamsingh/PycharmProjects/Strategic Management/Journal-Info/Making-Business-Model-Decision-Journal.json", "r") as file:
    journal_data = json.load(file)

# Title and Basic Information
st.title(journal_data["literature_review"]["basic_information"]["title"])

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Authors Section
st.header("Authors")
authors = journal_data["literature_review"]["basic_information"]["authors"]
cols = st.columns(len(authors))

for idx, author in enumerate(authors):
    with cols[idx]:
        st.image(author["photo"], caption=author["name"], use_container_width=True)
        st.markdown(f"<p><b>Name:</b> {author['name']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><b>Affiliation:</b> {author['affiliation']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><b>Expertise:</b> {author['expertise']}</p>", unsafe_allow_html=True)

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Year of Publication and Journal
st.markdown(f"<p><b>Year of Publication:</b> {journal_data['literature_review']['basic_information']['year_of_publication']}</p>", unsafe_allow_html=True)
journal_info = journal_data["literature_review"]["basic_information"]["journal"]
st.markdown(f"<p><b>Journal:</b> {journal_info['name']} ({journal_info['publisher']})</p>", unsafe_allow_html=True)
st.markdown(f"<p><b>Impact:</b> {journal_info['impact']}</p>", unsafe_allow_html=True)
st.markdown(f"<p><a href='{journal_data['literature_review']['basic_information']['doi']}'><b>DOI:</b> {journal_data['literature_review']['basic_information']['doi']}</a></p>", unsafe_allow_html=True)


# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Abstract Section
st.header("Abstract")
st.write(journal_data["literature_review"]["abstract"]["summary"])


# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Theory and Theoretical Basis
st.header("Theory and Theoretical Basis")
theories = journal_data["literature_review"]["details"]["theory_and_theoretical_basis"]["core_theories"]
for theory in theories:
    st.markdown(f"<p><b>{theory['name']}:</b> {theory['description']}</p>", unsafe_allow_html=True)
st.markdown("**Supporting Frameworks:**", unsafe_allow_html=True)
frameworks = journal_data["literature_review"]["details"]["theory_and_theoretical_basis"]["supporting_frameworks"]
for framework in frameworks:
    st.markdown(f"<li>{framework}</li>", unsafe_allow_html=True)
st.markdown("**Key Insights:**", unsafe_allow_html=True)
key_insights = journal_data["literature_review"]["details"]["theory_and_theoretical_basis"]["key_insights"]
for insight in key_insights:
    st.markdown(f"<li>{insight}</li>", unsafe_allow_html=True)


# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Hypotheses Section
st.header("Hypotheses")
hypotheses = journal_data["literature_review"]["details"]["hypotheses"]
for hypothesis in hypotheses:
    for key, value in hypothesis.items():
        st.markdown(f"<p><b>{key}:</b> {value}</p>", unsafe_allow_html=True)

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Key Variables
st.header("Key Variables")
st.subheader("Independent Variables")
for variable in journal_data["literature_review"]["details"]["key_variables"]["independent_variables"]:
    st.markdown(f"<li>{variable}</li>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


st.subheader("Dependent Variables")
for variable in journal_data["literature_review"]["details"]["key_variables"]["dependent_variables"]:
    st.markdown(f"<li>{variable}</li>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


st.subheader("Moderators")
for moderator in journal_data["literature_review"]["details"]["key_variables"]["moderators"]:
    st.markdown(f"<p><b>{moderator['name']}:</b> {moderator['description']}</p>", unsafe_allow_html=True)

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Statistical Method
st.header("Method: Statistical Method")
method = journal_data["literature_review"]["details"]["method_statistical_method"]
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

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Sample and Data Sources
st.header("Sample and Data Sources")
sample_info = journal_data["literature_review"]["details"]["sample_and_data_sources"]
st.markdown(f"<p><b>Sample:</b> {sample_info['sample']}</p>", unsafe_allow_html=True)
st.markdown("**Industries:**", unsafe_allow_html=True)
for industry in sample_info["industries"]:
    st.markdown(f"<li>{industry}</li>", unsafe_allow_html=True)
st.markdown("**Data Sources:**", unsafe_allow_html=True)
for source in sample_info["data_sources"]:
    st.markdown(f"<li>{source}</li>", unsafe_allow_html=True)


# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Embedding Table Images
st.header("Balance Checks")
st.image("images/Making-Business-Model-Decision-Table1.png", caption="Table 1: Balance Checks", use_container_width=True)
st.image("images/Making-Business-Model-Decision-Table1-Continued.png", caption="Table 1: Balance Checks (Continued)", use_container_width=True)
# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

st.header("Descriptive Statistics and Pairwise Correlation")
st.image("/Users/shivamsingh/PycharmProjects/Strategic Management/images/Making-Business-Model-Decision-Table2.png", caption="Table 2: Descriptive Statistics and Pairwise Correlation", use_container_width=True)

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

st.header("Impact of the Treatment on Performance")
st.image("images/Making-Business-Model-Decision-Table3.png", caption="Impact of the Treatment on Performance", use_container_width=True)

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

st.header("Impact of Treatment on Performance for different degrees of business model development")
st.image("images/Making-Business-Model-Decision-graph1.png", caption="Impact of Treatment on Performance for different degrees of business model development", use_container_width=True)

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


st.header("Alternative interpretations #1 and #2: Confidence and experience")
st.image("images/Making-Business-Model-Decision-Table5.png", caption="Alternative interpretations #1 and #2: Confidence and experience", use_container_width=True)

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

st.header("Alternative interpretation #3: Choice commitment, value expectations, and certainty about value distribution")
st.image("images/Making-Business-Model-Decision-Table6.png", caption="Alternative interpretation #3: Choice commitment, value expectations, and certainty about value distribution", use_container_width=True)

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

st.header("Effect of the treatment on expectations and certainty about value distribution.")
st.image("images/Making-Business-Model-Decision-graph2.png", caption="Effect of the treatment on expectations and certainty about value distribution.", use_container_width=True)

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Results and Conclusions
st.header("Results and Conclusions")
results = journal_data["literature_review"]["details"]["results_and_conclusions"]

st.subheader("Impact of Scientific Decision-Making")
st.markdown("**Positive Outcomes for Mature Business Models:**", unsafe_allow_html=True)
for outcome in results["impact_of_scientific_decision_making"]["positive_outcomes_for_mature_business_models"]:
    st.markdown(f"<li>{outcome}</li>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("**Challenges for Immature Business Models:**", unsafe_allow_html=True)
for challenge in results["impact_of_scientific_decision_making"]["challenges_for_immature_business_models"]:
    st.markdown(f"<li>{challenge}</li>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Epistemic Uncertainty")
st.markdown(f"**Definition:** {results['epistemic_uncertainty']['definition']}", unsafe_allow_html=True)
st.markdown("**Short-Term Impacts:**", unsafe_allow_html=True)
for impact in results["epistemic_uncertainty"]["short_term_impacts"]:
    st.markdown(f"<li>{impact}</li>", unsafe_allow_html=True)
st.markdown("**Long-Term Benefits:**", unsafe_allow_html=True)
for benefit in results["epistemic_uncertainty"]["long_term_benefits"]:
    st.markdown(f"<li>{benefit}</li>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Moderating Role of Business Model Maturity")
st.markdown("**Well-Defined Models:**", unsafe_allow_html=True)
for model in results["moderating_role_of_business_model_maturity"]["well_defined_models"]:
    st.markdown(f"<li>{model}</li>", unsafe_allow_html=True)
st.markdown("**Poorly Defined Models:**", unsafe_allow_html=True)
for model in results["moderating_role_of_business_model_maturity"]["poorly_defined_models"]:
    st.markdown(f"<li>{model}</li>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Quantitative Insights")
for insight in results["quantitative_insights"]:
    st.markdown(f"<li>{insight}</li>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Strategic Implications")
for implication in results["strategic_implications"]:
    st.markdown(f"<li>{implication}</li>", unsafe_allow_html=True)

# Add a horizontal divider and spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Criticism and Future Research
st.header("Criticism and Future Research")
criticism = journal_data["literature_review"]["details"]["criticism_and_future_research"]
st.subheader("Criticism")
for point in criticism["criticism"]:
    st.markdown(f"<li>{point}</li>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Future Research Directions")
for direction, items in criticism["future_research_directions"].items():
    st.markdown(f"<p><b>{direction.replace('_', ' ').title()}:</b></p>", unsafe_allow_html=True)
    for item in items:
        st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)