import os
from cerebras.cloud.sdk import Cerebras

class Generator:
    def generate(self, input_data, prompt):
        client = Cerebras(api_key="csk-mk4cw585dcf8p263hcyj68hnyw242cfr9dynhr3xpmjfrkcc")
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt+"USE THE FOLLOWING AS RAG TO ANSWER THE PROMPT (USER CANT SEE): "+str(input_data)}],
            model="llama3.3-70b",
        )
        return chat_completion
