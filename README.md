"""
# LangGraph Software Quality Control (SQC) Agent

This app audits source code for:
- ✅ Code Style (PEP8, linting)
- ✅ Security (OWASP, Bandit-style)
- ✅ Performance Issues
- ✅ Test Coverage
- ✅ Compliance (GDPR/PCI)

## 📦 Tech Stack
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Streamlit](https://streamlit.io)
- [OpenAI API](https://platform.openai.com)

## 🚀 Getting Started
```bash
git clone https://github.com/your-username/sqc-agent.git
cd sqc-agent
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 🌍 Deployment (Streamlit Cloud)
1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Create New App → Select this repo
4. Set main file to `streamlit_app.py`

## 🔐 API Key
Store your OpenAI key as an environment variable:
```bash
export OPENAI_API_KEY=sk-...
```
Or add a `.streamlit/secrets.toml` file:
```toml
OPENAI_API_KEY = "sk-..."
```

## 🧠 Sample
```python
# Run inside notebook or script
from langgraph_agent import run_code_audit
result = run_code_audit("""
def hello():
    print('Hello, World!')
""")
print(result)
```

---
© 2025 Satish Kuppuswamy | LangGraph Quality Auditor
""""# sqc-agent" 
