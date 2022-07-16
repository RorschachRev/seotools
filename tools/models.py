from django.db import models,connections
from django.core.urlresolvers import reverse
class temp: pass

#bingscrape.py
import requests#, whois
from BeautifulSoup import BeautifulSoup as BS
from hashlib import sha256
from socket import gethostbyname as dns
from dateutil import parser as dtparse
import httplib
import random
import pycurl
import xml.etree.ElementTree as ET
import StringIO

def GetHash (query):
	SEED = "Mining PageRank is AGAINST GOOGLE'S TERMS OF SERVICE. Yes, I'm talking to you, scammer."
	Result = 0x01020345
	for i in range(len(query)) :
		Result ^= ord(SEED[i%len(SEED)]) ^ ord(query[i])
		Result = Result >> 23 | Result << 9
		Result &= 0xffffffff
	return '8%x' % Result
def GetPageRank (query):
	#mozaccessID=member-5ef61f5695		https://moz.com/products/api/keys
	#secretkey=234ec52ff69174b858d16bd1b53517f8
	
	prhost='toolbarqueries.google.com'
	prpath='/tbr?client=navclient-auto&ch=%s&features=Rank&q=info:%s'
	conn = httplib.HTTPConnection(prhost)
	hash = GetHash(query)
	conn.request("GET", prpath % (hash,query) )
	response = conn.getresponse()
	data = response.read()
	conn.close()
	pr= data.split(":")[-1]
	if len(pr) > 0 and len(pr) <13 : #tos is 38, pr10 is 11
		if int(pr) >= 0:
			return int(pr)
		else:
			return -1
	else:
		return -1
			
#TODO: if getting backlinks had an error, we need to resume!
class WebDomain_Manager(models.Manager):
	def new_dom(self,dom):
		chunks=dom.split(".")
		if chunks[0] in ['www', 'm'] or chunks[0].isdigit():	#add country codes?
			chunks=chunks[1:]
			base='.'.join(chunks)
		try:
			d= WebDomain.objects.get(domain_fqdn=dom)
		except:
			d= 0
		if d:
			return(d)
		else:
			try:
				if chunks[-2]=="co":
					droot=chunks[-3]
				else:
					droot=chunks[-2]
			except:	#index error, shouldn't happen. if it does, I want to save it big and bold
				droot=dom
			#~ ip=dns(dom)
			#~ ipoct=ip.split('.')[:3]+[0]
			
			#~ w=whois.whois(str(dom))
			#~ try:
				#~ whoisc=w.creation_date.year
				#~ whoise=w.expiration_date.year
			#~ except:
			whoisc=0
			whoise=0
				#~ z=w.text.split("\n")
				#~ for x in z:
					#~ if "Date" in x:
						#~ if "eati" in x or "tart" in x:		#creation, start
							#~ whoisc=dtparse.parse(x.split(":")[1]).year
						#~ if "xpir" in x:					#expiry expiration
							#~ whoise=dtparse.parse(x.split(":")[1]).year
			dpr=GetPageRank('http://'+dom+'/')
			if dpr > 0:
				prrange=WebDomain.prlist[dpr]
				prest=random.randrange( prrange[0], prrange[2] )
			else:
				prest=0.15
			#~ d=WebDomain(domain_fqdn=dom, pagerank= dpr,pagerank_real= prest, domainIP=ip, subnetIP=".".join(map(str,ipoct)) , whoisexpire=whoise, whoiscreate=whoisc, \
			d=WebDomain(domain_fqdn=dom, pagerank= dpr,pagerank_real= prest, domainIP='', subnetIP='', whoisexpire=whoise, whoiscreate=whoisc, \
					domain_tld= base, domain_root=droot)
			d.save()
			return(d)
	def get_dom(self,dom):
		return super(WebDomain_Manager, self).filter(domain_fqdn=dom)
		#~ return super(WebDomain_Manager, self).all()

class WebPage_Manager(models.Manager):
	def get_url(self, dom):
		return super(WebPage_Manager, self).filter(domain=dom)
		#~ return super(WebPage_Manager, self).all()
		#~ return (0, 0)
	def get_bl(self,dom):
		chunks=dom.split(".")
		try:
			client_d= WebDomain.objects.get(domain_fqdn=dom)
		except:
			client_d= 0
		if client_d:
			urls=WebPage.objects.filter(domain=dom)
			total=len(urls)
		else:
			urls=[]
			c = pycurl.Curl()
			url="https://api.datamarket.azure.com/Bing/Search/v1/Web?Query=%27inbody%3A%22"+str(dom)+"%22%27&Adult=%27Off%27"
			c.setopt(pycurl.URL, url) 
			c.setopt(pycurl.HTTPHEADER, ["Accept:"])
			AppID= "REdwSkwvZ3dBVjhyUVFRdlNSOGd2cDlLaXhLMFRzemZNWHVGQVZvZnkvODpER3BKTC9nd0FWOHJRUVF2U1I4Z3ZwOUtpeEswVHN6Zk1YdUZBVm9meS84"
			c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0")
			c.setopt(pycurl.HTTPHEADER, ["Authorization: Basic "+AppID])
			c.setopt(pycurl.FOLLOWLOCATION, 1)
			c.setopt(pycurl.MAXREDIRS, 5)
			b = StringIO.StringIO()
			c.setopt(pycurl.WRITEFUNCTION, b.write)
			c.perform()
			f=open("allbingbl.xml","a")
			f.write(b.getvalue())
			f.flush()
			urls=[]
			root = ET.fromstring(b.getvalue())
			 #~ root= tree.getroot()
			entries=root.findall('{http://www.w3.org/2005/Atom}entry')
			for e in entries:
				urls.append(e[3][0][4].text)						
			set = 0				
			for page in xrange(0,21):
				set=set+1
				#~ c.setopt(pycurl.URL, "https://api.datamarket.azure.com/Bing/Search/v1/Web?Query=%27inbody%3A%22"+str(dom)+"%22%27&Adult=%27Off%27&$skip="+set*50) 
				url="https://api.datamarket.azure.com/Bing/Search/v1/Web?Query=%27inbody%3A%22"+str(dom)+"%22%27&Adult=%27Off%27&$skip="+str(set*50)
				c.setopt(pycurl.URL, url) 
				b = StringIO.StringIO()
				c.setopt(pycurl.WRITEFUNCTION, b.write)
				c.perform()
				f.write(b.getvalue())
				f.flush()
				root= ET.fromstring(b.getvalue())
				#~ tree = ET.fromstring(b.getvalue())
				#~ root = tree.getroot()
				entries=root.findall('{http://www.w3.org/2005/Atom}entry')
				for e in entries:
					urls.append(e[3][0][4].text)						
				if len(entries) < 5:
					break
			f.close()		
			WebDomain.objects.new_dom(dom)
			client_d= WebDomain.objects.get(domain_fqdn=dom)
			#~ raise()
			for u in urls:
				linkd=	WebDomain.objects.new_dom(u.split('/')[2])
				#~ ppr=GetPageRank(u)
				ppr=-2
				sub= WebPage(domain=client_d, doc_domain=linkd, url_sha=sha256(u).hexdigest(), url_page=u, doc_changed= False, doc_live=True, links_int_on_page=0, links_ext_on_page=0, links_ad_on_page= 0, page_PR=ppr, page_PRreal=-1.0  ) 
				sub.save()
		return( len(urls) )
		
class WebDomain(models.Model):
	prlist=[(0,10,5),
		(11,120,65),
		(120,1328,724),
		(1328,14602,7965),
		(14602,160480,87541),
		(160480,1763681,962081),
		(1763681,19382862,10573272),
		(19382862,213017664,116200263),
		(213017664,2341064130,1277040897),
		(2341064130,25728294792,14034679461),
		(25728294792,282753959767,154241127280),
	]

	domain_fqdn=models.CharField(max_length=256, primary_key=True)
	domain_root=models.CharField(max_length=256)		#www.ibm.com become ibm
	domain_tld=models.CharField(max_length=20)		#www.ibm.com becomes com		#summary
	pagerank= models.IntegerField()		#inc
	pagerank_real= models.FloatField()	
	domainIP=models.IPAddressField()		#inc
	subnetIP=models.IPAddressField()		#inc
	country_code=models.CharField(max_length=3)
	http_header=models.TextField()		#lynx -head -dump
	whoiscreate= models.IntegerField()		#inc
	whoisexpire= models.IntegerField()		#inc
	objects= WebDomain_Manager()
	
class WebPage(models.Model):		#this is a page
	#~ pass
	url_sha=models.CharField(max_length=64, primary_key=True)	#sha256 of the URL
	url_page=models.URLField(max_length=1024)		#actual URL fetched, this should probably become a foreign key later			#inc
	domain=models.ForeignKey(WebDomain, related_name='domain_fqdn+')			#Domain of client - this is very useful for lookup	
	
	doc_domain=models.ForeignKey(WebDomain, related_name='domain_fqdn+')		#Domain of page - this is very useful for lookup	#inc
	doc_id=models.CharField(max_length=64)		#sha256 of the document
	doc_changed=models.BooleanField()		#Has the document changed since first crawl? Which sections are critical for this? SHA will reveal delta
	doc_live=models.BooleanField()		#currently returns this document or other										#inc
	
	page_PR= models.IntegerField()					#inc
	page_PRreal= models.FloatField()
	
	links_int_on_page=models.PositiveSmallIntegerField() 	#inc
	links_ext_on_page=models.PositiveSmallIntegerField() 	#inc
	links_ad_on_page=models.PositiveSmallIntegerField() 	#inc?
	
	url_desc_goog=models.TextField()			#as it appears on search engines
	url_desc_bing=models.TextField()			#as it appears on search engines
	
	page_dmoz_link=models.URLField(max_length=1024) 	#inc
	page_dmoz_desc=models.TextField()			#inc
	
	doc_content_text=models.TextField()			#stripped down text
	doc_content_head=models.TextField()			#head minus javascript
	doc_content_html=models.TextField()			#full html of page, try to discard this ASAP
#language
#authority
#meta:
	page_title=models.CharField(max_length=1024) 	#inc
	#title, keyword, etc
	#microformats
	#special: google tags, author, publisher, dublincore, All Possibly Disambiguating Data
	#standard
	#uses CDN content 
	#canonical - disambiguation of URL
	#membership in Sitemap boolean
	#Header Text or IMG
	
	#forwards barrels, backwards barrels, buckets
	
	index_date=models.DateTimeField(auto_now=True)	#inc
	objects= WebPage_Manager()
#~ class WebObject(models.Model):
	#of type: Text, IMG, href, special media(audio, video, plugins, java, silverlight)
	#where it occurred
	#what occurred around it
	#anchor# ?
	#~ pass
#~ class WebImage(models.Model):
	#~ pass
	#html
	#alt
	#title
	#href
	#image dimensions (icon sets)
	
#~ class WebSocial(models.Model):
	#site
	#hashtag
	#linked profileID
	#~ pass
	
class URL_Link(models.Model):		#this is a link on a page
	tar_title =models.CharField(max_length=1024)
	tar_href=models.URLField(max_length=1024)
	tar_anchor=models.CharField(max_length=1024)
	tar_url=models.CharField(max_length=1024)
	tar_dom=models.ForeignKey(WebDomain, related_name='domain_fqdn+')
	tar_url_sha=models.CharField(max_length=64) #from <a to </a>
	tar_url_nofollow=models.BooleanField()
	tar_url_sitewide=models.BooleanField()
	tar_url_type=models.PositiveSmallIntegerField() #0 = text, 1 = iframe, 2 = img, 3 = redirect, 4 = JS, 5= form, 6 = social, 7= ad, ... 10= other
	url_redirect=models.URLField(max_length=1024)		#redirect URL, this is essentially chaining. TODO Figure out better data representation
	url_redirect_code=models.IntegerField()		#redirect code: 301, 302, 404, etc
	
	divtop =models.CharField(max_length=256)	#what was the name of the top div
	divpath =models.CharField(max_length=1024)	#total div path from Doc to link 
	link_pos=models.PositiveSmallIntegerField() #0 = body, 1 = left, 2 = right, 3 = header, 4 = footer, 5= head, 6 = other
	src_url_sha=models.ForeignKey(WebPage, related_name='+')
	tar_url_sha=models.ForeignKey(WebPage, related_name='+')
	#what kind of data is Authority?
	index_date=models.DateTimeField(auto_now=True)

class TermsManager(models.Manager):
	def testraw(self,term):
		q="""SELECT ssensenum AS sense, spos AS pos, sw.lemma AS swlem, link, dw.lemma AS linklem,  sdefinition as sdef
			FROM sensesXsemlinksXsenses AS l
			LEFT JOIN words AS sw ON l.swordid = sw.wordid
			LEFT JOIN words AS dw ON l.dwordid = dw.wordid
			LEFT JOIN linktypes
			USING ( linkid ) 
			WHERE sw.lemma = %s
			ORDER BY pos, sense, linkid"""
		#term="reading"
		conn=connections['wn']
		c=conn.cursor()
		c.execute(q,[term])
		if not c.rowcount: 	#If 0 rows
			q1="""SELECT lemma FROM  `morphology` WHERE morph =  %s """
			c.execute(q1,[term])
			if c.rowcount: 	#If rows > 0
				r=dictfetchall(c)
				c.execute(q,[r[0]['lemma']])
			elif len(term) > 3:
				if term[-2:] =="es":
					q="""SELECT ssensenum AS sense, spos AS pos, sw.lemma AS swlem, link, dw.lemma AS linklem,  sdefinition as sdef
			FROM sensesXsemlinksXsenses AS l
			LEFT JOIN words AS sw ON l.swordid = sw.wordid
			LEFT JOIN words AS dw ON l.dwordid = dw.wordid
			LEFT JOIN linktypes
			USING ( linkid ) 
			WHERE sw.lemma = %s
			ORDER BY pos, sense, linkid"""
					#term="reading"
					conn=connections['wn']
					c=conn.cursor()
					c.execute(q,[term[:-2]])
					if not c.rowcount: 	#If 0 rows
						q1="""SELECT lemma FROM  `morphology` WHERE morph =  %s """
						c.execute(q1,[term[:-2]])
						if c.rowcount: 	#If rows > 0
							r=dictfetchall(c)
							c.execute(q,[r[0]['lemma']])
							if c.rowcount:
								return dictfetchall(c)
				if term[-1:] == "s":
					q="""SELECT ssensenum AS sense, spos AS pos, sw.lemma AS swlem, link, dw.lemma AS linklem,  sdefinition as sdef
			FROM sensesXsemlinksXsenses AS l
			LEFT JOIN words AS sw ON l.swordid = sw.wordid
			LEFT JOIN words AS dw ON l.dwordid = dw.wordid
			LEFT JOIN linktypes
			USING ( linkid ) 
			WHERE sw.lemma = %s
			ORDER BY pos, sense, linkid"""
					#term="reading"
					conn=connections['wn']
					c=conn.cursor()
					c.execute(q,[term[:-1]])
					if not c.rowcount: 	#If 0 rows
						q1="""SELECT lemma FROM  `morphology` WHERE morph =  %s """
						c.execute(q1,[term[:-1]])
						if c.rowcount: 	#If rows > 0
							r=dictfetchall(c)
							c.execute(q,[r[0]['lemma']])
							if c.rowcount:
								return dictfetchall(c)
				else:
					return {}
		return dictfetchall(c)
class Terms(models.Model):
	sense= models.IntegerField()
	pos=models.CharField(max_length=1, blank=True)
	swlem= models.CharField(max_length=80, blank=True)
	link = models.CharField(max_length=50, blank=True)
	linklem = models.CharField(max_length=80, blank=True)
	sdef = models.TextField(blank=True)
	objects= TermsManager()

class VerbDictManager(models.Manager):
	def verbdef(self,v):
		q=u"""SELECT lemma,synsetid,definition,parse FROM words LEFT JOIN senses USING (wordid) INNER JOIN synsets USING (synsetid) INNER JOIN xwnparselfts USING (synsetid) WHERE pos='v' and lemma=%s"""
		conn=connections['wn']
		c=conn.cursor()
		c.execute(q,[v])
		return dictfetchall(c)
class VerbDict(models.Model):
	lemma=models.CharField(max_length=80, blank=True)
	synsetid=models.IntegerField()
	definition=models.TextField(blank=True)
	parse=models.TextField(blank=True)
	objects= VerbDictManager()

class DictManager(models.Manager):
	def getdef(self,term):
		q="""SELECT lemma,pos,sensenum,synsetid,definition AS defin,sampleset AS sample FROM dict WHERE lemma = %s ORDER BY pos,sensenum"""
		conn=connections['wn']
		c=conn.cursor()
		c.execute(q,[term])
		return dictfetchall(c)
class WNDict(models.Model):
	lemma=models.CharField(max_length=80, blank=True)
	pos=models.CharField(max_length=1, blank=True)
	sensenum=models.IntegerField()
	synsetid=models.IntegerField()
	defin=models.TextField(blank=True)
	sample=models.TextField(blank=True)
	objects= DictManager()
	
def dictfetchall(cursor):
	"Returns all rows from a cursor as a dict"
	desc = cursor.description
	return [
		dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()
	]
class WP_User_Manager(models.Manager):
	def get_wpuser(self,username):
		q="""SELECT user_id, membership_id, status FROM `wp_pmpro_memberships_users` AS wpmem LEFT JOIN `wp_users` AS wpuser ON wpmem.user_id = wpuser.ID WHERE wpuser.user_nicename=%s"""
		q1=""" SELECT * FROM  `wp_usermeta` WHERE user_id =%s AND meta_key =  'domain_name' """
		conn=connections['wp']
		c=conn.cursor()
		c.execute(q, [username])
		r=dictfetchall(c)
		c1=conn.cursor()
		c1.execute(q1,[r[0]['user_id']])
		r1=dictfetchall(c1)
		if c1.rowcount:
			r[0]['domain_name']=r1[0]['meta_value']
		else:
			r[0]['domain_name']=''
		return( r )
class WP_User(models.Model):
	user_id=models.IntegerField()
	membership_id=models.IntegerField()
	status=models.CharField(max_length=32, blank=True)
	domain_name=models.CharField(max_length=256, blank=True)
	objects= WP_User_Manager()
