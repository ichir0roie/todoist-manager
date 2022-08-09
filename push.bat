echo %ACCOUNT_ID%

aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin %ACCOUNT_ID%.dkr.ecr.ap-northeast-1.amazonaws.com
docker build -t todoist-manager .
docker tag todoist-manager:latest %ACCOUNT_ID%.dkr.ecr.ap-northeast-1.amazonaws.com/todoist-manager:latest
docker push %ACCOUNT_ID%.dkr.ecr.ap-northeast-1.amazonaws.com/todoist-manager:latest
