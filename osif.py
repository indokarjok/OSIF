import json , sys , hashlib , os , time

########################################################################
#                             COLOR
if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[31;1m'
else:
	W = ''
	G = ''
	R = ''
#
########################################################################

try:
	import requests
except ImportError:
	print R + '_     _'.center(44)
	print "o' \.=./ `o".center(44)
	print '(o o)'.center(44)
	print 'ooO--(_)--Ooo'.center(44)
	print W + ' '
	print ('O S I F').center(44)
	print ' '
	print "[!] Can't import module 'requests'\n"
	sys.exit()

######################################################################

reload (sys)
sys . setdefaultencoding ( 'utf8' )

############################################################

jml = []
jmlgetdata = []
n = []

###########################################################
#
def baliho():
	try:
		token = open('cookie/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		n.append(a['name'])

		print R + '_     _'.center(44)
		print "o' \.=./ `o".center(44)
		print '(o o)'.center(44)
		print 'ooO--(_)--Ooo'.center(44)
		print ' ' + W
		print ('[*] ' + name + ' [*]').center(44)
		print ' '
	except (KeyError,IOError):
		print R + '_     _'.center(44)
		print "o' \.=./ `o".center(44)
		print '(o o)'.center(44)
		print 'ooO--(_)--Ooo'.center(44)
		print ' ' + W
		print ('O S I F').center(44)
		print (W + '     [' + G +'Open Source Information Facebook'+ W + ']')
		print ' '
#
############################################################

############################################################
#		    Print In terminal
def show_program():
	print G + '''
                    INFORMATION''' + W + """
 ------------------------------------------------------

    Coded      by IndoKarjok
    Name       OSIF 'Open Source Information Facebook'
    version    5.1
    Date       16/05/2018 09:35:12
    Email      tnherp2202@gmail.com

* if you find any errors or problems , please contact
  author
"""
def info_ga():
	print G + '''
     COMMAND                      DESCRIPTION''' + W + """
  -------------       -------------------------------------

   get_data           fetching all friends data
   get_info           show information about your friend

   dump_id            fetching all id from friend list
   dump_phone         fetching all phone number from friend list
   dump_mail          fetching all emails from friend list

   token              Generate access token
   cat_token          show your access token
   rm_token           remove access token

   bot                open bot menu

   clear              clear terminal
   help               show help
   about              Show information about this program
   exit               Exit the program
"""

def menu_bot():
	print G + '''
   Number                  INFO ''' + W + """
 ---------   ------------------------------------

   [ 1 ]       like all posts
   [ 2 ]       React all post with emoji 'Love'
   [ 3 ]       React all post with emoji 'Wow'
   [ 4 ]       React all post with emoji 'Haha'
   [ 5 ]       React all post with emoji 'Sad'
   [ 6 ]       React all post with emoji "Angry'
   [ 7 ]       Comment all posts

   [ 0 ]       Back to main menu
"""
#
###########################################################

###########################################################
#                     GENERATE ACCESS TOKEN

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie / token.log'
		main()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		main()
def id():
	print '[*] login to your facebook account         ';id = raw_input('[?] Username : ');pwd = raw_input('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET

	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)
#
#################################################################################

#################################################################################
#       	     Bot Like And Comment

	                # Execute #

def post():
	global token , WT

	print '[*] fetching all posts id'
	try:
	  if WT == 'wallpost':

		r = requests.get('https://graph.facebook.com/me?fields=home.limit(150)&access_token='+token)
		result = json.loads(r.text)

		return result['home']['data']

	  else:
		r = requests.get("https://graph.facebook.com/%s?fields=feed.limit(150)&access_token=%s"%(id,token))
		result = json.loads(r.text)

		return result['feed']['data']
	except KeyError:
		print '[!] failed to retrieve all post id'
		print '[!] Stopped'
		bot()
	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		bot()

def like(posts , amount):
	global type , token , WT

	print '[*] All posts id successfuly retrieved'
	print '[*] Start'

	try:
		counter = 0
		for post in posts:

			if counter >= amount:
				break
			else:
				counter = counter + 1

			parameters = {'access_token' : token , 'type' : type}
			url = "https://graph.facebook.com/{0}/reactions".format(post['id'])
			s = requests.post(url, data = parameters)

			id = post['id'].split('_')[0]

			try:
				print W + '[' + G + id + W + '] ' + post['message'][:40].replace('\n',' ') + '...'
			except KeyError:
				try:
					print W + '[' + G + id + W + '] ' + post['story'].replace('\n',' ')
				except KeyError:
					print W + '[' + G + id + W + '] Successfully liked'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()

def comment(posts , amount):
	global message , token

	print '[*] All posts id successfuly retrieved'
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= amount:
				break
			else:
				counter = counter + 1

			parameters = {'access_token' : token, 'message' : message}
			url = "https://graph.facebook.com/{0}/comments".format(post['id'])
			s = requests.post(url, data = parameters)

			id = post['id'].split('_')[0]

			try:
				print W + '[' + G + id + W + '] ' +post['message'][:40].replace('\n',' ') + '...'
			except KeyError:
				try:
					print W + '[' + G + id + W + '] ' + post['story'].replace('\n',' ')
				except KeyError:
					print W + '[' + G + id + W + '] successfully commented'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
                print '\r[!] Stopped'
		bot()
#
######################################################################################################################

######################################################################################################################
#			bot comment and like
			   # Prepairing #
def bot_ask():
	global id , WT , token

	print '[*] load access token '
	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] Failed load access token'
		print "[!] type 'token' to generate access token"
		bot()

	WT = raw_input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
	if WT.upper() == 'T':
		id = raw_input('[?] id facebook : ')

		if id == '':
			print "[!] id target can't be empty"
			print '[!] Stooped'
			bot()

	else:
		WT = 'wallpost'

	like(post(),150)

def bot():
  try:
	global type , message , id , WT , token

	cek = raw_input(R + 'Karjok' + W +'/' + R +'Bot ' + W + '>> ')

	if cek == '1':
		type = "LIKE"
		bot_ask()
	elif cek == "2":
		type = "LOVE"
		bot_ask()
	elif cek == "3":
		type = "WOW"
		bot_ask()
	elif cek == "4":
		type = 'HAHA'
		bot_ask()
	elif cek == '5':
		type = 'SAD'
		bot_ask()
	elif cek == '6':
		type = 'ANGRY'
		bot_ask()
	elif cek == '7':
		print '[*] load access token'
		try:
			token = open('cookie/token.log','r').read()
		        print '[*] Success load access token'
		except IOError:
	                print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
	                bot()

		WT = raw_input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
		if WT.lower() == "w" or WT.lower() == '':
			WT = 'wallpost'
		else:
			id = raw_input('[?] Id Target : ')

			if id == '':
				print "[!] id target can't be empty"
				print '[!] Stopped'
				bot()

		print '--------------------------------------------------'
		print "  [Note] Use the '</>' symbol to change the line\n"

		message = raw_input('[?] Your Message : ')
		if message == '':
			print "[!] Message can't be emty"
			print '[!] Stopped'
			bot()
		else:
			message = message.replace('</>','\n')

		comment(post(),150)
	elif cek == '0':
		print '[*] Back to main menu'
		main()
	elif cek.lower() == 'menu':
		menu_bot()
		bot()
	elif cek.lower() == 'exit':
		print '[!] Exiting program'
		sys.exit()
	else:
		if cek == '':
			bot()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "menu" to show menu bot'
			bot()
  except KeyboardInterrupt:
	bot()
#
###############################################################################

###############################################################################
#                         Dump Data

def dump_id():

	print '[*] Load Access Token'
	try:
		token = open("cookie/token.log",'r').read()
		print '[*] success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all friends id'
	try:

		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_id.txt','w')
		for i in a['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.001)

		out.close()
		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_id.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] failed to fetch friend id'
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def dump_phone():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print "[*] fetching all phone numbers"
	print '[*] start\n'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_phone.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
			z = json.loads(x.text)

			try:
				out.write(z['mobile_phone'] + '\n')
				print ' ~ ' + z['name'] + G + ' >> ' + W + z['mobile_phone']
			except KeyError:
				pass
		out.close()
		print ' '
		print '[*] done'
		print "[*] all phone numbers successfuly retrieved"
		print '[*] file saved : output/'+n[0].split(' ')[0] + '_phone.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch all phone numbers"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def dump_mail():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
                print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all emails'
	print '[*] start\n'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
                a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_mails.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
                        z = json.loads(x.text)

			try:
                                out.write(z['email'] + '\n')
                                print ' ~ ' + z['name'] + G + ' >> ' + W + z['email']
			except KeyError:
				pass
		out.close()
		print ' '
                print '[*] done'
                print "[*] all emails successfuly retrieved"
		print '[*] file saved : output/'+n[0].split(' ')[0] + '_mails.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch all emails"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()
#
###############################################################################

###############################################################################
#                         Main

def main():
  try:
	cek = raw_input(R + 'Karjok' + W +' >> ')

	if cek.lower() == 'get_data':
		if len(jml) == 0:
			getdata()
		else:
			print '[*] You have retrieved %s friends data'%(len(jml))
			main()
	elif cek.lower() == 'get_info':
		print '\n'+'[*] Information Gathering [*]'.center(44) + '\n'
		search()
	elif cek.lower() == 'bot':
		menu_bot()
		bot()
	elif cek.lower() == "cat_token":
		try:
			o = open('cookie/token.log','r').read()
			print '[*] Your access token !!\n\n' + o + '\n'
			main()
		except IOError:
			print '[!] failed to open cookie/token.log'
			print "[!] type 'token' to generate access token"
			main()

	elif cek.lower() == 'clear':
		if sys.platform == 'win32':
			os.system('cls')
			baliho()
			main()
		else:
			os.system('clear')
			baliho()
			main()

	elif cek.lower() == 'token':
		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'

		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	elif cek.lower() == 'rm_token':
		print '''
[Warn] you must create access token again if 
       your access token is deleted
'''
		a = raw_input("[!] type 'delete' to continue : ")
		if a.lower() == 'delete':
			try:
				os.system('rm -rf cookie/token.log')
				print '[*] Success delete cookie/token.log'
				main()
			except OSError:
				print '[*] failed to delete cookie/token.log'
				main()
		else:
			print '[*] failed to delete cookie/token.log'
			main()
	elif cek.lower() == 'about':
		show_program()
		main()
	elif cek.lower() == 'exit':
		print "[!] Exiting Program"
		sys.exit()
	elif cek.lower() == 'help':
		info_ga()
		main()
	elif cek.lower() == 'dump_id':
		dump_id()
	elif cek.lower() == 'dump_phone':
		dump_phone()
	elif cek.lower() == 'dump_mail':
		dump_mail()
	else:
		if cek == '':
			main()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "help" to show command'
			main()
  except KeyboardInterrupt:
	main()
#
######################################################################################################################

################################################################################
#                          Get Data

def getdata():
	global a , token

	print '[*] Load Access Token'

	try:
		token = open("cookie/token.log","r").read()
		print '[*] Success load access token '
	except IOError:
		print '[!] failed to open cookie/token.log'
		print "[!] type 'token' to generate access token"
		main()

	print '[*] fetching all friends data'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

	except KeyError:
		print '[!] Your access token is expired'
		print "[!] type 'token' to generate access token"
		main()

	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

	for i in a['data']:
		jml.append(i['id'])
		print '\r[*] fetching %s data from friends'%(len(jml)),;sys.stdout.flush();time.sleep(0.001)

	print '\r[*] '+str(len(jml))+' data of friends successfully retrieved'
	main()

def search():

	if len(jml) == 0:
                print "[!] no friend data in the database"
                print '[!] type "get_data" to collect friends data'
                main()
        else:
                pass

	target = raw_input("[!] Search Name or Id : ")

	if target == '':
		print "[!] name or id can't be empty !!"
		search()
	else:
		info(target)

def info(target):
        global a , token

        print '[*] Searching ...'
	for i in a['data']:

	  if target in  i['name'] or target in i['id']:

		x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
		y = json.loads(x.text)

		print ' '
		print G + '[-------- INFORMATION --------]'.center(44)
		print W

		try:
			print '\n[*] Id : '+i['id']
		except KeyError:
			pass
		try:
			print '[*] Username : '+y['username']
		except KeyError:
			pass
		try:
			print '[*] Email : '+y['email']
		except KeyError:
			pass
		try:
			print '[*] Mobile Phone : '+y['mobile_phone']
		except KeyError:
			pass
		try:
			print '[*] Name : '+y['name']
		except KeyError:
			pass
		try:
			print '[*] First name : '+y['first_name']
		except KeyError:
			pass
		try:
			print '[*] Midle name : '+y['middle_name']
		except KeyError:
			pass
		try:
			print '[*] Last name : '+y['last_name']
		except KeyError:
			pass
		try:
			print '[*] Locale : '+y['locale'].split('_')[0]
		except KeyError:
			pass
		try:
			print '[*] location : '+y['location']['name']
		except KeyError:
			pass
		try:
			print '[*] hometown : '+y['hometown']['name']
		except KeyError:
			pass
		try:
			print '[*] gender : '+y['gender']
		except KeyError:
			pass
		try:
			print '[*] religion : '+y['religion']
		except KeyError:
			pass
		try:
			print '[*] relationship status : '+y['relationship_status']
		except KeyError:
			pass
		try:
			print '[*] political : '+y['political']
		except KeyError:
			pass
		try:
			print '[*] Work :'

			for i in y['work']:
				try:
					print '   [-] position : '+i['position']['name']
				except KeyError:
					pass
				try:
					print '   [-] employer : '+i['employer']['name']
				except KeyError:
					pass
				try:
					if i['start_date'] == "0000-00":
						print '   [-] start date : ---'
					else:
						print '   [-] start date : '+i['start_date']
				except KeyError:
					pass
				try:
					if i['end_date'] == "0000-00":
						print '   [-] end date : ---'
					else:
						print '   [-] end date : '+i['end_date']
				except KeyError:
					pass
				try:
					print '   [-] location : '+i['location']['name']
				except KeyError:
					pass
				print ' '
		except KeyError:
			pass
		try:
			print '[*] Updated time : '+y['updated_time'][:10]+' '+y['updated_time'][11:19]
		except KeyError:
			pass
		try:
			print '[*] Languages : '
			for i in y['languages']:
				try:
					print ' ~ '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] Bio : '+y['bio']
		except KeyError:
			pass
		try:
			print '[*] quotes : '+y['quotes']
		except KeyError:
			pass
		try:
			print '[*] birthday : '+y['birthday'].replace('/','-')
		except KeyError:
			pass
		try:
			print '[*] link : '+y['link']
		except KeyError:
			pass
		try:
			print '[*] Favourite teams : '
			for i in y['favorite_teams']:
				try:
					print '  ~ '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] School : '
			for i in y['education']:
				try:
					print ' ~ '+i['school']['name']
				except KeyError:
					pass
		except KeyError:
			pass
	  else:
		pass

        else:
		print W + ' '
		print '[*] Done ... '
		main()

#
##########################################################################

##########################################################################
#

if __name__ == '__main__':

	baliho()
	main()

#
##########################################################################
