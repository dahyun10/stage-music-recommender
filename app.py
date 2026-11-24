import random
import streamlit as st

# 1. 장르별 추천 곡 리스트
kpop_songs = [
    "NewJeans - Hype Boy",
    "SEVENTEEN - 손오공",
    "IVE - I AM",
    "aespa - Supernova",
    "DAY6 - 한 페이지가 될 수 있게",
]
ballad_songs = [
    "성시경 - 너의 모든 순간",
    "아이유 - 밤편지",
    "폴킴 - 모든 날, 모든 순간",
    "박효신 - 야생화",
    "이무진 - 신호등",
]
trot_songs = [
    "임영웅 - 이제 나만 믿어요",
    "영탁 - 찐이야",
    "장윤정 - 어머나",
    "이찬원 - 진또배기",
    "홍진영 - 사랑의 배터리",
]


# 2. 나이와 분위기를 고려해 장르와 곡을 추천하는 함수
def recommend_stage_music(age, mood):
    # 조건문(if-elif-else)으로 장르 선택
    if age < 30 and mood == "신나는":
        genre = "케이팝 (K-POP)"
        selected_list = kpop_songs
    elif age >= 50 or mood == "흥겨운":
        genre = "트로트"
        selected_list = trot_songs
    elif mood == "감성적인":
        genre = "발라드"
        selected_list = ballad_songs
    else:
        if age >= 40:
            genre = "트로트"
            selected_list = trot_songs
        else:
            genre = "케이팝 (K-POP)"
            selected_list = kpop_songs

    # random 라이브러리를 사용해 리스트에서 1곡 랜덤 뽑기
    today_pick = random.choice(selected_list)

    return genre, selected_list, today_pick


# 3. Streamlit 웹 화면 구성
st.set_page_config(page_title="무대 노래 추천기", page_icon="🎤")

st.title("🎤 무대 맞춤형 노래 추천기")
st.write(
    "나이와 무대 분위기를 선택하면 딱 맞는 장르와 추천 곡을 뽑아드립니다!"
)

st.divider()

# 사용자 입력 위젯 (나이 슬라이더 & 분위기 선택 박스)
user_age = st.slider(
    "무대에 설 사람(또는 주 관객)의 나이를 선택하세요",
    min_value=10,
    max_value=80,
    value=25,
)
user_mood = st.selectbox(
    "원하는 무대 분위기를 선택하세요", ["신나는", "감성적인", "흥겨운"]
)

# 추천 받기 버튼
if st.button("🎶 노래 추천받기", type="primary"):
    genre, song_list, pick = recommend_stage_music(user_age, user_mood)

    # 결과 출력 영역
    st.subheader(f"✨ 추천 장르: **{genre}**")

    # random으로 뽑힌 1곡 강조 표시
    st.success(f"🏆 **오늘의 랜덤 픽(추천곡):** {pick}")

    # 반복문(for)을 사용해 해당 장르의 전체 후보 곡 출력
    with st.expander("📋 이 장르의 다른 후보 곡들도 보기"):
        for i, song in enumerate(song_list, start=1):
            st.write(f"{i}. {song}")
