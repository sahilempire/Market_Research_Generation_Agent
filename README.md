Certainly, here’s the updated README file with links to the **High-Level/Low-Level Design Document** and **Source Code Architecture Overview**.

---

# **Market Research & Use Case Generation Agent**

## **Project Overview**

This project builds a multi-agent system designed to perform comprehensive market research and generate AI use cases tailored for a specified company or industry. The goal is to analyze market standards, assess competitors, and propose AI-driven solutions that align with the company's operational goals and enhance customer experiences.

---

## **Table of Contents**
1. [High-Level and Low-Level Design](#high-level-and-low-level-design)
2. [Source Code Architecture Overview](#source-code-architecture-overview)
3. [Installation and Setup](#installation-and-setup)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Contributing](#contributing)
7. [License](#license)

---

## **High-Level and Low-Level Design**

### **High-Level Design (HLD)**
The high-level design provides a broad overview of the application, outlining the main components and data flow:
1. **User Interface**:
   - Built with **Streamlit** to capture user input for the company name and industry.
2. **Multi-Agent System**:
   - A set of modular agents, each handling a specific aspect of the workflow, from industry research to proposal creation.
3. **Proposal Generation**:
   - Agents produce insights and a final structured document with suggested use cases and relevant resources.

### **Low-Level Design (LLD)**
The low-level design details the responsibilities and functionalities within each agent:
1. **Industry Research Agent**: Fetches high-level insights on the specified industry.
2. **Competitor Analysis Agent**: Analyzes competitors’ AI usage within the industry.
3. **Use Case Generation Agent**: Proposes AI applications aligned with the company's focus areas.
4. **Resource Collection Agent**: Finds datasets or resources for implementing the use cases.
5. **Proposal Creation Agent**: Compiles all gathered information into a Markdown document.

For an in-depth look at the **High-Level and Low-Level Design**, refer to the full document [here](https://docs.google.com/document/d/1dF4K5eq-rGsFWemyIB7jWYisbDhw6UZsLMs1l3mt78A/edit?usp=sharing).

---

## **Source Code Architecture Overview**

### **Objective**
The objective of this project is to create a structured, modular system where each agent performs a designated role, contributing to the overall goal of producing a tailored AI use-case proposal.

### **Components**

1. **User Interface (UI)**: 
   - **File**: `app.py`
   - **Role**: Takes user input and initiates the process.

2. **Agents**:
   - **Industry Research Agent** (`industry_research.py`): Collects high-level insights into the company’s industry.
   - **Competitor Analysis Agent** (`competitor_analysis.py`): Identifies competitors and their AI initiatives.
   - **Use Case Generation Agent** (`use_case_generation.py`): Proposes AI/ML use cases based on industry insights.
   - **Resource Collection Agent** (`resource_collection.py`): Finds datasets for the proposed use cases.
   - **Proposal Creation Agent** (`proposal_creation.py`): Compiles the insights, use cases, and resources into a formatted Markdown proposal.

3. **Utility Module** (`utils.py`): 
   - Contains helper functions used across different agents.

4. **Output**:
   - **File**: `output/proposal.md`
   - **Content**: A Markdown file containing a well-structured AI/ML use-case proposal.

### **Data Flow**
1. **User Input**: User provides the company name and industry in the UI.
2. **Industry Research**: Insights are generated about the industry.
3. **Competitor Analysis**: Competitors are analyzed for their AI use.
4. **Use Case Generation**: Relevant AI use cases are proposed.
5. **Resource Collection**: Datasets are linked for each use case.
6. **Proposal Creation**: The final proposal document is generated.

For a more detailed **Source Code Architecture Overview**, refer to the document [here](https://docs.google.com/document/d/19vYVqlAD4qdOTYUiH_twYgIcKK2fv9NJXL8nOf0AMG0/edit?usp=sharing).

---

## **Installation and Setup**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/market-research-use-case-generator.git
   cd market-research-use-case-generator
   ```

2. **Install Dependencies**
   Make sure you have `streamlit` and other required packages installed. You can install them via:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## **Usage**

1. **Enter Company Information**:
   - When prompted, enter the company's name and select its industry from the dropdown.
   
2. **Generate Proposal**:
   - The agents will gather insights, suggest use cases, and generate a `proposal.md` file.

3. **Review Proposal**:
   - The proposal document can be found in the `output/` directory.

---

## **Project Structure**

```plaintext
├── app.py                      # Main application file (Streamlit UI)
├── industry_research.py         # Industry research agent
├── competitor_analysis.py       # Competitor analysis agent
├── use_case_generation.py       # Use case generation agent
├── resource_collection.py       # Resource collection agent
├── proposal_creation.py         # Proposal creation agent
├── utils.py                     # Utility functions
├── requirements.txt             # Project dependencies
├── output/
│   └── proposal.md              # Generated proposal file
```

---

## **Contributing**

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
