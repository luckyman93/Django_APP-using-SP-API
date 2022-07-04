# -*- coding: utf-8 -*-
import os,sys,time
import hashlib
import hmac
import urllib.parse
import requests
import json
from time import gmtime, strftime
from datetime import datetime

### =====================================================================================
### Access Token 取得関数
### =====================================================================================

def SPAPI_Get_Token(SPAPI_LWA_Client_ID, SPAPI_LWA_Client_PW, SPAPI_Refresh_Token, SPAPI_Access_Token_Endpoint):
    print("Func : SPAPI_Get_Token")
    
    ### === 引数の説明 ================================================
    ### SPAPI_LWA_Client_ID           : LWA 認証情報 クライアントID
    ### SPAPI_LWA_Client_PW           : LWA 認証情報 クライアント機密情報
    ### SPAPI_Refresh_Token           : リフレッシュトークン
    ### SPAPI_Access_Token_Endpoint   : LWA認証サーバURL
    ### ==============================================================

    ### 認証情報の作成
    auth = (SPAPI_LWA_Client_ID, SPAPI_LWA_Client_PW)

    ### POSTパラメータ作成
    params = {
        "grant_type":"refresh_token",
        "refresh_token":SPAPI_Refresh_Token
    }

    ### POSTリクエスト処理の実行
    SPAPI_Response = requests.post(url=SPAPI_Access_Token_Endpoint, auth=auth, data=params)

    ### レスポンスをDict型へデコード
    SPAPI_Response_dict = SPAPI_Response.json()


    ### POST後のHTTPレスポンスコードとレスポンス内容の表示（確認用）
    #print(SPAPI_Response, flush=True)
    #print(json.dumps(SPAPI_Response_dict, indent=2, ensure_ascii=False), flush=True)

    ### 値の取得
    resp_access_token = SPAPI_Response_dict['access_token']
    resp_refresh_token = SPAPI_Response_dict['refresh_token']
    resp_token_type = SPAPI_Response_dict['token_type']
    resp_expires_in = SPAPI_Response_dict['expires_in']

    return resp_access_token, resp_refresh_token, resp_token_type, resp_expires_in

### =====================================================================================
### SP－API「getCatalogItem」にアクセスし、指定したASINコードの商品情報を取得する関数
### =====================================================================================

def SPAPI_GetCatalogItemsForASIN(Asin_Code, SPAPI_Access_Token, SPAPI_IAM_User_Access_Key, SPAPI_IAM_User_Secret_Key, SPAPI_Method, SPAPI_Service, SPAPI_Domain, SPAPI_MarketplaceId, SPAPI_Region, SPAPI_Endpoint, SPAPI_SignatureMethod, SPAPI_UserAgent):
    print('Function : SPAPI_GetCatalogItemsForASIN')

    ### === 引数の説明 ============================
    ### Asin_Code                   : リクエストするASINコード
    ### SPAPI_Access_Token          : リフレッシュトークンから取得したアクセストークン
    ### SPAPI_IAM_User_Access_Key   : IAMユーザのアクセスキー
    ### SPAPI_IAM_User_Secret_Key   : IAMユーザのシークレットキー
    ### SPAPI_Method                : HTTPアクセスプロトコル（GET）
    ### SPAPI_Service               : IAMユーザのアクセス権限設定（execute-api）
    ### SPAPI_Domain                : SP-APIエンドポイントのURLのドメイン部分（sellingpartnerapi-fe.amazon.com）
    ### SPAPI_MarketplaceId         : APIリクエストするAmazonマーケットプレイスのID
    ### SPAPI_Region                : APIリクエストするエンドポイントのAWS Region
    ### SPAPI_Endpoint              : SP-APIエンドポイントのURL（https://を含むやつ）
    ### SPAPI_SignatureMethod       : 署名方式（AWS4-HMAC-SHA256）
    ### SPAPI_UserAgent             : APIリクエストする際のユーザエージェント情報(アクセス識別用)
    ### ==========================================

    ### ====================
    ### SP-API Path の定義
    ### ====================
    # ### Version : 0 ★2022年3月31日で使えなくなる★
    # ## パス設定
    # SPAPI_API_Path = '/catalog/v0/items/{}'.format(Asin_Code)
    # ## リクエストパラメータ設定
    # request_parameters = 'MarketplaceId=' + str(SPAPI_MarketplaceId)

    ### Version : 2020-12-01
    ## パス設定
    SPAPI_API_Path = '/catalog/2020-12-01/items/{}'.format(Asin_Code)
    ## リクエストパラメータ設定（パラメータはアルファベット順にすること！ & URLエンコードしないと、リクエストエラーになる場合あり！カンマ区切り文字入れるならURLエンコード必須）
    request_parameters_unencode = {
        'includedData' : 'attributes',
        'marketplaceIds' : str(SPAPI_MarketplaceId)
    } 
    request_parameters = urllib.parse.urlencode(request_parameters_unencode)

    ### Python による署名キーの取得関数
    ## 参考：http://docs.aws.amazon.com/general/latest/gr/signature-v4-examples.html#signature-v4-examples-python
    def sign(key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    def getSignatureKey(key, dateStamp, regionName, serviceName):
        kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
        kRegion = sign(kDate, regionName)
        kService = sign(kRegion, serviceName)
        kSigning = sign(kService, 'aws4_request')
        return kSigning

    ### ヘッダー情報と問合せ資格(credential)情報のための時刻情報作成
    t = datetime.utcnow()
    amzdate = t.strftime('%Y%m%dT%H%M%SZ')
    datestamp = t.strftime('%Y%m%d') # Date w/o time, used in credential scope


    ### =================================================================================
    ### Canonical Request の作成
    ### 参考：http://docs.aws.amazon.com/general/latest/gr/sigv4-create-canonical-request.html
    ### =================================================================================

    ## URI設定
    canonical_uri = SPAPI_API_Path

    ## 正規リクエストパラメータ設定
    canonical_querystring = request_parameters

    ## 正規リクエストヘッダリストの作成
    canonical_headers = 'host:' + SPAPI_Domain + '\n' + 'user-agent:' + SPAPI_UserAgent + '\n' + 'x-amz-access-token:' + SPAPI_Access_Token + '\n' + 'x-amz-date:' + amzdate + '\n'

    ## 正規リクエストヘッダリストの項目情報の作成(hostとx-amz-dateも入れてる)
    signed_headers = 'host;user-agent;x-amz-access-token;x-amz-date'

    ## ペイロードハッシュ（リクエスト本文コンテンツのハッシュ）の作成
    ## ※GETリクエストの場合、ペイロードは空の文字列（""）になる。
    payload_hash = hashlib.sha256(('').encode('utf-8')).hexdigest()

    ## 正規リクエストの作成
    canonical_request = SPAPI_Method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

    ## 問合せ資格情報を作成し、署名方式、ハッシュ化された正規リクエスト情報を結合した情報を作成する
    credential_scope = datestamp + '/' + SPAPI_Region + '/' + SPAPI_Service + '/' + 'aws4_request'
    string_to_sign = SPAPI_SignatureMethod + '\n' +  amzdate + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

    ## 定義した関数を用いて署名鍵を作成
    signing_key = getSignatureKey(SPAPI_IAM_User_Secret_Key, datestamp, SPAPI_Region, SPAPI_Service)

    ## 署名鍵で、上記で作成した「string_to_sign」に署名
    signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

    ## Authorizationヘッダの作成
    authorization_header = SPAPI_SignatureMethod + ' ' + 'Credential=' + SPAPI_IAM_User_Access_Key + '/' + credential_scope + ', ' +  'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

    ## API問合せ用ヘッダ情報の作成
    headers = {'user-agent':SPAPI_UserAgent, 'x-amz-access-token':SPAPI_Access_Token, 'x-amz-date':amzdate, 'Authorization':authorization_header}

    ## APIリクエストURLの作成
    request_url = SPAPI_Endpoint + canonical_uri + '?' + request_parameters

    ### ====================
    ### SP-APIリクエスト
    ### ====================
    # print('=== Request ===')
    print('Request URL = ' + request_url)
    api_response = requests.get(request_url, headers=headers)

    return api_response

def SPAPI_GetCatalogItemsForJAN(Jan_Code, SPAPI_Access_Token, SPAPI_IAM_User_Access_Key, SPAPI_IAM_User_Secret_Key, SPAPI_Method, SPAPI_Service, SPAPI_Domain, SPAPI_MarketplaceId, SPAPI_Region, SPAPI_Endpoint, SPAPI_SignatureMethod, SPAPI_UserAgent):
    print('Function : SPAPI_GetCatalogItemsForJAN')
    print(Jan_Code)
    ### === 引数の説明 ============================
    ### Asin_Code                   : リクエストするASINコード
    ### SPAPI_Access_Token          : リフレッシュトークンから取得したアクセストークン
    ### SPAPI_IAM_User_Access_Key   : IAMユーザのアクセスキー
    ### SPAPI_IAM_User_Secret_Key   : IAMユーザのシークレットキー
    ### SPAPI_Method                : HTTPアクセスプロトコル（GET）
    ### SPAPI_Service               : IAMユーザのアクセス権限設定（execute-api）
    ### SPAPI_Domain                : SP-APIエンドポイントのURLのドメイン部分（sellingpartnerapi-fe.amazon.com）
    ### SPAPI_MarketplaceId         : APIリクエストするAmazonマーケットプレイスのID
    ### SPAPI_Region                : APIリクエストするエンドポイントのAWS Region
    ### SPAPI_Endpoint              : SP-APIエンドポイントのURL（https://を含むやつ）
    ### SPAPI_SignatureMethod       : 署名方式（AWS4-HMAC-SHA256）
    ### SPAPI_UserAgent             : APIリクエストする際のユーザエージェント情報(アクセス識別用)
    ### ==========================================

    ### ====================
    ### SP-API Path の定義
    ### ====================
    # ### Version : 0 ★2022年3月31日で使えなくなる★
    # ## パス設定
    # SPAPI_API_Path = '/catalog/v0/items/{}'.format(Asin_Code)
    # ## リクエストパラメータ設定
    # request_parameters = 'MarketplaceId=' + str(SPAPI_MarketplaceId)

    ### Version : 2020-12-01
    ## パス設定
    SPAPI_API_Path = '/catalog/2020-12-01/items'
    ## リクエストパラメータ設定（パラメータはアルファベット順にすること！ & URLエンコードしないと、リクエストエラーになる場合あり！カンマ区切り文字入れるならURLエンコード必須）
    request_parameters_unencode = {
        'includedData' : 'identifiers,images,productTypes,salesRanks,summaries,variations',
        'keywords' : str(Jan_Code),
        'marketplaceIds' : str(SPAPI_MarketplaceId),
    } 
    request_parameters = urllib.parse.urlencode(request_parameters_unencode)

    ### Python による署名キーの取得関数
    ## 参考：http://docs.aws.amazon.com/general/latest/gr/signature-v4-examples.html#signature-v4-examples-python
    def sign(key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    def getSignatureKey(key, dateStamp, regionName, serviceName):
        kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
        kRegion = sign(kDate, regionName)
        kService = sign(kRegion, serviceName)
        kSigning = sign(kService, 'aws4_request')
        return kSigning

    ### ヘッダー情報と問合せ資格(credential)情報のための時刻情報作成
    t = datetime.utcnow()
    amzdate = t.strftime('%Y%m%dT%H%M%SZ')
    datestamp = t.strftime('%Y%m%d') # Date w/o time, used in credential scope


    ### =================================================================================
    ### Canonical Request の作成
    ### 参考：http://docs.aws.amazon.com/general/latest/gr/sigv4-create-canonical-request.html
    ### =================================================================================

    ## URI設定
    canonical_uri = SPAPI_API_Path

    ## 正規リクエストパラメータ設定
    canonical_querystring = request_parameters

    ## 正規リクエストヘッダリストの作成
    canonical_headers = 'host:' + SPAPI_Domain + '\n' + 'user-agent:' + SPAPI_UserAgent + '\n' + 'x-amz-access-token:' + SPAPI_Access_Token + '\n' + 'x-amz-date:' + amzdate + '\n'

    ## 正規リクエストヘッダリストの項目情報の作成(hostとx-amz-dateも入れてる)
    signed_headers = 'host;user-agent;x-amz-access-token;x-amz-date'

    ## ペイロードハッシュ（リクエスト本文コンテンツのハッシュ）の作成
    ## ※GETリクエストの場合、ペイロードは空の文字列（""）になる。
    payload_hash = hashlib.sha256(('').encode('utf-8')).hexdigest()

    ## 正規リクエストの作成
    canonical_request = SPAPI_Method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

    ## 問合せ資格情報を作成し、署名方式、ハッシュ化された正規リクエスト情報を結合した情報を作成する
    credential_scope = datestamp + '/' + SPAPI_Region + '/' + SPAPI_Service + '/' + 'aws4_request'
    string_to_sign = SPAPI_SignatureMethod + '\n' +  amzdate + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

    ## 定義した関数を用いて署名鍵を作成
    signing_key = getSignatureKey(SPAPI_IAM_User_Secret_Key, datestamp, SPAPI_Region, SPAPI_Service)

    ## 署名鍵で、上記で作成した「string_to_sign」に署名
    signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

    ## Authorizationヘッダの作成
    authorization_header = SPAPI_SignatureMethod + ' ' + 'Credential=' + SPAPI_IAM_User_Access_Key + '/' + credential_scope + ', ' +  'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

    ## API問合せ用ヘッダ情報の作成
    headers = {'user-agent':SPAPI_UserAgent, 'x-amz-access-token':SPAPI_Access_Token, 'x-amz-date':amzdate, 'Authorization':authorization_header}

    ## APIリクエストURLの作成
    request_url = SPAPI_Endpoint + canonical_uri + '?' + request_parameters

    ### ====================
    ### SP-APIリクエスト
    ### ====================
    print('=== Request ===')
    print('Request URL = ' + request_url)
    print(headers)
    api_response = requests.get(request_url, headers=headers)
    print(api_response)

    return api_response


















if __name__ == '__main__':
    SPAPI_LWA_Client_ID='amzn1.application-oa2-client.3ca0ac9d9ff5410f87242e09cded92bd'
    SPAPI_LWA_Client_PW='ecabec54f2a4198acecfb117342fcbdb6f05f27ee84ca6b710881a571e3a689c'
    SPAPI_Refresh_Token='Atzr|IwEBIE5lGWIuZAiz8k9fH_6OQnel3ZGo9qHO1zwVplAF5VQmuFb2tTDL0BOs6luCyaXZSMeXsy_zl6CytzxpzdKiXKzJ7cvIhBFz1QphYIFSyeoatryEWW3QFCDGFZZ9LFyVpwhsC25m6iKxSunXn71aIaQXyEa_25_cSfLB5Mswbk9jZJhY-Gh1uX_WQTmSGD87vmUK-zBv00RcjW4TV-_GbWIafFrN60gY9F_kfOC8SuPot2svsoTmdQ2jR5_5DFjSeJhVe--bAV_0cD4cI443os4Ha9GHjZNSJwdYnYwSrwkomKVCTqQw4oE1TV14uBlUAok'
    SPAPI_Access_Token_Endpoint='https://api.amazon.com/auth/o2/token'
    token=SPAPI_Get_Token(SPAPI_LWA_Client_ID, SPAPI_LWA_Client_PW, SPAPI_Refresh_Token, SPAPI_Access_Token_Endpoint)
    #print('####')
    SPAPI_Access_Token=token[0]
    #print(SPAPI_Access_Token)
    SPAPI_IAM_User_Access_Key='AKIARB5KAK2FVE3IQZ3I'
    SPAPI_IAM_User_Secret_Key='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'
    SPAPI_Method='GET'
    SPAPI_Service='execute-api'
    SPAPI_Domain='sellingpartnerapi-fe.amazon.com'
    SPAPI_MarketplaceId='A1VC38T7YXB528'
    SPAPI_Region='us-west-2'
    SPAPI_Endpoint='https://sellingpartnerapi-fe.amazon.com'
    SPAPI_SignatureMethod='AWS4-HMAC-SHA256'
    SPAPI_UserAgent='Amazon Info'

    Asin_Code='B07XV8VSZT'
    Jan_Code='4902370535730'

    api_ASINresponse=SPAPI_GetCatalogItemsForASIN(Asin_Code, SPAPI_Access_Token, SPAPI_IAM_User_Access_Key, SPAPI_IAM_User_Secret_Key, SPAPI_Method, SPAPI_Service, SPAPI_Domain, SPAPI_MarketplaceId, SPAPI_Region, SPAPI_Endpoint, SPAPI_SignatureMethod, SPAPI_UserAgent)

    api_JANresponse=SPAPI_GetCatalogItemsForJAN(Jan_Code, SPAPI_Access_Token, SPAPI_IAM_User_Access_Key, SPAPI_IAM_User_Secret_Key, SPAPI_Method, SPAPI_Service, SPAPI_Domain, SPAPI_MarketplaceId, SPAPI_Region, SPAPI_Endpoint, SPAPI_SignatureMethod, SPAPI_UserAgent)


    
    print('###')
    ## レスポンスをdict形式に変換
    # print(api_JANresponse)
    ASINresponse_dict = json.loads(api_ASINresponse.text)

    JANresponse_dict = json.loads(api_JANresponse.text)

    ## 見やすく表示する加工
    ASINresponse_json = json.dumps(ASINresponse_dict, indent=4)
    JANresponse_json = json.dumps(JANresponse_dict, indent=4)

    ## 表示
    # print('=== Response detail - SPAPI_GetCatalogItemsForASIN ===')
    # print('Response Status : ' + str(api_ASINresponse.status_code))
    # print('Response headers :\r\n' + str(api_ASINresponse.headers))
    # print('Response json :\r\n' + str(ASINresponse_json))

    print('#######################################')

    print('Response json :\r\n' + str(ASINresponse_dict))