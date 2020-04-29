import os
import sys
import requests
import google
import argparse




def facebook_gather(word):
	print(word)

def twitter_gather(word):
	print (word)

def reddit_gather(word):
	print (word)

def main():
	parser = argparse.ArgumentParser(description="Information Gathering tool")
	parser.add_argument('-d','--domain'
		,help="domain name to gather info")
	parser.add_argument('-f','--facebook'
		,help="facebook option for gather information")
	parser.add_argument('-t','--twitter'
		,help="twitter option for gather information")
	parser.add_argument('-r','--reddit'
		,help="reddit option for gather information")
	args = parser.parse_args()
	if args.facebook.lower() == "true":
		info = facebook_gather(args.domain)
	if args.twitter.lower() == "true":
		info = twitter_gather(args.domain)
	if args.reddit.lower() == "true":
		info = reddit_gather(args.domain)


if __name__ == "__main__":
	main()