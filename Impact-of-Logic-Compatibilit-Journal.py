import streamlit as st
import json

# Load the JSON data
with open("/Users/shivamsingh/PycharmProjects/Strategic_Management/Journal-Info/Impact-of-logic-data.json", "r") as f:
    data = json.load(f)

# Load Custom CSS
def load_css(css_file_path):
    with open(css_file_path, "r") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Path to the CSS file
css_file_path = "/Users/shivamsingh/PycharmProjects/Strategic_Management/Styling/Genereal-Styling.css"
load_css(css_file_path)

st.markdown("""
       <header>
           <h1>Systematic Literature Review</h1>
       </header>
   """, unsafe_allow_html=True)

# Display Basic Information
st.header("Basic Information")
st.markdown(f"### Title: {data['literature_review']['basic_information']['title']}")
st.markdown(f"**Year of Publication:** {data['literature_review']['basic_information']['year_of_publication']}")
journal = data['literature_review']['basic_information']['journal']
st.markdown(
    f"**Journal:** {journal['name']}, Volume {journal['volume']}, Issue {journal['issue']}, Pages {journal['pages']}")
st.markdown(f"**DOI:** {data['literature_review']['basic_information']['doi']}")

# Authors Section
st.header("Authors")
authors = data["literature_review"]["basic_information"]["authors"]
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

# Abstract Section
st.header("Abstract")
st.markdown(data['literature_review']['abstract']['summary'])

# Theory/Theoretical Basis
st.header("Theory and Theoretical Basis")
theories = data['literature_review']['details']['theory_and_theoretical_basis']['core_theories']
for theory in theories:
    st.markdown(f"**{theory['name']}:** {theory['description']}")
key_insights = data['literature_review']['details']['theory_and_theoretical_basis']['key_insights']
st.markdown("**Key Insights:**")
st.write(", ".join(key_insights))

# Hypotheses Section
st.header("Hypotheses")
st.markdown('<div class="hypotheses">', unsafe_allow_html=True)
for hypothesis in data['literature_review']['details']['hypotheses']:
    for key, value in hypothesis.items():
        st.markdown(f"**{key}:** {value}")
st.markdown('</div>', unsafe_allow_html=True)

# Key Variables
st.header("Key Variables")
st.markdown("**Independent Variables:**")
st.write(", ".join(data['literature_review']['details']['key_variables']['independent_variables']))
st.markdown("**Dependent Variables:**")
st.write(", ".join(data['literature_review']['details']['key_variables']['dependent_variables']))
st.markdown("**Moderators:**")
for moderator in data['literature_review']['details']['key_variables']['moderators']:
    st.markdown(f"- **{moderator['name']}**: {moderator['description']}")

# Method Section
st.header("Methodology")
st.markdown(
    f"**Research Design:** {data['literature_review']['details']['method_statistical_method']['research_design']}")
analysis_techniques = data['literature_review']['details']['method_statistical_method']['analysis_techniques']
st.markdown("**Analysis Techniques:**")
st.write(", ".join(analysis_techniques))
control_vars = data['literature_review']['details']['method_statistical_method']['control_variables']
st.markdown("**Control Variables:**")
st.write(", ".join(control_vars))

# Sample & Data Sources
st.header("Sample & Data Sources")
sample = data['literature_review']['details']['sample_and_data_sources']
st.markdown(f"**Sample:** {sample['sample']}")
st.markdown("**Data Sources:**")
st.write(", ".join(sample['data_sources']))

# Results and Conclusions
st.header("Results and Conclusions")

# Display Findings
findings = data['literature_review']['details']['results_and_conclusions']['findings']
for finding in findings:
    st.markdown(f"### {finding['title']}")
    for detail in finding['details']:
        st.markdown(f"- {detail}")

# Display Implications
implications = data['literature_review']['details']['results_and_conclusions']['implications']
st.markdown("**Implications:**")
for implication in implications:
    st.markdown(f"### {implication['title']}")
    for detail in implication['details']:
        st.markdown(f"- {detail}")

# Criticism and Future Research
st.header("Criticism and Future Research")

# Display Criticism
criticism = data['literature_review']['details']['criticism_and_future_research']['criticism']
st.markdown("**Criticism:**")
for item in criticism:
    st.markdown(f"### {item['title']}")
    for detail in item['details']:
        st.markdown(f"- {detail}")

# Display Future Research Directions
future_research = data['literature_review']['details']['criticism_and_future_research']['future_research_directions']
st.markdown("**Future Research Directions:**")
for item in future_research:
    st.markdown(f"### {item['title']}")
    for detail in item['details']:
        st.markdown(f"- {detail}")

# Footer
st.markdown("""
       <footer>
           <p>&copy; 2024 Systematic Literature Review App</p>
       </footer>
   """, unsafe_allow_html=True)

