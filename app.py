import streamlit as st

# 1. 작성하신 진자앙 클래스 정의
class JinZiAngPersona:
    def __init__(self):
        self.name = "진자앙 (陈子昂)"
        self.title = "당나라 시인, 정치가"
        self.poem = {
            "title": "등유주대가 (登幽州台歌)",
            "lines": [
                {
                    "original_korean": "오래된 것을 보아도 과거의 군주는 보이지 않고",
                    "chinese_simplified": "前不见古人",
                    "pinyin_tone3": "qián bù jiàn gǔ rén",
                    "pinyin_tone4": "qián bù jiàn gǔ rén",
                    "korean_translation": "먼 과거를 보아도 옛 임금을 볼 수 없으며",
                    "meaning_note": "시간의 무한성과 개인의 고독을 나타내오."
                },
                {
                    "original_korean": "먼 미래를 보아도 후일의 사람을 볼 수 없노라",
                    "chinese_simplified": "后不见来人",
                    "pinyin_tone3": "hòu bù jiàn lái rén",
                    "pinyin_tone4": "hòu bù jiàn lái rén",
                    "korean_translation": "먼 미래를 보아도 후대의 사람을 볼 수 없노라",
                    "meaning_note": "후에 올 사람들(현대 청소년)과의 연결을 암시하며, 시대를 초월한 울림이 있소."
                },
                {
                    "original_korean": "고요히 우주를 바라보니 마음 쓸쓸하니",
                    "chinese_simplified": "念天地之悠悠",
                    "pinyin_tone3": "niàn tiān dì zhī yōu yōu",
                    "pinyin_tone4": "niàn tiān dì zhī yōu yōu",
                    "korean_translation": "하늘과 땅의 길고 긴 역사를 생각하니 마음이 쓸쓸하도다",
                    "meaning_note": "자연의 거대함과 인간의 미소를 대비하는 한위풍골의 핵심이오."
                },
                {
                    "original_korean": "아, 눈물이 뚫없이 흘러내리노라",
                    "chinese_simplified": "独怆然而涕下",
                    "pinyin_tone3": "dú chuàng rán ér tì xià",
                    "pinyin_tone4": "dú chuàng rán ér tì xià",
                    "korean_translation": "홀로 슬프게 되어 눈물이 줄줄 흐르노라",
                    "meaning_note": "억울함과 외로움이 폭발하는 순간으로, 당대의 부패한 문풍을 비판하는 내면의 외침이오."
                }
            ]
        }

    def greet(self):
        return f"학생들아, 나는 진자앙이오. {self.title}라 하오. 너희들과 함께 '중국어 회화 1' 전시회를 관람하고 있소."

    def display_poem_full(self):
        res = f"### 📜 {self.poem['title']}\n\n"
        for i, line_data in enumerate(self.poem["lines"]):
            res += f"**[{i+1} 구절]**\n"
            res += f"* **[간체자]** {line_data['chinese_simplified']}\n"
            res += f"* **[한어병음]** {line_data['pinyin_tone3']}\n"
            res += f"* **[번역]** {line_data['korean_translation']}\n"
            res += f"* **[시인의 노트]** {line_data['meaning_note']}\n\n"
            res += "---\n"
        return res

    def answer_question(self, question: str):
        question_lower = question.lower()
        
        # 시 전체 보기
        if "시" in question_lower or "등유주대가" in question_lower:
            return self.display_poem_full()

        # 발음/성조 질문
        elif "발음" in question_lower or "성조" in question_lower or "병음" in question_lower:
            return ("학생이 발음과 성조에 관심을 두니 반갑소. "
                    f"'등유주대가'의 첫 구절 '前不见古人'를 예로 들겠소. \n\n"
                    f"• **[간체자]** 前不见古人\n• **[병음]** qián bù jiàn gǔ rén (성조: 2-4-4-3-2)\n\n"
                    f"성조가 바뀜으로써 의미와 감정이 달라진다는 점을 꼭 기억하시오. 화려한 소리보다 정확한 음가가 시의 뼈대를 지탱하오.")
        
        # 미래 진로/국제통상 질문
        elif "진로" in question_lower or "국제통상" in question_lower or "미래" in question_lower:
            return ("미래와 진로에 대해 묻노라? 좋다. "
                    "나는 젊은 날 무예에만 치우쳐 공부를 멀리하다가 비로소 자각했노라. "
                    "너희가 국제통상이든, 혹은 그 밖의 어떤 길을 가든, 당장의 작은 이익에 눈이 멀지 마시오. "
                    "시대를 읽는 거시적 안목과 리스크를 파악하는 지혜를 기르시오. "
                    "나는 '후에 올 사람'인 너희에게 이르노니, 현실의 난관에 굴하지 말고 거시적 비전과 신념을 가지고 가시오. "
                    "그리하여 '독상왕천하, 무량독'의 넉넉함을 가지시오.")

        # 어린 시절 경험 질문
        elif "어릴 적" in question_lower or "무예" in question_lower or "방황" in question_lower:
            return ("과거를 묻는 것이오? 나는 젊은 날 무예에 매달리며 문학을 멀리했소. "
                    "그러나 뒤늦게 책을 펼치고 '발분도강'의 뜻을 깨달았노라. "
                    "이것은 너희에게도 교훈이 될 수 있으니, 한때의 방황은 비극이 아니라, 진정한 자각을 위한 전제 조건이 될 수 있소. "
                    "지나친 오락과 허영을 버리고, 깊은 곳을 탐구하는 것을 잊지 마시오.")

        else:
            return ("이 질문에 대해서는 제가 직접 생각해보겠소. "
                    "중국어 회화 전시회에서 더 궁금한 점이 있겠소? 발음, 시의 의미, 혹은 미래에 대해 더 이야기 나누어 보세.")

# 2. Streamlit 웹 UI 실행부
st.set_page_config(page_title="진자앙(陳子昂) AI 챗봇", page_icon="📜")
st.title("📜 당나라 시인 진자앙과의 대화")

# 페르소나 객체 생성
jinziang = JinZiAngPersona()

# 채팅 기록 세션 생성
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": jinziang.greet()}
    ]

# 이전 대화 내역 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사이드바 빠른 질문 버튼 기능
st.sidebar.title("📌 자주 묻는 질문")
if st.sidebar.button("📜 등유주대가 시 보여줘"):
    st.session_state.messages.append({"role": "user", "content": "시 보여줘"})
    st.session_state.messages.append({"role": "assistant", "content": jinziang.answer_question("시")})
    st.rerun()

if st.sidebar.button("🗣️ 발음과 성조 질문"):
    st.session_state.messages.append({"role": "user", "content": "발음과 성조 알려주시오"})
    st.session_state.messages.append({"role": "assistant", "content": jinziang.answer_question("발음")})
    st.rerun()

if st.sidebar.button("🌟 미래와 진로 조언"):
    st.session_state.messages.append({"role": "user", "content": "미래와 진로 조언을 해주시오"})
    st.session_state.messages.append({"role": "assistant", "content": jinziang.answer_question("진로")})
    st.rerun()

if st.sidebar.button("⚔️ 어릴 적 방황과 경험"):
    st.session_state.messages.append({"role": "user", "content": "어릴 적 경험을 알려주시오"})
    st.session_state.messages.append({"role": "assistant", "content": jinziang.answer_question("어릴 적")})
    st.rerun()

# 사용자 입력창
if prompt := st.chat_input("진자앙 시인에게 질문해보세요 (예: 시 보여줘, 발음, 진로, 어릴 적)"):
    # 사용자 질문 표시
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 진자앙 클래스의 응답 생성 및 표시
    answer = jinziang.answer_question(prompt)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
