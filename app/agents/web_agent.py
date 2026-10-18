from crewai import Agent

from app.tools.crewai_web_search import TavilySearchTool


def create_web_research_agent():

    web_search_tool = TavilySearchTool()

    web_agent = Agent(
        role="Web Research Analyst",

        goal=(
            "Search for and analyze relevant and recent information "
            "from reliable web sources to support research questions."
        ),

        backstory=(
            "You are an experienced web research analyst. "
            "You find relevant and recent information, evaluate "
            "available sources, and clearly separate factual "
            "information from unsupported claims."
        ),

        tools=[
            web_search_tool
        ],

        verbose=True,

        allow_delegation=False
    )

    return web_agent