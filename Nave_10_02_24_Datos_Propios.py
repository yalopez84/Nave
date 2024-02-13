from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
azureOpenAI_endpoint = os.environ.get("AZUREOPENAI_ENDPOINT")
azureOpenAI_key = os.environ.get("AZUREOPENAI_KEY")
deployment_name = os.environ.get("DEPLOYMENT_NAME")
azureOpenAI_version = os.environ.get("AZUREOPENAI_VERSION")
search_endpoint = os.environ.get("SEARCH_ENDPOINT")
search_key = os.environ.get("SEARCH_KEY")
search_index_name = os.environ.get("SEARCH_INDEX_NAME")

client = AzureOpenAI(
    base_url=f'{azureOpenAI_endpoint}/openai/deployments/{deployment_name}/extensions',
    api_key=azureOpenAI_key,
    api_version= azureOpenAI_version,
)
question= 'que es la universidad de la habana?'
print(f"User: {question}")
completion = client.chat.completions.create(model= deployment_name, messages= [
    {
        "role": "user","content": question
        }
        ], extra_body={
            "dataSources": [
                {
                    "type": "AzureCognitiveSearch",
                    "parameters": {
                        "endpoint": search_endpoint,
                        "key": search_key,
                        "indexName": search_index_name,
                        "inScope": False,
                        "roleInformation": 'You are an AI assistant that helps people find information.',
                        "filter": None,
                        "strictness": 4,
                        "topNDocuments": 5,
                        }
                    }
                ], 
            "temperature":0,
            "top_p":1,
            "max_tokens":800, 
            "stop": None 
            })
# print(completion.model_dump_json(indent=2)) #json del response
print(f'Chatbot: {completion.choices[0].message.content}')