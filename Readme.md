# An intelligent financial planning system that combines:

-  Portfolio Analysis
-  Rebalancing Engine
-  AI Advisor (LLM-based)
-  Recommendations Engine
-  Financial Planning (FIRE, Tax, Insurance, Goals)
-------------------------------------------------------------------------------------------------------------------------------
# Overview

This project is a **full-stack fintech decision system** built using Python and Streamlit.

It helps users:
- Understand their portfolio
- Optimize investments
- Plan long-term financial goals
- Get AI-driven financial advice

---------------------------------------------------------------------------------------------------------------------------------
# Key Features

1. Portfolio Analysis
- Asset allocation breakdown
- Risk assessment (Conservative / Moderate / Aggressive)
- Diversification scoring
- Visual charts (Pie + Bar)



2. Rebalancing Engine
- Detects portfolio imbalance
- Suggests actionable buy/sell strategies
- Aligns with risk profile



3. Insights Engine
- Identifies issues like:
  - High equity exposure
  - Low debt allocation
  - Idle cash
- Rule-based financial insights



4. Recommendation Engine
- Actionable financial decisions
- Prioritized suggestions
- Example:
  - Reduce equity exposure
  - Increase debt allocation


5. AI Advisor (LLM-based)
- Explains recommendations in simple language
- Answers user queries
- Context-aware financial assistant



6. Financial Planning Module

  6.1 FIRE (Retirement Planning)
  - Calculates required retirement corpus
  - Monthly SIP needed

  6.2 Goal Planning
  - Inflation-adjusted goal cost
  - SIP required to achieve goals

  6.3Tax Analysis
  - Estimates tax liability
  - Suggests tax-saving strategies

  6.4Insurance Analysis
  - Life insurance requirement
  - Health coverage suggestions

  6.5 XIRR Engine
  - Calculates portfolio returns
----------------------------------------------------------------------------------------------------------------------------------
# Tech Stack

- Python
- Streamlit
- Ollama (Local LLM)
- Matplotlib
----------------------------------------------------------------------------------------------------------------------------------
# Run Locally

```bash
pip install streamlit matplotlib requests numpy pandas scipy
streamlit run app.py
