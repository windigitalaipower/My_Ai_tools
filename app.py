import streamlit as st
import google.generativeai as genai
import os

# Page Config
st.set_page_config(page_title="AI B2B Lead Generator", layout="centered")

# API Key Config (Streamlit Secrets से)
try:
    genai.configure(api_key=st.secrets["API_KEY"])
except:
    st.error("API Key नहीं मिली! कृपया Streamlit Settings -> Secrets में API_KEY सेट करें।")

st.title("🚀 AI B2B Outreach Tool")
st.subheader("क्लाइंट्स ढूँढें और सटीक ईमेल लिखें")

# Inputs
client_name = st.text_input("कंपनी का नाम (Company Name):")
industry = st.selectbox("इंडस्ट्री चुनें:", ["Rice Milling", "E-commerce", "Real Estate", "Consultancy", "Others"])
pain_point = st.text_area("क्लाइंट की समस्या या लक्ष्य (जैसे: कम एक्सपोर्ट, पुरानी वेबसाइट):")

if st.button("प्रोफेशनल ईमेल जनरेट करें"):
    if client_name and pain_point:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        एक प्रोफेशनल और प्रभावशाली कोल्ड ईमेल लिखो जो {client_name} को भेजा जाएगा।
        इंडस्ट्री: {industry}
        क्लाइंट की समस्या/लक्ष्य: {pain_point}
        
        ईमेल का लहजा प्रोफेशनल और वैल्यू-आधारित होना चाहिए। 
        उन्हें बताओ कि मैं उनकी डिजिटल ब्रांडिंग और ऑटोमेशन में कैसे मदद कर सकता हूँ।
        ईमेल छोटा रखें और अंत में एक 'Call to Action' रखें।
        """
        
        with st.spinner('AI ईमेल लिख रहा है...'):
            response = model.generate_content(prompt)
            st.success("ईमेल तैयार है:")
            st.text_area("यहाँ से कॉपी करें:", response.text, height=300)
    else:
        st.warning("कृपया सभी जानकारी भरें!")

# Footer
st.markdown("---")
st.write("WINDIGITAL Powered Tool")
