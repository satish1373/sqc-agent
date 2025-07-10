# streamlit_app.py
import streamlit as st
from langgraph_agent import run_code_audit
import sys
import os

st.set_page_config(page_title="Software Quality Auditor", layout="wide")
st.title("\U0001F4BB Software Quality Control Auditor")

st.markdown("""
Upload your code, and the multi-agent system will audit it for:
- Style & Linting
- Security Risks
- Performance
- Test Coverage
- Compliance (GDPR/PCI)
""")

uploaded_file = st.file_uploader("Upload Python Code File", type=[".py"])

if uploaded_file:
    code = uploaded_file.read().decode("utf-8")
    st.code(code, language="python")

    if st.button("Run Audit"):
        with st.spinner("Running LangGraph Audit..."):
            report = run_code_audit(code)
        st.success("Audit Completed!")

        st.subheader("Audit Reports")
        for section, content in report.items():
            if section != 'code':
                with st.expander(section.replace("_", " ").title()):
                    st.markdown(f"```text\n{content}\n```")

        st.download_button("Download JSON Report", data=str(report), file_name="report.json")

# langgraph_agent.py

