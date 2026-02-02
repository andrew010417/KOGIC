#2월 2일 git + vs KOGIC 호크서버 /BiO/Access/jaehyung/myfirstjob/4kdata와 동기화 완료

1. VS code에서 github 업데이트
cd /BiO/Access/jaehyung/myfirstjob/4kdata  # Git 레포 안으로 이동
1. git status       # 변경사항 확인
2. git add -A       # 수정된 파일 staging (추적 대상만)
3. git commit -m "Modify scripts/XYZ"  # 커밋
4. git push origin main               # GitHub에 반영


2. Github에서 Vs code 업데이트
1. Github에서 수정 cd /BiO/Access/jaehyung/myfirstjob/4kdata
2. git pull origin main   # GitHub 변경사항을 로컬로 가져오기
