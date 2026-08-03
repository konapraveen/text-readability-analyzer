import gradio as gr
import textstat
import os

def analyze_readability(text):
    if not text.strip():
        return "⚠️ Please enter some text to analyze."
    
    score = textstat.flesch_reading_ease(text)
    
    if score >= 60:
        category = "✅ Easy"
    elif score >= 30:
        category = "🟡 Moderate"
    else:
        category = "🔴 Difficult"
    
    result = f"📊 Flesch Reading Ease Score: {score:.2f}\n📖 Readability Category: {category}"
    return result

custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

body, .gradio-container {
    background: linear-gradient(135deg, #1B1035 0%, #3B2E7A 50%, #6C63FF 100%) !important;
    font-family: 'Poppins', sans-serif !important;
    min-height: 100vh;
}

.gr-block.gr-box, .block {
    background: rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(12px);
    border-radius: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

h1 {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    text-align: center;
}

.prose {
    color: #E5E1FF !important;
    text-align: center;
}

textarea, input {
    background: rgba(255, 255, 255, 0.1) !important;
    color: #FFFFFF !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
}

button {
    border-radius: 14px !important;
    font-weight: 600 !important;
    transition: transform 0.15s ease !important;
}

button:hover {
    transform: scale(1.03);
}

#component-0 {
    max-width: 700px !important;
    margin: auto !important;
}
"""

demo = gr.Interface(
    fn=analyze_readability,
    inputs=gr.Textbox(lines=8, label="✏️ Paste your essay or text here", placeholder="Start typing or paste your text..."),
    outputs=gr.Textbox(label="📊 Readability Result"),
    title="📖 Text Readability Score Analyzer",
    description="Evaluates readability ease and reading level of text using the Flesch Reading Ease formula.",
    theme=gr.themes.Soft(primary_hue="violet", secondary_hue="purple"),
    css=custom_css,
    examples=[
        ["I like to play with my dog. My dog is brown and small. We run in the park every day."],
        ["Climate change refers to long-term shifts in temperatures and weather patterns."],
    ],
)

demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
