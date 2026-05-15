
import streamlit as st
import random
from datetime import datetime
import json
import os

# Page configuration
st.set_page_config(
    page_title="Chkoun L-Khrouf? PRO",
    page_icon="🐑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ULTIMATE CSS - Glassmorphism, Particles, 3D, Animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@300;400;600;700;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');

    * {
        font-family: 'Noto Sans Arabic', sans-serif;
    }

    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #0a0a0a, #1a1a2e, #16213e, #0f3460, #1a1a2e, #0a0a0a);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        background-attachment: fixed;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Hide defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}

    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    /* Glassmorphism card base */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
        transition: all 0.4s ease;
    }

    .glass-card:hover {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(255, 255, 255, 0.2);
        box-shadow: 
            0 12px 40px rgba(0, 0, 0, 0.4),
            0 0 60px rgba(255, 215, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transform: translateY(-2px);
    }

    /* Animated title */
    .game-title {
        text-align: center;
        font-size: clamp(2.5rem, 10vw, 4.5rem);
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 15px;
        text-shadow: 
            0 0 20px rgba(255, 215, 0, 0.5),
            0 0 40px rgba(255, 215, 0, 0.3),
            0 0 80px rgba(255, 215, 0, 0.1);
        letter-spacing: 3px;
        animation: titleFloat 4s ease-in-out infinite;
        font-family: 'Orbitron', sans-serif;
    }

    @keyframes titleFloat {
        0%, 100% { 
            transform: translateY(0);
            text-shadow: 0 0 20px rgba(255, 215, 0, 0.5), 0 0 40px rgba(255, 215, 0, 0.3);
        }
        50% { 
            transform: translateY(-10px);
            text-shadow: 0 0 30px rgba(255, 215, 0, 0.8), 0 0 60px rgba(255, 215, 0, 0.5), 0 0 100px rgba(255, 215, 0, 0.2);
        }
    }

    .game-subtitle {
        text-align: center;
        font-size: clamp(1rem, 3vw, 1.4rem);
        color: rgba(255, 255, 255, 0.6);
        margin-bottom: 40px;
        font-weight: 300;
        letter-spacing: 2px;
        animation: fadeInUp 1.5s ease-out;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* 3D Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #ffd700 0%, #ffaa00 50%, #ffd700 100%) !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 22px 40px !important;
        font-size: 1.3rem !important;
        font-weight: 900 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        text-transform: none !important;
        margin-top: 20px !important;
        box-shadow: 
            0 10px 30px rgba(255, 215, 0, 0.3),
            0 0 60px rgba(255, 215, 0, 0.2),
            inset 0 2px 0 rgba(255, 255, 255, 0.3) !important;
        position: relative;
        overflow: hidden;
    }

    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: left 0.5s ease;
    }

    .stButton > button:hover::before {
        left: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: 
            0 15px 40px rgba(255, 215, 0, 0.5),
            0 0 80px rgba(255, 215, 0, 0.3),
            inset 0 2px 0 rgba(255, 255, 255, 0.4) !important;
    }

    .stButton > button:active {
        transform: translateY(0) scale(0.98) !important;
    }

    /* Glass input */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 20px !important;
        padding: 20px 24px !important;
        font-size: 1.2rem !important;
        text-align: right !important;
        transition: all 0.4s ease !important;
        box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.2) !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #ffd700 !important;
        box-shadow: 
            0 0 30px rgba(255, 215, 0, 0.2),
            inset 0 2px 10px rgba(0, 0, 0, 0.2) !important;
        background: rgba(255, 255, 255, 0.08) !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.3) !important;
    }

    .stTextInput > label {
        color: rgba(255, 255, 255, 0.7) !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        text-align: right !important;
        display: block !important;
        margin-bottom: 10px !important;
    }

    /* Result card - EPIC */
    .result-card {
        background: rgba(255, 215, 0, 0.05);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 2px solid rgba(255, 215, 0, 0.3);
        border-radius: 30px;
        padding: 50px 40px;
        text-align: center;
        margin: 30px 0;
        box-shadow: 
            0 20px 60px rgba(0, 0, 0, 0.5),
            0 0 100px rgba(255, 215, 0, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        animation: epicEntrance 1.2s cubic-bezier(0.68, -0.55, 0.265, 1.55) both;
    }

    @keyframes epicEntrance {
        0% { 
            opacity: 0; 
            transform: scale(0.3) rotate(-15deg) translateY(100px);
            filter: blur(20px);
        }
        60% { 
            transform: scale(1.05) rotate(2deg) translateY(-10px);
            filter: blur(0);
        }
        100% { 
            opacity: 1; 
            transform: scale(1) rotate(0) translateY(0);
        }
    }

    .winner-name {
        font-size: clamp(3rem, 14vw, 6rem);
        font-weight: 900;
        color: #ffd700;
        margin: 25px 0;
        text-shadow: 
            0 0 30px rgba(255, 215, 0, 0.6),
            0 0 60px rgba(255, 215, 0, 0.4),
            0 0 100px rgba(255, 215, 0, 0.2);
        line-height: 1.2;
        word-break: break-word;
        animation: winnerPulse 2s ease-in-out infinite;
        font-family: 'Orbitron', sans-serif;
    }

    @keyframes winnerPulse {
        0%, 100% { 
            transform: scale(1);
            text-shadow: 0 0 30px rgba(255, 215, 0, 0.6);
        }
        50% { 
            transform: scale(1.08);
            text-shadow: 0 0 50px rgba(255, 215, 0, 1), 0 0 100px rgba(255, 215, 0, 0.6), 0 0 150px rgba(255, 215, 0, 0.3);
        }
    }

    .winner-label {
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.5);
        margin-bottom: 20px;
        letter-spacing: 5px;
        text-transform: uppercase;
        animation: fadeInUp 1s ease-out 0.3s both;
    }

    /* Punishment box */
    .punishment-box {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 30px;
        margin-top: 35px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        animation: fadeInUp 1s ease-out 0.8s both;
    }

    .punishment-label {
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.4);
        margin-bottom: 12px;
        letter-spacing: 2px;
    }

    .punishment-text {
        font-size: clamp(1.5rem, 5vw, 2.2rem);
        color: #ffffff;
        font-weight: 700;
        margin: 0;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
    }

    /* Sheep with 3D effect */
    .sheep-emoji {
        font-size: clamp(4rem, 14vw, 7rem);
        margin-bottom: 20px;
        display: block;
        animation: sheep3D 1.5s ease-in-out infinite;
        filter: drop-shadow(0 0 30px rgba(255, 215, 0, 0.5));
    }

    @keyframes sheep3D {
        0%, 100% { 
            transform: translateY(0) rotateY(0deg) scale(1);
            filter: drop-shadow(0 0 30px rgba(255, 215, 0, 0.5));
        }
        25% { 
            transform: translateY(-20px) rotateY(-15deg) scale(1.1);
            filter: drop-shadow(0 0 50px rgba(255, 215, 0, 0.8));
        }
        50% { 
            transform: translateY(0) rotateY(0deg) scale(1);
            filter: drop-shadow(0 0 30px rgba(255, 215, 0, 0.5));
        }
        75% { 
            transform: translateY(-15px) rotateY(15deg) scale(1.05);
            filter: drop-shadow(0 0 40px rgba(255, 215, 0, 0.7));
        }
    }

    /* Name tags with glass effect */
    .names-list {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        justify-content: center;
        margin: 25px 0;
        padding: 25px;
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .name-tag {
        background: rgba(255, 215, 0, 0.1);
        backdrop-filter: blur(5px);
        color: #ffd700;
        padding: 10px 20px;
        border-radius: 30px;
        font-size: 1.1rem;
        font-weight: 700;
        border: 1px solid rgba(255, 215, 0, 0.3);
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.1);
        transition: all 0.3s ease;
        animation: tagGlow 3s ease-in-out infinite;
    }

    .name-tag:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.3);
        background: rgba(255, 215, 0, 0.2);
    }

    @keyframes tagGlow {
        0%, 100% { box-shadow: 0 4px 15px rgba(255, 215, 0, 0.1); }
        50% { box-shadow: 0 4px 25px rgba(255, 215, 0, 0.3), 0 0 30px rgba(255, 215, 0, 0.2); }
    }

    /* Score board glass */
    .score-board {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 30px;
        margin: 25px 0;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    }

    .score-title {
        text-align: center;
        font-size: 1.5rem;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 25px;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
        letter-spacing: 2px;
    }

    .score-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 20px;
        margin: 12px 0;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        transition: all 0.4s ease;
    }

    .score-item:hover {
        background: rgba(255, 255, 255, 0.06);
        transform: translateX(-8px);
        border-color: rgba(255, 215, 0, 0.2);
        box-shadow: 0 5px 20px rgba(255, 215, 0, 0.1);
    }

    .score-name {
        color: #ffffff;
        font-weight: 700;
        font-size: 1.2rem;
    }

    .score-points {
        color: #00ff88;
        font-weight: 900;
        font-size: 1.4rem;
        text-shadow: 0 0 20px rgba(0, 255, 136, 0.5);
    }

    .score-points.negative {
        color: #ff4444;
        text-shadow: 0 0 20px rgba(255, 68, 68, 0.5);
    }

    /* Player card VIP */
    .player-card {
        background: rgba(255, 215, 0, 0.05);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(255, 215, 0, 0.2);
        border-radius: 24px;
        padding: 30px;
        margin: 20px 0;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3), 0 0 60px rgba(255, 215, 0, 0.1);
        animation: cardFloat 4s ease-in-out infinite;
    }

    @keyframes cardFloat {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
    }

    .player-name {
        font-size: 2rem;
        font-weight: 900;
        color: #ffd700;
        text-shadow: 0 0 30px rgba(255, 215, 0, 0.4);
        font-family: 'Orbitron', sans-serif;
    }

    .player-status {
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.5);
        margin-top: 10px;
    }

    .host-badge {
        background: linear-gradient(135deg, #ffd700 0%, #ff8c00 100%);
        color: #000000;
        padding: 8px 20px;
        border-radius: 30px;
        font-size: 1rem;
        font-weight: 900;
        display: inline-block;
        margin-top: 15px;
        box-shadow: 0 5px 20px rgba(255, 215, 0, 0.4);
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Divider with gradient */
    .divider {
        height: 2px;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 215, 0, 0.3), 
            rgba(255, 255, 255, 0.5), 
            rgba(255, 215, 0, 0.3), 
            transparent
        );
        margin: 35px 0;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.2);
    }

    /* Footer */
    .footer-text {
        text-align: center;
        color: rgba(255, 255, 255, 0.3);
        font-size: 0.9rem;
        margin-top: 50px;
        letter-spacing: 3px;
    }

    /* Online section */
    .online-section {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 30px;
        margin: 25px 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }

    .online-title {
        color: #ffd700;
        font-size: 1.3rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
        letter-spacing: 2px;
    }

    .url-display {
        background: rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 215, 0, 0.3);
        border-radius: 16px;
        padding: 16px 20px;
        color: #ffd700;
        font-family: 'Orbitron', monospace;
        font-size: 0.95rem;
        word-break: break-all;
        text-align: center;
        margin: 15px 0;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.15);
        letter-spacing: 1px;
    }

    /* Waiting animation */
    .waiting-text {
        text-align: center;
        color: rgba(255, 255, 255, 0.5);
        font-size: 1.2rem;
        margin: 30px 0;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0%, 100% { opacity: 0.4; }
        50% { opacity: 1; }
    }

    /* Responsive */
    @media (max-width: 480px) {
        .main-container { padding: 15px; }
        .result-card { padding: 35px 25px; }
        .score-board { padding: 25px 20px; }
        .glass-card { padding: 25px 20px; }
    }

    /* Success/Error with glass */
    .stSuccess {
        background: rgba(0, 255, 136, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(0, 255, 136, 0.3) !important;
        color: #00ff88 !important;
        border-radius: 16px !important;
        font-weight: 700 !important;
        box-shadow: 0 5px 20px rgba(0, 255, 136, 0.1) !important;
    }

    .stError {
        background: rgba(255, 50, 50, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 50, 50, 0.3) !important;
        color: #ff6666 !important;
        border-radius: 16px !important;
        font-weight: 700 !important;
        box-shadow: 0 5px 20px rgba(255, 50, 50, 0.1) !important;
    }

    /* Particle effect container */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
        overflow: hidden;
    }

    .particle {
        position: absolute;
        width: 4px;
        height: 4px;
        background: rgba(255, 215, 0, 0.5);
        border-radius: 50%;
        animation: particleFloat 20s infinite;
    }

    @keyframes particleFloat {
        0%, 100% { 
            transform: translateY(100vh) translateX(0);
            opacity: 0;
        }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { 
            transform: translateY(-100px) translateX(100px);
            opacity: 0;
        }
    }
</style>
""", unsafe_allow_html=True)

# Particles background
st.markdown("""
    <div class="particles">
        <div class="particle" style="left: 10%; animation-delay: 0s; animation-duration: 15s;"></div>
        <div class="particle" style="left: 20%; animation-delay: 2s; animation-duration: 20s;"></div>
        <div class="particle" style="left: 30%; animation-delay: 4s; animation-duration: 18s;"></div>
        <div class="particle" style="left: 40%; animation-delay: 1s; animation-duration: 22s;"></div>
        <div class="particle" style="left: 50%; animation-delay: 3s; animation-duration: 16s;"></div>
        <div class="particle" style="left: 60%; animation-delay: 5s; animation-duration: 19s;"></div>
        <div class="particle" style="left: 70%; animation-delay: 2.5s; animation-duration: 21s;"></div>
        <div class="particle" style="left: 80%; animation-delay: 1.5s; animation-duration: 17s;"></div>
        <div class="particle" style="left: 90%; animation-delay: 4.5s; animation-duration: 23s;"></div>
        <div class="particle" style="left: 15%; animation-delay: 6s; animation-duration: 14s;"></div>
        <div class="particle" style="left: 25%; animation-delay: 7s; animation-duration: 25s;"></div>
        <div class="particle" style="left: 35%; animation-delay: 3.5s; animation-duration: 20s;"></div>
        <div class="particle" style="left: 45%; animation-delay: 5.5s; animation-duration: 18s;"></div>
        <div class="particle" style="left: 55%; animation-delay: 8s; animation-duration: 22s;"></div>
        <div class="particle" style="left: 65%; animation-delay: 2s; animation-duration: 16s;"></div>
        <div class="particle" style="left: 75%; animation-delay: 6.5s; animation-duration: 19s;"></div>
        <div class="particle" style="left: 85%; animation-delay: 4s; animation-duration: 21s;"></div>
        <div class="particle" style="left: 5%; animation-delay: 7.5s; animation-duration: 24s;"></div>
        <div class="particle" style="left: 95%; animation-delay: 1s; animation-duration: 15s;"></div>
        <div class="particle" style="left: 50%; animation-delay: 9s; animation-duration: 20s;"></div>
    </div>
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

# Initialize session state
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
st.markdown('<div class="game-subtitle">💎 VIP EDITION - PRO DESIGN</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Show current URL for sharing
data = load_data()

# Display QR Code prominently
st.markdown('<div class="online-section">', unsafe_allow_html=True)
st.markdown('<div class="online-title">📱 مسح بالكاميرا وادخل!</div>', unsafe_allow_html=True)

# Display QR code image
st.image("qr_code.png", use_container_width=True)

st.markdown("""
    <div style="
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
        border: 3px solid #ffd700;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        text-align: center;
        box-shadow: 0 0 50px rgba(255, 215, 0, 0.3), 0 0 100px rgba(255, 215, 0, 0.1);
    ">
        <div style="color: #ffd700; font-size: 1.5rem; font-weight: 900; margin-bottom: 15px; text-shadow: 0 0 20px rgba(255,215,0,0.5);">
            👆 ولا مسح بالكاميرا!
        </div>
        <div style="color: rgba(255,255,255,0.6); font-size: 1rem; margin-top: 15px; line-height: 1.8;">
            📱 <b>افتح الكاميرا ووجهها للQR Code</b><br>
            🔗 <b>غادي يفتح الرابط مباشرة</b><br>
            🎮 <b>ويلعبو معاك Online!</b>
        </div>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ====== JOIN GAME ======
if not st.session_state.joined:
    st.markdown("""
        <div style="text-align: right; color: rgba(255,255,255,0.7); font-size: 1.1rem; margin-bottom: 20px; font-weight: 700;">
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
                    st.error("⚠️ هاد السمية موجودة! جرب سمية أخرى")
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
                    st.error("⚠️ هاد السمية موجودة!")
            else:
                st.error("⚠️ دخل سميتك أولا!")

# ====== GAME LOBBY ======
else:
    # Show player card
    st.markdown(f"""
        <div class="player-card">
            <div class="player-name">👤 {st.session_state.player_name}</div>
            <div class="player-status">{'🎮 لاعب' if not st.session_state.is_host else '👑 Host - كتحكم فاللعبة'}</div>
            {f'<div class="host-badge">HOST</div>' if st.session_state.is_host else ''}
        </div>
    """, unsafe_allow_html=True)

    # Show all players
    data = load_data()

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="score-title">👥 اللاعبين ({len(data["players"])})</div>', unsafe_allow_html=True)

    if data["players"]:
        tags_html = '<div class="names-list">'
        for name in data["players"]:
            tags_html += f'<span class="name-tag">{name}</span>'
        tags_html += '</div>'
        st.markdown(tags_html, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="text-align: center; color: rgba(255,255,255,0.4); font-size: 0.9rem;">
                🔄 مازال ما كاين حتى لاعب...
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # HOST CONTROLS
    if st.session_state.is_host:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; color: #ffd700; font-size: 1.3rem; font-weight: 900; margin-bottom: 25px; text-shadow: 0 0 20px rgba(255,215,0,0.3);">
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
                st.success("✅ جولة جديدة!")
                st.rerun()

        with col3:
            if st.button("🆕 لعبة جديدة", use_container_width=True):
                new_game()
                st.session_state.joined = False
                st.session_state.player_name = ""
                st.session_state.is_host = False
                st.success("✅ لعبة جديدة!")
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

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
                    <div style="color: #ff4444; font-size: 1.3rem; margin-top: 20px; font-weight: 900; text-shadow: 0 0 20px rgba(255,68,68,0.5);">
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
                    <div style="color: #00ff88; font-size: 1.3rem; margin-top: 20px; font-weight: 900; text-shadow: 0 0 20px rgba(0,255,136,0.5);">
                        ⭐ +100 نقطة! ما كنتيش الخروف!
                    </div>
                    <div class="punishment-box">
                        <div class="punishment-label">الحكم ديال {data["winner"]}:</div>
                        <div class="punishment-text">{data["punishment"]}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        # Round scores
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="score-title">📊 نقاط الجولة رقم {data["round"]} - VIP!</div>', unsafe_allow_html=True)

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
                <span style="font-size: 0.9rem;">🔄 كليك تحديث باش تشوف التغييرات</span>
            </div>
        """, unsafe_allow_html=True)

        if st.button("🔄 تحديث", use_container_width=True):
            st.rerun()

st.markdown('<div class="footer-text">💎 VIP EDITION | Made with ❤️ for the Drari | 🐑 Chkoun L-Khrouf? PRO</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
