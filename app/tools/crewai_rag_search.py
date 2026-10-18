from crewai.tools import BaseTool

from app.rag.pipeline import RAGPipeline


class RAGSearchTool(BaseTool):

    name: str = "Research Document Search"

    description: str = (
        "Search the uploaded research document for information "
        "relevant to a research question. Use this tool when "
        "you need evidence from the provided research paper."
    )

    rag_pipeline: RAGPipeline

    def _run(
        self,
        query: str
    ) -> str:

        if not query or not query.strip():
            return "Search query cannot be empty."

        results = self.rag_pipeline.retrieve(
            query=query,
            top_k=5
        )

        if not results:
            return (
                "No relevant information was found "
                "in the research document."
            )

        formatted_results = []

        for i, result in enumerate(
            results,
            start=1
        ):

            formatted_results.append(
                f"""
DOCUMENT RESULT {i}

Similarity Distance:
{result["distance"]}

Content:
{result["document"]}
"""
            )

        return "\n".join(
            formatted_results
        )