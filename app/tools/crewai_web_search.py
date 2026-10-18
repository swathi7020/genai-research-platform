import os

from dotenv import load_dotenv
from crewai.tools import BaseTool
from tavily import TavilyClient


load_dotenv()


class TavilySearchTool(BaseTool):

    name: str = "Tavily Web Search"

    description: str = (
        "Search the web for relevant and recent information. "
        "Use this tool when current web information or "
        "external sources are needed."
    )

    def _run(
        self,
        query: str
    ) -> str:

        api_key = os.getenv("TAVILY_API_KEY")

        if not api_key:
            raise ValueError(
                "TAVILY_API_KEY is not set in the .env file."
            )

        client = TavilyClient(
            api_key=api_key
        )

        response = client.search(
            query=query,
            max_results=5,
            search_depth="advanced"
        )

        results = response.get(
            "results",
            []
        )

        if not results:
            return "No web search results were found."

        formatted_results = []

        for result in results:

            formatted_results.append(
                f"""
Title: {result.get("title", "")}

URL: {result.get("url", "")}

Content:
{result.get("content", "")}
"""
            )

        return "\n".join(
            formatted_results
        )