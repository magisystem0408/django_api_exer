## cors-headerを使えるようにするために

1. middlewareに以下を追加する
    - 'corsheaders.middleware.CorsMiddleware',
1. ホワイトリストを作成する
   - CORS_ORIGIN_WHITELIST =["http://localhost:3000"]
   
   