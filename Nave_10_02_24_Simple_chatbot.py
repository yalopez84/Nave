from openai import AzureOpenAI 

azureOpenAI_key = "f93d8e26153543d18b2e1124ade3d01d" 
api_version = "2023-07-01-preview" 
azureOpenAI_endpoint = "https://lanave-assistant-ia-service.openai.azure.com/" 
deployment_name = "gpt-4" 
client = AzureOpenAI(api_version= api_version, azure_endpoint= azureOpenAI_endpoint, api_key= azureOpenAI_key) 
completion = client.chat.completions.create(
    model= deployment_name, 
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?"
        }
        ]
    ) 
print(completion.model_dump_json(indent=2)) 