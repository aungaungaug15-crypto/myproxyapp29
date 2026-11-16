import gradio as gr

def check_status():
    return "Server is successfully running on Render!"

demo = gr.Interface(
    fn=check_status,
    inputs=[],
    outputs="text",
    title="Proxy Status"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=10000)
  
