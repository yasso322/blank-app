import streamlit as st
import random
from datetime import datetime
import json
import os

# Page configuration
st.set_page_config(
    page_title="Chkoun L-Khrouf?",
    page_icon="🐑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for All Black Aesthetic + Darija + Responsive
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

    .stButton > button:active {
        transform: translateY(0) !important;
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

    .round-info {
        text-align: center;
        color: #666666;
        font-size: 0.9rem;
        margin: 15px 0;
        padding: 10px;
        background: rgba(255,255,255,0.02);
        border-radius: 10px;
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
</style>
""", unsafe_allow_html=True)

# Punishments list - NO nested quotes, NO apostrophes inside strings
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

# File for persistent scores
SCORES_FILE = "scores.json"

def load_scores():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_scores(scores):
    with open(SCORES_FILE, 'w', encoding='utf-8') as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)

def update_score(name, points):
    scores = load_scores()
    if name not in scores:
        scores[name] = {"total": 0, "wins": 0, "losses": 0, "history": []}

    scores[name]["total"] += points
    if points > 0:
        scores[name]["wins"] += 1
    else:
        scores[name]["losses"] += 1

    scores[name]["history"].append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "points": points
    })

    scores[name]["history"] = scores[name]["history"][-50:]

    save_scores(scores)
    return scores

def get_leaderboard():
    scores = load_scores()
    leaderboard = []
    for name, data in scores.items():
        leaderboard.append({
            "name": name,
            "total": data["total"],
            "wins": data["wins"],
            "losses": data["losses"]
        })
    leaderboard.sort(key=lambda x: x["total"], reverse=True)
    return leaderboard

def reset_all_scores():
    if os.path.exists(SCORES_FILE):
        os.remove(SCORES_FILE)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'input'
if 'names' not in st.session_state:
    st.session_state.names = []
if 'winner' not in st.session_state:
    st.session_state.winner = None
if 'punishment' not in st.session_state:
    st.session_state.punishment = None
if 'round_history' not in st.session_state:
    st.session_state.round_history = []
if 'round_number' not in st.session_state:
    st.session_state.round_number = 0
if 'scores_updated' not in st.session_state:
    st.session_state.scores_updated = False

def reset_game():
    st.session_state.page = 'input'
    st.session_state.winner = None
    st.session_state.punishment = None
    st.session_state.scores_updated = False

def new_game():
    st.session_state.page = 'input'
    st.session_state.names = []
    st.session_state.winner = None
    st.session_state.punishment = None
    st.session_state.round_history = []
    st.session_state.round_number = 0
    st.session_state.scores_updated = False

def pick_winner():
    if st.session_state.names:
        st.session_state.winner = random.choice(st.session_state.names)
        st.session_state.punishment = random.choice(PUNISHMENTS)
        st.session_state.page = 'result'
        st.session_state.round_number += 1
        st.session_state.scores_updated = False

        st.session_state.round_history.append({
            'round': st.session_state.round_number,
            'winner': st.session_state.winner,
            'punishment': st.session_state.punishment,
            'time': datetime.now().strftime("%H:%M:%S")
        })

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title
st.markdown('<div class="game-title">🐑 Chkoun L-Khrouf?</div>', unsafe_allow_html=True)
st.markdown('<div class="game-subtitle">لعبة الدراري - اللي ما يكونش الخروف هو اللي يربح 100 نقطة!</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ====== SCORE BOARD ======
leaderboard = get_leaderboard()
if leaderboard:
    st.markdown('<div class="score-board">', unsafe_allow_html=True)
    st.markdown('<div class="score-title">🏆 لائحة النقاط</div>', unsafe_allow_html=True)

    for i, player in enumerate(leaderboard[:10]):
        crown = "👑" if i == 0 else ""
        medal = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else "•"

        st.markdown(f"""
            <div class="score-item">
                <span class="score-name">{medal} {player['name']} {crown}</span>
                <span class="score-points">{player['total']} نقطة</span>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ====== ONLINE PLAY SECTION ======
st.markdown('<div class="online-section">', unsafe_allow_html=True)
st.markdown('<div class="online-title">🌐 كيفاش تلعبو Online مع الدراري؟</div>', unsafe_allow_html=True)

st.markdown("""
    <div style="color: #aaaaaa; font-size: 0.9rem; line-height: 1.8; text-align: center;">
        <p>1️⃣ شغل التطبيق فـ PC ديالك</p>
        <p>2️⃣ شارك الرابط مع الدراري</p>
        <p>3️⃣ كلو يدخل من تليفونو ويلعبو!</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="margin-top: 15px;">
        <div style="color: #888888; font-size: 0.85rem; text-align: center; margin-bottom: 5px;">
            🔗 الرابط ديالك (Local Network):
        </div>
        <div class="url-display">
            http://localhost:8501
        </div>
        <div style="color: #666666; font-size: 0.8rem; text-align: center; margin-top: 10px;">
            💡 بش تعرف IP ديالك: افتح CMD وكتب ipconfig (Windows) أو ifconfig (Mac/Linux)
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ====== INPUT PAGE ======
if st.session_state.page == 'input':
    st.markdown("""
        <div style="text-align: right; color: #cccccc; font-size: 1rem; margin-bottom: 20px; font-weight: 600;">
            📝 دخل سميات الدراري (بفاصلة):
        </div>
    """, unsafe_allow_html=True)

    names_input = st.text_input(
        "",
        placeholder="مثلاً: Yassine, Adam, Simo, Omar, Karim...",
        key="names_input",
        label_visibility="collapsed"
    )

    if names_input:
        raw_names = [name.strip() for name in names_input.split(',') if name.strip()]
        seen = set()
        st.session_state.names = []
        for name in raw_names:
            if name not in seen:
                seen.add(name)
                st.session_state.names.append(name)

        if st.session_state.names:
            tags_html = '<div class="names-list">'
            for name in st.session_state.names:
                tags_html += f'<span class="name-tag">{name}</span>'
            tags_html += '</div>'
            st.markdown(tags_html, unsafe_allow_html=True)

            st.markdown(f"""
                <div style="text-align: center; color: #666666; font-size: 0.9rem; margin: 10px 0;">
                    👥 {len(st.session_state.names)} دراري مشاركين
                </div>
            """, unsafe_allow_html=True)

    if st.session_state.round_number > 0:
        st.markdown(f"""
            <div class="round-info">
                🎮 الجولة رقم {st.session_state.round_number} | 📊 {len(st.session_state.round_history)} لعبة لعبو
            </div>
        """, unsafe_allow_html=True)

    if st.session_state.names and len(st.session_state.names) >= 2:
        if st.button("🔍 شكون هو الخروف؟", key="pick_btn", use_container_width=True):
            pick_winner()
            st.rerun()
    elif st.session_state.names and len(st.session_state.names) < 2:
        st.error("⚠️ خاص يكونو جوج على الأقل!")
    else:
        st.markdown("""
            <div style="text-align: center; color: #444444; font-size: 0.9rem; margin-top: 30px;">
                👆 دخل سميات الدراري باش نبدأو اللعبة
            </div>
        """, unsafe_allow_html=True)

# ====== RESULT PAGE ======
elif st.session_state.page == 'result':
    if not st.session_state.scores_updated:
        for name in st.session_state.names:
            if name == st.session_state.winner:
                update_score(name, 0)  # الخروف كياخد 0 (خسر)
            else:
                update_score(name, 100)  # الباقيين كيربحو 100 نقطة
        st.session_state.scores_updated = True

    st.markdown(f"""
        <div class="result-card">
            <span class="sheep-emoji">🐑</span>
            <div class="winner-label">الخروف ديال النهار هو</div>
            <div class="winner-name">{st.session_state.winner}</div>
            <div style="color: #ff4444; font-size: 1rem; margin-top: 10px; font-weight: 700;">
                ❌ 0 نقاط - الخروف خسر!
            </div>
            <div class="punishment-box">
                <div class="punishment-label">الحكم ديالو:</div>
                <div class="punishment-text">{st.session_state.punishment}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="score-board">', unsafe_allow_html=True)
    st.markdown(f'<div class="score-title">📊 نقاط الجولة رقم {st.session_state.round_number}</div>', unsafe_allow_html=True)

    for name in st.session_state.names:
        points = 0 if name == st.session_state.winner else 100
        points_class = "score-points negative" if points == 0 else "score-points"
        st.markdown(f"""
            <div class="score-item">
                <span class="score-name">{name}</span>
                <span class="{points_class}">{'+' if points > 0 else ''}{points}</span>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔄 Replay", key="replay_btn", use_container_width=True):
            reset_game()
            st.rerun()

    with col2:
        if st.button("🆕 لعبة جديدة", key="new_game_btn", use_container_width=True):
            new_game()
            st.rerun()

    with col3:
        if st.button("🗑️ Reset", key="reset_scores_btn", use_container_width=True):
            reset_all_scores()
            st.success("✅ تم مسح جميع النقاط!")
            st.rerun()

    if st.session_state.round_history:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; color: #666666; font-size: 0.9rem; margin-bottom: 15px;">
                📜 تاريخ الخرفان
            </div>
        """, unsafe_allow_html=True)

        for i, record in enumerate(reversed(st.session_state.round_history[-10:]), 1):
            st.markdown(f"""
                <div style="
                    background: rgba(255,255,255,0.03);
                    border: 1px solid rgba(255,255,255,0.08);
                    border-radius: 12px;
                    padding: 12px 15px;
                    margin: 8px 0;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                ">
                    <span style="color: #888888; font-size: 0.8rem;">#{record['round']} {record['time']}</span>
                    <span style="color: #ffffff; font-weight: 700;">{record['winner']}</span>
                    <span style="color: #aaaaaa; font-size: 0.85rem;">{record['punishment']}</span>
                </div>
            """, unsafe_allow_html=True)

st.markdown('<div class="footer-text">Made with ❤️ for the Drari | 🐑 Chkoun L-Khrouf?</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
