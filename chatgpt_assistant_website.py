import openai
import gradio

openai.api_key = "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"

# messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]
messages = [{"role": "system", "content": "i am a student"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Demo Chat Bot")

demo.launch(share=True)