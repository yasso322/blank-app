
import import streamlit as st
import random
import json
import os

# إعدادات الصفحة
st.set_page_config(page_title="Chkoun L-Khrouf? PRO", page_icon="🐑", layout="centered")

# [نفس الديزاين الرهيب ديالك مع إضافة لمسة للأحكام]
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@300;400;600;700;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    * { font-family: 'Noto Sans Arabic', sans-serif; }
    .stApp { background: linear-gradient(-45deg, #0a0a0a, #1a1a2e, #16213e, #0f3460); background-size: 400% 400%; animation: gradientBG 15s ease infinite; background-attachment: fixed; }
    @keyframes gradientBG { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    .glass-card { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(20px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 24px; padding: 30px; margin: 20px 0; border-right: 4px solid #ffd700; }
    .game-title { text-align: center; font-size: clamp(2.5rem, 10vw, 4.5rem); font-weight: 900; color: #ffffff; font-family: 'Orbitron', sans-serif; text-shadow: 0 0 20px rgba(255, 215, 0, 0.5); }
    .stButton > button { width: 100%; background: linear-gradient(135deg, #ffd700 0%, #ffaa00 100%) !important; color: #000000 !important; border-radius: 20px !important; font-weight: 900 !important; padding: 15px !important; border: none !important; box-shadow: 0 10px 20px rgba(0,0,0,0.3) !important; }
    .word-box { background: rgba(255, 215, 0, 0.1); border: 2px dashed #ffd700; border-radius: 20px; padding: 25px; text-align: center; margin: 15px 0; }
    .secret-text { font-size: 2.2rem; font-weight: 900; color: #ffffff; }
    .punishment-card { background: rgba(255, 68, 68, 0.1); border: 2px solid #ff4444; border-radius: 20px; padding: 20px; margin-top: 20px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# لستة الكلمات ولستة الأحكام
WORDS_DATABASE = ["طاجين", "براد د أتاي", "صندالة", "تليفون", "موتور", "بحر", "كسكس", "كاسكيطة", "طوبيس", "الوالدين"]
PUNISHMENTS = ["☕ خلص القهوة", "🎤 غني أغنية شعبية", "🧼 غسل المواعن", "🕺 در رقصة 'Worm'", "📸 صور فيديو وقول 'أنا خروف'", "🤣 قول نكتة حامضة", "📞 عيط لشي واحد وقول ليه أنا خروف"]

DATA_FILE = "game_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f: return json.load(f)
        except: pass
    return {"players": [], "state": "setup", "word": "", "khrouf": "", "punishment": ""}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f: json.dump(data, f, ensure_ascii=False)

data = load_data()

st.markdown('<div class="game-title">🐑 Chkoun L-Khrouf?</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; color: #ffd700; letter-spacing: 2px; font-weight: bold;">💎 VIP IMPOSTER & PUNISH 💎</div>', unsafe_allow_html=True)

# --- SETUP ---
if data["state"] == "setup":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    names_input = st.text_input("📝 دخل سميات الدراري (بفاصلة):", placeholder="Yassine, Adam, Simo...")
    if st.button("🚀 بدا اللعبة"):
        player_list = [n.strip() for n in names_input.split(',') if n.strip()]
        if len(player_list) >= 3:
            data.update({"players": player_list, "word": random.choice(WORDS_DATABASE), 
                         "khrouf": random.choice(player_list), "state": "roles", 
                         "punishment": random.choice(PUNISHMENTS)})
            save_data(data)
            st.rerun()
        else: st.error("⚠️ خاص 3 د الناس على الأقل!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- ROLES ---
elif data["state"] == "roles":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; color: #888; margin-bottom: 20px;">🤫 كل واحد يكليكي على سميتو يشوف فالسكتة</div>', unsafe_allow_html=True)
    for player in data["players"]:
        with st.expander(f"👁️ أنا {player}"):
            if player == data["khrouf"]:
                st.markdown('<div class="word-box"><div style="color: #ff4444;">🤫 نتا هو</div><div class="secret-text">الخرووووف!</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="word-box"><div style="color: #ffd700;">الكلمة السرية:</div><div class="secret-text">{data["word"]}</div></div>', unsafe_allow_html=True)
    if st.button("🏁 سالينا؟ بداو الهضرة!"):
        data["state"] = "playing"; save_data(data); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PLAYING ---
elif data["state"] == "playing":
    st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #00ff88;">🔥 اللعبة شاعلة!</h2>', unsafe_allow_html=True)
    st.write("بقاو تسولو بعضياتكم حتى تعيقو بالخروف")
    if st.button("⚖️ كشف الخروف والحكم"):
        data["state"] = "reveal"; save_data(data); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- REVEAL ---
elif data["state"] == "reveal":
    st.markdown(f"""
        <div class="glass-card" style="text-align: center;">
            <div style="color: #ffd700; font-size: 1.2rem;">الخروف اللي تفرش هو:</div>
            <div style="font-size: 4rem; font-weight: 900; color: #ff4444; font-family: 'Orbitron';">{data["khrouf"]}</div>
            <div class="punishment-card">
                <div style="color: #ff4444; font-weight: bold; text-transform: uppercase;">⚖️ الحكم عليه:</div>
                <div style="font-size: 1.8rem; color: #fff; margin-top: 10px;">{data["punishment"]}</div>
            </div>
            <div style="margin-top: 25px; color: #888;">الكلمة كانت هي: <b>{data["word"]}</b></div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🔄 لعبة جديدة"):
        data = {"players": [], "state": "setup", "word": "", "khrouf": "", "punishment": ""}
        save_data(data); st.rerun()

st.markdown('<div style="text-align: center; color: rgba(255,255,255,0.1); font-size: 0.8rem; margin-top: 50px;">💎 Chkoun L-Khrouf? PRO | VIP Edition</div>', unsafe_allow_html=True)
