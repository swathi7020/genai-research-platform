import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


from app.tools.crewai_web_search import TavilySearchTool


def main():

    print("\n" + "=" * 60)
    print("TESTING CREWAI TAVILY TOOL")
    print("=" * 60)

    tool = TavilySearchTool()

    print(f"\nTool name: {tool.name}")

    print(f"\nTool description:")
    print(tool.description)

    print("\nRunning web search...")

    result = tool.run(
        "latest developments in multimodal machine learning"
    )

    print("\n" + "=" * 60)
    print("SEARCH RESULTS")
    print("=" * 60)

    print(result[:3000])

    print("\n" + "=" * 60)
    print("CREWAI TAVILY TOOL TEST SUCCESSFUL")
    print("=" * 60)


if __name__ == "__main__":
    main()