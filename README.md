# Chatbot-aws-bedrock-jurrasic2-ultra
 The above program is a Streamlit-based chatbot powered by the AWS Bedrock Jurrasic2-ultra LLM (Language Model). Here's a short description of how it works:

User Interaction: Users can interact with the chatbot by typing their queries into the chat input box.

AWS Authentication: Users need to provide their AWS Access Key Id and Secret Access Key via the Streamlit sidebar for authentication with the AWS services.

Chatbot Response: Upon receiving a user query, the program sends a request to the AWS Bedrock model, providing the user's query as input.

Processing Response: The program receives a response from the AWS Bedrock model, which includes completions containing generated text and associated information like tokens, log probabilities, and text ranges.

Displaying Response: The generated text from the response is extracted and displayed in the chat interface as the assistant's reply. Only the exact reply is displayed, and the JSON response is not shown to the user.

Error Handling: If there are any issues with retrieving a valid response from the AWS Bedrock model, an error message is displayed to the user.
