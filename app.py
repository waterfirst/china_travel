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

# 추가: 공용 와이파이 및 모바일 데이터 정보
st.markdown(
    "<h2 class='sub-header'>여행 중 인터넷 연결 옵션</h2>", unsafe_allow_html=True
)

internet_options = st.radio(
    "선호하는 인터넷 연결 방식",
    ["E-SIM 사용", "국제 로밍", "현지 유심 구매", "포켓 와이파이 렌탈"],
)

if internet_options == "E-SIM 사용":
    st.markdown(
        """
    <div class="info-box">
        <h3>E-SIM 추천</h3>
        <p>물리적 유심 교체 없이 디지털로 유심을 다운로드하는 방식입니다.</p>
        <p><strong>장점:</strong></p>
        <ul>
            <li>물리적 유심 교체 필요 없음</li>
            <li>출국 전 미리 설치 가능</li>
            <li>복수 통신사 선택 가능</li>
        </ul>
        <p><strong>권장 서비스:</strong></p>
        <ul>
            <li>Airalo: 중국 7일 5GB 약 $13 (약 17,000원)</li>
            <li>Ubigi: 중국 7일 3GB 약 $14 (약 18,000원)</li>
            <li>GigSky: 중국 7일 5GB 약 $24 (약 31,000원)</li>
        </ul>
        <p><strong>지원 기기:</strong> iPhone XS/XR 이상, 갤럭시 S20 이상, 픽셀 3 이상</p>
        <p><strong>사용 준비:</strong> 출국 전 E-SIM 앱 설치 및 데이터 플랜 구매 필요</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.warning(
        "참고: E-SIM이 설치된 후에도 중국에서 VPN 앱이 필요할 수 있습니다. 출국 전 VPN 앱을 설치하세요."
    )

elif internet_options == "국제 로밍":
    st.markdown(
        """
    <div class="info-box">
        <h3>통신사 로밍 서비스</h3>
        <p>한국 통신사의 로밍 서비스를 사용하는 방식입니다.</p>
        <p><strong>한국 통신사별 중국 로밍 요금:</strong></p>
        <ul>
            <li>SKT: 데이터 로밍 하루 11,000원 (무제한)</li>
            <li>KT: 데이터 로밍 하루 10,000원 (무제한)</li>
            <li>LG U+: 데이터 로밍 하루 9,900원 (무제한)</li>
        </ul>
        <p><strong>장점:</strong></p>
        <ul>
            <li>번호 유지로 국내 연락 유지 가능</li>
            <li>별도 설정 필요 없음</li>
            <li>도착 즉시 사용 가능</li>
        </ul>
        <p><strong>단점:</strong></p>
        <ul>
            <li>비용이 상대적으로 비쌈</li>
            <li>일부 지역에서 속도 제한 있을 수 있음</li>
        </ul>
        <p><strong>신청 방법:</strong> 통신사 앱 또는 고객센터(114)로 출국 전 신청</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

elif internet_options == "현지 유심 구매":
    st.markdown(
        """
    <div class="info-box">
        <h3>중국 현지 유심 구매</h3>
        <p>현지 공항이나 통신사 매장에서 유심을 구매하는 방식입니다.</p>
        <p><strong>주요 통신사:</strong></p>
        <ul>
            <li>China Mobile (차이나 모바일): 최대 통신사, 전국 커버리지 우수</li>
            <li>China Unicom (차이나 유니콤): 외국인 대상 서비스 많음, 영어 지원 상대적으로 나음</li>
            <li>China Telecom (차이나 텔레콤): 대도시 위주 커버리지</li>
        </ul>
        <p><strong>예상 비용:</strong></p>
        <ul>
            <li>7일권: 100-200위안 (약 19,000-38,000원), 데이터 3-8GB</li>
            <li>관광객용 특별 요금제: 100위안 (약 19,000원), 7일 4GB + 통화</li>
        </ul>
        <p><strong>구매 장소:</strong></p>
        <ul>
            <li>공항 도착장 통신사 부스</li>
            <li>지난 시내 주요 통신사 매장</li>
        </ul>
        <p><strong>필요 서류:</strong> 여권</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.info(
        "팁: 공항에서 구매하는 것이 언어 문제로 가장 편리합니다. 영어 가능 직원을 찾으세요."
    )

elif internet_options == "포켓 와이파이 렌탈":
    st.markdown(
        """
    <div class="info-box">
        <h3>포켓 와이파이 렌탈</h3>
        <p>출국 전 한국에서 포켓 와이파이를 렌탈하여 사용하는 방식입니다.</p>
        <p><strong>장점:</strong></p>
        <ul>
            <li>여러 기기 동시 연결 가능 (보통 3-5대)</li>
            <li>번호 변경 없이 데이터 사용 가능</li>
            <li>설정이 간편함</li>
        </ul>
        <p><strong>단점:</strong></p>
        <ul>
            <li>별도 기기를 휴대해야 함</li>
            <li>배터리 충전 필요</li>
            <li>분실 시 변상비용 발생</li>
        </ul>
        <p><strong>예상 비용:</strong></p>
        <ul>
            <li>일 7,000원-13,000원 (업체 및 데이터 용량에 따라 다름)</li>
            <li>3일 기준 약 21,000원-39,000원</li>
        </ul>
        <p><strong>인기 렌탈 서비스:</strong> 와이파이도시락, 글로벌와이파이, KT로밍, 에그인사이드 등</p>
        <p><strong>대여/반납:</strong> 인천공항 카운터 또는 편의점 택배</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# 태산 역사 및 지리 섹션
st.markdown("<h2 class='sub-header'>태산의 역사 및 지리</h2>", unsafe_allow_html=True)

history_geo_tab = st.tabs(["역사적 의미", "지리적 특징", "문화적 가치", "동산 정보"])

with history_geo_tab[0]:
    st.markdown("<h3>태산의 역사적 의미</h3>", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="info-box">
        <p>태산은 중국 역사에서 가장 신성한 산으로 여겨져 왔습니다.</p>
        
        <p><strong>고대 제사의 중심지:</strong> 태산은 약 3,000년 전부터 중국 황제들이 하늘에 제사를 지내는 '봉선(封禪)' 
        의식을 거행하던 장소였습니다. 진시황(기원전 219년), 한무제(기원전 110년), 당태종(637년) 등 수많은 황제들이 
        이곳에서 봉선 의식을 거행했습니다.</p>
        
        <p><strong>도교와 불교의 성지:</strong> 태산은 도교에서 '동악대제(東嶽大帝)'를 모시는 신성한 장소로, 
        많은 도교 사원이 건립되었습니다. 수/당 시대에는 불교 사원들도 들어서면서 종교적 다양성을 갖게 되었습니다.</p>
        
        <p><strong>문인들의 영감 원천:</strong> 이백, 두보, 왕안석, 수잔 등 중국의 유명 시인과 문인들이 태산을 방문하고
        이를 작품에 담았습니다. 공자도 "태산에 올라 천하가 작게 보인다(登泰山而小天下)"라는 유명한 말을 남겼습니다.</p>
        
        <p><strong>현대적 의미:</strong> 1987년 유네스코 세계문화자연유산으로 등재되었으며, 현재는 중국인들에게 있어
        국가적 자부심의 상징이자 중요한 순례지로 여겨집니다.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with history_geo_tab[1]:
    st.markdown("<h3>태산의 지리적 특징</h3>", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="info-box">
        <p><strong>위치:</strong> 산동성 태안시 북부에 위치, 좌표: 북위 36° 15′, 동경 117° 06′</p>
        
        <p><strong>지형:</strong> 태산은 주요 산봉우리 7개와 142개의 작은 봉우리로 이루어져 있으며, 
        주봉인 옥황정(玉皇頂)의 높이는 해발 1,545m입니다. 북쪽은 완만하고 남쪽은 가파른 비대칭 지형을 가지고 있습니다.</p>
        
        <p><strong>지질학적 특징:</strong> 약 27억-6억 년 전에 형성된 변성암과 퇴적암으로 이루어졌으며, 
        주로 화강암, 편마암, 석회암으로 구성되어 있습니다. 다양한 지질시대의 암석과 화석이 발견되어 
        지질학적으로도 중요한 가치를 지닙니다.</p>
        
        <p><strong>하천과 계곡:</strong> 태산에는 130여 개의 계곡과 72개의 폭포가 있으며, 
        주요 수계로는 태산 북쪽으로 흐르는 이하(沂河)와 남쪽으로 흐르는 소하(消河)가 있습니다.</p>
        
        <p><strong>기후:</strong> 온대 계절풍 기후로, 사계절이 뚜렷합니다. 연평균 기온은 12.8°C이며, 
        여름(6-8월)에는 평균 24°C, 겨울(12-2월)에는 평균 -2°C입니다. 연평균 강수량은 850mm로 주로 여름에 집중됩니다.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with history_geo_tab[2]:
    st.markdown("<h3>태산의 문화적 가치</h3>", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="info-box">
        <p><strong>유교, 도교, 불교의 융합:</strong> 태산에는 세 종교의 건축물과 유적이 공존합니다. 
        도교의 비천문(飛天門), 유교의 공자묘, 불교의 사가사(四家寺) 등이 대표적입니다.</p>
        
        <p><strong>비석과 석각:</strong> 태산에는 2,200여 개의 역사적 비석과 석각이 있으며, 
        이는 중국 서예 예술의 중요한 유산입니다. 특히 당나라 이사진(李斯眞)의 '금강경(金剛經)' 석각과 
        한나라 장추(張超)의 '치평석경(治平石經)'은 문화적 가치가 높습니다.</p>
        
        <p><strong>전통 건축물:</strong> 태산에는 22개의 사원, 97개의 사당, 819개의 석탑이 있으며, 
        특히 옥황정(玉皇頂)의 옥황묘, 비천문(飛天門), 남천문(南天門) 등은 전통 중국 건축의 아름다움을 보여줍니다.</p>
        
        <p><strong>문학과 예술:</strong> 태산은 수천 년간 시인, 화가, 서예가들에게 영감을 주었습니다. 
        당대 시인 이백의 "등태산(登泰山)" 시와 송대 화가 범성대(范成大)의 태산 그림은 중국 예술사에서 중요한 위치를 차지합니다.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with history_geo_tab[3]:
    st.markdown("<h3>동산 정보</h3>", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="info-box">
        <p><strong>등산 경로 안내:</strong></p>
        <ul>
            <li><strong>동쪽 코스 (홍문로, 紅門路):</strong> 
                <ul>
                    <li>가장 인기 있는 전통적인 경로</li>
                    <li>길이: 약 6.5km, 6,660개의 돌계단</li>
                    <li>소요 시간: 도보로 3-4시간</li>
                    <li>주요 명소: 홍문(紅門), 중천문(中天門), 18굽이길, 남천문(南天門)</li>
                </ul>
            </li>
            <li><strong>서쪽 코스 (천계로, 天階路):</strong>
                <ul>
                    <li>상대적으로 덜 붐비는 코스</li>
                    <li>길이: 약 9km</li>
                    <li>소요 시간: 도보로 4-5시간</li>
                    <li>특징: 동쪽 코스보다 경사가 완만하나 거리가 더 김</li>
                </ul>
            </li>
        </ul>
        
        <p><strong>방문 팁:</strong></p>
        <ul>
            <li>이른 아침에 방문하면 혼잡을 피할 수 있습니다</li>
            <li>날씨 변화에 대비해 여분의 옷을 준비하세요</li>
            <li>충분한 물과 간식을 준비하세요</li>
            <li>편안한 등산화 착용을 권장합니다</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )
