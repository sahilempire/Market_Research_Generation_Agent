import os
from agents.industry_research import industry_research, competitor_analysis
from agents.use_case_generation import generate_use_cases
from agents.resource_asset_collection import resource_asset_collection
from agents.proposal_creation import create_proposal

def main():
    # Define the industry name (you can also make this user input if desired)
    industry_name = "Finance"  # You can adjust this as needed

    # Ensure the output directory exists
    os.makedirs("output", exist_ok=True)

    # Prompt the user for the company name
    company_name = input("Please enter the company name: ")

    print(f"Processing {company_name}...")

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
    proposal_file_name = f"output/proposal_{company_name.replace(' ', '_')}.md"  # Use underscores for file naming
    with open(proposal_file_name, "w", encoding="utf-8") as file:
        file.write(proposal)

    print(f"Proposal for {company_name} created successfully at {proposal_file_name}.")

if __name__ == "__main__":
    main()
