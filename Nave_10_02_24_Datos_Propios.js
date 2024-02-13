const { OpenAIClient,AzureKeyCredential } = require("@azure/openai");

const endpoint = "https://lanave-assistant-ia-service.openai.azure.com/";
const azureApiKey = "f93d8e26153543d18b2e1124ade3d01d";
const searchEndpoint = "https://lanaveassistantsearch.search.windows.net";
const searchKey = "gCXGhPxaufktNMDObsMReXknUhZTu5mpDQP1VZnDdvAzSeBOR61v";
const searchIndex = "lanave-assistant-index-dev"
const deploymentId = "gpt-4"

async function main(){
    const client = new OpenAIClient(endpoint, new AzureKeyCredential(azureApiKey));
    const messages = [
        { role: "user", content: "que es la nave?" },
    ];

    console.log(`User: ${messages.map((m) => m.content).join("\n")}`);

    const events = await client.streamChatCompletions(deploymentId, messages, {   
    azureExtensionOptions: {
      extensions: [
        {
          type: "AzureCognitiveSearch",
          endpoint: searchEndpoint,
          key: searchKey,
          indexName: searchIndex,
          inScope: false,
          roleInformation: "You are an AI assistant that helps people find information.",
          filter: undefined,
          strictness: 4,
          topNDocuments: 5,          
        },
      ],
    },
    temperature:0,
    top_p:1,
    max_tokens:800, 
    stop: undefined,  
  });
  let cadena=''
  for await (const event of events) {
    for (const choice of event.choices) {
      const delta = choice.delta?.content;
      if (delta !== undefined) {
        cadena += delta
      }
    }
  }
  console.log(`Chatbot: ${cadena}`)
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});