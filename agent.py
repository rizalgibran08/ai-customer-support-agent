from langchain_google_genai import ChatGoogleGenerativeAI
import re
from tools import cek_order, create_ticket
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY") or st.secrets["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=google_api_key,
    temperature=0.3
)


def call_llm(prompt):
    full_prompt = f"""
    Kamu adalah customer support yang ramah dan membantu.
    Jawab dengan bahasa Indonesia yang jelas.

    Pertanyaan: {prompt}
    Jawaban:
    """

    response = llm.invoke(full_prompt)
    return response.content.strip()


def extract_order_id(text):
    match = re.search(r"\b\d{3}\b", text)
    return match.group() if match else None


def agent_response(user_input):
    order_id = extract_order_id(user_input)

    # 🔢 CASE: hanya angka
    if user_input.strip().isdigit():
        return "Mohon sertakan konteks, misalnya: 'cek pesanan 123'"

    # 🔎 cek order
    if "status" in user_input or "pesanan" in user_input:
        if order_id:
            return f"Saya akan mengecek pesanan Anda...\n\n{cek_order(order_id)}"
        else:
            return "Mohon berikan nomor order Anda."

    # 🧾 komplain
    elif "komplain" in user_input or "masalah" in user_input:
        return f"Saya akan membuat tiket...\n\n{create_ticket(user_input)}"

    # 🤖 fallback ke AI
    else:
        return call_llm(user_input)
