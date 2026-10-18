import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class LLMClient:

    def __init__(self):

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is not set in the .env file."
            )

        self.client = OpenAI(
            api_key=api_key
        )

    def generate_answer(
        self,
        question: str,
        context: str
    ):

        prompt = f"""
You are a research assistant.

Answer the user's question using only the
provided research context.

If the context does not contain enough
information to answer the question, say:

"I could not find enough information in
the provided document."

Do not invent facts.

Research Context:
-----------------
{context}
-----------------

User Question:
{question}

Provide a clear and concise answer.
"""

        response = self.client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return response.output_text