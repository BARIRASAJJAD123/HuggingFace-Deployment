import gradio as gr

def predict(text):
    return f"Hello, {text}!"

interface = gr.Interface(fn=predict, inputs="text", outputs="text")
interface.launch()
