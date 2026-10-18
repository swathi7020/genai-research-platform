import requests
import streamlit as st


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

API_URL = "http://127.0.0.1:8000"


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="GenAI Research Intelligence",
    page_icon="🔬",
    layout="wide"
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title(
    "🔬 GenAI Research Intelligence Platform"
)

st.markdown(
    """
    Upload a research paper and ask questions using:

    **RAG + FAISS + Tavily + CrewAI + LLM**
    """
)


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.header("⚙️ Research Settings")

    st.markdown(
        """
        ### AI Components

        🧠 CrewAI Agents

        📚 RAG / FAISS

        🌐 Tavily Web Search

        🤖 LLM

        ⚡ FastAPI
        """
    )

    st.markdown("---")

    st.info(
        "Upload a PDF to start your research."
    )


# ---------------------------------------------------------
# PDF Upload
# ---------------------------------------------------------

st.subheader("📄 Upload Research Document")

uploaded_file = st.file_uploader(
    "Choose a research paper",
    type=["pdf"],
    help="Upload a PDF research paper for analysis."
)


if uploaded_file:

    st.success(
        f"Document ready: {uploaded_file.name}"
    )


# ---------------------------------------------------------
# Question
# ---------------------------------------------------------

st.subheader(
    "🔎 Ask a Research Question"
)

question = st.text_area(
    "Research Question",

    placeholder=(
        "Example: What are the major findings "
        "of this research paper?"
    ),

    height=120
)


# ---------------------------------------------------------
# Research button
# ---------------------------------------------------------

if st.button(
    "🔎 Start Multi-Agent Research",
    type="primary"
):

    if uploaded_file is None:

        st.warning(
            "Please upload a PDF research paper first."
        )

    elif not question.strip():

        st.warning(
            "Please enter a research question."
        )

    else:

        with st.spinner(
            "Research agents are analyzing your document..."
        ):

            try:

                response = requests.post(

                    f"{API_URL}/research/upload-and-ask",

                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            "application/pdf"
                        )
                    },

                    data={
                        "question": question
                    },

                    timeout=600
                )


                # ------------------------------------------------
                # API error
                # ------------------------------------------------

                if response.status_code != 200:

                    st.error(
                        f"API Error: {response.status_code}"
                    )

                    st.code(
                        response.text
                    )


                else:

                    result = response.json()


                    # ------------------------------------------------
                    # Success
                    # ------------------------------------------------

                    st.success(
                        "Research completed successfully."
                    )


                    st.subheader(
                        "🤖 Research Answer"
                    )

                    st.markdown(
                        result.get(
                            "answer",
                            "No answer returned."
                        )
                    )


                    # ------------------------------------------------
                    # Document information
                    # ------------------------------------------------

                    st.subheader(
                        "📄 Analyzed Document"
                    )

                    st.info(
                        result.get(
                            "filename",
                            uploaded_file.name
                        )
                    )


                    # ------------------------------------------------
                    # Question
                    # ------------------------------------------------

                    with st.expander(
                        "🔎 Research Question"
                    ):

                        st.write(
                            result.get(
                                "question",
                                question
                            )
                        )


            except requests.exceptions.ConnectionError:

                st.error(
                    "Could not connect to FastAPI. "
                    "Make sure the FastAPI server is running."
                )


            except requests.exceptions.Timeout:

                st.error(
                    "The research request took too long. "
                    "Please try again."
                )


            except Exception as e:

                st.error(
                    f"Unexpected error: {str(e)}"
                )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown("---")

st.caption(
    "GenAI Research Intelligence Platform | "
    "RAG • FAISS • Tavily • CrewAI • FastAPI"
)