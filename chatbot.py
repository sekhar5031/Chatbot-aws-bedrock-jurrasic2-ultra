import streamlit as st
import boto3
import json

with st.sidebar:
    aws_access_key_id = st.text_input("AWS Access Key Id", placeholder="access key", type="password")
    aws_secret_access_key = st.text_input("AWS Secret Access Key", placeholder="secret", type="password")

boto_session = boto3.session.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key)

st.title("CloudCast Nepal- Chatbot")
st.caption("🚀 A streamlit chatbot powered by AWS Bedrock Jurrasicv2-ultra LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if customer_input := st.chat_input():

    if not aws_access_key_id and not aws_secret_access_key:
        st.info("Access Key Id or Secret Access Key are not provided yet!")
        st.stop()

    client = boto_session.client(
        service_name='bedrock-runtime',
        region_name="us-east-1"
    )
    st.session_state.messages.append({"role": "user", "content": customer_input})
    st.chat_message("user").write(customer_input)
    prompt = f"\n\nHuman:{customer_input}\n\nAssistant:"
    body = json.dumps({
        "prompt": prompt,
        "maxTokens": 400,
        "temperature": 0.9
    })
    response = client.invoke_model(
        body=body,
        modelId="ai21.j2-ultra-v1",
        accept='application/json',
        contentType='application/json'
    )
    response_json = json.loads(response.get('body').read())
    st.write("Response from AWS Bedrock model:")
    #st.write(response_json)

    # Check if the response contains completions
    if 'completions' in response_json and isinstance(response_json['completions'], list):
        # Iterate through each completion and extract the generated text
        for completion in response_json['completions']:
            if 'data' in completion and 'text' in completion['data']:
                generated_text = completion['data']['text']
                st.session_state.messages.append({"role": "assistant", "content": generated_text.strip()})
                st.chat_message("assistant").write(generated_text.strip())
            else:
                st.error("Failed to retrieve a valid response from AWS Bedrock model.")
    else:
        st.error("Failed to retrieve a valid response from AWS Bedrock model.")
