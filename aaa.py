import streamlit as st
import requests

# Function to fetch user's IP address
def fetch_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json()['ip']
        return ip
    except Exception as e:
        st.error(f"Error fetching IP address: {e}")
        return None

# Streamlit dashboard content
st.title("Streamlit IP Collection Dashboard")

# Fetch the user's IP address automatically
user_ip = fetch_ip_address()

if user_ip:
    # Display the fetched IP address
    st.write(f"**Your IP Address:** {user_ip}")
else:
    st.error("Unable to fetch the IP address.")

# Additional deployment instructions (optional for online deployment)
st.subheader("Deploying Streamlit App on Streamlit Cloud (Optional)")
st.write("""
1. Create a free account on [Streamlit Cloud](https://streamlit.io/cloud).
2. Connect your GitHub repository.
3. Deploy the app, and you’ll get a public URL to share with others!
""")
