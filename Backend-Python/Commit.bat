@ECHO OFF
copy /y D:\Study\untitled2\coronadata.json D:\Study\untitled2\corona-json
d:
cd D:\Study\untitled2\corona-json
git add .
git commit -m "updated"
git push origin
