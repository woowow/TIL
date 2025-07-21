import requests
import subprocess
from datetime import datetime, timedelta, timezone
from dateutil import parser

# GitLab 설정
GITLAB_API = "https://lab.ssafy.com/api/v4"
USERNAME = ""  # 본인 GitLab username
PRIVATE_TOKEN = ""

# 시간 계산: 24시간 이내
since = (datetime.utcnow() - timedelta(days=1)).isoformat()

# 프로젝트 목록 가져오기
response = requests.get(
    f"{GITLAB_API}/users/{USERNAME}/projects",
    headers={"PRIVATE-TOKEN": PRIVATE_TOKEN},
    params={"visibility": "private", "order_by": "last_activity_at", "sort": "desc", "per_page": 100}
)

projects = response.json()

# 업데이트된 프로젝트 중 24시간 이내만 필터링
for project in projects:
    last_activity = project['last_activity_at']
#    last_activity_dt = datetime.strptime(last_activity, "%Y-%m-%dT%H:%M:%S.%fZ")
    last_activity_dt = parser.isoparse(last_activity)
    
    if last_activity_dt >= datetime.utcnow().replace(tzinfo=timezone.utc) - timedelta(days=1):
        print(f"클론할 프로젝트: {project['name']} / 업데이트 시간: {last_activity_dt}")
        clone_url = project['http_url_to_repo']
        
        subprocess.run(["git", "clone", clone_url])