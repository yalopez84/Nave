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

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "Que es la nave?",
        },
    ],
    extra_body={
        "dataSources": [
            {
                "type": "AzureCognitiveSearch",
                "parameters": {
                    "endpoint": search_endpoint,
                    "key": search_key,
                    "indexName": search_index_name
                }
            }
        ]
    }
)
print(completion.model_dump_json(indent=2))
