#!/usr/bin/python

####
#  mmake.py
####  

import sys, os

DIFF = "diff -q -Bb"
TIME = "/usr/bin/time"

def usage():
	print "usage: %s sol|diff|time exec\n" %(sys.argv[0])
	sys.exit(1)

if (__name__ == "__main__"):

	####
	# get arguments
	####

	try:
		cmd = sys.argv[1]
		exe = sys.argv[2]
	except:
		usage()

	####
	# gen sample solution files
	####
	if cmd=='sample':
		base=os.path.join("..","tests","test0")
		ok=True
		for i in range(1,100):
			inp = os.path.join(base,"in")
			out = os.path.join(base,"out")
			if not os.path.exists("%s%d" % (inp,i)): break
			os.system("./%s < %s%d > %s%d" % (exe,inp,i,out,i))
			print >> sys.stderr, "%s%d" % (out,i)

	####
	# gen solution files
	####
	elif cmd=='sol':
		for j in range(1,101):
			base=os.path.join("..","tests","test%d" % j)
			if not os.path.exists(base): break
			for i in range(1,101):
				inp = os.path.join(base,"in")
				out = os.path.join(base,"out")
				if not os.path.exists("%s%d" % (inp,i)): break
				os.system("./%s < %s%d > %s%d" % (exe,inp,i,out,i))
				print >> sys.stderr, "%s%d" % (out,i)

	####
	# compare solution files
	####
	elif cmd=='diff':
		for j in range(0,101):
			base=os.path.join("..","tests","test%d" % j)
			if not os.path.exists(base): break
			for i in range(1,101):
				inp = os.path.join(base,"in")
				out = os.path.join(base,"out")
				if not os.path.exists("%s%d" % (inp,i)): break
				print >> sys.stderr, "%s%d" % (out,i)
				os.system("./%s < %s%d | %s -  %s%d" % (exe,inp,i,DIFF,out,i))

	####
	# change to dos line terminator
	####
	elif cmd=='todos':
		for j in range(0,101):
			base=os.path.join("","","test%d" % j)
			if not os.path.exists(base): break
			for i in range(1,101):
				inp = os.path.join(base,"in")
				out = os.path.join(base,"out")
				if not os.path.exists("%s%d" % (inp,i)): break
				print >> sys.stderr, "%s%d" % (out,i)
				os.system("~/bin/unix2dos.py < %s%d > tmp; mv tmp %s%d" % (inp,i,inp,i))
				os.system("~/bin/unix2dos.py < %s%d > tmp; mv tmp %s%d" % (out,i,out,i))

	####
	# change to dos line terminator
	####
	elif cmd=='tounix':
		for j in range(0,101):
			base=os.path.join("","","test%d" % j)
			if not os.path.exists(base): break
			for i in range(1,101):
				inp = os.path.join(base,"in")
				out = os.path.join(base,"out")
				if not os.path.exists("%s%d" % (inp,i)): break
				print >> sys.stderr, "%s%d" % (out,i)
				os.system("~/bin/dos2unix.py < %s%d > tmp; mv tmp %s%d" % (inp,i,inp,i))
				os.system("~/bin/dos2unix.py < %s%d > tmp; mv tmp %s%d" % (out,i,out,i))


	# measure time
	####
	elif cmd=='time':
		for j in range(1,101):
			base=os.path.join("..","tests","test%d" % j)
			if not os.path.exists(base): break
			for i in range(1,101):
				inp = os.path.join(base,"in")
				out = os.path.join(base,"out")
				if not os.path.exists("%s%d" % (inp,i)): break
				print >> sys.stderr, "%s%d" % (out,i)
				os.system("%s ./%s < %s%d > %s" % (TIME,exe,inp,i,"tmptmptmp"))
				os.system("rm tmptmptmp")

	else:
		usage()
