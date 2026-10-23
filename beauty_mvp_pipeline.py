# 기존 코드에서 headless=False 를 True로 변경 (깃허브 리눅스 서버 호환용)
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-infobars",
                "--disable-dev-shm-usage" # 서버 메모리 부족 방지 옵션 추가
            ]
        )