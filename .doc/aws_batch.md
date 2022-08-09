create : 2022/08/08 20:45:56
author : ichir0roie


# aws batch tutorial

<https://github.com/ryerkerk/aws-batch-python-tutorial>




# ecr_push



# 認証トークンを取得し、レジストリに対して Docker クライアントを認証します。
AWS CLI を使用する

aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin "account id".dkr.ecr.ap-northeast-1.amazonaws.com

注意: AWS CLI の使用中にエラーが発生した場合は、最新バージョンの AWS CLI と Docker がインストールされていることを確認してください。

# 以下のコマンドを使用して、Docker イメージを構築します。一から Docker ファイルを構築する方法については、「こちらをクリック 」の手順を参照してください。既にイメージが構築されている場合は、このステップをスキップします。

docker build -t todoist-manager .

構築が完了したら、このリポジトリにイメージをプッシュできるように、イメージにタグを付けます。

docker tag todoist-manager:latest "account id".dkr.ecr.ap-northeast-1.amazonaws.com/todoist-manager:latest

# 以下のコマンドを実行して、新しく作成した AWS リポジトリにこのイメージをプッシュします:

docker push "account id".dkr.ecr.ap-northeast-1.amazonaws.com/todoist-manager:latest

# docker commit todoist-manager todoist-manager















