#!/usr/bin/env python
import codecs
import locale
import sys

# Wrap sys.stdout into a StreamWriter to allow writing unicode.
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 

import time as stime

from termcolor import colored
from lxml import html
import requests
from pprint import pprint
import sys, getopt

def usage():
        print "GIO (Games of Interest), Version 4.0"
	print 'gio.py -s[--sport] <sport> [-d[--day]] <day>'
        print "supported sports are cbb, nba, cfl, and mlb"
        print "example: ./goi.py -s cbb -d Sunday"
        

def main(argv):
        found_s = False
	dayFilter = None
	try:
	    opts, args = getopt.getopt(argv,"hs:d:",["help", "sport=", "day="])
        except getopt.GetoptError:
            usage()
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                usage()                     
                sys.exit(2)
            elif opt in ("-s", "--sport") and arg in ("cbb","nba","cfl","mlb"): 
                sport=arg
                found_s = True
            elif opt in ("-d", "--day"):
                dayFilter=arg
            else:
                usage()
        if not found_s:
            usage()
            sys.exit(2)

	baseURL="http://statfeed.statfox.com"
        wwwBaseURL="http://www.statfox.com"
	daily = requests.get(baseURL+'/feed/statfeedv2/'+sport+'/daily.php?sn=5')
	tree = html.fromstring(daily.content)
	reports = tree.xpath('//a[@class="sf" and text()="Report"]/@href')

        print "Updated: " + stime.strftime("%c") + "\n\n"

	for report in reports:
	    page = requests.get(baseURL+report)
	    tree = html.fromstring(page.content)
	    edge = tree.xpath('//td/img[@src="http://statfeed.statfox.com/images/star.gif"]/preceding::td[2]/text()')
	    if edge:
		edgeTeam = edge[0].strip()

		tree = html.fromstring(page.content)
		day = tree.xpath('normalize-space((//table[@class="datatable"]/tr[1]/th[1]/text())[1])')

		if dayFilter is None or dayFilter.lower() in day.lower():

			time = tree.xpath('normalize-space((//table[@class="datatable"]/tr[1]/th[1]/b/text())[1])')

			hteam = tree.xpath("string((//td[contains(@class, 'matchupCells')])[4])").strip()
			hestimate = tree.xpath("string((//td[contains(@class, 'matchupCells')])[5])").strip()

			ateam = tree.xpath("string((//td[contains(@class, 'matchupCells')])[1])").strip()
			aestimate = tree.xpath("string((//td[contains(@class, 'matchupCells')])[2])").strip()

			ateam = ateam.strip()
			hteam = hteam.strip()
			# get real spread
			page = requests.get(wwwBaseURL+'/'+sport+'/gamematchup.asp')
			tree = html.fromstring(page.content)
			ateamLine = tree.xpath("string((//td/a[text()='"+ateam+"']/following::td[1])[2])")
			hteamLine = tree.xpath("string((//td/a[text()='"+hteam+"']/following::td[1])[2])")

			ateamDisplay=ateam+" "+ateamLine
			hteamDisplay=hteam+" "+hteamLine

			print day + " " + time

			if aestimate:
				if hteamLine == "PK":
					hteamLine = 0
				if float(hteamLine) > 0:
				    lineDiff = abs(abs(float(hteamLine)) - abs(float(aestimate)))
				else: 
				    lineDiff = abs(float(hteamLine) + float(aestimate))
				ateamDisplay=ateamDisplay+" ("+aestimate+" powerspread)"
			if hestimate:
				if hteamLine == "PK":
                                        hteamLine = 0
                                lineDiff = abs(abs(float(hteamLine)) - abs(float(hestimate)))
				hteamDisplay=hteamDisplay+" ("+hestimate+" powerspread)"

			if ateam==edgeTeam:
			    ateamDisplay=ateamDisplay+", "+str(lineDiff)+"pt edge"
			elif hteam==edgeTeam:
			    hteamDisplay=hteamDisplay+", "+str(lineDiff)+"pt edge"

                        if lineDiff >= 6:
                            print colored("$$$$************Big Money************$$$$",'green')

			print ateamDisplay
			print hteamDisplay
			print "\n"

if __name__ == "__main__":
   main(sys.argv[1:])

