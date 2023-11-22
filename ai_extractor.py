import os

from dotenv import load_dotenv
from langchain.chains import create_extraction_chain, create_extraction_chain_pydantic
from langchain.chat_models import AzureChatOpenAI

load_dotenv("Credentials.env")

COMPLETION_TOKENS = 1000

# Set this to `azure`
os.environ["OPENAI_API_BASE"] = os.environ["AZURE_OPENAI_ENDPOINT"]
os.environ["OPENAI_API_KEY"] = os.environ["AZURE_OPENAI_API_KEY"]
os.environ["OPENAI_API_VERSION"] = "2023-07-01-preview"
os.environ["OPENAI_API_TYPE"] = "azure"
MODEL_NAME = "gpt-35-turbo"
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = AzureChatOpenAI(
    deployment_name=MODEL_NAME, temperature=0.5, max_tokens=COMPLETION_TOKENS
)


def extract(content: str, **kwargs):
    response = ""
    try:
        if "schema_pydantic" in kwargs:
            response = create_extraction_chain_pydantic(
                pydantic_schema=kwargs["schema_pydantic"], llm=llm
            ).run(content)
        else:
            response = create_extraction_chain(schema=kwargs["schema"], llm=llm).run(
                content
            )
    except Exception as e:
        print(f"Error: {e}")

    return response
