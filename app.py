import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import matplotlib.pyplot as plt

# 앱 기본 설정
st.set_page_config(
    page_title="중국 여행 가이드",
    page_icon="🧳",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 스타일 정의 (CSS)
st.markdown(
    """
<style>
    .main-header {color: #1E3A8A; font-size: 2.5rem; font-weight: bold; text-align: center;}
    .sub-header {color: #1E3A8A; font-size: 1.8rem; margin-top: 2rem;}
    .info-box {background-color: #E6F3FF; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;}
    .warning-box {background-color: #FFF3CD; padding: 1rem; border-radius: 0.5rem;}
    .emergency-box {background-color: #F8D7DA; padding: 1rem; border-radius: 0.5rem; border: 1px solid #dc3545;}
    
</style>
""",
    unsafe_allow_html=True,
)

# 네비게이션
st.sidebar.markdown("## 중국 여행 가이드 🇨🇳")

app_mode = st.sidebar.selectbox(
    "메뉴 선택",
    ["홈", "일정표", "지도", "언어 도우미", "관광 정보", "긴급 연락처", "인터넷/통신"],
)


# 홈 화면
if app_mode == "홈":
    st.markdown(
        '<h1 class="main-header">중국 여행 가이드 🇨🇳</h1>', unsafe_allow_html=True
    )

    st.markdown(
        """
    <div class="warning-box">
        <strong>여행 알림:</strong> 내일(2025-03-03) 태산 방문 일정이 있습니다. 날씨 예보: 맑음, 기온: 8°C~15°C
    </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<h2 class="sub-header">여행 개요</h2>', unsafe_allow_html=True)
        st.markdown(
            """
        <div class="info-box">
            <p><strong>여행자:</strong> 박상욱</p>
            <p><strong>동행자:</strong> 최낙초</p>
            <p><strong>여행 기간:</strong> 2025년 3월 2일 ~ 3월 4일</p>
            <p><strong>여행 경로:</strong> 인천 → 지난 → 태산 → 곡부 → 지난 → 인천</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown('<h2 class="sub-header">오늘의 일정</h2>', unsafe_allow_html=True)
        st.markdown(
            """
        <div class="info-box">
            <p><strong>3월 2일(일)</strong></p>
            <p>22:05 - 22:55: 인천국제공항 → 지난국제공항 (산동항공 SC8004)</p>
            <p>23:30 - 24:00: 지난 레일웨이 호텔 체크인</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # 날씨 정보
        st.markdown('<h2 class="sub-header">현재 날씨</h2>', unsafe_allow_html=True)
        st.markdown(
            """
        <div class="info-box">
            <p><strong>지난:</strong> 맑음, 7°C</p>
            <p><strong>태산:</strong> 맑음, 5°C</p>
            <p><strong>곡부:</strong> 구름조금, 8°C</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# 일정표 화면
if app_mode == "일정표":
    st.markdown('<h1 class="main-header">여행 일정표</h1>', unsafe_allow_html=True)

    # 일정 선택 탭
    tabs = st.tabs(["3월 2일 (일)", "3월 3일 (월)", "3월 4일 (화)", "전체 일정"])

    # 3월 2일 일정
    with tabs[0]:
        st.markdown(
            '<h2 class="sub-header">3월 2일 - 인천 → 지난</h2>', unsafe_allow_html=True
        )
        st.markdown(
            """
        <div class="info-box">
            <p><strong>22:05 - 22:55</strong>: 인천국제공항 → 지난국제공항</p>
            <p><em>산동항공 SC8004, 보잉 737-800</em></p>
            <p><strong>23:30 - 24:00</strong>: 지난 레일웨이 호텔 체크인</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 3월 3일 일정
    with tabs[1]:
        st.markdown(
            '<h2 class="sub-header">3월 3일 - 지난 → 태산 → 곡부</h2>',
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        <div class="info-box">
            <p><strong>08:00 - 09:00</strong>: 호텔 조식</p>
            <p><strong>09:00 - 09:36</strong>: 지난역 → 태산역 (고속철도 C669)</p>
            <p><strong>10:00 - 11:00</strong>: 태산역 → 태산입구 (택시 10분)</p>
            <p><strong>11:00 - 12:00</strong>: 입장권 구매 및 케이블카 탑승</p>
            <p><strong>12:00 - 13:00</strong>: 점심 식사 (산 중턱 식당)</p>
            <p><strong>13:00 - 16:00</strong>: 태산 관광 (주요 명소 방문)</p>
            <p><strong>16:00 - 17:00</strong>: 하산 및 기념품 쇼핑</p>
            <p><strong>17:00 - 18:00</strong>: 태산입구 → 태안역 (택시 20분)</p>
            <p><strong>18:00 - 19:08</strong>: 태안역 → 곡부동부역 (고속철도 G159)</p>
            <p><strong>19:00 - 21:00</strong>: 석식 및 라방 호텔 체크인</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 3월 4일 일정
    with tabs[2]:
        st.markdown(
            '<h2 class="sub-header">3월 4일 - 곡부 → 지난 → 인천</h2>',
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        <div class="info-box">
            <p><strong>08:00 - 09:00</strong>: 호텔 조식</p>
            <p><strong>09:00 - 12:00</strong>: 공자묘 방문 (공자묘, 공자가묘, 공자림)</p>
            <p><strong>12:00 - 13:00</strong>: 중식 (현지 전통 음식)</p>
            <p><strong>13:00 - 15:40</strong>: 곡부동부역 → 지난서부역 (고속철도 G382)</p>
            <p><strong>16:00 - 18:00</strong>: 지난 시내 관광 (탑승수술, 취푸광장)</p>
            <p><strong>18:30 - 21:05</strong>: 지난국제공항 → 인천국제공항 (산동항공 SC8003)</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 전체 일정 요약
    with tabs[3]:
        st.markdown(
            '<h2 class="sub-header">전체 여행 일정 요약</h2>', unsafe_allow_html=True
        )

        # 간트 차트 스타일의 일정 시각화
        st.markdown(
            """
        <style>
        .gantt-chart {
            width: 100%;
            border-collapse: collapse;
        }
        .gantt-chart th, .gantt-chart td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        .gantt-header {
            background-color: #f2f2f2;
        }
        .gantt-cell {
            height: 30px;
        }
        .day1-cell { background-color: #ffcccc; }
        .day2-cell { background-color: #ccffcc; }
        .day3-cell { background-color: #ccccff; }
        .empty-cell { background-color: #ffffff; }
        </style>
        
        <table class="gantt-chart">
            <tr class="gantt-header">
                <th>시간</th>
                <th>3월 2일 (일)</th>
                <th>3월 3일 (월)</th>
                <th>3월 4일 (화)</th>
            </tr>
            <tr>
                <td>오전</td>
                <td class="empty-cell"></td>
                <td class="day2-cell">지난→태산 이동<br>태산 등산</td>
                <td class="day3-cell">공자묘 관광</td>
            </tr>
            <tr>
                <td>오후</td>
                <td class="empty-cell"></td>
                <td class="day2-cell">태산 관광<br>태산→곡부 이동</td>
                <td class="day3-cell">곡부→지난 이동<br>지난 시내 관광</td>
            </tr>
            <tr>
                <td>저녁</td>
                <td class="day1-cell">인천→지난 항공<br>호텔 체크인</td>
                <td class="day2-cell">곡부 석식<br>호텔 체크인</td>
                <td class="day3-cell">지난→인천 항공</td>
            </tr>
        </table>
        """,
            unsafe_allow_html=True,
        )

        # 일정 요약 정보
        st.markdown('<h3 class="sub-header">여행 통계</h3>', unsafe_allow_html=True)
        st.markdown(
            """
        <div class="info-box">
            <p><strong>총 이동 거리:</strong> 약 3,500 km</p>
            <p><strong>방문 도시:</strong> 3개 (지난, 태산, 곡부)</p>
            <p><strong>주요 교통 수단:</strong>
                <ul>
                    <li>항공: 2회</li>
                    <li>고속철도: 3회</li>
                    <li>택시: 4회</li>
                </ul>
            </p>
            <p><strong>숙박:</strong> 지난 레일웨이 호텔(1박), 곡부 라방 호텔(1박)</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # 지도로 경로 보기 버튼
        if st.button("🗺️ 지도로 경로 보기"):
            st.session_state.app_mode = "지도"
            st.experimental_rerun()

if app_mode == "지도":
    st.markdown('<h1 class="main-header">여행 지도</h1>', unsafe_allow_html=True)

    st.info(
        "참고: 중국에서는 구글 지도가 차단되어 있습니다. 이 앱에서는 오프라인 지도와 바이두 지도 링크를 제공합니다."
    )

    # 지도 선택
    map_option = st.radio(
        "지도 선택", ["오프라인 지도", "바이두 지도 링크", "여행 경로 미리보기"]
    )

    if map_option == "오프라인 지도":
        st.markdown("### 오프라인 지도")
        st.markdown("여행 전 지도를 다운로드하여 오프라인으로 사용할 수 있습니다.")

        # 오프라인 지도는 folium을 사용하여 미리 저장된 지도 표시
        offline_map = folium.Map(
            location=[36.6, 117.0], zoom_start=7, tiles="OpenStreetMap"
        )

        # 주요 여행지 표시
        locations = [
            {"name": "지난", "lat": 36.6512, "lon": 117.1201},
            {"name": "태산", "lat": 36.2325, "lon": 117.1106},
            {"name": "곡부", "lat": 35.6005, "lon": 116.9927},
        ]

        for loc in locations:
            folium.Marker(
                [loc["lat"], loc["lon"]],
                popup=loc["name"],
                icon=folium.Icon(color="red"),
            ).add_to(offline_map)

        folium_static(offline_map, width=800, height=500)

        st.download_button(
            label="오프라인 지도 다운로드",
            data="지도데이터",
            file_name="china_offline_map.mbtiles",
            mime="application/octet-stream",
        )

    elif map_option == "바이두 지도 링크":
        st.markdown("### 바이두 지도 링크")
        st.markdown("중국에서는 바이두 지도를 사용하실 수 있습니다.")

        baidu_links = {
            "지난": "https://map.baidu.com/search/济南/@13220371.56,4374801.71,12z",
            "태산": "https://map.baidu.com/search/泰山/@13165025.14,4330685.64,12z",
            "곡부": "https://map.baidu.com/search/曲阜/@13159019.73,4275943.25,12z",
        }

        for location, link in baidu_links.items():
            st.markdown(f"[{location} 바이두 지도 열기]({link})")

    elif map_option == "여행 경로 미리보기":
        # 여행 경로 미리보기 (오프라인 사용을 위해)
        st.markdown("### 여행 경로 미리보기")
        preview_map = folium.Map(location=[36.6, 117.0], zoom_start=7)

        route_points = [
            {"location": "인천국제공항", "lat": 37.4602, "lon": 126.4407},
            {"location": "지난국제공항", "lat": 36.8521, "lon": 117.2158},
            {"location": "지난 레일웨이 호텔", "lat": 36.6635, "lon": 117.0010},
            {"location": "태산", "lat": 36.2325, "lon": 117.1106},
            {"location": "곡부 (공자묘)", "lat": 35.6005, "lon": 116.9927},
            {"location": "지난국제공항", "lat": 36.8521, "lon": 117.2158},
            {"location": "인천국제공항", "lat": 37.4602, "lon": 126.4407},
        ]

        # 경로 그리기
        route_coords = [(point["lat"], point["lon"]) for point in route_points]
        folium.PolyLine(route_coords, color="blue", weight=3, opacity=0.7).add_to(
            preview_map
        )

        # 마커 추가
        for point in route_points:
            folium.Marker(
                [point["lat"], point["lon"]],
                popup=point["location"],
                icon=folium.Icon(color="green"),
            ).add_to(preview_map)

        folium_static(preview_map, width=800, height=500)

if app_mode == "언어 도우미":
    st.markdown('<h1 class="main-header">언어 도우미</h1>', unsafe_allow_html=True)

    # 언어 선택
    language_option = st.radio(
        "언어 선택", ["한국어 → 중국어", "한국어 → 영어", "중국어 → 한국어"]
    )

    # 카테고리 선택
    category = st.selectbox(
        "상황 선택", ["기본 회화", "호텔", "식당", "교통", "관광", "쇼핑", "긴급상황"]
    )

    # 필수 구문 - 한국어/중국어
    chinese_phrases = {
        "기본 회화": [
            {
                "한국어": "안녕하세요",
                "중국어": "你好 (Nǐ hǎo)",
                "영어": "Hello",
                "발음": "니 하오",
            },
            {
                "한국어": "감사합니다",
                "중국어": "谢谢 (Xiè xiè)",
                "영어": "Thank you",
                "발음": "셰이셰이",
            },
            {
                "한국어": "죄송합니다",
                "중국어": "对不起 (Duì bù qǐ)",
                "영어": "I'm sorry",
                "발음": "뛰이 부 치",
            },
            {
                "한국어": "네/아니오",
                "중국어": "是/不是 (Shì/Bú shì)",
                "영어": "Yes/No",
                "발음": "스/부 스",
            },
            {
                "한국어": "이해하지 못했습니다",
                "중국어": "我不明白 (Wǒ bù míng bái)",
                "영어": "I don't understand",
                "발음": "워 부 밍 바이",
            },
        ],
        "호텔": [
            {
                "한국어": "체크인하고 싶습니다",
                "중국어": "我想办理入住 (Wǒ xiǎng bàn lǐ rù zhù)",
                "영어": "I would like to check in",
                "발음": "워 샹 반 리 루 주",
            },
            {
                "한국어": "체크아웃하고 싶습니다",
                "중국어": "我想办理退房 (Wǒ xiǎng bàn lǐ tuì fáng)",
                "영어": "I would like to check out",
                "발음": "워 샹 반 리 투이 팡",
            },
            {
                "한국어": "방 키를 잃어버렸습니다",
                "중국어": "我丢了房卡 (Wǒ diū le fáng kǎ)",
                "영어": "I lost my room key",
                "발음": "워 디우 러 팡 카",
            },
            {
                "한국어": "와이파이 비밀번호가 뭔가요?",
                "중국어": "Wi-Fi密码是什么? (Wi-Fi mì mǎ shì shén me?)",
                "영어": "What's the Wi-Fi password?",
                "발음": "와이파이 미 마 스 션 머",
            },
            {
                "한국어": "수건을 더 주세요",
                "중국어": "请再给我一些毛巾 (Qǐng zài gěi wǒ yī xiē máo jīn)",
                "영어": "Please give me more towels",
                "발음": "칭 짜이 게이 워 이 시에 마오 진",
            },
        ],
        # 나머지 카테고리...
    }

    if category in chinese_phrases:
        st.markdown(
            f"<h2 class='sub-header'>{category} 필수 표현</h2>", unsafe_allow_html=True
        )

        # 표현 테이블 표시
        if language_option == "한국어 → 중국어":
            for phrase in chinese_phrases[category]:
                st.markdown(
                    f"""
                <div class="info-box">
                    <h3>{phrase['한국어']}</h3>
                    <p class="chinese-phrase">{phrase['중국어']}</p>
                    <p><strong>발음:</strong> {phrase['발음']}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

        elif language_option == "한국어 → 영어":
            for phrase in chinese_phrases[category]:
                st.markdown(
                    f"""
                <div class="info-box">
                    <h3>{phrase['한국어']}</h3>
                    <p class="chinese-phrase">{phrase['영어']}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

    # 실시간 번역 시뮬레이션
    st.markdown("<h2 class='sub-header'>실시간 번역</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        user_input = st.text_area("번역할 텍스트 입력", height=100)
        translate_button = st.button("번역하기")

    with col2:
        if translate_button and user_input:
            st.markdown("<h3>번역 결과</h3>", unsafe_allow_html=True)
            st.info(
                "이 기능은 인터넷 연결이 필요합니다. 오프라인 사용을 위해 필수 문구를 미리 저장해두세요."
            )
            st.markdown(
                f"<p class='chinese-phrase'>번역된 텍스트가 여기에 표시됩니다.</p>",
                unsafe_allow_html=True,
            )

    # 음성 번역에 대한 안내
    st.warning(
        "참고: 실제 앱에서 음성 인식 및 카메라 텍스트 인식 기능은 사전에 오프라인 모델을 다운로드해야 중국 내에서도 사용 가능합니다."
    )

if app_mode == "인터넷/통신":
    st.markdown(
        '<h1 class="main-header">중국 인터넷 및 통신 안내</h1>', unsafe_allow_html=True
    )

    st.markdown("<h2 class='sub-header'>중국 인터넷 환경</h2>", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="warning-box">
        <p><strong>중요 안내:</strong> 중국에서는 구글(지도, Gmail, 유튜브 포함), 페이스북, 인스타그램, 트위터, 왓츠앱 등 해외 서비스가 차단되어 있습니다.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # 통신 옵션 탭
    tabs = st.tabs(["로밍 서비스", "현지 유심", "E-SIM", "호텔 와이파이", "VPN 서비스"])

    with tabs[0]:
        st.markdown("### 로밍 서비스")
        st.markdown(
            """
        <div class="info-box">
            <p><strong>장점:</strong></p>
            <ul>
                <li>별도 설정 없이 바로 사용 가능</li>
                <li>번호 유지로 국내 연락 편리</li>
                <li>도착 즉시 사용 가능</li>
            </ul>
            <p><strong>단점:</strong></p>
            <ul>
                <li>상대적으로 높은 비용 (일 9,900원~15,000원)</li>
                <li>데이터 사용량 제한 있을 수 있음</li>
            </ul>
            <p><strong>통신사별 로밍 서비스:</strong></p>
            <ul>
                <li>SKT: T로밍 중국 데이터 무제한 요금제 (일 11,000원)</li>
                <li>KT: 중국 데이터로밍 요금제 (일 10,000원)</li>
                <li>LG U+: 중국 데이터로밍 요금제 (일 9,900원)</li>
            </ul>
            <p><strong>신청 방법:</strong> 통신사 앱 또는 고객센터 통해 출국 전 신청</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[1]:
        st.markdown("### 현지 유심")
        st.markdown(
            """
        <div class="info-box">
            <p><strong>장점:</strong></p>
            <ul>
                <li>저렴한 비용 (7일 사용 기준 약 2만원~3만원)</li>
                <li>넉넉한 데이터 제공량</li>
                <li>현지 통화 가능</li>
            </ul>
            <p><strong>단점:</strong></p>
            <ul>
                <li>번호가 바뀌어 국내 연락 불편</li>
                <li>공항 또는 현지 매장 방문 필요</li>
                <li>유심 교체 및 설정 필요</li>
            </ul>
            <p><strong>추천 중국 통신사:</strong></p>
            <ul>
                <li>China Mobile: 가장 넓은 커버리지</li>
                <li>China Unicom: 외국인에게 친화적인 서비스</li>
                <li>China Telecom: 대도시 커버리지 우수</li>
            </ul>
            <p><strong>구매 장소:</strong> 공항 도착장, 시내 통신사 매장</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[2]:
        st.markdown("### E-SIM")
        st.markdown(
            """
        <div class="info-box">
            <p><strong>장점:</strong></p>
            <ul>
                <li>물리적 유심 교체 필요 없음</li>
                <li>출국 전 미리 설정 가능</li>
                <li>필요한 기간만큼 유연하게 구매 가능</li>
            </ul>
            <p><strong>단점:</strong></p>
            <ul>
                <li>모든 스마트폰이 지원하지는 않음 (iPhone XS 이상, 갤럭시 S20 이상 등 최신 기기 필요)</li>
                <li>설정이 다소 복잡할 수 있음</li>
            </ul>
            <p><strong>추천 E-SIM 서비스:</strong></p>
            <ul>
                <li>Airalo: 중국 데이터 7일 20GB 약 2만원</li>
                <li>eSIMdb: 다양한 요금제 비교 가능</li>
            </ul>
            <p><strong>설치 방법:</strong> 서비스 웹사이트/앱에서 구매 후 QR코드 스캔으로 설치</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[3]:
        st.markdown("### 호텔 와이파이")
        st.markdown(
            """
        <div class="info-box">
            <p><strong>호텔 와이파이 상황:</strong></p>
            <ul>
                <li>대부분의 호텔에서 무료 와이파이 제공</li>
                <li>속도는 호텔마다 차이가 있음 (국제 체인 호텔이 일반적으로 더 빠름)</li>
                <li>로비보다 객실 신호가 약할 수 있음</li>
            </ul>
            <p><strong>여행지별 호텔 와이파이 정보:</strong></p>
            <ul>
                <li>지난 레일웨이 호텔: 무료 와이파이 제공 (평균 속도: 20Mbps)</li>
                <li>라방 호텔(쿠푸): 무료 와이파이 제공 (평균 속도: 15Mbps)</li>
            </ul>
            <p><strong>주의사항:</strong> 보안에 취약할 수 있으니 중요한 금융거래는 피하세요</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[4]:
        st.markdown("### VPN 서비스")
        st.markdown(
            """
        <div class="warning-box">
            <p><strong>주의:</strong> 중국에서는 대부분의 VPN 서비스가 차단되어 있으며, VPN 사용이 법적으로 제한될 수 있습니다. 다음 정보는 참고용으로만 제공됩니다.</p>
        </div>
        <div class="info-box">
            <p><strong>출국 전 준비사항:</strong></p>
            <ul>
                <li>중국 방문 전 VPN 앱 설치 필요 (현지에서는 앱스토어 접근이 제한될 수 있음)</li>
                <li>여러 VPN 옵션을 준비해두는 것이 좋음</li>
            </ul>
            <p><strong>VPN 사용 주의사항:</strong></p>
            <ul>
                <li>호텔이나 공공장소에서 사용시 주의</li>
                <li>안정적인 연결을 위해 홍콩/싱가포르/한국 서버 선택 권장</li>
                <li>배터리 소모가 증가할 수 있으니 보조배터리 필요</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 오프라인 사용 팁
    st.markdown("<h2 class='sub-header'>오프라인 사용 팁</h2>", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="info-box">
        <p><strong>출국 전 준비:</strong></p>
        <ul>
            <li>구글맵 지도 오프라인 저장 (대체: 바이두 맵 앱 설치)</li>
            <li>필요한 정보를 PDF나 메모로 저장</li>
            <li>주요 목적지 주소를 중국어로 미리 저장</li>
            <li>번역 앱 오프라인 패키지 다운로드</li>
            <li>음악, 영화 등 엔터테인먼트 콘텐츠 다운로드</li>
       </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

if app_mode == "관광 정보":
    st.markdown('<h1 class="main-header">관광 정보</h1>', unsafe_allow_html=True)

    # 관광지 선택
    attraction = st.selectbox(
        "관광지 선택", ["태산(泰山)", "곡부(공자묘)", "지난 시내"]
    )

    if attraction == "태산(泰山)":
        st.markdown(
            "<h2 class='sub-header'>태산 (泰山, Mount Tai)</h2>", unsafe_allow_html=True
        )

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(
                """
            <div class="info-box">
                <p><strong>소개:</strong> 태산은 중국 산동성 태안시에 위치한 산으로, 중국 오악(五嶽) 중 동악(東嶽)으로 불립니다. 해발 1,545m로 '천하제일산(天下第一山)'이라 불리며, 1987년 유네스코 세계문화 및 자연유산으로 등재되었습니다.</p>
                
                <p><strong>역사적 의미:</strong> 태산은 중국 문화에서 3,000년 이상의 역사를 가진 성산(聖山)으로, 고대부터 중국 황제들이 천제(天帝)에게 제사를 지내던 곳입니다. 진시황, 한무제, 당태종을 포함한 많은 황제들이 태산에 올라 봉선(封禪) 의식을 거행했습니다.</p>
                
                <p><strong>방문 정보:</strong></p>
                <ul>
                    <li>개장 시간: 하절기(4월~10월) 05:30~22:00, 동절기(11월~3월) 07:00~19:00</li>
                    <li>입장료: 125위안 (약 24,000원)</li>
                    <li>케이블카(편도): 100위안 (약 19,000원)</li>
                    <li>소요 시간: 하루 종일 관광 권장 (최소 5-6시간)</li>
                </ul>
                
                <p><strong>주요 명소:</strong></p>
                <ul>
                    <li>천계(天界): 태산 정상부 지역</li>
                    <li>옥황정(玉皇頂): 태산의 정상, 해발 1,545m</li>
                    <li>비천문(飛天門): '하늘을 나는 문'이라는 뜻의 관문</li>
                    <li>남천문(南天門): 정상 지역으로 들어가는 주요 입구</li>
                    <li>중천문(中天門): 등산로 중간의 휴식처</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

            # 방문 팁
            st.markdown("<h3>방문 팁</h3>", unsafe_allow_html=True)
            st.markdown(
                """
            <div class="info-box">
                <ul>
                    <li>이른 아침에 방문하면 혼잡을 피할 수 있습니다.</li>
                    <li>날씨 변화에 대비해 여분의 옷을 준비하세요.</li>
                    <li>충분한 물과 간식을 준비하세요.</li>
                    <li>케이블카는 오후에 줄이 길어질 수 있습니다.</li>
                    <li>등산로에는 많은 계단이 있으니 편안한 신발을 착용하세요.</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            # 태산 오프라인 지도
            taishan_map = folium.Map(location=[36.2325, 117.1106], zoom_start=13)
            folium.Marker(
                [36.2325, 117.1106],
                popup="태산 정상 (옥황정)",
                icon=folium.Icon(color="red"),
            ).add_to(taishan_map)

            # 주요 지점 표시
            taishan_points = [
                {"name": "남천문", "lat": 36.2561, "lon": 117.1015},
                {"name": "중천문", "lat": 36.2632, "lon": 117.0970},
                {"name": "홍문(입구)", "lat": 36.2750, "lon": 117.1342},
            ]

            for point in taishan_points:
                folium.Marker(
                    [point["lat"], point["lon"]],
                    popup=point["name"],
                    icon=folium.Icon(color="blue"),
                ).add_to(taishan_map)

            folium_static(taishan_map, height=400)

            # 영어 정보
            st.markdown("<h3>English Information</h3>", unsafe_allow_html=True)
            st.markdown(
                """
            <div class="info-box">
                <p><strong>Mount Tai</strong> (Tài Shān) is one of China's Five Great Mountains, located in Shandong Province.</p>
                <p><strong>Hours:</strong> Summer (Apr-Oct) 5:30AM-10PM; Winter (Nov-Mar) 7AM-7PM</p>
                <p><strong>Entrance Fee:</strong> 125 Yuan</p>
                <p><strong>Cable Car:</strong> 100 Yuan (one way)</p>
                <p><strong>Essential English phrases:</strong></p>
                <ul>
                    <li>"Where is the entrance?" - "Where is the entrance to Mount Tai?"</li>
                    <li>"How much is the ticket?" - "How much is the entrance ticket?"</li>
                    <li>"Where is the cable car?" - "Where can I find the cable car station?"</li>
                    <li>"How long does it take to climb?" - "How long does it take to hike to the summit?"</li>
                    <li>"Is this the way to the top?" - "Is this the correct path to the summit?"</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

if app_mode == "긴급 연락처":
    st.markdown('<h1 class="main-header">긴급 연락처</h1>', unsafe_allow_html=True)

    # 긴급 상황별 탭
    tabs = st.tabs(["대사관/영사관", "긴급전화", "병원", "호텔", "비상 대처법"])

    with tabs[0]:
        st.markdown(
            "<h2 class='sub-header'>한국 대사관/영사관</h2>", unsafe_allow_html=True
        )

        embassy_data = [
            {
                "이름": "주중국대한민국대사관",
                "위치": "베이징",
                "전화": "+86-10-8531-0700",
                "긴급전화": "+86-186-1173-0089 (24시간)",
                "주소": "No.20, DongfangDonglu, Chaoyang District, Beijing, China",
                "영어주소": "No.20, DongfangDonglu, Chaoyang District, Beijing, China",
                "업무시간": "월-금 09:00-17:30 (점심시간: 12:00-13:30)",
                "거리": "지난에서 약 400km",
            },
            {
                "이름": "주칭다오총영사관",
                "위치": "칭다오",
                "전화": "+86-532-8897-6001",
                "긴급전화": "+86-186-6185-7713 (24시간)",
                "주소": "No.88, Wannianhua Lu, Shinan District, Qingdao, China",
                "영어주소": "No.88, Wannianhua Lu, Shinan District, Qingdao, China",
                "업무시간": "월-금 09:00-17:30 (점심시간: 12:00-13:30)",
                "거리": "지난에서 약 370km",
            },
        ]

        for embassy in embassy_data:
            st.markdown(
                f"""
            <div class="emergency-box">
                <h3>{embassy['이름']} ({embassy['위치']})</h3>
                <p><strong>대표전화:</strong> {embassy['전화']}</p>
                <p><strong>긴급전화:</strong> {embassy['긴급전화']}</p>
                <p><strong>주소(중):</strong> {embassy['주소']}</p>
                <p><strong>주소(영):</strong> {embassy['영어주소']}</p>
                <p><strong>업무시간:</strong> {embassy['업무시간']}</p>
                <p><strong>현재 위치에서:</strong> {embassy['거리']}</p>
                <button>지도에서 보기</button>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with tabs[1]:
        st.markdown("<h2 class='sub-header'>중국 긴급전화</h2>", unsafe_allow_html=True)

        emergency_calls = [
            {"서비스": "경찰(Police)", "번호": "110", "참고": "영어 서비스 제한적"},
            {"서비스": "화재/소방(Fire)", "번호": "119", "참고": "영어 서비스 제한적"},
            {
                "서비스": "구급차(Ambulance)",
                "번호": "120",
                "참고": "영어 서비스 제한적",
            },
            {
                "서비스": "교통사고(Traffic Police)",
                "번호": "122",
                "참고": "영어 서비스 제한적",
            },
            {
                "서비스": "관광경찰(Tourism Police)",
                "번호": "12301",
                "참고": "관광지 부근에서만 서비스",
            },
        ]

        st.markdown(
            """
        <div class="emergency-box">
            <h3>전화 사용 팁</h3>
            <p>• 중국에서 긴급전화는 무료이며 SIM 카드 없이도 사용 가능합니다.</p>
            <p>• 영어 서비스가 제한적이므로 간단한 중국어 표현을 준비하세요.</p>
            <p>• 가능하면 호텔 직원이나 현지인의 도움을 요청하세요.</p>
            <p>• 현재 위치를 중국어로 저장해두면 도움이 됩니다.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        for call in emergency_calls:
            st.markdown(
                f"""
            <div class="info-box">
                <h3>{call['서비스']}</h3>
                <p style="font-size: 24px; font-weight: bold;">{call['번호']}</p>
                <p><strong>참고:</strong> {call['참고']}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
    # 병원 탭 내용
with tabs[2]:
    st.markdown("<h2 class='sub-header'>주요 병원 정보</h2>", unsafe_allow_html=True)

    hospitals = [
        {
            "이름": "지난시 제일인민병원",
            "위치": "지난",
            "전화": "+86-531-8798-7777",
            "주소": "16 Jingshilu, Huaiyin District, Jinan",
            "영어 가능": "일부 의사/간호사",
            "24시간 응급실": "가능",
            "특징": "국제 진료부 있음",
            "거리": "지난 레일웨이 호텔에서 약 3km",
        },
        {
            "이름": "태안시 중심병원",
            "위치": "태안",
            "전화": "+86-538-6297-999",
            "주소": "29 Longtan Road, Taishan District, Tai'an",
            "영어 가능": "제한적",
            "24시간 응급실": "가능",
            "특징": "태산 관광객 응급처치 경험 많음",
            "거리": "태산 입구에서 약 5km",
        },
        {
            "이름": "곡부시 인민병원",
            "위치": "곡부",
            "전화": "+86-537-4491-120",
            "주소": "59 Chunqiu Middle Road, Qufu",
            "영어 가능": "매우 제한적",
            "24시간 응급실": "가능",
            "특징": "기본 응급처치 가능",
            "거리": "라방 호텔에서 약 2km",
        },
    ]

    for hospital in hospitals:
        st.markdown(
            f"""
        <div class="emergency-box">
            <h3>{hospital['이름']} ({hospital['위치']})</h3>
            <p><strong>전화:</strong> {hospital['전화']}</p>
            <p><strong>주소:</strong> {hospital['주소']}</p>
            <p><strong>영어 의사소통:</strong> {hospital['영어 가능']}</p>
            <p><strong>24시간 응급실:</strong> {hospital['24시간 응급실']}</p>
            <p><strong>특징:</strong> {hospital['특징']}</p>
            <p><strong>위치:</strong> {hospital['거리']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 기본 의학 용어
    st.markdown("<h3>의료 긴급상황 필수 표현</h3>", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="info-box">
        <table width="100%">
            <tr>
                <th>한국어</th>
                <th>중국어</th>
                <th>영어</th>
            </tr>
            <tr>
                <td>응급실이 어디 있나요?</td>
                <td>急诊室在哪里? (Jí zhěn shì zài nǎlǐ?)</td>
                <td>Where is the emergency room?</td>
            </tr>
            <tr>
                <td>의사를 불러주세요</td>
                <td>请叫医生 (Qǐng jiào yīshēng)</td>
                <td>Please call a doctor</td>
            </tr>
            <tr>
                <td>두통이 있어요</td>
                <td>我头疼 (Wǒ tóu téng)</td>
                <td>I have a headache</td>
            </tr>
            <tr>
                <td>복통이 있어요</td>
                <td>我肚子疼 (Wǒ dùzi téng)</td>
                <td>I have a stomachache</td>
            </tr>
            <tr>
                <td>열이 있어요</td>
                <td>我发烧了 (Wǒ fāshāo le)</td>
                <td>I have a fever</td>
            </tr>
            <tr>
                <td>알레르기가 있어요</td>
                <td>我有过敏 (Wǒ yǒu guòmǐn)</td>
                <td>I have allergies</td>
            </tr>
        </table>
    </div>
    """,
        unsafe_allow_html=True,
    )

# 호텔 탭 내용
with tabs[3]:
    st.markdown("<h2 class='sub-header'>호텔 정보</h2>", unsafe_allow_html=True)

    hotels = [
        {
            "이름": "지난 레일웨이 호텔",
            "주소": "No.19 Chezhan Street, Jinan, China",
            "전화": "+86-531-8288-9999",
            "체크인": "14:00 이후",
            "체크아웃": "12:00 이전",
            "와이파이": "무료 (로비 및 객실)",
            "조식": "1층 레스토랑 06:30-10:00",
            "편의시설": "헬스장, 비즈니스 센터, 세탁 서비스",
            "프론트 데스크": "24시간 운영, 일부 직원 영어 가능",
            "예약번호": "JN8765432",
        },
        {
            "이름": "라방 호텔 (곡부)",
            "주소": "No.29 Jingxuan East Road, Qufu, China",
            "전화": "+86-537-505-8888",
            "체크인": "14:00 이후",
            "체크아웃": "12:00 이전",
            "와이파이": "무료 (로비 및 객실)",
            "조식": "2층 레스토랑 06:30-09:30",
            "편의시설": "스파, 실내 수영장, 기념품점",
            "프론트 데스크": "06:00-24:00 운영, 제한적 영어 가능",
            "예약번호": "QF4289651",
        },
    ]

    for hotel in hotels:
        st.markdown(
            f"""
        <div class="info-box">
            <h3>{hotel['이름']}</h3>
            <p><strong>주소:</strong> {hotel['주소']}</p>
            <p><strong>전화:</strong> {hotel['전화']}</p>
            <p><strong>체크인/체크아웃:</strong> {hotel['체크인']} / {hotel['체크아웃']}</p>
            <p><strong>와이파이:</strong> {hotel['와이파이']}</p>
            <p><strong>조식:</strong> {hotel['조식']}</p>
            <p><strong>편의시설:</strong> {hotel['편의시설']}</p>
            <p><strong>프론트 데스크:</strong> {hotel['프론트 데스크']}</p>
            <p><strong>예약번호:</strong> {hotel['예약번호']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 호텔 이용 시 유용한 표현
    st.markdown("<h3>호텔 관련 유용한 표현</h3>", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="info-box">
        <ul>
            <li><strong>수건을 더 주세요:</strong> 请再给我一些毛巾 (Qǐng zài gěi wǒ yīxiē máojīn)</li>
            <li><strong>방 청소해 주세요:</strong> 请打扫我的房间 (Qǐng dǎsǎo wǒ de fángjiān)</li>
            <li><strong>오늘 청소는 필요 없습니다:</strong> 今天不需要打扫 (Jīntiān bù xūyào dǎsǎo)</li>
            <li><strong>카드키가 작동하지 않습니다:</strong> 房卡不能用了 (Fáng kǎ bùnéng yòng le)</li>
            <li><strong>세탁 서비스 이용하고 싶습니다:</strong> 我想使用洗衣服务 (Wǒ xiǎng shǐyòng xǐyī fúwù)</li>
            <li><strong>조식은 몇 시까지인가요?:</strong> 早餐到几点? (Zǎocān dào jǐ diǎn?)</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

# 비상 대처법 탭 내용
with tabs[4]:
    st.markdown("<h2 class='sub-header'>비상 상황 대처법</h2>", unsafe_allow_html=True)

    emergency_scenarios = [
        {
            "상황": "여권 분실",
            "대처법": [
                "즉시 가까운 파출소(警察局)에 분실 신고하고 분실증명서(报失证明) 발급받기",
                "주중한국대사관/영사관에 연락하여 여행증명서(여권 임시 대체 문서) 발급 신청",
                "필요 서류: 신분증 사본, 여권 사본(가능한 경우), 증명사진 2장",
                "각 지역 영사관 긴급 연락처로 연락하기",
                "항공사에 사전 연락하여 여행증명서로 귀국 가능한지 확인",
            ],
        },
        {
            "상황": "도난/강도 피해",
            "대처법": [
                "즉시 110에 전화하여 경찰 신고",
                "가능하면 주변 CCTV 위치 확인하기",
                "신용카드 분실 시 즉시 카드사에 연락하여 분실 신고",
                "현지 경찰서에서 도난 신고서(报案证明) 발급받기",
                "여행자 보험 가입자는 보험사에 연락하여 보상 절차 확인",
                "대사관/영사관에 연락하여 도움 요청",
            ],
        },
        {
            "상황": "질병/부상",
            "대처법": [
                "가벼운 증상: 가까운 약국(药店) 방문하여 기본 약품 구매",
                "중증 증상: 120에 전화하여 구급차 요청 또는 택시로 병원 응급실 방문",
                "호텔 직원에게 가까운 병원 추천 요청",
                "여행자 보험 가입자는 병원 방문 전 보험사에 연락하여 적용 여부 확인",
                "대형 병원에서는 여권과 현금/카드 지참 필수",
                "처방약은 반드시 영수증과 처방전 보관 (보험 청구용)",
            ],
        },
        {
            "상황": "자연재해/악천후",
            "대처법": [
                "현지 기상 정보 및 재난 경보 지속적 확인",
                "호텔 직원이나 현지인의 안내에 따라 대피",
                "대피소(避难所) 위치 파악하기",
                "대사관/영사관 공지사항 확인 및 연락",
                "이동 제한 시 충분한 식수와 비상식품 확보",
                "항공/철도 일정 변경 필요시 즉시 예약 변경 시도",
            ],
        },
    ]

    for scenario in emergency_scenarios:
        st.markdown(
            f"""
        <div class="emergency-box">
            <h3>🚨 {scenario['상황']} 시 대처법</h3>
            <ol>
        """,
            unsafe_allow_html=True,
        )

        for step in scenario["대처법"]:
            st.markdown(f"<li>{step}</li>", unsafe_allow_html=True)

        st.markdown(
            """
            </ol>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 비상 연락처 카드
    st.markdown("<h3>비상 연락처 카드 (인쇄 권장)</h3>", unsafe_allow_html=True)
    st.markdown(
        """
    <div style="border: 2px solid #dc3545; padding: 15px; border-radius: 5px; background-color: #fff;">
        <h4 style="text-align: center; color: #dc3545;">비상 연락처 카드</h4>
        <hr>
        <p><strong>긴급전화:</strong> 110 (경찰), 120 (구급차), 119 (소방)</p>
        <p><strong>한국 대사관 긴급전화:</strong> +86-186-1173-0089</p>
        <p><strong>여행자 이름:</strong> 박상욱 / PARK SANG WOOK</p>
        <p><strong>여권번호:</strong> M12345678</p>
        <p><strong>혈액형:</strong> _______</p>
        <p><strong>알레르기:</strong> _______</p>
        <p><strong>한국 긴급연락처:</strong> _______</p>
        <p><strong>여행자보험:</strong> _______ (번호: _______)</p>
        <p><strong>숙소:</strong> 지난 레일웨이 호텔(+86-531-8288-9999)<br>
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;라방 호텔(+86-537-505-8888)</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # 다운로드 버튼 (실제로는 작동하지 않음, 구현 필요)
    st.download_button(
        label="비상 연락처 카드 PDF 다운로드",
        data="비상연락처카드_데이터",
        file_name="emergency_card.pdf",
        mime="application/pdf",
    )
