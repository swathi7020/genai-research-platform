import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


from app.agents.crew import create_research_crew


def main():

    question = (
        "What are the major findings about "
        "social brain development during childhood?"
    )

    print("\n" + "=" * 70)
    print("STARTING MULTI-AGENT RESEARCH")
    print("=" * 70)

    print(f"\nResearch Question:\n{question}")

    crew = create_research_crew(
        question=question
    )

    print("\n" + "=" * 70)
    print("RUNNING CREW")
    print("=" * 70)

    result = crew.kickoff()

    print("\n" + "=" * 70)
    print("FINAL CREW RESULT")
    print("=" * 70)

    print("\n")
    print(result)

    print("\n" + "=" * 70)
    print("MULTI-AGENT RESEARCH COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()