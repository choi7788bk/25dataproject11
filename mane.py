import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# 예시 데이터 - 실제 데이터로 교체 가능
data = pd.DataFrame({
    '이름': ['서울장애인복지관', '부산장애인종합복지관', '대구장애인복지관'],
    '위도': [37.5665, 35.1796, 35.8714],
    '경도': [126.9780, 129.0756, 128.6014],
    '주소': ['서울특별시 중구 세종대로', '부산광역시 중구 중앙대로', '대구광역시 중구 동인동'],
    '전화번호': ['02-1234-5678', '051-9876-5432', '053-1111-2222']
})

# Streamlit 앱 시작
st.title("전국 장애인 복지 시설 위치 서비스")

# folium 지도 생성
center_lat = data['위도'].mean()
center_lon = data['경도'].mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=7)

# 마커 추가
for idx, row in data.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=f"<b>{row['이름']}</b><br>주소: {row['주소']}<br>전화: {row['전화번호']}"
    ).add_to(m)

# Streamlit에 folium 지도 표시
st_folium(m, width=700, height=500)

# 데이터 테이블 출력
if st.checkbox("시설 목록 보기"):
    st.dataframe(data)
