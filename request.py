import json
import re
from urllib.parse import urlencode, quote

import brotli
import zlib
import gzip
import requests


class request_fb:

    def make_request(self, params, method, authority, origin, is_referer, referer, user_agent, cookie, is_body, body,
                     is_header=True):
        try:
            headers = {
                'authority': authority,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookie,
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

            # cookies = cookie

            if is_body:
                data = body
            else:
                data = None
            # data = body if is_body else None

            response = requests.request(method, params, headers=headers, data=data,
                                        allow_redirects=True)
            # if response.headers.get('Content-Encoding') == 'br':
            #     compressed_data = response.content
            #     uncompressed_data = brotli.decompress(compressed_data)
            #     content = uncompressed_data.decode('utf-8')
            # else:
            #     content = response.text

            # hai = response.headers
            # hai = response.headers.get('Set-Cookie')
            # hai = response.cookies.get_dict()

            return response
            # if is_header:
            #     return str(response.headers) + response.text
            # else:
            #     return response.text

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def get_approvals_code(self, url):
        try:
            response = requests.request('GET', url, allow_redirects=True, verify=False)
            return response
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi lấy code 2FA!'
            })

    def get_cookie_before_login_facebook_mbasic(self, user_agent):
        try:
            response = self.make_request('https://mbasic.facebook.com/login.php', 'GET',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', False, '',
                                         user_agent, '', False, '')
            if response.text.__contains__('accept_only_essential'):
                pattern = r'name=\"lsd\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                lsd = matchs[1]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[1]
                referer = response.headers.get('Referer')
                body = 'jazoest=' + quote(jazoest, safe="") + '&lsd=' + quote(lsd, safe="") + '&accept_only_essential=1'

                response = self.make_request(
                    'https://mbasic.facebook.com/cookie/consent/?next_uri=https%3A%2F%2Fmbasic.facebook.com%2Flogin.php',
                    'POST', 'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                    'https://mbasic.facebook.com/cookie/consent_prompt/?next_uri=https%3A%2F%2Fmbasic.facebook.com%2Flogin.php&refsrc=deprecated&_rdr',
                    user_agent, '', True, body)

                cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
                response = self.make_request('https://mbasic.facebook.com/login.php?_rdr', 'GET',
                                             'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                             'https://mbasic.facebook.com/cookie/consent_prompt/?next_uri=https%3A%2F%2Fmbasic.facebook.com%2Flogin.php&refsrc=deprecated&_rdr',
                                             user_agent, cookies, False, '')

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            if cookies != '':
                pattern = r'name=\"lsd\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                lsd = matchs[0]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[0]
                pattern = r'name=\"m_ts\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                m_ts = matchs[0]
                pattern = r'name=\"li\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                li = matchs[0]
                pattern = r'name=\"bi_xrwh\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                bi_xrwh = matchs[0]
                pattern = r'input value=\"([^"]*)\" type=\"submit\" name=\"login\"'
                matchs = re.findall(pattern, response.text)
                login = matchs[0]
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'lsd': lsd,
                    'jazoest': jazoest,
                    'm_ts': m_ts,
                    'li': li,
                    'bi_xrwh': bi_xrwh,
                    'login': login,
                    'message': 'Đăng nhập...!',
                })
            else:
                return json.dumps({
                    'status': 400,
                    'message': 'Login lỗi!',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def get_cookie_checkpoint_2fa(self, id_fb, pass_fb, cookie, lsd, jazoest, m_ts, li, login, bi_xrwh, user_agent):
        try:
            body = 'lsd=' + quote(lsd, safe="") + '&jazoest=' + quote(jazoest, safe="") + '&m_ts=' + quote(m_ts,
                                                                                                           safe="") + '&li=' + quote(
                li, safe="") + '&try_number=0&unrecognized_tries=0&email=' + quote(id_fb, safe="") + '&pass=' + quote(
                pass_fb, safe="") + '&login=' + quote(login, safe="") + '&bi_xrwh=' + quote(bi_xrwh, safe="")
            response = self.make_request(
                'https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9',
                'POST', 'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                'https://mbasic.facebook.com/login.php', user_agent, cookie, True,
                body)

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            if cookies != '':
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'message': 'Get code 2FA',
                })
            else:
                return json.dumps({
                    'status': 400,
                    'message': 'Login lỗi!',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def check_approvals_code(self, cookie, code_2fa, user_agent):
        try:
            response = self.make_request('https://mbasic.facebook.com/checkpoint/?_rdr', 'GET',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         'https://mbasic.facebook.com/login.php', user_agent, cookie, False, '')

            flag = response.text.__contains__('approvals_code')
            if flag:
                cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
                pattern = r'name=\"fb_dtsg\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                fb_dtsg = matchs[0]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[0]
                pattern = r'name=\"nh\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                nh = matchs[0]
                pattern = r'input value=\"(.*?)\" type=\"submit\" name=\"submit\[(.*?)\]\"'
                matchs = re.findall(pattern, response.text)
                submit_name = matchs[0][1]
                submit_value = matchs[0][0]
                # get code 2fa
                url = "https://2fa.live/tok/" + re.sub(r'\s+', '', code_2fa)
                response_approvals_code = json.loads(self.get_approvals_code(url).text)
                approvals_code = response_approvals_code['token']
                if len(code_2fa) < 13:
                    return json.dumps({
                        'status': 404,
                        'message': '2fa bị sai!'
                    })
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'nh': nh,
                    'approvals_code': approvals_code,
                    'submit_name': submit_name,
                    'submit_value': submit_value,
                    'message': 'Submit code 2FA: ' + approvals_code,
                })
            else:
                return json.dumps({
                    'status': 404,
                    'message': 'Lỗi vượt 2FA!'
                })
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def submit_code_2fa(self, fb_dtsg, jazoest, approvals_code, nh, cookie, user_agent, submit_name, submit_value):
        try:
            body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                              safe="") + '&checkpoint_data=&approvals_code=' + quote(
                approvals_code, safe="") + '&codes_submitted=0&submit%5B' + submit_name + '%5D=' + quote(submit_value,
                                                                                                         safe="") + '&nh=' + quote(
                nh, safe="") + '&fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest, safe="")
            response = self.make_request('https://mbasic.facebook.com/login/checkpoint/', 'POST',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         'https://mbasic.facebook.com/checkpoint/?_rdr', user_agent, cookie, True, body)

            flag = response.text.__contains__('name_action_selected')
            if flag:
                cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
                pattern = r'name=\"fb_dtsg\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                fb_dtsg = matchs[0]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[0]
                pattern = r'name=\"nh\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                nh = matchs[0]
                pattern = r'input value=\"(.*?)\" type=\"submit\" name=\"submit\[(.*?)\]\"'
                matchs = re.findall(pattern, response.text)
                submit_name = matchs[0][1]
                submit_value = matchs[0][0]
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'nh': nh,
                    'submit_name': submit_name,
                    'submit_value': submit_value,
                    'message': 'Đang đăng nhập...',
                })
            else:
                return json.dumps({
                    'status': 404,
                    'message': 'Đăng nhập thất bại!'
                })
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def get_cookie_dont_save_browser(self, fb_dtsg, jazoest, nh, cookie, user_agent, submit_name, submit_value):
        try:
            body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                              safe="") + '&checkpoint_data=&name_action_selected=dont_save&submit%5B' + submit_name + '%5D=' + quote(
                submit_value, safe="") + '&nh=' + quote(nh, safe="") + '&fb_dtsg=' + quote(fb_dtsg,
                                                                                           safe="") + '&jazoest=' + quote(
                fb_dtsg, safe="")
            response = self.make_request('https://mbasic.facebook.com/login/checkpoint/', 'POST',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         'https://mbasic.facebook.com/login/checkpoint/', user_agent, cookie, True,
                                         body)

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            if response.text.__contains__('checkpointSubmitButton-actual-button'):
                pattern = r'name=\"fb_dtsg\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                fb_dtsg = matchs[0]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[0]
                pattern = r'name=\"nh\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                nh = matchs[0]
                pattern = r'input value=\"(.*?)\" type=\"submit\" name=\"submit\[(.*?)\]\"'
                matchs = re.findall(pattern, response.text)
                submit_name = matchs[0][1]
                submit_value = matchs[0][0]
                return json.dumps({
                    'status': 302,
                    'cookie': cookies,
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'nh': nh,
                    'submit_name': submit_name,
                    'submit_value': submit_value,
                    'message': 'Đang đăng nhập...',
                })
            else:
                previous_cookie = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.history[0].cookies])
                if str(previous_cookie).__contains__('checkpoint=deleted'):
                    cookies = cookies + str(previous_cookie).replace('checkpoint=deleted', '')
                else:
                    cookies = cookies + '; ' + previous_cookie
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'message': 'Đăng nhập thành công!',
                })
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'message': 'Đang đăng nhập...',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def review_recent_login(self, fb_dtsg, jazoest, nh, cookie, user_agent, submit_name, submit_value):
        try:
            body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                              safe="") + '&checkpoint_data=&submit%5B' + submit_name + '%5D=' + quote(
                submit_value, safe="") + '&nh=' + quote(nh, safe="") + '&fb_dtsg=' + quote(fb_dtsg,
                                                                                           safe="") + '&jazoest=' + quote(
                jazoest, safe="")
            response = self.make_request('https://mbasic.facebook.com/login/checkpoint/', 'POST',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         'https://mbasic.facebook.com/login/checkpoint/', user_agent, cookie, True,
                                         body)

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            if response.text.__contains__('checkpointSubmitButton-actual-button'):
                pattern = r'name=\"fb_dtsg\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                fb_dtsg = matchs[0]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[0]
                pattern = r'name=\"nh\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                nh = matchs[0]
                pattern = r'input value=\"(.*?)\" type=\"submit\" name=\"submit\[(.*?)\]\"'
                matchs = re.findall(pattern, response.text)
                submit_name = matchs[1][1]
                submit_value = matchs[1][0]
                # This is me
                body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                                  safe="") + '&checkpoint_data=&submit%5B' + submit_name + '%5D=' + quote(
                    submit_value, safe="") + '&nh=' + quote(nh, safe="") + '&fb_dtsg=' + quote(fb_dtsg,
                                                                                               safe="") + '&jazoest=' + quote(
                    jazoest, safe="")
                response = self.make_request('https://mbasic.facebook.com/login/checkpoint/', 'POST',
                                             'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                             'https://mbasic.facebook.com/login/checkpoint/', user_agent, cookies, True,
                                             body)
                if response.text.__contains__('name_action_selected'):
                    cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
                    pattern = r'name=\"fb_dtsg\" value=\"(.*?)\"'
                    matchs = re.findall(pattern, response.text)
                    fb_dtsg = matchs[0]
                    pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                    matchs = re.findall(pattern, response.text)
                    jazoest = matchs[0]
                    pattern = r'name=\"nh\" value=\"(.*?)\"'
                    matchs = re.findall(pattern, response.text)
                    nh = matchs[0]
                    pattern = r'input value=\"(.*?)\" type=\"submit\" name=\"submit\[(.*?)\]\"'
                    matchs = re.findall(pattern, response.text)
                    submit_name = matchs[0][1]
                    submit_value = matchs[0][0]
                    # Submit don't save browser
                    response = self.get_cookie_dont_save_browser(fb_dtsg, jazoest, nh, cookies, user_agent, submit_name,
                                                                 submit_value)
                    return response
                else:
                    return json.dumps({
                        'status': 404,
                        'message': 'Đăng nhập thất bại!',
                    })
            else:
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'message': 'Đang đăng nhập...',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def check_login_to_home(self, cookie, user_agent):
        try:
            response = self.make_request('https://mbasic.facebook.com/home.php?refsrc=deprecated&_rdr', 'GET',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         'https://mbasic.facebook.com/login/checkpoint/', user_agent, cookie, False, '')

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            if cookies != '':
                if str(cookie).__contains__('checkpoint=deleted'):
                    cookies = cookies + str(cookie).replace('checkpoint=deleted', '')
                else:
                    cookies = cookies + cookie
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'message': 'Đăng nhập thành công!',
                })
            else:
                return json.dumps({
                    'status': 400,
                    'message': 'Đăng nhập thất bại!',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def check_account_quality(self, id_fb, cookie, user_agent):
        try:
            response = self.make_request('https://www.facebook.com/accountquality/' + id_fb + '/?source=link', 'GET',
                                         'www.facebook.com', 'https://www.facebook.com', True,
                                         'https://www.facebook.com/accountquality',
                                         user_agent, cookie, False, '')

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            pattern = r'"token":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            lsd = matchs[1]
            pattern = r'"sessionID":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            session_id = matchs[0]
            pattern = r'"haste_session":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            haste_session = matchs[0]
            pattern = r'"connectionClass":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            __ccg = matchs[0]
            pattern = r'"server_revision":\s*(\d+)'
            matchs = re.findall(pattern, response.text)
            __rev = matchs[0]
            pattern = r'"hsi":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            __hsi = matchs[0]
            pattern = r'"token":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            fb_dtsg = matchs[0]
            pattern = r'"__spin_r":\s*(\d+)'
            matchs = re.findall(pattern, response.text)
            __spin_r = matchs[0]
            pattern = r'"__spin_b":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            __spin_b = matchs[0]
            pattern = r'"__spin_t":\s*(\d+)'
            matchs = re.findall(pattern, response.text)
            __spin_t = matchs[0]

            headers = {
                'authority': 'www.facebook.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookie,
                'origin': 'https://www.facebook.com',
                'referer': 'https://www.facebook.com/accountquality/' + id_fb,
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent,
                'x-asbd-id': '198387',
                'x-fb-friendly-name': 'AccountQualityHubAssetOwnerViewV2Query',
                'x-fb-lsd': lsd,
                'accept-encoding': 'gzip, deflate, br',
                'connection': 'keep-alive',
            }

            data = 'av=' + quote(id_fb, safe="") + '&session_id=' + quote(session_id, safe="") + '&__user=' + quote(
                id_fb, safe="") + '&__a=1&__req=1&__hs=' + quote(haste_session, safe="") + '&dpr=2&__ccg=' + quote(
                __ccg, safe="") + '&__rev=' + quote(__rev, safe="") + '&__s=ma0z7e%3A573g7w%3Adpehmi&__hsi=' + quote(
                __hsi,
                safe="") + '&__dyn=7xeUmxa2C5rgydwn8K2abBWqxu59o9E4a2i5VGxK5FEG484S4UKewPGi4FoixWE-16xq4EOezobo-4Lxe1kx21FxG9xedz8hwgo5qq3a4EuCx62a2q5E9UeUryFE4WWBBwLjzu2SJaECfiwzlwXyXwBxu1UxO6AcK2y5oeEjx63K7EC11xnzoO9ws8nw8ScwgECu7EK3i2a3Fe6rwiolDwFwBgaohzE8U98doK78-4Ea8mwnHxJUpx2aK2a4p8y26U8U-UbE4S7VEjCx6Etw9O3ifzobEaUiwm8myUnwUzpA6EfEO32fxiFVoa9obGwgUy1kx6bCyVUCcG2-qaUK2e0UFU2RwiU8U6Ci2G1bzFHwCwmo4S7EaUkw&__csr=&fb_dtsg=' + quote(
                fb_dtsg, safe="") + '&jazoest=25769&lsd=' + quote(lsd, safe="") + '&__spin_r=' + quote(__spin_r,
                                                                                                       safe="") + '&__spin_b=' + quote(
                __spin_b, safe="") + '&__spin_t=' + quote(__spin_t,
                                                          safe="") + '&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=AccountQualityHubAssetOwnerViewV2Query&variables=%7B%22assetOwnerId%22%3A%22' + quote(
                id_fb, safe="") + '%22%7D&server_timestamps=true&doc_id=6139497919470985'

            response = requests.request('POST', 'https://www.facebook.com/api/graphql/', headers=headers, data=data,
                                        allow_redirects=True)
            response = json.loads(response.text)
            acc_is_restricted = response['data']['assetOwnerData']['advertising_restriction_info']['is_restricted']
            return json.dumps({
                'status': 200,
                'acc_is_restricted': acc_is_restricted,
                'message': 'Check trạng thái tài khoản thành công!',
            })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def get_view_checkpoint_282(self, cookie, user_agent):
        try:
            # response = self.make_request(
            #     'https://www.facebook.com/',
            #     'GET',
            #     'www.facebook.com', 'https://www.facebook.com/', False, '',
            #     user_agent, cookie, False, '')
            # cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            # cookie = cookie + '; ' + cookies
            response = self.make_request(
                'https://adsmanager.facebook.com/accountquality/advertising_access/?callsite=15&enforcement=1&intent=1',
                'GET',
                'adsmanager.facebook.com', '', False, '',
                user_agent, cookie, False, '')
            location = response.history[1].headers.get('Location')
            pattern = r'https:\/\/www.facebook.com\/checkpoint\/[0-9]+\/([0-9]+)'
            matchs = re.findall(pattern, location)
            number_checkpoint = matchs[0]

            response = self.make_request(
                'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F',
                'GET',
                'mbasic.facebook.com', 'https://mbasic.facebook.com', False, '',
                user_agent, cookie, False, '')
            referer = 'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F'
            # Upload your ID
            if response.text.__contains__('mobile_image_data'):
                return json.dumps({
                    'status': 200,
                    'action': 'upload_your_id',
                    'number_checkpoint': number_checkpoint,
                    'message': 'Upload your id',
                })
            # Starting process to request a review
            elif response.text.__contains__('action_proceed'):
                return json.dumps({
                    'status': 200,
                    'action': 'action_proceed',
                    'number_checkpoint': number_checkpoint,
                    'message': 'Bắt đầu XMDT',
                })
            # Captcha
            elif response.text.__contains__('captcha_response'):
                return json.dumps({
                    'status': 200,
                    'action': 'captcha',
                    'number_checkpoint': number_checkpoint,
                    'message': 'Giải captcha',
                })
            # View input phone number
            elif response.text.__contains__('contact_point'):
                return json.dumps({
                    'status': 200,
                    'action': 'add_phone_number',
                    'number_checkpoint': number_checkpoint,
                    'message': 'Thêm SĐT',
                })
            else:
                return json.dumps({
                    'status': 404,
                    'message': 'Không tìm thấy link XMDT!',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def submit_continue_checkpoint(self, number_checkpoint, cookie, user_agent):
        try:
            response = self.make_request(
                'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F',
                'GET',
                'mbasic.facebook.com', 'https://mbasic.facebook.com', False, '',
                user_agent, cookie, False, '')
            referer = 'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F'
            pattern = r'form\s+method="[^"]+"\s+action="\/checkpoint([^"]+)"'
            matchs = re.findall(pattern, response.text)
            params = 'https://mbasic.facebook.com/checkpoint' + str(matchs[0]).replace('&amp;', '&')
            pattern = r'name="fb_dtsg"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            fb_dtsg = matchs[0]
            pattern = r'name="jazoest"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            jazoest = matchs[0]
            pattern = r'value="([^"]+)"\s+type="submit"\s+name="action_proceed"'
            matchs = re.findall(pattern, response.text)
            action_proceed = matchs[0]

            body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                              safe="") + '&action_proceed=' + quote(
                action_proceed, safe="")
            response = self.make_request(params,
                                         'POST', 'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         referer, user_agent, cookie, True, body)

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def submit_code_checkpoint(self, number_checkpoint ,cookie, user_agent, client_key):
        try:
            response = self.make_request(
                'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F',
                'GET',
                'mbasic.facebook.com', 'https://mbasic.facebook.com', False, '',
                user_agent, cookie, False, '')
            referer = 'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F'
            pattern = r'form\s+method="[^"]+"\s+action="\/checkpoint([^"]+)"'
            matchs = re.findall(pattern, response.text)
            params = 'https://mbasic.facebook.com/checkpoint' + str(matchs[0]).replace('&amp;', '&')
            pattern = r'name="fb_dtsg"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            fb_dtsg = matchs[0]
            pattern = r'name="jazoest"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            jazoest = matchs[0]
            pattern = r'value="([^"]+)"\s+type="submit"\s+name="action_proceed"'
            matchs = re.findall(pattern, response.text)
            action_proceed = matchs[0]

            body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                              safe="") + '&action_proceed=' + quote(
                action_proceed, safe="")
            response = self.make_request(params,
                                         'POST', 'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         referer, user_agent, cookie, True, body)

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })
