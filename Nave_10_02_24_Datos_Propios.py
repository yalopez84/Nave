from openai import AzureOpenAI

azureOpenAI_endpoint = "https://lanave-assistant-ia-service.openai.azure.com/"
azureOpenAI_key = "f93d8e26153543d18b2e1124ade3d01d"
deployment_name = "gpt-4"
azureOpenAI_version = "2023-08-01-preview"
search_endpoint = "https://lanaveassistantsearch.search.windows.net"
search_key = "gCXGhPxaufktNMDObsMReXknUhZTu5mpDQP1VZnDdvAzSeBOR61v"
search_index_name = "lanave-assistant-index-dev"

client = AzureOpenAI(
    base_url=f"{azureOpenAI_endpoint}/openai/deployments/{deployment_name}/extensions",
    api_key=azureOpenAI_key,
    api_version= azureOpenAI_version,
)
question= "que es la nave?"
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
                    "roleInformation": "You are an AI assistant that helps people find information.",
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