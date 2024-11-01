import streamlit as st
import base64

# Set page background
def set_background(png_file):
    with open(png_file, "rb") as file:
        bg_image = file.read()
    bg_image_encoded = base64.b64encode(bg_image).decode()
    background_style = f"""
    <style>
        .stApp {{
        background-image: url("data:image/png;base64,{bg_image_encoded}");
        background-size: cover;
        background-position: center;
        font-family: 'Georgia', serif;
    }}
    .center-title {{
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 36px;
        font-weight: bold;
        color: #2C3E50;
        margin-top: 10px;
        gap: 10px;
    }}
    .center-title img {{
        width: 80px;  /* Adjust logo size */
        height: 80px;
    
    }}
    h1, h2, h3, h4 {{
        color: #2C3E50;
        text-align: left;
    }}
    .card {{
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    }}
    .section-title {{
        font-size: 22px;
        font-weight: bold;
        color: #FF5733;
        margin-bottom: 10px;
    }}
    .section-content {{
        font-size: 16px;
        color: #2C3E50;
        line-height: 1.6;
    }}
    .center-title {{
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: navyblue;
        margin-top: 10px;
    }}
    .center-subtitle {{
        text-align: center;
        font-size: 18px;
        color: #2C3E50;
        margin-top: -15px;
        margin-bottom: 20px;
    }}
    .nav-bar {{
    background-color: rgba(255, 255, 255, 0.8);
    padding: 10px 20px;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    gap: 30px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }}
    .nav-item {{
        font-size: 16px;
        font-weight: bold;
        color: #2C3E50;
        cursor: pointer;
    }}
    .nav-item-selected {{
        color: #FF5733;
        border-bottom: 2px solid #FF5733;
    }}
            .stRadio > div {{
            display: flex;
            justify-content: center;
            gap: 20px;
            font-size: 16px;
            font-weight: bold;
            color: #2C3E50;
        }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Set background image
set_background("brics-webpage.png")  # Adjust with the correct file path if needed

# Centered Title and Subtitle
st.markdown("""
<div class="center-title">
    <img src="data:image/png;base64,{}" alt="BRICS Logo">
    BRICS Coin
</div>
""".format(base64.b64encode(open("BRICS.png", "rb").read()).decode()), unsafe_allow_html=True)

# Navigation Buttons
selected_section = st.radio("", ["About BRICS", "Tokenomics", "Roadmap"], horizontal=True)

# Apply style based on the selected section
nav_items = {
    "About BRICS": "nav-item-selected" if selected_section == "About BRICS" else "nav-item",
    "Tokenomics": "nav-item-selected" if selected_section == "Tokenomics" else "nav-item",
    "Roadmap": "nav-item-selected" if selected_section == "Roadmap" else "nav-item"
}

# Custom HTML for the Navigation Bar
st.markdown(f"""
<div class="nav-bar">
    <span class="{nav_items['About BRICS']}">About BRICS</span>
    <span class="{nav_items['Tokenomics']}">Tokenomics</span>
    <span class="{nav_items['Roadmap']}">Roadmap</span>
</div>
""", unsafe_allow_html=True)

# Display the selected section in a card
if selected_section == "About BRICS":
    st.markdown("""
    <div class="card">
        <div class="section-title">About BRICS</div>
        <div class="section-content">
            Ever wanted to own a piece of five entire economies? Well, now you can... kind of. BRICS is your ticket to ride the waves of digital finance, backed by a community of fellow dreamers, schemers, and, let’s face it, memers. With BRICS, you're not just holding a coin; you're holding onto hope, hilarity, and the possibility of "to the moon!" moments.
            So come aboard, grab a BRICS or a billion, and let’s show the world that emerging markets and meme coins are the combo we never knew we needed. Because, after all, if it’s got BRICS in the name, it’s gotta be solid, right?
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected_section == "Tokenomics":
    st.markdown(f"""
    <div class="card">
        <div class="section-title">BRICS Coin Tokenomics</div>
        <div class="section-content">
            <strong>Total Initial Supply</strong>: 786,000,000 BRICS Coins<br><br>
            <strong>Burned Supply</strong>:<br>
            - 90% Burned: 707,400,000 BRICS Coins permanently removed from circulation.<br>
            - Remaining Circulating Supply: 78,600,000 BRICS Coins.<br><br>
            <strong>Founder’s Allocation</strong>:<br>
            - 10% of Circulating Supply: 7,860,000 BRICS Coins reserved for the founder.<br><br>
            <strong>Transaction Fees</strong>:<br>
            - 2% Burn: Further reducing the circulating supply over time.<br>
            - 2% Redistribution: Rewarding existing holders.<br>
            - 1% Liquidity Pool: Added to the liquidity pool to help stabilize the price.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected_section == "Roadmap":
    st.markdown(f"""
    <div class="card">
        <div class="section-title">BRICS Coin Roadmap</div>
        <div class="section-content">
            <strong>Phase 1: Concept & Community Building</strong><br>
            - Research & Development, Social Media Launch, Website Launch, Initial Airdrop.<br><br>
            <strong>Phase 2: Token Launch & Liquidity Setup</strong><br>
            - Token Creation, Listing on DEX, Establish Liquidity Pool, Community Incentives.<br><br>
            <strong>Phase 3: Marketing & Partnerships</strong><br>
            - Community Contests & Giveaways, Influencer Partnerships, Educational Content, Partnerships.<br><br>
            <strong>Phase 4: Utility Expansion</strong><br>
            - Exclusive Access & Rewards, NFT Integration, Voting & Governance, Charity Initiatives.<br><br>
            <strong>Phase 5: Global Expansion & Sustainability</strong><br>
            - Cross-Chain Expansion, Partnerships with Emerging Markets, Exchange Listings, Sustainability Initiatives.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<div style="
    background-color: rgba(255, 255, 255, 0.8); 
    padding: 15px; 
    border-radius: 10px; 
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); 
    max-width: 300px;
    margin: 20px auto;
    text-align: center;
">
    <h3 style="color: #2C3E50; margin-top: 0;">Join the Community</h3>
    <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 10px;">
        <img src="https://img.icons8.com/color/48/000000/twitter.png" width="24"/>
        <a href="https://x.com/BRICS_Coins" target="_blank" style="color: #1DA1F2; text-decoration: none; font-weight: bold;">Follow us on Twitter</a>
    </div>
    <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 10px;">
        <img src="https://img.icons8.com/color/48/000000/telegram-app.png" width="24"/>
        <a href="https://t.me/+B3yvPHQ9N0hjMmRl" target="_blank" style="color: #0088cc; text-decoration: none; font-weight: bold;">Join our Telegram</a>
    </div>
</div>
""", unsafe_allow_html=True)
