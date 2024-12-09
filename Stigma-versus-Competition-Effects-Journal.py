import streamlit as st
import json

# Load the JSON data
with open("/Users/shivamsingh/PycharmProjects/Strategic_Management/Journal-Info/Stigma-versus-Competition-Effect-Data.json", "r") as f:
    data = json.load(f)

# Load Custom CSS
def load_css(css_file_path):
    with open(css_file_path, "r") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Path to the CSS file
css_file_path = "/Users/shivamsingh/PycharmProjects/Strategic_Management/Styling/Genereal-Styling.css"
load_css(css_file_path)

# Header Section
st.markdown("""
       <header>
           <h1>Systematic Literature Review</h1>
       </header>
   """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# 2. Title
st.header("Title")
st.subheader(f"{data['systematic_literature_review']['2. Title']}")

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# 1. Authors Section
st.header("Authors")
for author in data["systematic_literature_review"]["1. Authors"]:
    st.image(author["photo"], caption=author["name"], width=300)  # Use correct path here
    st.write(f"**Affiliation:** {author['affiliation']}")
    st.write(f"**Expertise:** {author['expertise']}")
    st.write(f"**Contributions:** {author['contributions']}")
    st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)



# 3. Year of Publication
st.header("Year of Publication")
st.markdown(f"<p>{data['systematic_literature_review']['3. Year of Publication']}</p>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# 4. Journal
st.header("Journal")
journal = data["systematic_literature_review"]["4. Journal"]
st.markdown(f"""
   <p><b>Name:</b> {journal['name']}</p>
   <p><b>Volume:</b> {journal['volume']}, <b>Issue:</b> {journal['issue']}, <b>Pages:</b> {journal['pages']}</p>
   <p>{journal['description']}</p>
   """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# 5. Link/DOI
st.header("Link/DOI")
st.markdown(f"<a href='https://doi.org/{journal['name']}'>{data['systematic_literature_review']['5. Link/DOI']}</a>",
            unsafe_allow_html=True)

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# 6. Abstract
st.header("Abstract")
abstract = data["systematic_literature_review"]["6. Abstract"]
st.markdown(f"<p>{abstract['summary']}</p>", unsafe_allow_html=True)
for effect in abstract["effects"]:
    st.markdown(f"<b>{effect['name']}:</b> {effect['description']}", unsafe_allow_html=True)
st.markdown(f"<p><b>Findings:</b> {abstract['findings']}</p>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# 7. Theory/Theoretical Basis
st.header("Theory and Theoretical Basis")
theories = data["systematic_literature_review"]["7. Theory/Theoretical Basis"]
for theory in theories:
    st.markdown(f"<h3>{theory['name']}</h3>", unsafe_allow_html=True)
    for point in theory["key_points"]:
        st.markdown(f"- {point}")

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# 8. Hypotheses
st.header("Hypotheses")
hypotheses = data["systematic_literature_review"]["8. Hypotheses"]
for hypothesis in hypotheses:
    st.markdown(f"<b>{hypothesis['hypothesis']}:</b> {hypothesis['statement']} <i>({hypothesis['rationale']})</i>",
                unsafe_allow_html=True)

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# 9. Key Variables
st.header("Key Variables")
variables = data["systematic_literature_review"]["9. Key Variables"]
st.markdown("**Independent Variables:**")
st.write(", ".join(variables["independent_variables"]))
st.markdown("**Dependent Variables:**")
st.write(", ".join(variables["dependent_variables"]))
st.markdown("**Moderators:**")
st.write(", ".join(variables["moderators"]))

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# 10. Statistical Method
st.header("Method: Statistical Method")
method = data["systematic_literature_review"]["10. Method: Statistical Method"]
st.markdown("**Event Study Method:**")
for point in method["event_study_method"]:
    st.markdown(f"- {point}")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("**OLS Regression:**")
for point in method["ols_regression"]:
    st.markdown(f"- {point}")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("**Robustness Checks:**")
for point in method["robustness_checks"]:
    st.markdown(f"- {point}")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("**Data Sources:**")
st.write(", ".join(method["data_sources"]))

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# 11. Sample & Data Sources
st.header("Sample & Data Sources")
sample_data = data["systematic_literature_review"]["11. Sample & Data Sources/Databases"]
st.markdown(f"<p>{sample_data['sample']}</p>", unsafe_allow_html=True)
st.markdown("**Data Sources:**")
st.write(", ".join(sample_data["data_sources"]))

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Embedding Table Images
st.header("Predicted Association of Stock Market Valuation and Product Market Overlap")
st.image("/Users/shivamsingh/PycharmProjects/Strategic_Management/Journal-Figure/Stigma-versus-Competition-Figure1.png", caption="Figure 1: Predicted Association of Stock Market Valuation and Product Market Overlap", use_container_width=True)

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Embedding Table Images
st.header("Distributions of Market Overlap at Three Levels of Granularity")
st.image("/Users/shivamsingh/PycharmProjects/Strategic_Management/Journal-Figure/Stigma-versus-Competition-Figure2.png", caption="Figure 2: Distributions of Market Overlap at Three Levels of Granularity", use_container_width=True)


st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Embedding Table Images
st.header("Regression of Non-accused Firm’s CAR on Market Overlap at Three Levels of Granularity (N = 2,759)")
st.image("/Users/shivamsingh/PycharmProjects/Strategic_Management/Journal-Table/Stigma-versus-Competition-Table1.png", caption="Table 1: Regression of Non-accused Firm’s CAR on Market Overlap at Three Levels of Granularity (N = 2,759)", use_container_width=True)


st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Embedding Table Images
st.header("Regression of Non-accused Firm’s CAR on Market Overlap at Three Levels of Granularity (N = 2,759)")
st.image("/Users/shivamsingh/PycharmProjects/Strategic_Management/Journal-Table/Stigma-versus-Competition-Table1_Continued.png", caption="Table 1 Continued: Regression of Non-accused Firm’s CAR on Market Overlap at Three Levels of Granularity (N = 2,759)", use_container_width=True)

# Embedding Table Images
st.header("Observed Association between CAR and Product Market Overlap")
st.image("/Users/shivamsingh/PycharmProjects/Strategic_Management/Journal-Figure/Stigma-versus-Competition-Figure3.png", caption="Figure 3: Observed Association between CAR and Product Market Overlap", use_container_width=True)

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Embedding Table Images
st.header("Regression on Change in Investor Shareholding in Non-accused Firms (N = 151,062)")
st.image("/Users/shivamsingh/PycharmProjects/Strategic_Management/Journal-Table/Stigma-versus-Competition-Table2.png", caption="Table 2: Regression on Change in Investor Shareholding in Non-accused Firms (N = 151,062)", use_container_width=True)


st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Embedding Table Images
st.header("Regression on Change in Investor Shareholding in Non-accused Firms (N = 151,062)")
st.image("/Users/shivamsingh/PycharmProjects/Strategic_Management/Journal-Table/Stigma-versus-Competition-Table2_Contiued.png", caption="Table 2 Continued: Regression on Change in Investor Shareholding in Non-accused Firms (N = 151,062)", use_container_width=True)


st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Embedding Table Images
st.header("Shareholdings in Non-accused Firms by Market Overlap and Investor Sophistication")
st.image("/Users/shivamsingh/PycharmProjects/Strategic_Management/Journal-Figure/Stigma-versus-Competition-Figure4.png", caption="Figure 4: Shareholdings in Non-accused Firms by Market Overlap and Investor Sophistication", use_container_width=True)

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# Results and Conclusions
st.header("Results and Conclusions")
results = data["systematic_literature_review"]["results_and_conclusions"]
for finding in results["findings"]:
    st.markdown(f"<h3>{finding['title']}</h3>", unsafe_allow_html=True)
    for detail in finding["details"]:
        st.markdown(f"- {detail}")

        # st.markdown("<br>", unsafe_allow_html=True)
st.markdown("**Implications:**")
for key, implications in results["implications"].items():

    for implication in implications:
        st.markdown(f"<h3>{implication['title']}</h3>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        for detail in implication["details"]:
            st.markdown(f"- {detail}")

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)
# Criticism and Future Research
st.header("Criticism and Future Research")
criticism = data["systematic_literature_review"]["criticism_and_future_research"]["criticism"]
st.markdown("**Criticism:**")
for point in criticism:
    st.markdown(f"<h3>{point['title']}</h3>", unsafe_allow_html=True)
    for detail in point["details"]:
        st.markdown(f"- {detail}")


future_research = data["systematic_literature_review"]["criticism_and_future_research"]["future_research"]
st.markdown("**Future Research:**")
for point in future_research:
    st.markdown(f"<h3>{point['title']}</h3>", unsafe_allow_html=True)
    for detail in point["details"]:
        st.markdown(f"- {detail}")

# Footer
st.markdown("""
       <footer>
           <p>&copy; 2024 Systematic Literature Review</p>
       </footer>
   """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

