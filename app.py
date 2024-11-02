import streamlit as st
import os
from agents.industry_research import industry_research, competitor_analysis
from agents.use_case_generation import generate_use_cases
from agents.resource_asset_collection import resource_asset_collection
from agents.proposal_creation import create_proposal

def main():
    # Set the title of the Streamlit app
    st.title("AI & Generative AI Use Case Generator")

    # Define the industry name
    industry_name = "Finance"  # You can also allow the user to select or input the industry

    # Input for company name
    company_name = st.text_input("Please enter the company name:")

    if st.button("Generate Proposal"):
        if company_name:
            st.write(f"Processing {company_name}...")

            # Ensure the output directory exists
            os.makedirs("output", exist_ok=True)

            # Step 1: Conduct industry and competitor research
            insights = industry_research(industry_name, company_name)  # Pass both industry and company
            competitors = competitor_analysis(company_name)

            # Step 2: Generate use cases
            use_cases = generate_use_cases(insights, industry_name)

            # Step 3: Collect resource assets
            dataset_links = resource_asset_collection(use_cases, industry_name)

            # Step 4: Create a final proposal
            proposal = create_proposal(insights, use_cases, dataset_links, industry_name)

            # Save the proposal to a file, named after the company
            proposal_file_name = f"output/proposal_{company_name.replace(' ', '_')}.md"
            with open(proposal_file_name, "w", encoding="utf-8") as file:
                file.write(proposal)

            st.success(f"Proposal for {company_name} created successfully at {proposal_file_name}.")
        else:
            st.warning("Please enter a valid company name.")

if __name__ == "__main__":
    main()