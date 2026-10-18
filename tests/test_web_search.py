from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


from app.tools.web_search import WebSearchTool


def main():

    print("\n" + "=" * 60)
    print("TESTING TAVILY WEB SEARCH")
    print("=" * 60)

    web_search = WebSearchTool()

    query = "latest developments in multimodal machine learning"

    print(f"\nQuery: {query}")

    results = web_search.search(
        query=query,
        max_results=3
    )

    print("\n" + "=" * 60)
    print("SEARCH RESULTS")
    print("=" * 60)

    for i, result in enumerate(results, start=1):

        print(f"\nRESULT {i}")
        print("-" * 50)

        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Score: {result['score']}")

        print("\nContent:")
        print(result["content"][:500])


if __name__ == "__main__":
    main()