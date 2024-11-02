def generate_use_cases(insights, industry_name):
    """Generate unique, relevant use cases tailored to each industry."""
    use_cases = []
    for insight in insights:
        if "predictive analytics" in insight:
            use_cases.append(f"{industry_name}-specific Predictive maintenance for equipment.")
        if "customer experience" in insight:
            use_cases.append(f"Customer sentiment analysis using AI in {industry_name}.")

        # Unique case generation based on industry name
        if "supply chain" in insight and industry_name in ["Retail", "Manufacturing"]:
            use_cases.append("AI-powered real-time supply chain optimization.")
        if "customer retention" in insight and industry_name == "Finance":
            use_cases.append("Churn prediction using ML for high-value clients.")
    return use_cases
