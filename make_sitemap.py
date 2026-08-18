import os
from datetime import datetime

try:
    # 1. 내 홈페이지 기본 주소 세팅
    base_url = "https://shinsegaetotal.github.io/shinsegaetotal/"

    # 2. 지도(sitemap.xml)의 머리말 작성
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    today = datetime.now().strftime("%Y-%m-%d")

    # 3. 폴더 안의 모든 html 파일을 찾아서 지도에 추가하기
    html_count = 0
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            html_count += 1
            url = base_url + filename
            
            # 대문(index.html)은 구글이 가장 먼저 읽도록 중요도(1.0)를 높게 설정
            priority = "1.0" if filename == "index.html" else "0.8"
            
            xml_content += '  <url>\n'
            xml_content += f'    <loc>{url}</loc>\n'
            xml_content += f'    <lastmod>{today}</lastmod>\n'
            xml_content += f'    <priority>{priority}</priority>\n'
            xml_content += '  </url>\n'

    # 4. 지도 마무리
    xml_content += '</urlset>'

    # 5. sitemap.xml 파일로 저장하기
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)

    print(f"✅ 대성공! 총 {html_count}개의 파일이 담긴 sitemap.xml 지도가 완성되었습니다!")

except Exception as e:
    print("❌ 앗! 에러가 발생했습니다! (아래 내용을 복사해서 알려주세요)")
    print(e)

# 창이 자동으로 꺼지는 것을 막는 마법 주문
input("\n[엔터 키]를 누르면 창이 닫힙니다...")