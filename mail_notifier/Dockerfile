# ベースイメージ：Python 3.11 を使う
FROM python:3.11-slim

# 作業ディレクトリ作成
WORKDIR /app

# プロジェクトの中身をコピー
COPY . /app

# 依存パッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# cron をインストール
RUN apt-get update && apt-get install -y cron

# cronジョブの設定をコピーして有効化
COPY crontab.txt /etc/cron.d/mail-cron
RUN chmod 0644 /etc/cron.d/mail-cron && \
    crontab /etc/cron.d/mail-cron

# 起動スクリプトをコピーして実行権限を与える
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# 環境変数をロードして cron を起動する
ENTRYPOINT ["/docker-entrypoint.sh"]

