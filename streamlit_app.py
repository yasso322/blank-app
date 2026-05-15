import streamlit as st
import random
import json
import os

# --- Page Config ---
st.set_page_config(page_title="Chkoun L-Khrouf? PRO", page_icon="🐑", layout="centered")

# --- Database ديال الكلمات ---
# هادو هما الكلمات اللي غيطلعو للناس العاديين
WORDS_LIST = [
    "الطاجين", "الكسكس", "البراد", "البحر", "جامع الفنا", "الدار البيضاء", 
    "المسمن", "الحريرة", "حكيم زياش", "الموطور", "القهوة", "البغرير",
    "القفطان", "البلغة", "التكشيطة", "الصحراء المغربية", "مراكش"
]

# --- CSS Design ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@400;900&display=swap');
    * { font-family: 'Noto Sans Arabic', sans-serif; text-align: right; }
    .stApp { background: #0e1117; }
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 215, 0, 0.2);
        margin-bottom: 20px;
    }
    .secret-box {
        background: linear-gradient(135deg, #ffd700 0%, #ff8c00 100%);
        color: black;
        padding: 30px;
        border-radius: 15px;
        font-size: 2.5rem;
        font-weight: 900;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(255, 215, 0, 0.3);
    }
    .imposter-box {
        background: linear-gradient(135deg, #ff4b4b 0%, #8b0000 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        font-size: 2rem;
        font-weight: 900;
        text-align: center;
        margin: 20px 0;
    }
    .name-tag {
        background: #1e2130;
        color: #ffd700;
        padding: 8px 15px;
        border-radius: 10px;
        margin: 5px;
        display: inline-block;
        border: 1px solid #ffd700;
    }
</style>
""", unsafe_allow_html=True)

# --- Data Management ---
DATA_FILE = "game_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except: pass
    return {"players": [], "game_state": "waiting", "imposter": None, "secret_word": "", "revealed": []}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# --- App Interface ---
st.markdown('<h1 style="text-align:center; color:#ffd700;">🐑 شكون الخروف؟</h1>', unsafe_allow_html=True)

data = load_data()

# Initialize session
if 'player_name' not in st.session_state:
    st.session_state.player_name = ""

# --- 1. Registration ---
if not st.session_state.player_name:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    name = st.text_input("دخل سميتك باش تبدا:", key="reg_name")
    if st.button("انضمام للعبة 🎮"):
        if name and name.strip():
            if name not in data["players"]:
                data["players"].append(name.strip())
                save_data(data)
            st.session_state.player_name = name.strip()
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # Header Info
    st.write(f"👤 أنت: **{st.session_state.player_name}**")
    
    # Display Players
    players_html = "".join([f'<span class="name-tag">{p}</span>' for p in data["players"]])
    st.markdown(f'<div class="glass-card">👥 الدراري اللي داخلين:<br>{players_html}</div>', unsafe_allow_html=True)

    # --- 2. Host Controls ---
    # أول واحد كيدخل هو اللي كيتحكم (أو تقدر تزيد Logic د الـ Host)
    if len(data["players"]) > 0 and data["players"][0] == st.session_state.player_name:
        st.markdown("### 👑 تحكم الـ Host")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🚀 توزيع الأدوار"):
                data["imposter"] = random.choice(data["players"])
                data["secret_word"] = random.choice(WORDS_LIST)
                data["game_state"] = "playing"
                data["revealed"] = []
                save_data(data)
                st.rerun()
        with col2:
            if st.button("🔄 ريستارت"):
                save_data({"players": [], "game_state": "waiting", "imposter": None, "secret_word": "", "revealed": []})
                st.session_state.player_name = ""
                st.rerun()

    # --- 3. Playing State ---
    if data["game_state"] == "playing":
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        
        # المرحلة فين كيشوف الكلمة
        if st.session_state.player_name not in data["revealed"]:
            st.warning("⚠️ يلاه، برك باش تشوف شكون أنت. رد بالك يشوفك شي واحد!")
            if st.button("👁️ كشف الدور ديالي"):
                data["revealed"].append(st.session_state.player_name)
                save_data(data)
                st.rerun()
        else:
            # هنا فين كاين اللوجيك اللي بغيتي
            if st.session_state.player_name == data["imposter"]:
                # الخروف ما كيشوف والو
                st.markdown('<div class="imposter-box">🕵️ أنت هو الخروف!<br><span style="font-size:1.2rem; font-weight:normal;">ماكاينش الكلمة، حاول تعيق بيهم بلا ما يعرفوك.</span></div>', unsafe_allow_html=True)
            else:
                # الناس العاديين كيشوفو الكلمة
                st.markdown(f'<div class="secret-box">الكلمة هي:<br>{data["secret_word"]}</div>', unsafe_allow_html=True)
                st.info("💡 هضر على هاد الكلمة بلا ما تعطيها نيشان، باش الخروف ما يفرشهاش.")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # --- 4. Refresh Button ---
    st.button("🔄 تحديث (Update)")

    if data["game_state"] == "playing":
        if st.button("🏁 كشف شكون الخروف"):
            st.error(f"🐑 الخروف اللي كان بيناتنا هو: {data['imposter']}")

st.markdown('<p style="text-align:center; color:gray; font-size:0.8rem;">Made for Drari 🐑 v2.0</p>', unsafe_allow_html=True)
