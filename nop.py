# -*- coding: utf-8 -*-
# credit           : Mr ALI
# coded by        : Malik
# Python version : v3.11.4
# _________________________________________
	# First jin idz ki file put hu un ma group Jo ham da wo join hu
	# Phr un pa sharing jitna fast ho saka
	# .....or sath likha jaii ka itni sharing ho gai
import os
import asyncio
import json
import sys
import time
import re
import glob
import random
import string

from concurrent.futures import ThreadPoolExecutor
try:import brotli,requests,bs4
except:os.system('pip install brotli requests bs4')

import requests
# MODULES WORKING WITH
try:os.mkdir('/sdcard/00Friends')
except:pass
fast = [2]
line="-"*58
letters=sorted(string.ascii_uppercase)
rd='\033[38;5;208m';grnh='\033[1;32m'
grn='\033[38;5;42m';rdh='\033[1;31m'
yl='\033[38;5;220m';bl='\033[38;5;38m'
bk1='\033[38;5;235m';bk2='\033[38;5;238m'
bk3='\033[38;5;250m';bk4='\033[38;5;255m'
unk=f'\033[38;5;{random.randint(1,200)}m';en='\033[0m'
ok=[];dd=[];tts=[0];cp=[];ts=[];ac=[]
boxs=[];maxs=[10];stop=['p']
restricted = []
listIds = [] ; filex = ['filename']
class FacebookLogin:
	def __init__(self):
		self.banner = """
 YOUR LOGO HERE
 """                                                              
		self.data = {}
		self.status = None
		self.android = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
	def clear(self):
		os.system('clear')
	def login(self,uid,password):
		with requests.Session() as session:
			session.headers.update({"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-language": "en-US,en;q=0.9","save-data": "on","user-agent": self.android,"sec-ch-ua": "\"Google Chrome\";v=\"112\", \"Chromium\";v=\"112\", \"Not=A?Brand\";v=\"24\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","sec-fetch-dest": "document","sec-fetch-mode": "navigate","sec-fetch-site": "none","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referrerPolicy": "strict-origin-when-cross-origin"})
			with session.get("https://m.facebook.com/", allow_redirects=True, timeout=300) as responses:
				session.headers.update({"referer":f"{responses.url}"})
				cookies = session.cookies.get_dict()
				response = responses.text;html = parser(response,'html.parser')
				m_ts = None;fb_dtsg = None;li = None;lsd = None;jazoest = None
				try:
					m_ts = html.find('input',{'name':'m_ts'})['value']
					fb_dtsg = re.search('{"dtsg":{"token":"(.*?)"',response).group(1)
					li = html.find('input',{'name':'li'})['value']
					lsd = html.find('input',{'name':'lsd'})['value']
					jazoest = html.find('input',{'name':'jazoest'})['value']
				except:pass
				data = {
					'fb_dtsg':fb_dtsg,
					'm_ts':m_ts,
					'li':li,
					'lsd':lsd,
					'jazoest':jazoest,
					'email':str(uid),
					'pass':str(password),
					'masked_cp':f'+8801******046',
					'prefill_contact_point':uid,
					'try_number':'0',
					'unrecognized_tries':'0',
					'prefill_source':'browser_dropdown',
					'prefill_type':'contact_point',
					'first_prefill_source':'header',
					'first_prefill_type':'contact_point',
					'had_cp_prefilled':'true',
					'had_password_prefilled':'true',
					'is_smart_lock':'false',
					'bi_xrwh':'0',
					'bi_wvdp':'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}'
				}
				with session.post("https://m.facebook.com/login.php",data=data,cookies=cookies) as responses2:
					# open('responses2.html','wb').write(responses2.content)
					cookiez = session.cookies.get_dict()
					cookie = ';'.join(c+'='+cookiez[c] for c in cookiez)
					if "checkpoint" in str(cookie) or "1501092823525282" in responses2.text:return {'status':'bad','cookie':cookie}
					elif "c_user" in cookie and not "828281030927956" in responses2.text:return {'status':'ok','cookie':cookie,'id':cookiez['c_user']}
					elif 'Invalid username or password' in responses2.text or 'incorrect password' in str(responses2.text).lower() or 'The phone number' in responses2.text or 'The mobile number or email address' in responses2.text or 'name="reset_action"' in responses2.text or 'The password' in responses2.text or '/recover/code/?ars=contact_point_login' in responses2.text:
						return {'status':'no','cookie':cookie}
					elif "approvals_code" in responses2.text:return {'status':'2fa','cookie':cookie}
					else:return {'status':'bad','cookie':cookie}
	def genCookie(self,uid,password):
		sys.stdout.write(f'\r{bk4}processing:[{len(ts)}/{tts[0]}|done:{len(ok)}|dead:{len(dd)}{en}]')
		cookiez = self.login(uid,password);ts.append('t')
		if cookiez['status']=='ok':
			cookie = cookiez['cookie'];ok.append('o')
			with open('/sdcard/00Friends/cookies.txt','a') as saf:
				saf.write(f'{uid}|{password}|{cookie}\n')
				print(f"\r[ {grnh}[{len(ok)}] => {uid}|{password}|{cookie}{en} ]")
		elif cookiez['status']=='no':
			with open(f"/sdcard/00Friends/incorrect_.txt",'a') as saf:
				saf.write(f'{uid}|{password}\n')
				print(f"\r[ {rd}[xx] {uid}|Incorrect Email/Password{en} ]")
		else:
			with open(f"/sdcard/00Friends/dead_account.txt",'a') as saf:
				saf.write(f'{uid}|{password}\n')
				print(f"\r[ {rdh}[xx] {uid}|{password}|dead_account{en} ]")
	def CookieSetting(self):
		file=list(filter(None,open(input(f" {rd}ɪɴᴘᴜᴛ ɪᴅꜱ ꜰɪʟᴇɴᴀᴍᴇ{en}: ")).read().split('\n')))
		tts[0]=len(file)
		print(f'''
 {line}
 [1] Run Fast (Threading)
 [2] Run Slow
 {line}
''')
		fast[0] = int(input('option: '))
		with ThreadPoolExecutor(max_workers=5) as tp:
			for uidx in file:
				sys.stdout.write(f'\r{bk4}processing:[{len(ts)}/{tts[0]}|done:{len(ok)}|dead:{len(dd)}{en}]')
				try:
					idx=uidx.split('|')
					password = idx[1]
					uid      = idx[0]
					if fast[0]==1:tp.submit(self.genCookie,uid,password)
					else:self.genCookie(uid,password)
				except requests.exceptions.ConnectionError:input(f"\r {yl}No internet, press enter to continue{en}: ")
				except KeyboardInterrupt:print(f"\r {yl}See you later{en}: ");break
				except Exception as e:time.sleep(10)
		reslt=f"""\r
 {line}
 process has been completed...
 {line}
 Total Accounts   : {len(file)},
 Total cookied    : {len(ok)},
 Total dead ids   : {len(dd)},
>>>>invalid/dead ids saved in 'dead_ids.txt'
		"""
		open('last_result.txt','w').write(reslt)
		input(reslt)
		self.menu()
		sys.exit()
	def menu(self):
		self.clear()
		ts.clear()
		ok.clear()
		cp.clear()
		dd.clear()
		self.status=None
		print(self.banner)
		print(f'''{bk3}
 {line}{yl}
                   SELECT ANY OPTION{bk3}
 {line}{bk2}
 [1 - ADD FRIENDS]{bk3}
 [2 - COOKIE GENERATOR]{bk2}
 [3 - POST SHARE GROUPS]
 [4 - PROFILE UPDATES]
 {line}{bk3}
 [0 - Quit.
 {line}{en}''')
		try:
			opt=input(f" {rd}option{en}>>")
			# if opt in ['01','1']:self.FriendSetting();sys.exit()
			if opt in ['02','2']:self.CookieSetting();sys.exit()
			# elif opt in ['03','3']:self.ShareSetting();sys.exit()
			# elif opt in ['04','4']:self.ProfileSetting();sys.exit()
			else:print('invalid option')
		except KeyboardInterrupt:print(f" {yl}See you later{en}: ");time.sleep(1);sys.exit()
		except FileNotFoundError:print('file location not found..');time.sleep(1);self.menu();sys.exit()


fb = FacebookLogin()
fb.menu()
