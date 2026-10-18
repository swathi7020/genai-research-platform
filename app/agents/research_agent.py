from crewai import Agent


def create_research_agent():

    research_agent = Agent(
        role="Research Analyst",

        goal=(
            "Analyze research questions and identify "
            "important findings from reliable research information."
        ),

        backstory=(
            "You are an experienced research analyst specializing "
            "in scientific and technical research. "
            "You carefully examine available evidence, "
            "identify important findings, and avoid inventing information."
        ),

        verbose=True,

        allow_delegation=False
    )

    return research_agent