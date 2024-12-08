import streamlit as st
import json
from pathlib import Path

# Load the JSON data
with open("Journal-Info/Imapact-of-Logic-(In)Compatibility-Data.json", "r") as f:
    data = json.load(f)

# Load the CSS file
def load_css(css_file_path):
    with open("Styling/Genereal-Styling.css", "r") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Initialize Streamlit App
def main():
    # Load the CSS
    load_css("Genereal-Styling.css")

    # App Header
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
    st.markdown(f"**Journal:** {journal['name']}, Volume {journal['volume']}, Issue {journal['issue']}, Pages {journal['pages']}")
    st.markdown(f"**DOI:** {data['literature_review']['basic_information']['doi']}")

    # Display Authors
    st.header("Authors")
    for author in data['literature_review']['basic_information']['authors']:
        st.markdown(f"""
            <div class="table-image">
                <img src="{author['photo']}" class="author-image" alt="{author['name']}">
                <p><strong>{author['name']}</strong><br>{author['affiliation']}<br>{author['expertise']}</p>
            </div>
        """, unsafe_allow_html=True)

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
    st.markdown(f"**Research Design:** {data['literature_review']['details']['method_statistical_method']['research_design']}")
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
    findings = data['literature_review']['details']['results_and_conclusions']['findings']
    for finding in findings:
        for key, value in finding.items():
            st.markdown(f"**{key}:**")
            st.write(", ".join(value))
    implications = data['literature_review']['details']['results_and_conclusions']['implications']
    st.markdown("**Implications:**")
    for implication in implications:
        for key, value in implication.items():
            st.markdown(f"- **{key}:** {value}")

    # Criticism and Future Research
    st.header("Criticism and Future Research")
    criticism = data['literature_review']['details']['criticism_and_future_research']['criticism']
    st.markdown("**Criticism:**")
    st.write(", ".join(criticism))
    future_research = data['literature_review']['details']['criticism_and_future_research']['future_research_directions']
    st.markdown("**Future Research Directions:**")
    st.write(", ".join(future_research))

    # Footer
    st.markdown("""
        <footer>
            <p>&copy; 2024 Systematic Literature Review App</p>
        </footer>
    """, unsafe_allow_html=True)

