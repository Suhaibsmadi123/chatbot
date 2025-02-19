from together import Together

# Set your API key here
api_key = '1f8c45937bc1c7506521aed43107e049887f888ff61c4388bd4a9876805827d1'


client = Together(
    api_key=api_key
)  # Use your API key in the client initialization


def chat_with_together(prompt):
    response = client.chat.completions.create(
        model='meta-llama/Llama-3.3-70B-Instruct-Turbo',  # Model specified
        messages=[{'role': 'user', 'content': prompt}],
    )
    return response.choices[0].message.content
if __name__ == '__main__':
    print(
        "Chatbot: Hello! I am here to chat. Type 'exit', 'quit', or 'bye' to end."
    )

    while True:
        user_input = input('You: ')

        if user_input.lower() in ['quit', 'exit', 'bye']:
            print('Chatbot: Goodbye! take care!')
            break

        response = chat_with_together(user_input)
        print(f'Chatbot: {response}')
        print ()



