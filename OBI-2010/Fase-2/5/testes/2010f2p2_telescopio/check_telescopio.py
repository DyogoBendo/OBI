#!/usr/bin/python

####
#  check_matrizes.py
####  

import sys, os, string, re

line_number=0
finput=''

def get_integer(s,MIN,MAX):
	global line_number
	try:
		v=int(s)
	except:
		print >> sys.stderr, 'integer expected (line %d)' % line_number
		sys.exit(-1)
	if v<MIN or v>MAX:
		print >> sys.stderr, 'integer outside limits (line %d)' % line_number, v
		sys.exit(-1)
	return v

def get_string_letters(s,MAX):
	global line_number
	if len(s)>MAX:
		print >> sys.stderr, 'string size outside limits (line %d)' % line_number
		sys.exit(-1)
	for c in s:
		if c not in string.lowercase:
			print >> sys.stderr, 'string contents, unexpected char (line %d)' % line_number
			sys.exit(-1)
	return s

def get_line():
	global line_number
	l=finput.readline()
	if not l:
		print >> sys.stderr, 'unexpected end of file (line %d)' % line_number
		sys.exit(-1)
	if l[0]==' ' or l[-1]==' ' or l.find('  ')>0:
		print >> sys.stderr, 'spaces in wrong places (line %d)' % line_number
		sys.exit(-1)
	line_number+=1
	return l.split(' ')


def check(finput,N):
	global line_number
	line_number=1
	tokens=get_line()
	a=get_integer(tokens[0],1,10000)
	tokens=get_line()
	n=get_integer(tokens[0],1,N)
	for i in range(n):
		tokens=get_line()
		f=get_integer(tokens[0],0,20000)
	# end of file
	l=finput.readline()
	if l:
		print >> sys.stderr, 'wrong values (line %d)' % line_number
			

if (__name__ == "__main__"):
	####
	# check input
	####
	for j in range(1,2):
		base=os.path.join("..","tests","test%d" % j)
		if not os.path.exists(base): break
		for i in range(1,101):
			inp = os.path.join(base,"in")
			if not os.path.exists("%s%d" % (inp,i)): break
			print >> sys.stderr, "%s%d" % (inp,i)
			finput=open("%s%d" % (inp,i))
			check(finput,10)
	for j in range(2,4):
		base=os.path.join("..","tests","test%d" % j)
		if not os.path.exists(base): break
		for i in range(1,101):
			inp = os.path.join(base,"in")
			if not os.path.exists("%s%d" % (inp,i)): break
			print >> sys.stderr, "%s%d" % (inp,i)
			finput=open("%s%d" % (inp,i))
			check(finput,100)
	for j in range(4,101):
		base=os.path.join("..","tests","test%d" % j)
		if not os.path.exists(base): break
		for i in range(1,101):
			inp = os.path.join(base,"in")
			if not os.path.exists("%s%d" % (inp,i)): break
			print >> sys.stderr, "%s%d" % (inp,i)
			finput=open("%s%d" % (inp,i))
			check(finput,10000)
			
	else:
		print >> sys.stderr, "usage: %s problem_name\n" %(sys.argv[0])
		sys.exit(1)
