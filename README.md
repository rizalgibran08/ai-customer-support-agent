# Simple Customer Support AI Agent

AI-powered customer support agent that can:
- Answer general questions using LLM
- Check order status
- Handle customer complaints automatically

Built using LangChain + Gemini API + Streamlit

## 🎯 Use Case
- E-commerce customer support automation
- AI-powered helpdesk
- Chatbot with tool integration

## 🚀 Demo
![App Screenshot](assets/demo.png)

## ✨ Features
- Check order status using order ID
- Create complaint tickets automatically
- AI-powered responses for general questions
- Hybrid system (rule-based + LLM)
- Fast and interactive UI with Streamlit

## 🧠 How It Works
The system uses a hybrid AI agent approach:
1. User input is analyzed
2. If it matches a specific intent:
   - Order → call order checking tool
   - Complaint → create ticket
3. Otherwise:
   - Forward to LLM (Gemini API)

Flow:
User → Agent → Decision → Tool / LLM → Response

## 🛠️ Tech Stack
- Python
- LangChain
- Google Gemini API
- Streamlit

  ## ⚙️ Installation
```bash
git clone https://github.com/username/project-name
cd project-name
pip install -r requirements.txt

## 🔑 Environment Variables

Create a `.env` file:
GOOGLE_API_KEY=your_api_key_here

## ▶️ Run the App
```bash
streamlit run app.py
