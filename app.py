import gradio as gr
import textstat
import os

def analyze_readability(text):
    if not text.strip():
        return "Please enter some text."
    
    score = textstat.flesch_reading_ease(text)
    
    if score >= 60:
        category = "Easy"
    elif score >= 30:
        category = "Moderate"
    else:
        category = "Difficult"
    
    result = f"Flesch Reading Ease Score: {score:.2f}\nReadability Category: {category}"
    return result

demo = gr.Interface(
    fn=analyze_readability,
    inputs=gr.Textbox(lines=8, label="✏️ Paste your essay/text here"),
    outputs=gr.Textbox(label="📊 Readability Result"),
    title="📖 Text Readability Score Analyzer",
    description="Evaluates readability ease and reading level of text using textstat.",
    theme=gr.themes.Soft()
)

demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
