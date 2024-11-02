import requests
from bs4 import BeautifulSoup
import re

def industry_research(industry_name, company_name):
    """Fetch more specific industry and company data based on keywords."""
    insights = []
    # Search query to include company and industry context
    query = f"{company_name} {industry_name} AI trends"
    # Perform a Google search or use an API for more specific data
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    for item in soup.find_all("div", class_="BNeawe"):
        if re.search(r"AI|ML|automation|technology", item.text):
            insights.append(item.text)

    # Example additions based on specific industry focus
    insights.append(f"Exploring GenAI for personalized {industry_name} customer experiences.")
    return insights

def competitor_analysis(company_name):
    """Analyze competitors with more specificity."""
    competitor_insights = []
    competitor_query = f"{company_name} competitors AI use cases"
    # Example placeholder for web scraping results
    competitor_insights.append(f"{company_name} competitor is focusing on AI for customer engagement.")
    return competitor_insights
