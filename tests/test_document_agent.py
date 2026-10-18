import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


from app.agents.document_agent import create_document_analyst_agent


def main():

    agent = create_document_analyst_agent()

    print("\n" + "=" * 60)
    print("CREWAI DOCUMENT ANALYST CREATED")
    print("=" * 60)

    print(f"\nRole: {agent.role}")

    print(f"\nGoal: {agent.goal}")

    print(f"\nBackstory: {agent.backstory}")

    print("\n" + "=" * 60)
    print("DOCUMENT ANALYST TEST SUCCESSFUL")
    print("=" * 60)


if __name__ == "__main__":
    main()