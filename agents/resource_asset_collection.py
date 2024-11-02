def resource_asset_collection(use_cases, industry_name):
    """Collect relevant datasets with an industry-based search."""
    dataset_links = []
    
    if "Predictive maintenance" in use_cases:
        dataset_links.append("https://www.kaggle.com/datasets/predictive-maintenance")

    if "sentiment analysis" in use_cases and industry_name == "Retail":
        dataset_links.append("https://huggingface.co/datasets/sentiment-analysis-retail")
    
    if "supply chain optimization" in use_cases and industry_name in ["Retail", "Manufacturing"]:
        dataset_links.append("https://github.com/datasets/supply-chain")
    
    if "churn prediction" in use_cases and industry_name == "Finance":
        dataset_links.append("https://www.kaggle.com/datasets/finance-churn")
    
    return dataset_links
