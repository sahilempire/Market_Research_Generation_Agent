def create_proposal(insights, use_cases, dataset_links, industry_name):
    """Create a comprehensive proposal with clear, industry-specific insights."""
    proposal = f"# AI Use Case Proposal for {industry_name}\n\n## Industry Insights\n"
    for insight in insights:
        proposal += f"- {insight}\n"

    proposal += "\n## Proposed Use Cases and Feasibility\n"
    for case in use_cases:
        feasibility = "High" if "Predictive maintenance" in case else "Medium"
        next_steps = "Implement ML models on historical data" if "maintenance" in case else "Develop customer sentiment datasets"

        proposal += f"- **Use Case**: {case}\n"
        proposal += f"  - **Feasibility**: {feasibility}\n"
        proposal += f"  - **Actionable Next Steps**: {next_steps}\n\n"

    proposal += "\n## Resource Links\n"
    for link in dataset_links:
        proposal += f"- [Dataset Link]({link})\n"

    return proposal
