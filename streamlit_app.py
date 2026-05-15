
import streamlit as st
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Chkoun L-Khrouf? 🐑",
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

    /* Main background - pure black */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0a0a0a 100%);
        background-attachment: fixed;
    }

    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}

    /* Main container */
    .main-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
    }

    /* Title styling */
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

    /* Input styling */
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

    /* Labels */
    .stTextInput > label {
        color: #cccccc !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        text-align: right !important;
        display: block !important;
        margin-bottom: 8px !important;
    }

    /* Button styling */
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

    /* Secondary button (Replay) */
    .replay-btn > button {
        background: transparent !important;
        color: #ffffff !important;
        border: 2px solid #ffffff !important;
        box-shadow: none !important;
    }

    .replay-btn > button:hover {
        background: rgba(255,255,255,0.1) !important;
        box-shadow: 0 0 20px rgba(255,255,255,0.1) !important;
    }

    /* Result card */
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
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
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

    /* Sheep animation */
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

    /* Names list display */
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

    /* Divider */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #333333, transparent);
        margin: 30px 0;
    }

    /* Footer */
    .footer-text {
        text-align: center;
        color: #444444;
        font-size: 0.8rem;
        margin-top: 40px;
    }

    /* Responsive adjustments */
    @media (max-width: 480px) {
        .main-container {
            padding: 15px;
        }
        .result-card {
            padding: 30px 20px;
        }
    }

    /* Hide streamlit spinner */
    .stSpinner > div {
        border-color: #ffffff !important;
    }

    /* Success message styling */
    .stSuccess {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
    }

    /* Error message styling */
    .stError {
        background: rgba(255,50,50,0.1) !important;
        border: 1px solid rgba(255,50,50,0.2) !important;
        color: #ff6666 !important;
        border-radius: 12px !important;
    }
</style>
""", unsafe_allow_html=True)

# Punishments list (in Darija)
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
    "😂 در "ميم" على راسك",
    "🎯 قول 3 حقائق مضحكة على راسك",
    "🎲 لعب دور جملة مشهورة",
    "🍰 جيب الحلوة",
    "🚶‍♂️ در 10 طوطوات قدام الناس",
    "🎭 حيد ليك القبعة/الطاقية 10 دقايق",
    "📸 صور فيديو قصير مع الجميع",
    "🎵 غني "عيد ميلاد" لشي واحد",
    "🤗 عطي hug لكل شي",
    "🎨 رسوم شي حاجة على ورقة",
    "🏆 قول "أنا الخروف" بصوت عالي",
    "🍜 طيب شي حاجة للجروب",
    "💬 بعت رسالة غرامية لشي صاحبك (مزحة)",
    "🎤 قول "أنا غنم" 3 مرات",
    "🥤 جيب الماء بارد للجميع",
    "🎯 در تحدي مع شي واحد",
    "📱 بعت "I love you" لوالديك",
    "🎭 در وجه مضحك 30 ثانية",
    "🍿 جيب الفشار",
    "🎵 رقص على أغنية عشوائية",
    "🤣 قول نكتة للجميع",
    "🎯 در 5 push-ups",
    "🎤 غني بالعكس",
    "📸 صور selfie مع كل شي",
    "🍕 طلب البيتزا على حسابك",
    "🎭 لعب دور شي شخصية مشهورة",
    "💬 بعت "أنا نحبكم" للجروب",
    "🎯 در تحدي لسانك",
    "🎵 غني بدون موسيقى",
    "🤗 عطي 5 compliments",
    "🎨 رسم خروف على ورقة",
    "🏆 قول "أنا الملك" بصوت عالي",
    "🍜 جيب الشباكية",
    "📱 بعت "أنا خروف" لأقرب شخص",
    "🎤 غني "Happy Birthday" بأي لغة",
    "🎯 در 10 jumping jacks",
    "🎭 لعب دور الحيوان المفضل ديالك",
    "💬 قول سر مضحك على راسك",
    "🎵 غني "Despacito" (لو تعرفها)",
    "🤣 در ضحكة غريبة 10 ثواني",
    "🎯 در تحدي الـtongue twister",
    "🍿 جيب الشيبس",
    "🎤 غني "Waka Waka"",
    "📸 صور boomerang",
    "🎭 لعب دور المغني المفضل ديالك",
    "💬 بعت "أنا نحبكم" لـ3 أشخاص",
    "🎯 در 15 squat",
    "🎵 غني "Baby Shark"",
    "🤗 عطي high-five لكل شي",
    "🎨 رسم وجه على بالون",
    "🏆 قول "أنا البطل" بصوت عالي",
    "🍜 جيب المخمار",
    "📱 بعت "أنا خروف" لأي رقم عشوائي",
    "🎤 غني "Let It Go" (لو تعرفها)",
    "🎯 در plank 30 ثانية",
    "🎭 لعب دور الشيف",
    "💬 قول 3 أشياء كتنحبهم في راسك",
    "🎵 غني "Yalla Nwali"",
    "🤣 در "dab" 3 مرات",
    "🎯 در تحدي الـmoonwalk",
    "🍿 جيب الكورني فليكس",
    "🎤 غني "3 Daqat"",
    "📸 صور TikTok قصير",
    "🎭 لعب دور المعلم",
    "💬 بعت "أنا نحب الدراري" للجروب",
    "🎯 در 20 lunge",
    "🎵 غني "Lma3allem"",
    "🤗 عطي fist bump لكل شي",
    "🎨 رسم قلب كبير",
    "🏆 قول "أنا النجم" بصوت عالي",
    "🍜 جيب السفوف",
    "📱 بعت "أنا خروف" لأول شخص في contacts",
    "🎤 غني "Bambola"",
    "🎯 در burpees 5 مرات",
    "🎭 لعب دور الطبيب",
    "💬 قول "أنا نحب الدراري" بـ3 لهجات",
    "🎵 غني "Zina"",
    "🤣 در "floss dance"",
    "🎯 در تحدي الـcartwheel",
    "🍿 جيب البيبسي",
    "🎤 غني "La Bamba"",
    "📸 صور Boomerang مضحك",
    "🎭 لعب دور البوليس",
    "💬 بعت "أنا خروف" لأخر 3 أشخاص درتي معاهم chat",
    "🎯 در 25 jumping jacks",
    "🎵 غني "Macarena"",
    "🤗 عطي hug virtual لكل شي",
    "🎨 رسم خروف كبير",
    "🏆 قول "أنا الأسطورة" بصوت عالي",
    "🍜 جيب البغرير",
    "📱 بعت "أنا نحبكم" لـ5 أشخاص",
    "🎤 غني "YMCA"",
    "🎯 در 30 ثانية wall sit",
    "🎭 لعب دور المغني",
    "💬 قول "أنا خروف" بـ5 لهجات مغربية",
    "🎵 غني "Wavin' Flag"",
    "🤣 در "worm dance"",
    "🎯 در تحدي الـhandstand",
    "🍿 جيب الكوكا",
    "🎤 غني "Waka Waka" بصوت عالي",
    "📸 صور فيديو "أنا خروف"",
    "🎭 لعب دور الممثل",
    "💬 بعت "أنا خروف" لشي celebrity",
    "🎯 در 40 jumping jacks",
    "🎵 غني "Despacito" كاملة",
    "🤗 عطي compliments لكل شي",
    "🎨 رسم وجه مضحك",
    "🏆 قول "أنا الملك" بصوت عالي",
    "🍜 جيب الحريرة",
    "📱 بعت "أنا خروف" لشي ex (مزحة!)",
    "🎤 غني "La Bamba" كاملة",
    "🎯 در 50 jumping jacks",
    "🎭 لعب دور الشيف المغربي",
    "💬 قول "أنا نحب الدراري" بصوت عالي",
    "🎵 غني "Happy" بصوت عالي",
    "🤣 در "twerking" 10 ثواني",
    "🎯 در تحدي الـ splits",
    "🍿 جيب الشيبس والكوكا",
    "🎤 غني "Uptown Funk"",
    "📸 صور فيديو رقص",
    "🎭 لعب دور المعلم المضحك",
    "💬 بعت "أنا خروف" لشي group chat",
    "🎯 در 60 jumping jacks",
   "🎵 غني 'Wavin' Flag'",
    "🤣 در 'worm dance'",
    "🎯 در تحدي الـhandstand",
    "🍿 جيب الكوكا",
    "🎤 غني 'Waka Waka' بصوت عالي",
    "📸 صور فيديو 'أنا خروف'",
    "🎭 لعب دور الممثل",
    "💬 بعت 'أنا خروف' لشي celebrity",
    "🎯 در 40 jumping jacks",
    "🎵 غني 'Despacito' كاملة",
    "🤗 عطي compliments لكل شي",
    "🎨 رسم وجه مضحك",
    "🏆 قول 'أنا الملك' بصوت عالي",
    "🍜 جيب الحريرة",
    "📱 بعت 'أنا خروف' لشي ex (مزحة!)",
    "🎤 غني 'La Bamba' كاملة",
    "🎯 در 50 jumping jacks",
    "🎭 لعب دور الشيف المغربي",
    "💬 قول 'أنا نحب الدراري' بصوت عالي",
    "🎵 غني 'Happy' بصوت عالي",
    "🤣 در 'twerking' 10 ثواني",
    "🎯 در تحدي الـ splits",
    "🍿 جيب الشيبس والكوكا",
    "🎤 غني 'Uptown Funk'",
    "📸 صور فيديو رقص",
    "🎭 لعب دور المعلم المضحك",
    "💬 بعت 'أنا خروف' لشي group chat",
    "🎯 در 60 jumping jacks",
    "🎵 غني 'Can't Stop the Feeling'",
    "🤗 عطي group hug",
    "🎨 رسم دراري كاملين",
    "🏆 قول 'أنا البطل' بصوت عالي",
    "🍜 جيب الطاجين",
    "📱 بعت 'أنا نحبكم' لكل contacts",
    "🎤 غني 'Shake It Off'",
    "🎯 در 70 jumping jacks",
    "🎭 لعب دور المغني المفضل",
    "💬 قول 'أنا خروف' بـ10 لهجات",
    "🎵 غني 'Roar' بصوت عالي",
    "🤣 در 'floss' 20 ثانية",
    "🎯 در تحدي الـbackflip (حتى لو مقدرتش)",
    "🍿 جيب كلشي",
    "🎤 غني 'Firework'",
    "📸 صور فيديو 'أنا نحب الدراري'",
    "🎭 لعب دور البطل",
    "💬 بعت 'أنا خروف' لشي random number",
    "🎯 در 100 jumping jacks",
    "🎵 غني 'Fight Song'",
    "🤗 عطي love لكل شي",
    "🎨 رسم دراري كاملين كخرفان",
    "🏆 قول 'أنا الأسطورة' بصوت عالي",
]
]

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'input'
if 'names' not in st.session_state:
    st.session_state.names = []
if 'winner' not in st.session_state:
    st.session_state.winner = None
if 'punishment' not in st.session_state:
    st.session_state.punishment = None
if 'history' not in st.session_state:
    st.session_state.history = []

def reset_game():
    st.session_state.page = 'input'
    st.session_state.winner = None
    st.session_state.punishment = None
    # Keep names for replay

def new_game():
    st.session_state.page = 'input'
    st.session_state.names = []
    st.session_state.winner = None
    st.session_state.punishment = None

def pick_winner():
    if st.session_state.names:
        st.session_state.winner = random.choice(st.session_state.names)
        st.session_state.punishment = random.choice(PUNISHMENTS)
        st.session_state.page = 'result'
        # Add to history
        st.session_state.history.append({
            'winner': st.session_state.winner,
            'punishment': st.session_state.punishment,
            'time': datetime.now().strftime("%H:%M:%S")
        })

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title
st.markdown('<div class="game-title">🐑 Chkoun L-Khrouf?</div>', unsafe_allow_html=True)
st.markdown('<div class="game-subtitle">لعبة الدراري باش تعرف شكون هو الخروف ديال النهار</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Input Page
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
        # Parse names
        raw_names = [name.strip() for name in names_input.split(',') if name.strip()]
        # Remove duplicates while preserving order
        seen = set()
        st.session_state.names = []
        for name in raw_names:
            if name not in seen:
                seen.add(name)
                st.session_state.names.append(name)

        # Display names as tags
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

    # Main button
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

# Result Page
elif st.session_state.page == 'result':
    st.markdown(f"""
        <div class="result-card">
            <span class="sheep-emoji">🐑</span>
            <div class="winner-label">الخروف ديال النهار هو</div>
            <div class="winner-name">{st.session_state.winner}</div>
            <div class="punishment-box">
                <div class="punishment-label">الحكم ديالو:</div>
                <div class="punishment-text">{st.session_state.punishment}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 Replay", key="replay_btn", use_container_width=True):
            reset_game()
            st.rerun()

    with col2:
        if st.button("🆕 لعبة جديدة", key="new_game_btn", use_container_width=True):
            new_game()
            st.rerun()

    # History
    if st.session_state.history:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; color: #666666; font-size: 0.9rem; margin-bottom: 15px;">
                📜 تاريخ الخرفان
            </div>
        """, unsafe_allow_html=True)

        for i, record in enumerate(reversed(st.session_state.history[-5:]), 1):
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
                    <span style="color: #888888; font-size: 0.8rem;">{record['time']}</span>
                    <span style="color: #ffffff; font-weight: 700;">{record['winner']}</span>
                    <span style="color: #aaaaaa; font-size: 0.85rem;">{record['punishment']}</span>
                </div>
            """, unsafe_allow_html=True)

st.markdown('<div class="footer-text">Made with ❤️ for the Drari</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
