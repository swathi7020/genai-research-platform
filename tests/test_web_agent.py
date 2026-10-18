import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


from app.agents.web_agent import create_web_research_agent


def main():

    agent = create_web_research_agent()

    print("\n" + "=" * 60)
    print("CREWAI WEB RESEARCH AGENT CREATED")
    print("=" * 60)

    print(f"\nRole: {agent.role}")

    print(f"\nGoal: {agent.goal}")

    print(f"\nBackstory: {agent.backstory}")

    print("\n" + "=" * 60)
    print("WEB RESEARCH AGENT TEST SUCCESSFUL")
    print("=" * 60)


if __name__ == "__main__":
    main()