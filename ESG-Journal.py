import os

import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Load Custom CSS
def load_css(css_file_path):
    with open("/Users/shivamsingh/PycharmProjects/Strategic Management/Styling/Genereal-Styling.css", "r") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Embed the CSS
css_path = os.path.join(os.path.dirname(__file__), "style.css")
load_css(css_path)



# Load JSON data for the literature review
with open("/Users/shivamsingh/PycharmProjects/pythonProject1/Journal-Info/ESG-Journal-Data.json", "r") as file:
    data = json.load(file)

# Load JSON data for Table 1 (Descriptive Statistics and Pairwise Correlations)
with open("/Users/shivamsingh/PycharmProjects/pythonProject1/Journal-Table/ESG-Journal-Table1.json", "r") as file:
    table_data = json.load(file)

# Load JSON data for Table 2 (Fixed-effects panel regressions)
with open("/Users/shivamsingh/PycharmProjects/pythonProject1/Journal-Table/ESG-Journal-Table2.json", "r") as file:
    table2_data = json.load(file)

# Load JSON data for Table 3
with open("/Users/shivamsingh/PycharmProjects/pythonProject1/Journal-Table/ESG-Journal-Table-3.json", "r") as file:
    table3_data = json.load(file)


# Load Table 4 JSON data
with open("/Users/shivamsingh/PycharmProjects/pythonProject1/Journal-Table/ESG-Journal-Table4.json", "r") as file:
    table4_data = json.load(file)

# Load JSON data for Table 5
with open("/Users/shivamsingh/PycharmProjects/pythonProject1/Journal-Table/ESG-Journal-Table5.json", "r") as file:
    table5_data = json.load(file)

# App Title and Basic Information
st.title(data["literature_review"]["basic_information"]["title"])
st.subheader("Authors: " + ", ".join(data["literature_review"]["basic_information"]["authors"]))
st.write(f"Year: {data['literature_review']['basic_information']['year_of_publication']}")
st.write(f"Journal: {data['literature_review']['basic_information']['journal']}")
st.write(f"[Read the Article]({data['literature_review']['basic_information']['link']})")


# Add spacing
st.markdown("<br><br>", unsafe_allow_html=True)


# Add Author Photos
st.subheader("Authors")
authors = data["literature_review"]["basic_information"]["authors_photos"]
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
st.write(data["literature_review"]["details"]["abstract"])


# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Key Variables Section
st.header("Key Variables")
variables_data = {
    "Variable Type": ["Independent", "Dependent", "Moderator"],
    "Details": [
        ", ".join(data["literature_review"]["details"]["key_variables"]["independent_variables"]),
        ", ".join(data["literature_review"]["details"]["key_variables"]["dependent_variables"]),
        ", ".join(data["literature_review"]["details"]["key_variables"]["moderators"]),
    ],
}
st.dataframe(pd.DataFrame(variables_data),hide_index=True, use_container_width=True)


# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Sample and Data Sources
st.header("Sample & Data Sources")
st.write(f"**Sample:** {data['literature_review']['details']['sample_and_data_sources']['sample']}")
st.write("**Data Sources:**")
for source in data["literature_review"]["details"]["sample_and_data_sources"]["data_sources"]:
    st.write(f"- {source}")
# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)



# Theory and Theoretical Basis Section
st.header("Theory and Theoretical Basis")
st.write("**Conceptual Foundation:**")
for concept in data["literature_review"]["details"]["theory_and_theoretical_basis"]["conceptual_foundation"]:
    st.write(f"- {concept}")
st.write("**Key Theoretical Insights:**")
for insight in data["literature_review"]["details"]["theory_and_theoretical_basis"]["key_theoretical_insights"]:
    st.write(f"- {insight}")
st.write(f"**Central Argument:** {data['literature_review']['details']['theory_and_theoretical_basis']['central_argument']}")


# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Hypotheses Section
st.header("Hypotheses")
for idx, hypothesis in enumerate(data["literature_review"]["details"]["hypotheses"], start=1):
    st.write(f"- **Hypothesis {idx}**: {hypothesis['rationale']}")
# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Method: Statistical Method
st.header("Method: Statistical Method")
st.write("**Research Design:**")
for design in data["literature_review"]["details"]["method_statistical_method"]["research_design"]:
    st.write(f"- {design}")
st.write("**Key Statistical Tools:**")
for tool in data["literature_review"]["details"]["method_statistical_method"]["key_statistical_tools"]:
    st.write(f"- {tool}")
st.write("**Analytical Details:**")
for detail in data["literature_review"]["details"]["method_statistical_method"]["analytical_details"]:
    st.write(f"- {detail}")


# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)



# Table: Descriptive Statistics and Pairwise Correlations
st.header("Descriptive Statistics and Pairwise Correlations")
variables = [var["Variable"] for var in table_data["Table"]["Variables"]]
means = [var["Mean"] for var in table_data["Table"]["Variables"]]
sds = [var["S.D."] for var in table_data["Table"]["Variables"]]
correlations = [var["Correlations"] for var in table_data["Table"]["Variables"]]

# Create DataFrame
correlation_table = pd.DataFrame(
    correlations,
    index=[f"{var} (Mean: {mean}, S.D.: {sd})" for var, mean, sd in zip(variables, means, sds)],
    columns=range(1, len(correlations[0]) + 1)
)

st.dataframe(correlation_table,hide_index=True, use_container_width=True)

# Add note from the table
st.caption(table_data["Table"]["Note"])

# Extract variables and correlations from JSON data
variables = [var["Variable"] for var in table_data["Table"]["Variables"]]
correlations = [var["Correlations"] for var in table_data["Table"]["Variables"]]

# Create a DataFrame for correlations
correlation_matrix = pd.DataFrame(correlations, index=variables, columns=variables)

# Generate a heatmap
st.header("Heatmap of Pairwise Correlations")
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Descriptive Statistics and Pairwise Correlations")
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.yticks(fontsize=8)

# Display the heatmap in Streamlit
st.pyplot(plt)
plt.clf()

# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Table: Fixed-effects Panel Regressions on ESG Scores
st.header("Fixed-effects Panel Regressions on ESG Scores")
st.subheader(table2_data["Table"]["Title"])

# Display the table
models_2 = table2_data["Table"]["Models"]
columns = ["Variable"] + [model["Model"] for model in models_2]
rows = []

for variable in models_2[0]:  # Get variable names from the first model
    if variable == "Model":  # Skip the "Model" key
        continue
    row = [variable]
    for model in models_2:
        coefficient = model[variable]["Coefficient"]
        standard_error = model[variable]["Standard Error"]
        p_value = model[variable]["P-value"]
        value = f"{coefficient} ({standard_error}) [{p_value}]" if coefficient is not None else "N/A"
        row.append(value)
    rows.append(row)

# Create a DataFrame to display the table
df_table2 = pd.DataFrame(rows, columns=columns)
st.dataframe(df_table2, hide_index=True, use_container_width=True)

# Add a note if any
st.caption("Note: This table presents the results of fixed-effects panel regressions where robust standard errors are clustered.")


# Ensure predictors are extracted correctly
predictors_table_2 = list(table2_data["Table"]["Models"][0].keys())
predictors_table_2.remove("Model")  # Remove the "Model" key

# Initialize lists to store coefficients and standard errors
coefficients_table_2 = []
std_errors_table_2 = []

# Loop through predictors to extract coefficients and errors
for predictor in predictors_table_2:
    coeffs = []
    errors = []
    for model in table2_data["Table"]["Models"]:
        if isinstance(model.get(predictor), dict):
            # Replace None with 0 for both coefficients and standard errors
            coeff = model[predictor].get("Coefficient", 0) or 0
            error = model[predictor].get("Standard Error", 0) or 0
            coeffs.append(coeff)
            errors.append(error)
        else:
            coeffs.append(0)  # Default to 0 if not a dictionary
            errors.append(0)
    coefficients_table_2.append(coeffs)
    std_errors_table_2.append(errors)

# Plot configuration
x = np.arange(len(predictors_table_2))  # Label locations
width = 0.2  # Width of bars

fig, ax = plt.subplots(figsize=(12, 6))

# Plot each model
for i, model_name in enumerate([model["Model"] for model in table2_data["Table"]["Models"]]):
    coeffs_table_2 = [coeff_table_2[i] for coeff_table_2 in coefficients_table_2]
    errors_table_2 = [err_table_2[i] for err_table_2 in std_errors_table_2]
    ax.bar(x + i * width, coeffs_table_2, width, label=model_name, yerr=errors_table_2, capsize=4)

# Add labels, title, and legend
ax.set_ylabel('Coefficients')
ax.set_title('Fixed-effects panel regression coefficients')
ax.set_xticks(x + width * (len(table2_data["Table"]["Models"]) - 1) / 2)
ax.set_xticklabels(predictors_table_2, rotation=45, ha="right")
ax.legend()

plt.tight_layout()
st.pyplot(fig)

# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Table 3: Fixed-effects panel regressions on the ESG scores
st.header("Fixed-effects panel regressions on the ESG scores-For check")
models_3 = table3_data["Table"]["Models"]

# Create a DataFrame for each model
rows = []
for model in models_3:
    model_name = model["Model"]
    for variable, stats in model.items():
        if variable != "Model":  # Skip the "Model" key itself
            rows.append({
                "Model": model_name,
                "Variable": variable,
                "Coefficient": stats["Coefficient"],
                "Standard Error": stats["Standard Error"],
                "P-value": stats["P-value"]
            })








# Convert rows into a DataFrame
df_table_3 = pd.DataFrame(rows)


# Display the table in Streamlit
st.dataframe(df_table_3, hide_index=True, use_container_width=True)

# Extract models and variables
models_table_3 = table3_data["Table"]["Models"]

# Extract variable names dynamically from the first model
predictors_table_3 = list(models_table_3[0].keys())
predictors_table_3.remove("Model")  # Remove "Model" key

# Prepare data for plotting
coefficients_table_3 = []
std_errors_table_3 = []

for variable in predictors_table_3:
    coeffs_table_3 = []
    errors_table_3 = []
    for model in models_table_3:
        coeff = model.get(variable, {}).get("Coefficient", None)
        std_err = model.get(variable, {}).get("Standard Error", None)
        coeffs_table_3.append(coeff if coeff is not None else 0)
        errors_table_3.append(std_err if std_err is not None else 0)
    coefficients_table_3.append(coeffs_table_3)
    std_errors_table_3.append(errors_table_3)

# Plot configuration
x = np.arange(len(predictors_table_3))  # Label locations
width = 0.2  # Width of bars

fig, ax = plt.subplots(figsize=(12, 6))

# Plot each model
for i, model in enumerate(models_table_3):
    model_name = model["Model"]
    coeffs = [coeff_table[i] for coeff_table in coefficients_table_3]
    errors = [err_table[i] for err_table in std_errors_table_3]
    ax.bar(x + i * width, coeffs, width, label=model_name, yerr=errors, capsize=4)

# Add labels, title, and legend
ax.set_ylabel('Coefficients')
ax.set_title('Fixed-effects panel regression coefficients (Table 3)')
ax.set_xticks(x + width * (len(models_table_3) - 1) / 2)
ax.set_xticklabels(predictors_table_3, rotation=45, ha="right")
ax.legend()

plt.tight_layout()

# Show the plot
st.pyplot(fig)

# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


st.header("Fixed-effects panel regressions on the ESG scores - Model-Wise")
# Create DataFrames for each model and display them
models_4 = table4_data["Table"]["Models"]
for model in models_4:
    st.write(f"### {model['Model']}")
    df_model = pd.DataFrame({
        "Variable": list(model.keys())[1:],
        "Coefficient": [model[var]["Coefficient"] for var in list(model.keys())[1:]],
        "Standard Error": [model[var]["Standard Error"] for var in list(model.keys())[1:]],
        "P-value": [model[var]["P-value"] for var in list(model.keys())[1:]],
    })
    st.dataframe(df_model, hide_index=True, use_container_width=True)


# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# App Section for Table 5
st.header(table5_data["Table"]["Title"])
st.subheader(f"Dependent Variable: {table5_data['Table']['Dependent Variable']}")

# Extract and Display Data for Models
models_5 = table5_data["Table"]["Models"]

# Prepare Data for the Table
table_data = []
for model in models_5:
    row = {"Model": model["Model"]}
    for key, value in model.items():
        if key != "Model" and isinstance(value, dict):  # Handle fields with Coefficient, SE, and P-value
            row[f"{key} Coefficient"] = value.get("Coefficient", "N/A")
            row[f"{key} SE"] = value.get("Standard Error", "N/A")
            row[f"{key} P-value"] = value.get("P-value", "N/A")
        elif key != "Model":
            row[key] = value
    table_data.append(row)

# Create a DataFrame for Display
df_table_5 = pd.DataFrame(table_data)

# Render DataFrame in Streamlit
st.dataframe(df_table_5, hide_index=True, use_container_width=True)

# Results and Conclusions
st.header("Results and Conclusions")
st.subheader("Substitution Dynamics")
for substitution in data["literature_review"]["details"]["results_and_conclusions"]["substitution_dynamics"]:
    st.write(f"- {substitution}")

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Moderating Effects")
st.write("**Historical Conflict:**")
for historical in data["literature_review"]["details"]["results_and_conclusions"]["moderating_effects"]["historical_conflict"]:
    st.write(f"- {historical}")

st.markdown("<br>", unsafe_allow_html=True)

st.write("**Ongoing Conflict:**")
for ongoing in data["literature_review"]["details"]["results_and_conclusions"]["moderating_effects"]["ongoing_conflict"]:
    st.write(f"- {ongoing}")

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Strategic Implications")
for implication in data["literature_review"]["details"]["results_and_conclusions"]["strategic_implications"]:
    st.write(f"- {implication}")


# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)


# Criticism and Future Research
st.header("Criticism and Future Research")
st.subheader("Criticism")
for criticism in data["literature_review"]["details"]["criticism_and_future_research"]["criticism"]:
    st.write(f"- {criticism}")
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Future Research Directions")
for future_research in data["literature_review"]["details"]["criticism_and_future_research"]["future_research_directions"]:
    st.write(f"- {future_research}")



# Add spacing
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)



# Final spacing for clean layout
st.markdown("<br><br>", unsafe_allow_html=True)
