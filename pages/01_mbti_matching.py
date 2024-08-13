import streamlit as st

# MBTI 설명 데이터
mbti_descriptions = {
    "ISTJ": "ISTJ는 신중하고 신뢰할 수 있으며, 논리적이고 실용적인 성향을 가진 유형입니다.",
    "ISFJ": "ISFJ는 따뜻하고 책임감이 있으며, 타인을 돕는 것을 좋아하는 유형입니다.",
    "INFJ": "INFJ는 통찰력 있고 창의적이며, 깊이 있는 사고를 하는 유형입니다.",
    "INTJ": "INTJ는 독립적이고 전략적이며, 미래지향적인 사고를 하는 유형입니다.",
    "ISTP": "ISTP는 분석적이고 문제 해결에 능하며, 실용적인 성향을 가진 유형입니다.",
    "ISFP": "ISFP는 온화하고 예술적이며, 자신의 가치를 중요하게 생각하는 유형입니다.",
    "INFP": "INFP는 이상적이고 감수성이 풍부하며, 자신의 가치에 충실한 유형입니다.",
    "INTP": "INTP는 논리적이고 탐구적이며, 아이디어를 분석하는 것을 좋아하는 유형입니다.",
    "ESTP": "ESTP는 활동적이고 현실적이며, 새로운 도전에 적극적인 유형입니다.",
    "ESFP": "ESFP는 사교적이고 에너지가 넘치며, 타인과의 관계를 중요하게 생각하는 유형입니다.",
    "ENFP": "ENFP는 창의적이고 열정적이며, 새로운 아이디어와 가능성을 탐구하는 유형입니다.",
    "ENTP": "ENTP는 재치 있고 논쟁을 즐기며, 새로운 아이디어에 관심이 많은 유형입니다.",
    "ESTJ": "ESTJ는 체계적이고 결정적이며, 조직화된 환경을 선호하는 유형입니다.",
    "ESFJ": "ESFJ는 사교적이고 책임감이 강하며, 타인을 돌보는 것을 중요하게 여기는 유형입니다.",
    "ENFJ": "ENFJ는 따뜻하고 카리스마가 있으며, 타인의 성장을 돕는 것을 좋아하는 유형입니다.",
    "ENTJ": "ENTJ는 지도력과 비전을 가진 강력한 리더로, 전략적 사고를 선호하는 유형입니다."
}

# MBTI 상성 데이터
mbti_compatibility = {
    "ISTJ": "상성이 좋은 MBTI: ESTP, ESFP",
    "ISFJ": "상성이 좋은 MBTI: ESFP, ESTP",
    "INFJ": "상성이 좋은 MBTI: ENTP, ENFP",
    "INTJ": "상성이 좋은 MBTI: ENFP, ENTP",
    "ISTP": "상성이 좋은 MBTI: ESFJ, ESTJ",
    "ISFP": "상성이 좋은 MBTI: ESFJ, ENFJ",
    "INFP": "상성이 좋은 MBTI: ENFJ, ENTJ",
    "INTP": "상성이 좋은 MBTI: ENTJ, ESTJ",
    "ESTP": "상성이 좋은 MBTI: ISTJ, ISFJ",
    "ESFP": "상성이 좋은 MBTI: ISFJ, ISTJ",
    "ENFP": "상성이 좋은 MBTI: INFJ, INTJ",
    "ENTP": "상성이 좋은 MBTI: INFJ, INTJ",
    "ESTJ": "상성이 좋은 MBTI: ISTP, INTP",
    "ESFJ": "상성이 좋은 MBTI: ISFP, ISTP",
    "ENFJ": "상성이 좋은 MBTI: INFP, ISFP",
    "ENTJ": "상성이 좋은 MBTI: INFP, INTP"
}

# Streamlit 앱
st.title("MBTI 유형 분석")

# 이름 입력 받기
name = st.text_input("이름을 입력해주세요.")

# MBTI 선택박스
mbti_type = st.selectbox("MBTI 유형을 선택해주세요.", list(mbti_descriptions.keys()))

# 버튼을 눌렀을 때 결과 출력
if st.button("MBTI 분석 결과 보기"):
    st.write(f"{name}님, 당신의 MBTI 유형은 {mbti_type}입니다.")
    st.write("설명: " + mbti_descriptions[mbti_type])
    st.write("상성: " + mbti_compatibility[mbti_type])
