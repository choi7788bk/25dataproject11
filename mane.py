import streamlit as st

st.set_page_config(
    page_title="Silver Health Navigator",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Silver Health Navigator")
st.subheader("건강한 노화를 위한 노년층 건강관리 플랫폼")

menu = st.sidebar.radio(
    "메뉴 선택",
    [
        "홈",
        "노화질환 백과",
        "증상 자가진단",
        "건강수명 계산기",
        "최신 연구 동향"
    ]
)

# -----------------------------
# 홈
# -----------------------------
if menu == "홈":

    st.header("건강하게 나이 들기")

    st.write("""
    이 플랫폼은 노년층과 가족들이 함께 사용할 수 있는
    건강수명 관리 플랫폼입니다.

    ✔ 노화질환 정보 제공

    ✔ 증상 자가진단

    ✔ 건강수명 점수 계산

    ✔ 최신 항노화 연구 소개
    """)

    st.info(
        "※ 본 서비스는 의료 진단이 아닌 건강관리 참고용입니다."
    )

# -----------------------------
# 노화질환 백과
# -----------------------------
elif menu == "노화질환 백과":

    disease = st.selectbox(
        "질환 선택",
        [
            "알츠하이머병",
            "파킨슨병",
            "근감소증",
            "당뇨병",
            "심혈관질환"
        ]
    )

    disease_info = {

        "알츠하이머병": {
            "정의": "기억력과 인지기능이 점차 감소하는 퇴행성 뇌질환",
            "증상": "기억력 저하, 언어능력 감소",
            "예방법": "운동, 독서, 충분한 수면"
        },

        "파킨슨병": {
            "정의": "도파민 신경세포 감소로 발생하는 질환",
            "증상": "손 떨림, 운동 장애",
            "예방법": "규칙적 운동, 건강한 식습관"
        },

        "근감소증": {
            "정의": "노화에 따른 근육량 감소",
            "증상": "근력 저하, 보행 속도 감소",
            "예방법": "근력운동, 단백질 섭취"
        },

        "당뇨병": {
            "정의": "혈당 조절 기능 이상",
            "증상": "갈증, 잦은 배뇨",
            "예방법": "체중 관리, 운동"
        },

        "심혈관질환": {
            "정의": "심장과 혈관 관련 질환",
            "증상": "흉통, 호흡곤란",
            "예방법": "금연, 혈압 관리"
        }
    }

    info = disease_info[disease]

    st.subheader(disease)

    st.write("### 정의")
    st.write(info["정의"])

    st.write("### 주요 증상")
    st.write(info["증상"])

    st.write("### 예방법")
    st.write(info["예방법"])

# -----------------------------
# 증상 자가진단
# -----------------------------
elif menu == "증상 자가진단":

    st.header("증상 자가진단")

    score = 0

    q1 = st.checkbox("최근 기억력이 감소했다")
    q2 = st.checkbox("손이 자주 떨린다")
    q3 = st.checkbox("계단 오르기가 힘들다")
    q4 = st.checkbox("최근 근력이 감소했다")

    if q1:
        score += 1

    if q2:
        score += 1

    if q3:
        score += 1

    if q4:
        score += 1

    if st.button("결과 확인"):

        if score == 0:
            st.success("현재 특별한 위험 신호는 적습니다.")

        elif score <= 2:
            st.warning("건강관리와 정기검진을 권장합니다.")

        else:
            st.error(
                "노화 관련 질환 위험 신호가 있을 수 있습니다. 전문의 상담을 권장합니다."
            )

# -----------------------------
# 건강수명 계산기
# -----------------------------
elif menu == "건강수명 계산기":

    st.header("건강수명 점수 계산")

    sleep = st.slider(
        "평균 수면 시간",
        0,
        10,
        7
    )

    exercise = st.slider(
        "주간 운동 횟수",
        0,
        7,
        3
    )

    smoking = st.selectbox(
        "흡연 여부",
        ["비흡연", "흡연"]
    )

    stress = st.selectbox(
        "스트레스 수준",
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

    st.subheader(f"건강수명 점수 : {score}점")

    if score >= 80:
        st.success("건강한 생활습관을 유지하고 있습니다.")

    elif score >= 50:
        st.warning("생활습관 개선이 필요합니다.")

    else:
        st.error("건강관리에 주의가 필요합니다.")

# -----------------------------
# 최신 연구 동향
# -----------------------------
elif menu == "최신 연구 동향":

    st.header("최신 항노화 연구")

    st.markdown("""
### 2026 Nature Communications

**호모해링토닌(HHT) 연구**

- 노화세포를 선택적으로 제거
- 비만 개선
- 혈당 조절 개선
- 인슐린 저항성 감소

---

### 세노테라피(Senotherapy)

노화세포를 제거하거나 조절하여
노화 관련 질환을 예방하려는 연구 분야

---

### HSPA5 연구

노화세포 생존에 관여하는 단백질

향후 항노화 치료제의 새로운 표적으로 주목받고 있음
""")

    st.info(
        "출처: Nature Communications(2026), 영남대학교 의과대학 연구팀"
    )
