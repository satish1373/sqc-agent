#from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langgraph.graph import StateGraph, END
from langchain.schema import SystemMessage, HumanMessage
from typing import TypedDict, Optional

llm = ChatOpenAI(model="gpt-4", temperature=0.3)

class QCState(TypedDict):
    code: str
    style_report: Optional[str]
    security_report: Optional[str]
    performance_report: Optional[str]
    testing_report: Optional[str]
    compliance_report: Optional[str]

def simple_node(prompt_header: str, key: str):
    def node(state: QCState):
        prompt = [
            SystemMessage(content=prompt_header),
            HumanMessage(content=f"Code:\n{state['code']}")
        ]
        return {key: llm(prompt).content}
    return node

def report_node(state: QCState):
    return state

def run_code_audit(code: str):
    builder = StateGraph(QCState)
    builder.add_node("StyleAuditor", simple_node("You are a style auditor. Check code for PEP8 issues.", "style_report"))
    builder.add_node("SecurityAuditor", simple_node("You are a security auditor. Identify OWASP-style issues.", "security_report"))
    builder.add_node("PerformanceAuditor", simple_node("You are a performance auditor. Identify bottlenecks.", "performance_report"))
    builder.add_node("TestingAuditor", simple_node("You are a testing auditor. Check test cases, coverage, mocks.", "testing_report"))
    builder.add_node("ComplianceAuditor", simple_node("You are a compliance auditor. Look for GDPR/PCI violations.", "compliance_report"))
    builder.add_node("Report", report_node)

    builder.set_entry_point("StyleAuditor")
    builder.add_edge("StyleAuditor", "SecurityAuditor")
    builder.add_edge("SecurityAuditor", "PerformanceAuditor")
    builder.add_edge("PerformanceAuditor", "TestingAuditor")
    builder.add_edge("TestingAuditor", "ComplianceAuditor")
    builder.add_edge("ComplianceAuditor", "Report")
    builder.add_edge("Report", END)

    graph = builder.compile()
    return graph.invoke({"code": code})