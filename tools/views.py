#from django.core import serializers
from django.utils import simplejson
from django.shortcuts import render, get_object_or_404
from tools.models import Terms, VerbDict, WNDict, WP_User
from tools.models import URL_Link, WebPage, WebDomain
from django.http import HttpResponseRedirect
import logging
from nltk.tag.simplify import simplify_wsj_tag
import nltk, string
import re

stopwords = nltk.corpus.stopwords.words('english')
swlfile=open('stopwordlist.txt')
for s in swlfile:
	stopwords.append(s.strip())
swlfile.close()
stopwords=set(stopwords)
regex = re.compile('[%s]' % re.escape(string.punctuation))
class temp: pass
def pr_est(request):
	u=temp()	
	u.user, u.group, u.uid, u.web= getuser(request)
	if u.group is 0:
		return HttpResponseRedirect("http://www.seogods.net/?page_id=131")
	dominfo=WebDomain.objects.get(domain_fqdn=u.web)
	return render(request, 'tools/pr_estimate.html', {'u': u,'dom':dominfo})

def getuser(request):
	logging.basicConfig(filename='test.log',level=logging.INFO)
	group=0
	id=0
	user="Guest"
	cookie= request._get_cookies()
	for k,v in cookie.iteritems():
		if k.startswith('wordpress_logged_in'):
			u=v.split('%7C')
			if len(u)==3: #no forging usernames by doing %7C in username
				user=u[0]
	if user == "Guest":
		user=0
		group=0
		id=0
		ug=0
		web=''
		#~ return HttpResponseRedirect("http://www.seogods.net/?page_id=131")
	else:
		ug=WP_User.objects.get_wpuser(user)
		try:
			if ug[0]['status'] =='active':
				group=ug[0]['membership_id']
				id=ug[0]['user_id']
				web=ug[0]['domain_name']
			else:
				user=group=id=ug=0
				web=''
		except:
			pass	#TODO redirect user to login page
	#~ logging.info("%s %s %s %s" % (user, group, id, ug.__str__() ) )
	return [user,group, id, web ]
 
def kw_vocab(request):
	try:
		s=request.POST['inputtext']
		s=s.split('.')[0]
		ss=regex.sub('', s)
		tokens = nltk.word_tokenize(ss)
	except:
		ss="This is sample text for analysis"
		tokens = nltk.word_tokenize(ss)
	u=temp()	
	u.user, u.group, u.uid, u.web= getuser(request)
	
	content = [w.lower() for w in tokens if w.lower() not in stopwords]
	if u.group <= 8:
		try:	
			content = content[:5]
		except:		#less than 5
			pass
	elif u.group == 9:
		try:
			content = content[:20]
		except:		#less than 20
			pass
	#Premiere and up, no word limit
	tagged_sent = nltk.pos_tag(content) 	#or tokens if stopwords skipped
	shortlist = [(word, simplify_wsj_tag(tag)) for word, tag in tagged_sent]
	terms=[]
	for s in shortlist:
		if s[1] not in ["ADJ", "ADV", "S"]:
			if s[0] not in terms:
				terms.append(s[0])
	terms.sort()
	if u.group <8:
		shortlist = ''		
	return render(request, 'tools/mockup2.html', {'u':u, 'tokens': tokens, 'terms':terms, 'withpos':shortlist})

def index(request):
	u=temp()	
	u.user, u.group, u.uid, u.web= getuser(request)
	if u.group is 0:
		return HttpResponseRedirect("http://www.seogods.net/?page_id=131")
	return render(request, 'tools/index.html', {'u': u})
	 
def bing_bl(request):
	u=temp()	
	urls=temp()
	u.user, u.group, u.uid, u.web= getuser(request)
	if u.group is 0:
		return HttpResponseRedirect("http://www.seogods.net/?page_id=131")	
	chunks=u.web.split(".")
	if chunks[0] in ['www', 'm'] or chunks[0].isdigit():
		chunks=chunks[1:]
		u.web='.'.join(chunks)
	
	if u.group >= 10:		#allows domain submission
		try:
			s=request.POST['domainin']
			u.web=s
		except:
			pass
	urls.total=WebPage.objects.get_bl(u.web)
			#~ #urls.reported,urls.total=WebPage.objects.get_url(u.web)		
	#~ urls=BL_Url.objects.get_url(u.web)		
	#~ db=WebPage.objects.get_url(u.web)
	db=WebPage.objects.filter(domain=u.web).order_by('doc_domain__domain_fqdn')
	#~ for page in db:
		#~ d=WebDomain.objects.get(domain_fqdn=page.doc_domain)
	return render(request, 'tools/backlinks.html', {'urls':urls, 'u': u, 'db':db})

def term_json(request, term):
	rows=Terms.objects.testraw(term)
	tags= simplejson.dumps(rows)
	return render(request, 'term.json', {'tags': tags, 'term':term})

def term_js(request, term):
	rows=Terms.objects.testraw(term)
	return render(request, 'term.js', {'rows': rows, 'term':term})

def wn_lemma(request, term):
	u=temp()	
	u.user, u.group, u.uid, u.web= getuser(request)
	
	rows=Terms.objects.testraw(term)
	return render(request, 'tools/terms.html', {'u':u,'rows': rows, 'term':term})

def verb_parse(request):
	u=temp()	
	u.user, u.group, u.uid, u.web= getuser(request)
	rows=VerbDict.objects.verbdef('want')
	return render(request, 'tools/verbs.html',{'u':u,'rows':rows})

def verb(request, verb):
	u=temp()	
	u.user, u.group, u.uid, u.web= getuser(request)
	rows=VerbDict.objects.verbdef(verb)
	return render(request, 'tools/verbs.html', {'u':u, 'rows': rows})

def wn_dict(request, term):
	u=temp()	
	u.user, u.group, u.uid, u.web= getuser(request)

	rows=WNDict.objects.getdef(term)
	return render(request, 'tools/dict.html',{'u':u,'rows':rows, 'term':term})

def content_fraction(text):
	content = [w for w in text if w.lower() not in stopwords]
	return 1.0* len(content) / len(text)

