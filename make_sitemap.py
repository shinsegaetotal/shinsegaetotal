import os
from datetime import datetime

# 1. 🎯 대표님의 깃허브 홈페이지 기본 주소
BASE_URL = "https://shinsegaetotal.github.io"

# 2. 🌟 13,890개의 파일이 실제로 들어있는 '진짜 폴더 경로' (사진 속 주소 반영)
# 대표님 컴퓨터의 GitHub 폴더 경로를 직접 지정해 줍니다!
TARGET_DIR = r"C:\Users\kisan\Documents\GitHub\shinsegaetotal"

def create_sitemap():
    print(f"🚀 '{TARGET_DIR}' 폴더 안의 13,890개 파일 스캔을 시작합니다!\n")
    
    # 해당 폴더가 진짜 있는지 확인하는 안전장치
    if not os.path.exists(TARGET_DIR):
        print(f"❌ 에러: 폴더를 찾을 수 없습니다! ({TARGET_DIR}) 경로를 다시 확인해주세요.")
        return

    # 오늘 날짜 구하기 (sitemap에 들어갈 최신 날짜)
    today = datetime.now().strftime("%Y-%m-%d")

    # xml 형식의 사이트맵 머리말 작성
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    # 메인 폴더(TARGET_DIR) 안의 모든 .html 파일을 찾아서 주소록에 추가!
    count = 0
    for file_name in os.listdir(TARGET_DIR):
        if file_name.endswith(".html"):
            file_url = f"{BASE_URL}/{file_name}"
            # index.html (대문)은 우선순위 1.0, 나머지는 0.8 부여
            priority = "1.0" if file_name == "index.html" else "0.8"
            
            xml_content += f"  <url>\n    <loc>{file_url}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>{priority}</priority>\n  </url>\n"
            count += 1

    # 사이트맵 꼬리말 닫기
    xml_content += '</urlset>'

    # 3. 완성된 초대형 지도를 'TARGET_DIR' 안에 sitemap.xml 이란 이름으로 저장!
    output_file = os.path.join(TARGET_DIR, "sitemap.xml")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(xml_content)

    print(f"🎉 대성공! 총 {count}개의 주소가 완벽하게 담긴 'sitemap.xml' 파일이 깃허브 폴더에 생성되었습니다!")
    print("이제 깃허브 데스크탑을 켜서 [Commit] -> [Push] 해주시면 진짜로 모든 세팅 끝입니다!!")

if __name__ == "__main__":
    create_sitemap()