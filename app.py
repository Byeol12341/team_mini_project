import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
from st_pages import Page, show_pages, add_page_title

st.title('Mini Project of Group 3')
st.subheader('<메가서울> 정책의 부동산 시장 측면의 효과 및 결과')
st.caption('Period of Data : 2023-06-01 ~ 2024-01-31')
st.write("-" * 50)

tab1, tab2, tab3, tab4 = st.tabs(["긍정1", "긍정2", "부정1", "부정2"])

with tab1:
    st.header("'메가 서울' 어디까지?…김포·고양 등 집값 상승 시간문제")
    st.image('images/20240206_133156.png', caption='https://www.news1.kr/articles/5216355 ')
    st.write('국민의힘이 수도권 총선 전략으로 경기 김포시를 비롯해 구리, 광명, 고양, 하남시 등을 서울로 편입하는 \'서울 메가시티\' 카드를 꺼내면서 집값에도 적지 않은 영향이 미칠 전망이다.')
    st.write('여기에 \'메가 서울\'로 편입될 때 인프라 강화로 김포 등 편입 지역이 인근 서울의 낙후 지역 집값을 뛰어넘을 가능성도 나온다.')
    st.write(
        '고준석 제이에듀투자자문 대표는 \"김포가 서울로 편입될 때 김포 집값이 올라가는 것은 시간문제다\"며 \"약 47조원(지난해 기준)에 달하는 서울시 예산으로 김포에도 각종 인프라 지원이 가능해지기 때문이다\"고 말했다.')
    st.write(
        '고 대표는 \"서울 집값은 분산 효과가 나타날 수 있다\"며 \"김포는 새로 만들어진 \'한강신도시\'이기 때문에 서울로의 교통환경 등 인프라만 강화되면 인접한 강서구 낙후된 지역보다 오히려 집값이 더 오를 가능성도 있다\"고 내다봤다.')
with tab2:
    st.header("\"서울시 김포구 될까\"…매물 거두는 집주인들")
    st.image('images/20240206_133217.png', caption='https://www.sedaily.com/NewsView/29X3DAW5MA')
    st.write(
        '경기도 김포시 풍무동에 사는 A 씨는 아이의 초등학교 입학을 앞두고 서울 진입을 위해 아파트를 팔려다 최근 마음을 바꿨다. ‘김포시의 서울시 편입’이 공론화되면서 집값이 지금보다는 더 오를 것이라는 판단에서다. A 씨는 “행정구역이 단순 서울시로 바뀐다는 것보다는 편입으로 인한 교통 인프라 개발이 기대되는 점”이라며 “당분간 매매를 보류하고 상황을 지켜볼 예정”이라고 말했다.')
    st.write(
        '3일 부동산 플랫폼 아실에 따르면 이날 김포시의 아파트 매매 매물 수는 8506건으로 10일 전(8307건)보다 2.3% 늘어나는 데 그쳤다. 이는 경기 31개 시군 중 가장 낮은 수치다.')
    st.write('매물을 내놓아도 호가를 올리는 사례가 많아졌다. 김포 고촌읍 ‘수기마을힐스테이트3단지’ 전용 156㎡의 호가는 11억 원에서 최근 11억 5000만 원으로 5000만 원 올랐다.')
with tab3:
    st.header("김포, 서울편입 특별법 두달여... 힘빠진 편입론에 김포 집값영향 '미미'")
    st.image('images/20240206_133307.png', caption='https://www.ajunews.com/view/20240121134429565')

    st.write(
        '경기 김포시 서울 편입 특별법이 발의된 지 두 달여가 지났지만 논의에 진전이 없으면서 김포시 부동산 시장도 가라앉는 분위기다. 서울 편입안이 발표됐을 당시 일부 아파트 단지를 중심으로 반짝 상승을 보이기도 했으나 다시 하락세로 돌아서는 등 집값에 미치는 영향은 미미하다는 반응이다.')
    st.write(
        '특별법이 발의된 지난해 11월 셋째 주 김포시 아파트 매매가격은 0.03% 오름세로 전환하며 반등했지만 이후 뚜렷한 추세 없이 하락과 상승을 보이며 혼조 양상을 띠었다. 특히 서울 편입론에 힘이 빠지면서 이달 1일 이후 셋째 주(15일 기준)까지 3주 연속 내림세를 보이고 있다.')

with tab4:
    st.header("\"얼마나 더 낮춰야 할까요\"…\'서울 편입\' 김포 집값")
    st.image('images/20240206_133329.png', caption='https://www.ajunews.com/view/20240121134429565')

    st.write('"아파트 내놓은지 두달이 다 되는데, 전화도 없네요. 가격을 얼마나 더 낮춰야 할까요."(김포 부동산 커뮤니티 중에서)')
    st.write('서울 편입에 대한 기대감이 들끓었던 경기도 김포시의 부동산 시장이 가라앉고 있다.')
    st.write(
        '매도자들은 메가시티에 대한 기대감으로 호가를 올리는 반면, 매수자들은 높아진 호가에 발길을 돌리고 있는 형편이다. 시장에서는 "정부의 괜한 기대감에 호가만 올라버린 상황"이라는 목소리도 나온다.')
    st.write(
        '10일 국토교통부 실거래가 공개시스템에 따르면 김포시 고촌읍 태리 \'캐슬앤파밀리에시티 1단지\'에서 지난 2일 전용 84㎡가 5억5500만원에 중개 거래됐다. 지난달 6억2000만원까지 올랐던 매매가가 다시 5억원대로 떨어지게 됐다.')

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be


show_pages(
    [
        Page("app.py", "Home", "🏠"),
        Page("pages/1_부동산 가격 추이.py", "부동산 가격 추이", ":books:"),
        Page("pages/2_부동산 거래량 추이.py", "부동산 거래량 추이", ":books:"),
        Page("pages/3_발표전후 총거래량 비교.py", "발표전후 총거래량 비교", ":books:"),
        Page("pages/4_메가서울 발표 후 김포 평균 가격 변화율.py", "메가서울 발표 후 김포 평균 가격 변화율", ":books:"),
        Page("pages/5_분석 결과 인사이트.py", "분석 결과 인사이트", ":books:"),
        Page("pages/6_건의사항.py", "건의사항", ":books:"),
    ]
)
