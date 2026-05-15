
import streamlit as st
import random
from datetime import datetime
import json
import os

# Page configuration
st.set_page_config(
    page_title="Chkoun L-Khrouf? - Multiplayer",
    page_icon="🐑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@400;700;900&display=swap');

    * {
        font-family: 'Noto Sans Arabic', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0a0a0a 100%);
        background-attachment: fixed;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}

    .main-container {
        max-width: 700px;
        margin: 0 auto;
        padding: 20px;
    }

    .game-title {
        text-align: center;
        font-size: clamp(2rem, 8vw, 3.5rem);
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 10px;
        text-shadow: 0 0 30px rgba(255,255,255,0.1);
        letter-spacing: 1px;
    }

    .game-subtitle {
        text-align: center;
        font-size: clamp(0.9rem, 3vw, 1.2rem);
        color: #888888;
        margin-bottom: 40px;
        font-weight: 400;
    }

    .stTextInput > div > div > input {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 2px solid #333333 !important;
        border-radius: 16px !important;
        padding: 16px 20px !important;
        font-size: 1.1rem !important;
        text-align: right !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #ffffff !important;
        box-shadow: 0 0 20px rgba(255,255,255,0.1) !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: #666666 !important;
    }

    .stTextInput > label {
        color: #cccccc !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        text-align: right !important;
        display: block !important;
        margin-bottom: 8px !important;
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #ffffff 0%, #e0e0e0 100%) !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 16px !important;
        padding: 18px 30px !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        text-transform: none !important;
        margin-top: 20px !important;
        box-shadow: 0 4px 20px rgba(255,255,255,0.15) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 30px rgba(255,255,255,0.25) !important;
        background: linear-gradient(135deg, #f0f0f0 0%, #ffffff 100%) !important;
    }

    .result-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #252525 100%);
        border: 1px solid #333333;
        border-radius: 24px;
        padding: 40px 30px;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        animation: fadeInUp 0.6s ease-out;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .winner-name {
        font-size: clamp(2.5rem, 10vw, 4.5rem);
        font-weight: 900;
        color: #ffffff;
        margin: 20px 0;
        text-shadow: 0 0 40px rgba(255,255,255,0.2);
        line-height: 1.2;
        word-break: break-word;
    }

    .winner-label {
        font-size: 1rem;
        color: #888888;
        margin-bottom: 10px;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    .punishment-box {
        background: rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 20px;
        margin-top: 25px;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .punishment-label {
        font-size: 0.9rem;
        color: #666666;
        margin-bottom: 8px;
    }

    .punishment-text {
        font-size: clamp(1.3rem, 5vw, 1.8rem);
        color: #ffffff;
        font-weight: 700;
        margin: 0;
    }

    .sheep-emoji {
        font-size: clamp(3rem, 10vw, 5rem);
        margin-bottom: 10px;
        display: block;
        animation: bounce 2s infinite;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    .names-list {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        justify-content: center;
        margin: 20px 0;
        padding: 15px;
        background: rgba(255,255,255,0.03);
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.08);
    }

    .name-tag {
        background: rgba(255,255,255,0.1);
        color: #ffffff;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1px solid rgba(255,255,255,0.15);
    }

    .score-board {
        background: linear-gradient(135deg, #1a1a1a 0%, #252525 100%);
        border: 1px solid #333333;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.3);
    }

    .score-title {
        text-align: center;
        font-size: 1.3rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 20px;
    }

    .score-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 15px;
        margin: 8px 0;
        background: rgba(255,255,255,0.03);
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.06);
    }

    .score-name {
        color: #ffffff;
        font-weight: 600;
        font-size: 1rem;
    }

    .score-points {
        color: #00ff88;
        font-weight: 900;
        font-size: 1.2rem;
        text-shadow: 0 0 10px rgba(0,255,136,0.3);
    }

    .score-points.negative {
        color: #ff4444;
        text-shadow: 0 0 10px rgba(255,68,68,0.3);
    }

    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #333333, transparent);
        margin: 30px 0;
    }

    .footer-text {
        text-align: center;
        color: #444444;
        font-size: 0.8rem;
        margin-top: 40px;
    }

    .online-section {
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 20px;
        margin: 20px 0;
    }

    .online-title {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 15px;
    }

    .url-display {
        background: #1a1a1a;
        border: 2px solid #333333;
        border-radius: 12px;
        padding: 12px 15px;
        color: #00ff88;
        font-family: monospace;
        font-size: 0.85rem;
        word-break: break-all;
        text-align: center;
        margin: 10px 0;
    }

    .player-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 16px;
        padding: 20px;
        margin: 10px 0;
        text-align: center;
    }

    .player-name {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
    }

    .player-status {
        font-size: 0.9rem;
        color: #888888;
        margin-top: 5px;
    }

    .host-badge {
        background: linear-gradient(135deg, #ffd700 0%, #ffaa00 100%);
        color: #000000;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        display: inline-block;
        margin-top: 10px;
    }

    .waiting-text {
        text-align: center;
        color: #666666;
        font-size: 1rem;
        margin: 20px 0;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0%, 100% { opacity: 0.5; }
        50% { opacity: 1; }
    }

    @media (max-width: 480px) {
        .main-container { padding: 15px; }
        .result-card { padding: 30px 20px; }
        .score-board { padding: 20px 15px; }
    }

    .stSuccess {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
    }

    .stError {
        background: rgba(255,50,50,0.1) !important;
        border: 1px solid rgba(255,50,50,0.2) !important;
        color: #ff6666 !important;
        border-radius: 12px !important;
    }
</style>
""", unsafe_allow_html=True)

# Punishments list
PUNISHMENTS = [
    "☕ خلص القهوة للجميع",
    "🧼 غسل المواعن كاملين",
    "🥐 جيب المسمن والحرشة",
    "🎤 غني أغنية كاملة",
    "💃 در رقصة قصيرة",
    "🤳 بعت snap مضحك للجروب",
    "🍕 شارك البيتزا مع الجميع",
    "📱 حيد التليفون 1 ساعة",
    "🥤 جيب العصير للناس",
    "😂 در ميم على راسك",
    "🎯 قول 3 حقائق مضحكة على راسك",
    "🎲 لعب دور جملة مشهورة",
    "🍰 جيب الحلوة",
    "🚶‍♂️ در 10 طوطوات قدام الناس",
    "🎭 حيد ليك القبعة 10 دقايق",
    "📸 صور فيديو قصير مع الجميع",
    "🎵 غني عيد ميلاد لشي واحد",
    "🤗 عطي hug لكل شي",
    "🎨 رسوم شي حاجة على ورقة",
    "🏆 قول انا الخروف بصوت عالي",
    "🍜 طيب شي حاجة للجروب",
    "💬 بعت رسالة غرامية لشي صاحبك",
    "🎤 قول انا غنم 3 مرات",
    "🥤 جيب الماء بارد للجميع",
    "🎯 در تحدي مع شي واحد",
    "📱 بعت I love you لوالديك",
    "🎭 در وجه مضحك 30 ثانية",
    "🍿 جيب الفشار",
    "🎵 رقص على أغنية عشوائية",
    "🤣 قول نكتة للجميع",
    "🎯 در 5 push-ups",
    "🎤 غني بالعكس",
    "📸 صور selfie مع كل شي",
    "🍕 طلب البيتزا على حسابك",
    "🎭 لعب دور شي شخصية مشهورة",
    "💬 بعت انا نحبكم للجروب",
    "🎯 در تحدي لسانك",
    "🎵 غني بدون موسيقى",
    "🤗 عطي 5 compliments",
    "🎨 رسم خروف على ورقة",
    "🏆 قول انا الملك بصوت عالي",
    "🍜 جيب الشباكية",
    "📱 بعت انا خروف لأقرب شخص",
    "🎤 غني Happy Birthday بأي لغة",
    "🎯 در 10 jumping jacks",
    "🎭 لعب دور الحيوان المفضل ديالك",
    "💬 قول سر مضحك على راسك",
    "🎵 غني Despacito لو تعرفها",
    "🤣 در ضحكة غريبة 10 ثواني",
    "🎯 در تحدي tongue twister",
    "🍿 جيب الشيبس",
    "🎤 غني Waka Waka",
    "📸 صور boomerang",
    "🎭 لعب دور المغني المفضل ديالك",
    "💬 بعت انا نحبكم لـ3 أشخاص",
    "🎯 در 15 squat",
    "🎵 غني Baby Shark",
    "🤗 عطي high-five لكل شي",
    "🎨 رسم وجه على بالون",
    "🏆 قول انا البطل بصوت عالي",
    "🍜 جيب المخمار",
    "📱 بعت انا خروف لأي رقم عشوائي",
    "🎤 غني Let It Go لو تعرفها",
    "🎯 در plank 30 ثانية",
    "🎭 لعب دور الشيف",
    "💬 قول 3 أشياء كتنحبهم في راسك",
    "🎵 غني Yalla Nwali",
    "🤣 در dab 3 مرات",
    "🎯 در تحدي moonwalk",
    "🍿 جيب الكورني فليكس",
    "🎤 غني 3 Daqat",
    "📸 صور TikTok قصير",
    "🎭 لعب دور المعلم",
    "💬 بعت انا نحب الدراري للجروب",
    "🎯 در 20 lunge",
    "🎵 غني Lma3allem",
    "🤗 عطي fist bump لكل شي",
    "🎨 رسم قلب كبير",
    "🏆 قول انا النجم بصوت عالي",
    "🍜 جيب السفوف",
    "📱 بعت انا خروف لأول شخص في contacts",
    "🎤 غني Bambola",
    "🎯 در burpees 5 مرات",
    "🎭 لعب دور الطبيب",
    "💬 قول انا نحب الدراري بـ3 لهجات",
    "🎵 غني Zina",
    "🤣 در floss dance",
    "🎯 در تحدي cartwheel",
    "🍿 جيب البيبسي",
    "🎤 غني La Bamba",
    "📸 صور Boomerang مضحك",
    "🎭 لعب دور البوليس",
    "💬 بعت انا خروف لأخر 3 أشخاص درتي معاهم chat",
    "🎯 در 25 jumping jacks",
    "🎵 غني Macarena",
    "🤗 عطي hug virtual لكل شي",
    "🎨 رسم خروف كبير",
    "🏆 قول انا الأسطورة بصوت عالي",
    "🍜 جيب البغرير",
    "📱 بعت انا نحبكم لـ5 أشخاص",
    "🎤 غني YMCA",
    "🎯 در 30 ثانية wall sit",
    "🎭 لعب دور المغني",
    "💬 قول انا خروف بـ5 لهجات مغربية",
    "🎵 غني Wavin Flag",
    "🤣 در worm dance",
    "🎯 در تحدي handstand",
    "🍿 جيب الكوكا",
    "🎤 غني Waka Waka بصوت عالي",
    "📸 صور فيديو انا خروف",
    "🎭 لعب دور الممثل",
    "💬 بعت انا خروف لشي celebrity",
    "🎯 در 40 jumping jacks",
    "🎵 غني Despacito كاملة",
    "🤗 عطي compliments لكل شي",
    "🎨 رسم وجه مضحك",
    "🏆 قول انا الملك بصوت عالي",
    "🍜 جيب الحريرة",
    "📱 بعت انا خروف لشي ex مزحة",
    "🎤 غني La Bamba كاملة",
    "🎯 در 50 jumping jacks",
    "🎭 لعب دور الشيف المغربي",
    "💬 قول انا نحب الدراري بصوت عالي",
    "🎵 غني Happy بصوت عالي",
    "🤣 در twerking 10 ثواني",
    "🎯 در تحدي splits",
    "🍿 جيب الشيبس والكوكا",
    "🎤 غني Uptown Funk",
    "📸 صور فيديو رقص",
    "🎭 لعب دور المعلم المضحك",
    "💬 بعت انا خروف لشي group chat",
    "🎯 در 60 jumping jacks",
    "🎵 غني Cant Stop the Feeling",
    "🤗 عطي group hug",
    "🎨 رسم دراري كاملين",
    "🏆 قول انا البطل بصوت عالي",
    "🍜 جيب الطاجين",
    "📱 بعت انا نحبكم لكل contacts",
    "🎤 غني Shake It Off",
    "🎯 در 70 jumping jacks",
    "🎭 لعب دور المغني المفضل",
    "💬 قول انا خروف بـ10 لهجات",
    "🎵 غني Roar بصوت عالي",
    "🤣 در floss 20 ثانية",
    "🎯 در تحدي backflip حتى لو مقدرتش",
    "🍿 جيب كلشي",
    "🎤 غني Firework",
    "📸 صور فيديو انا نحب الدراري",
    "🎭 لعب دور البطل",
    "💬 بعت انا خروف لشي random number",
    "🎯 در 100 jumping jacks",
    "🎵 غني Fight Song",
    "🤗 عطي love لكل شي",
    "🎨 رسم دراري كاملين كخرفان",
    "🏆 قول انا الأسطورة بصوت عالي",
]

# File for persistent data
DATA_FILE = "game_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {"players": [], "game_state": "waiting", "winner": None, "punishment": None, "round": 0}
    return {"players": [], "game_state": "waiting", "winner": None, "punishment": None, "round": 0}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def reset_game_data():
    save_data({"players": [], "game_state": "waiting", "winner": None, "punishment": None, "round": 0})

def add_player(name):
    data = load_data()
    if name not in data["players"]:
        data["players"].append(name)
        save_data(data)
        return True
    return False

def pick_sheep():
    data = load_data()
    if len(data["players"]) >= 2:
        data["winner"] = random.choice(data["players"])
        data["punishment"] = random.choice(PUNISHMENTS)
        data["game_state"] = "result"
        data["round"] += 1
        save_data(data)
        return data["winner"], data["punishment"]
    return None, None

def reset_round():
    data = load_data()
    data["game_state"] = "waiting"
    data["winner"] = None
    data["punishment"] = None
    save_data(data)

def new_game():
    save_data({"players": [], "game_state": "waiting", "winner": None, "punishment": None, "round": 0})

# Initialize session state for UI
if 'player_name' not in st.session_state:
    st.session_state.player_name = ""
if 'is_host' not in st.session_state:
    st.session_state.is_host = False
if 'joined' not in st.session_state:
    st.session_state.joined = False

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title
st.markdown('<div class="game-title">🐑 Chkoun L-Khrouf?</div>', unsafe_allow_html=True)
st.markdown('<div class="game-subtitle">كل واحد يدخل سميتو من تليفونو ونتوما تلعبو!</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Show current URL for sharing
data = load_data()

st.markdown('<div class="online-section">', unsafe_allow_html=True)
st.markdown('<div class="online-title">🔗 شارك هاد الرابط مع الدراري</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="url-display">
        https://blank-app-py3yziqwt6f5ajvmubjdso.streamlit.app
    </div>
    <div style="color: #666666; font-size: 0.8rem; text-align: center; margin-top: 10px;">
        💡 كل واحد يفتح هاد الرابط فتليفونو ويدخل سميتو
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ====== JOIN GAME ======
if not st.session_state.joined:
    st.markdown("""
        <div style="text-align: right; color: #cccccc; font-size: 1rem; margin-bottom: 20px; font-weight: 600;">
            📝 دخل سميتك باش تلتحق باللعبة:
        </div>
    """, unsafe_allow_html=True)

    player_name = st.text_input(
        "",
        placeholder="مثلاً: Yassine, Adam, Simo...",
        key="player_input",
        label_visibility="collapsed"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎮 انضم للعبة", use_container_width=True):
            if player_name and player_name.strip():
                name = player_name.strip()
                if add_player(name):
                    st.session_state.player_name = name
                    st.session_state.joined = True
                    st.session_state.is_host = False
                    st.success(f"✅ مرحبا {name}! انضميت للعبة!")
                    st.rerun()
                else:
                    st.error("⚠️ هاد السمية موجودة بالفعل! جرب سمية أخرى")
            else:
                st.error("⚠️ دخل سميتك أولا!")

    with col2:
        if st.button("👑 انا الـ Host", use_container_width=True):
            if player_name and player_name.strip():
                name = player_name.strip()
                if add_player(name):
                    st.session_state.player_name = name
                    st.session_state.joined = True
                    st.session_state.is_host = True
                    st.success(f"✅ مرحبا Host {name}!")
                    st.rerun()
                else:
                    st.error("⚠️ هاد السمية موجودة بالفعل!")
            else:
                st.error("⚠️ دخل سميتك أولا!")

# ====== GAME LOBBY ======
else:
    # Show player card
    st.markdown(f"""
        <div class="player-card">
            <div class="player-name">👤 {st.session_state.player_name}</div>
            <div class="player-status">{'🎮 لاعب' if not st.session_state.is_host else '👑 Host (كتحكم فاللعبة)'}</div>
        </div>
    """, unsafe_allow_html=True)

    # Show all players
    data = load_data()

    st.markdown('<div class="score-board">', unsafe_allow_html=True)
    st.markdown(f'<div class="score-title">👥 اللاعبين ({len(data["players"])})</div>', unsafe_allow_html=True)

    if data["players"]:
        tags_html = '<div class="names-list">'
        for name in data["players"]:
            tags_html += f'<span class="name-tag">{name}</span>'
        tags_html += '</div>'
        st.markdown(tags_html, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="text-align: center; color: #666666; font-size: 0.9rem;">
                🔄 مازال ما كاين حتى لاعب...
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # HOST CONTROLS
    if st.session_state.is_host:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; color: #ffd700; font-size: 1.1rem; font-weight: 700; margin-bottom: 20px;">
                👑 تحكمات الـ Host
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("🔍 شكون هو الخروف؟", use_container_width=True):
                if len(data["players"]) >= 2:
                    winner, punishment = pick_sheep()
                    if winner:
                        st.success(f"🐑 الخروف هو: {winner}!")
                        st.rerun()
                else:
                    st.error("⚠️ خاص يكونو جوج لاعبين على الأقل!")

        with col2:
            if st.button("🔄 جولة جديدة", use_container_width=True):
                reset_round()
                st.success("✅ جولة جديدة! اللاعبين كيبقاو نفسهم")
                st.rerun()

        with col3:
            if st.button("🆕 لعبة جديدة", use_container_width=True):
                new_game()
                st.session_state.joined = False
                st.session_state.player_name = ""
                st.session_state.is_host = False
                st.success("✅ لعبة جديدة! كلشي من جديد")
                st.rerun()

    # SHOW RESULT
    if data["game_state"] == "result" and data["winner"]:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        is_sheep = st.session_state.player_name == data["winner"]

        if is_sheep:
            st.markdown(f"""
                <div class="result-card">
                    <span class="sheep-emoji">🐑</span>
                    <div class="winner-label">أنت هو الخروف ديال النهار!</div>
                    <div class="winner-name">{data["winner"]}</div>
                    <div style="color: #ff4444; font-size: 1rem; margin-top: 10px; font-weight: 700;">
                        ❌ 0 نقاط - الخروف خسر!
                    </div>
                    <div class="punishment-box">
                        <div class="punishment-label">الحكم ديالك:</div>
                        <div class="punishment-text">{data["punishment"]}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="result-card">
                    <span class="sheep-emoji">🏆</span>
                    <div class="winner-label">الخروف ديال النهار هو</div>
                    <div class="winner-name">{data["winner"]}</div>
                    <div style="color: #00ff88; font-size: 1rem; margin-top: 10px; font-weight: 700;">
                        ⭐ +100 نقطة! ما كنتيش الخروف!
                    </div>
                    <div class="punishment-box">
                        <div class="punishment-label">الحكم ديال {data["winner"]}:</div>
                        <div class="punishment-text">{data["punishment"]}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        # Round scores
        st.markdown('<div class="score-board">', unsafe_allow_html=True)
        st.markdown(f'<div class="score-title">📊 نقاط الجولة رقم {data["round"]}</div>', unsafe_allow_html=True)

        for name in data["players"]:
            points = 0 if name == data["winner"] else 100
            points_class = "score-points negative" if points == 0 else "score-points"
            st.markdown(f"""
                <div class="score-item">
                    <span class="score-name">{name} {'🐑' if name == data["winner"] else '🏆'}</span>
                    <span class="{points_class}">{'+' if points > 0 else ''}{points}</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # Waiting message for non-host
    elif not st.session_state.is_host and data["game_state"] == "waiting":
        st.markdown("""
            <div class="waiting-text">
                ⏳ كنتظرو الـ Host باش يبدأ اللعبة...
                <br>
                <span style="font-size: 0.8rem;">كليك على الزر اللي فوق باش تشوف التحديثات</span>
            </div>
        """, unsafe_allow_html=True)

        if st.button("🔄 تحديث", use_container_width=True):
            st.rerun()

st.markdown('<div class="footer-text">Made with ❤️ for the Drari | 🐑 Chkoun L-Khrouf? Multiplayer</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
