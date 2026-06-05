import streamlit as st
import random

# -------------------------
# 페이지 설정
# -------------------------
st.set_page_config(
    page_title="Silver Health Navigator",
    page_icon="🩺",
    layout="wide"
)

# -------------------------
# 사이드바
# -------------------------
st.sidebar.title("🩺 Silver Health Navigator")

menu = st.sidebar.radio(
    "메뉴 선택",
    [
        "🏠 홈",
        "📚 노화질환 백과",
        "🔎 증상 자가진단",
        "❤️ 건강수명 계산기",
        "🔬 최신 연구 동향",
        "👨‍👩‍👧 보호자 건강관리"
    ]
)

# -------------------------
# 홈
# -------------------------
if menu == "🏠 홈":

    st.title("🌱 Silver Health Navigator")
    st.subheader("건강하게 나이 들기 위한 디지털 건강 파트너")

    st.success("""
    👵👴 건강수명 100세 시대!

    질병을 치료하는 것에서 나아가
    건강하게 나이 드는 방법을 함께 알아보세요.
    """)

    tips = [
        "🚶 하루 30분 걷기는 치매 위험 감소에 도움을 줄 수 있습니다.",
        "🥗 단백질 섭취는 근감소증 예방에 중요합니다.",
        "😴 충분한 수면은 뇌 건강 유지에 도움이 됩니다.",
        "🧠 독서와 퍼즐 활동은 인지기능 유지에 도움을 줄 수 있습니다.",
        "❤️ 규칙적인 운동은 심혈관질환 위험을 낮출 수 있습니다."
    ]

    st.info(random.choice(tips))

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🧠 주요 노화질환", "5종")

    with col2:
        st.metric("🔬 최신 연구 소개", "항노화 연구")

    with col3:
        st.metric("❤️ 건강수명 관리", "맞춤형")

    st.markdown("---")

    st.header("🎯 플랫폼 목표")

    st.write("""
    ✔ 노화 관련 질환 정보 제공

    ✔ 증상 자가진단

    ✔ 건강수명 평가

    ✔ 최신 항노화 연구 소개

    ✔ 보호자를 위한 건강관리 가이드 제공
    """)

# -------------------------
# 질환 백과
# -------------------------
elif menu == "📚 노화질환 백과":

    st.title("📚 노화질환 백과")

    disease = st.selectbox(
        "질환 선택",
        [
            "🧠 알츠하이머병",
            "🤲 파킨슨병",
            "💪 근감소증",
            "🍬 당뇨병",
            "❤️ 심혈관질환"
        ]
    )

    if disease == "🧠 알츠하이머병":

        st.header("🧠 알츠하이머병")

        st.write("""
        **정의**

        기억력과 인지기능이 점차 감소하는 퇴행성 뇌질환
        """)

        st.write("""
        **대표 증상**

        ✅ 기억력 저하

        ✅ 같은 질문 반복

        ✅ 길 찾기 어려움

        ✅ 언어능력 감소
        """)

        st.write("""
        **위험요인**

        🔺 고령

        🔺 고혈압

        🔺 당뇨

        🔺 운동 부족

        🔺 수면 부족
        """)

        st.write("""
        **예방 방법**

        🚶 유산소 운동

        📖 독서

        🥗 균형 잡힌 식사

        🤝 사회활동
        """)

    elif disease == "🤲 파킨슨병":

        st.header("🤲 파킨슨병")

        st.write("""
        **정의**

        도파민 신경세포 감소로 발생하는 신경퇴행성 질환
        """)

        st.write("""
        **대표 증상**

        ✅ 손 떨림

        ✅ 운동 느려짐

        ✅ 보행 장애

        ✅ 근육 경직
        """)

    elif disease == "💪 근감소증":

        st.header("💪 근감소증")

        st.write("""
        **정의**

        노화로 인해 근육량과 근력이 감소하는 질환
        """)

        st.write("""
        **대표 증상**

        ✅ 계단 오르기 힘듦

        ✅ 악력 감소

        ✅ 쉽게 피로함

        ✅ 균형감 저하
        """)

        st.write("""
        **예방 방법**

        🏋️ 근력운동

        🥚 단백질 섭취

        🚶 걷기 운동
        """)

    elif disease == "🍬 당뇨병":

        st.header("🍬 당뇨병")

        st.write("""
        **정의**

        혈당 조절 기능에 문제가 발생하는 대사질환
        """)

        st.write("""
        **대표 증상**

        ✅ 잦은 갈증

        ✅ 잦은 배뇨

        ✅ 피로감

        ✅ 체중 변화
        """)

    elif disease == "❤️ 심혈관질환":

        st.header("❤️ 심혈관질환")

        st.write("""
        **정의**

        심장과 혈관에 발생하는 질환
        """)

        st.write("""
        **대표 증상**

        ✅ 흉통

        ✅ 호흡곤란

        ✅ 혈압 상승

        ✅ 피로감
        """)

# -------------------------
# 자가진단
# -------------------------
elif menu == "🔎 증상 자가진단":

    st.title("🔎 노화질환 증상 자가진단")

    st.warning("※ 의료 진단이 아닌 참고용입니다.")

    score = 0

    st.subheader("🧠 기억력 영역")

    if st.checkbox("최근 기억력이 감소했다"):
        score += 1

    if st.checkbox("같은 질문을 반복한다"):
        score += 1

    if st.checkbox("약속을 자주 잊는다"):
        score += 1

    st.subheader("💪 운동 기능 영역")

    if st.checkbox("계단 오르기가 힘들다"):
        score += 1

    if st.checkbox("근력이 감소했다"):
        score += 1

    if st.checkbox("손이 떨린다"):
        score += 1

    st.subheader("🍬 대사 건강 영역")

    if st.checkbox("최근 체중이 증가했다"):
        score += 1

    if st.checkbox("갈증이 자주 난다"):
        score += 1

    if st.checkbox("쉽게 피곤해진다"):
        score += 1

    if st.button("결과 확인"):

        if score <= 2:
            st.success("🟢 위험도 낮음")

        elif score <= 5:
            st.warning("🟡 건강관리 필요")

        else:
            st.error("🔴 전문의 상담 권장")

# -------------------------
# 건강수명 계산기
# -------------------------
elif menu == "❤️ 건강수명 계산기":

    st.title("❤️ 건강수명 계산기")

    sleep = st.slider("😴 하루 수면시간", 0, 10, 7)

    exercise = st.slider("🏃 주간 운동 횟수", 0, 7, 3)

    smoking = st.selectbox(
        "🚭 흡연 여부",
        ["비흡연", "흡연"]
    )

    stress = st.selectbox(
        "😣 스트레스 수준",
        ["낮음", "보통", "높음"]
    )

    score = 0

    if sleep >= 7:
        score += 25

    if exercise >= 3:
        score += 25

    if smoking == "비흡연":
        score += 25

    if stress == "낮음":
        score += 25

    st.progress(score / 100)

    st.subheader(f"🌟 건강수명 점수 : {score}점")

    if score >= 80:
        st.success("매우 우수한 생활습관입니다!")

    elif score >= 50:
        st.warning("생활습관 개선이 필요합니다.")

    else:
        st.error("건강관리에 주의가 필요합니다.")

# -------------------------
# 연구 동향
# -------------------------
elif menu == "🔬 최신 연구 동향":

    st.title("🔬 최신 항노화 연구 동향")

    st.header("🧬 노화세포(Senescent Cell)")

    st.write("""
    노화세포는 세포분열을 멈추었지만
    체내에 남아있는 세포이다.
    """)

    st.header("⚠️ SASP")

    st.write("""
    노화세포는 SASP라는 염증성 물질을 분비한다.

    SASP 증가

    ⬇️

    만성염증

    ⬇️

    비만 · 당뇨

    ⬇️

    심혈관질환
    """)

    st.header("💊 호모해링토닌(HHT)")

    st.write("""
    영남대학교 의과대학 연구팀은

    혈액암 치료제인 HHT가

    노화세포를 선택적으로 제거할 수 있음을 확인하였다.
    """)

    st.success("""
    연구 결과

    ✅ 비만 개선

    ✅ 혈당 조절 개선

    ✅ 인슐린 저항성 감소

    ✅ 건강수명 연장 가능성 확인
    """)

    st.header("🧪 HSPA5")

    st.write("""
    HSPA5는 세포가 스트레스를 견디도록 돕는 단백질이다.

    연구진은 HSPA5를 억제하면

    노화세포를 선택적으로 제거할 수 있다는 가능성을 제시하였다.
    """)

    st.info("""
    출처

    Nature Communications (2026)

    Homoharringtonine exhibits senotherapeutic activity that mitigates diet- and age-associated obesity and insulin resistance and extends lifespan in mice
    """)

# -------------------------
# 보호자 건강관리
# -------------------------
elif menu == "👨‍👩‍👧 보호자 건강관리":

    st.title("👨‍👩‍👧 보호자 건강관리 가이드")

    age = st.number_input(
        "부모님 나이 입력",
        50,
        100,
        65
    )

    st.subheader("📋 권장 건강검진")

    if age >= 65:

        st.success("""
        ✅ 치매 선별검사

        ✅ 골다공증 검사

        ✅ 혈압 검사

        ✅ 당뇨 검사

        ✅ 심혈관질환 검사
        """)

    else:

        st.info("""
        ✅ 혈압 검사

        ✅ 혈당 검사

        ✅ 체중 관리

        ✅ 규칙적 운동
        """)

    st.markdown("---")

    st.header("❤️ 건강수명 늘리는 습관")

    st.write("""
    🚶 매일 걷기

    🥗 균형 잡힌 식단

    😴 충분한 수면

    🏋️ 근력운동

    🤝 사회활동 유지
    """)
