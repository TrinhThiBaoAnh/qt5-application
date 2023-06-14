import requests

class request:
    @staticmethod
    def make_request(params, method, is_referer, authority, origin, referer, user_agent, cookie, is_body, body,
                     is_header):
        try:
            headers = {
                'authority': authority,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': origin,
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': user_agent,
                'accept-encoding': 'gzip, deflate, br',
                'connection': 'keep-alive',
            }

            if is_referer:
                headers['referer'] = referer

            cookies = {
                'cookie': cookie
            }

            data = body if is_body else None

            response = requests.request(method, params, headers=headers, cookies=cookies, data=data,
                                        allow_redirects=True, verify=False)
            if is_header:
                return str(response.headers) + response.text
            else:
                return response.text

        except Exception as e:
            return {
                'status': 404,
                'message': 'Lỗi server!'
            }