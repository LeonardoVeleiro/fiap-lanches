import streamlit as st


def aplicar_estilo():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
        color: white;
    }

    h1, h2, h3 {
        color: #ED145B;
    }

    [data-testid="stSidebar"] {
        background-color: #111111;
        border-right: 1px solid #ED145B;
    }

    .stButton > button {
        background-color: #ED145B;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1rem;
        font-weight: bold;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background-color: #ff3d7f;
        color: white;
        transform: scale(1.03);
    }

    .card {
        background-color: #1f1f1f;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #333;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    }

    .card-title {
        color: #ED145B;
        font-size: 22px;
        font-weight: bold;
    }

    .price {
        color: #ffffff;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)