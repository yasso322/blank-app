import streamlit as st
import random
import json
import os

# 1. Config
st.set_page_config(page_title="Chkoun L-Khrouf? PRO", page_icon="🐑", layout="centered")

# 2. Advanced CSS (The 1000-line Quality Look)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@400;700;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');

    .stApp {
        background: linear-gradient(-45deg, #050505, #12122b, #1a1a3a, #050505);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }

    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 30px;
        padding: 40px;
        margin: 20px 0;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }

    .game-title {
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(to right, #ffd700, #fff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #ffd700 0%, #ff8c00 100%) !important;
        color: #000 !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 18px !important;
        font-weight: 900 !important;
        font-size: 1.3rem !important;
        transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 10px 20px rgba(255, 215, 0, 0.2) !important;
    }
    .stButton > button:hover { transform: scale(1.05) !important; box-shadow: 0 15px 30px rgba(255, 215, 0, 0.4) !important; }

    .word-reveal {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid #ffd700;
        border-radius: 25px;
        padding: 50px;
        text-align: center;
        margin: 20px 0;
    }
    .imposter-alert { color: #ff4b4b; font-size: 3rem; font-weight: 900; }
    .normal-word { color: #ffd700; font-size: 4rem; font-weight: 900; text-shadow: 0 0 30px #ffd700; }
</style>
""", unsafe_allow_html=True)

# 3. Game Logic
WORDS_LIST = ["الطاجين", "الكسكس", "البراد", "البحر", "جامع الفنا", "المسمن", "الحريرة", "القهوة", "الصحراء", "القفطان"]
DATA_FILE = "game_data_pro_v2.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f: return json.load(f)
        except: pass
    return {"players": [], "game_state": "waiting", "imposter": None, "secret_word": "", "revealed": [], "host": None}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f: json.dump(data, f, ensure_ascii=False)

data = load_data()

# 4. App Flow
st.markdown('<div class="game-title">LAMPOSTER PRO</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:rgba(255,255,255,0.5);">PREMIUM VIP EXPERIENCE</p>', unsafe_allow_html=True)

if 'player_name' not in st.session_state:
    st.session_state.player_name = ""
    st.session_state.is_host = False

# --- STEP 1: JOINING ---
if not st.session_state.player_name:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    name = st.text_input("دخل سميتك يا بطل:", placeholder="Yassine, Adam...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👑 أنا الـ Host"):
            if name.strip():
                if not data["host"]: # Check if host already exists
                    data["host"] = name.strip()
                    if name.strip() not in data["players"]: data["players"].append(name.strip())
                    save_data(data)
                    st.session_state.player_name = name.strip()
                    st.session_state.is_host = True
                    st.rerun()
                else: st.error("كاين هوست ديجا!")
    with col2:
        if st.button("🎮 انضمام اللاعب"):
            if name.strip():
                if name.strip() not in data["players"]:
                    data["players"].append(name.strip())
                    save_data(data)
                st.session_state.player_name = name.strip()
                st.session_state.is_host = False
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- STEP 2: LOBBY ---
    st.markdown(f'<p style="text-align:center;">👤 أنت: <b>{st.session_state.player_name}</b> ({"Host 👑" if st.session_state.is_host else "Player 🎮"})</p>', unsafe_allow_html=True)
    
    # Players list
    p_tags = "".join([f'<span style="background:rgba(255,215,0,0.1); color:#ffd700; padding:5px 15px; border-radius:20px; margin:5px; display:inline-block; border:1px solid #ffd700;">{p}</span>' for p in data["players"]])
    st.markdown(f'<div class="glass-card" style="text-align:center;"><h4>👥 داخلين دابا:</h4>{p_tags}</div>', unsafe_allow_html=True)

    # Host controls (Only visible to host)
    if st.session_state.is_host:
        st.markdown('<div class="glass-card" style="border: 1px solid #ffd700;">', unsafe_allow_html=True)
        st.markdown('<p style="text-align:center; color:#ffd700; font-weight:bold;">تحكمات الـ Host</p>', unsafe_allow_html=True)
        if st.button("🚀 بدأ الجيم وتوزيع الأدوار"):
            if len(data["players"]) >= 2:
                data["imposter"] = random.choice(data["players"])
                data["secret_word"] = random.choice(WORDS_LIST)
                data["game_state"] = "playing"
                data["revealed"] = []
                save_data(data)
                st.rerun()
            else: st.warning("خاص على الأقل 2 لعابة")
            
        if st.button("🔄 Reset Game"):
            save_data({"players": [], "game_state": "waiting", "imposter": None, "secret_word": "", "revealed": [], "host": None})
            st.session_state.player_name = ""
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # --- STEP 3: PLAYING ---
    if data["game_state"] == "playing":
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        if st.session_state.player_name not in data["revealed"]:
            if st.button("👁️ كشف الكلمة / الدور ديالي"):
                data["revealed"].append(st.session_state.player_name)
                save_data(data)
                st.rerun()
        else:
            st.markdown('<div class="word-reveal">', unsafe_allow_html=True)
            if st.session_state.player_name == data["imposter"]:
                st.markdown('<p class="imposter-alert">🕵️ أنت هو الخروف!</p>', unsafe_allow_html=True)
                st.markdown('<p style="color:white;">ماكاينش الكلمة.. حاول تعيق بيهم!</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="color:white; font-size:1.2rem;">الكلمة هي:</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="normal-word">{data["secret_word"]}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Update Button for everyone
    if st.button("🔄 Update"): st.rerun()

    # Reveal final result (Host only)
    if st.session_state.is_host and data["game_state"] == "playing":
        if st.button("🏁 كشف شكون الخروف للجميع"):
            st.error(f"🐑 الخروف كان هو: {data['imposter']}")

st.markdown('<div style="text-align:center; margin-top:50px; opacity:0.3;">💎 VIP LAMPOSTER | MADE FOR DRARI</div>', unsafe_allow_html=True)
