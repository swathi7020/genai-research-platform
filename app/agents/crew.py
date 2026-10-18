from crewai import Crew, Process, Task

from app.agents.research_agent import create_research_agent
from app.agents.web_agent import create_web_research_agent
from app.agents.document_agent import create_document_analyst_agent
from app.agents.report_agent import create_report_agent


def create_research_crew(
    question: str,
    pdf_path: str
):

    research_agent = create_research_agent()

    web_agent = create_web_research_agent()

    document_agent = create_document_analyst_agent(
        pdf_path=pdf_path
    )

    report_agent = create_report_agent()

    # ---------------------------------------------------------
    # Research Task
    # ---------------------------------------------------------

    research_task = Task(
        description=f"""
        Analyze the following research question:

        {question}

        Identify the key aspects that need to be investigated.
        Focus on producing useful research findings.
        """,

        expected_output=(
            "A structured list of the key research findings "
            "and important aspects of the question."
        ),

        agent=research_agent
    )

    # ---------------------------------------------------------
    # Web Research Task
    # ---------------------------------------------------------

    web_task = Task(
        description=f"""
        Research the following question using reliable web sources:

        {question}

        Use the available web search tool.

        Identify useful and relevant information.
        Include source information where available.
        """,

        expected_output=(
            "A structured summary of relevant web research "
            "with source information."
        ),

        agent=web_agent
    )

    # ---------------------------------------------------------
    # Document Analysis Task
    # ---------------------------------------------------------

    document_task = Task(
        description=f"""
        Analyze the uploaded research document for information
        relevant to this question:

        {question}

        Use the Research Document Search tool to retrieve
        relevant sections from the uploaded document.

        Identify important findings, evidence, methods,
        and conclusions relevant to the question.

        Do not invent information that is not supported
        by the uploaded document.
        """,

        expected_output=(
            "A structured analysis of relevant research-document "
            "evidence."
        ),

        agent=document_agent
    )

    # ---------------------------------------------------------
    # Report Task
    # ---------------------------------------------------------

    report_task = Task(
        description=f"""
        Prepare a final research response for:

        {question}

        Synthesize the findings from:

        1. Research analysis
        2. Web research
        3. Uploaded document analysis

        Produce a clear, factual, well-structured answer.

        Do not invent information.
        """,

        expected_output=(
            "A clear and structured final research response "
            "based on the findings provided by the other agents."
        ),

        agent=report_agent
    )

    # ---------------------------------------------------------
    # Crew
    # ---------------------------------------------------------

    crew = Crew(
        agents=[
            research_agent,
            web_agent,
            document_agent,
            report_agent
        ],

        tasks=[
            research_task,
            web_task,
            document_task,
            report_task
        ],

        process=Process.sequential,

        verbose=True
    )

    return crew