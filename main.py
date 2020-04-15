#!/usr/bin/env python

import os
import sys
import requests
import pandas as pd
from tqdm import tqdm
import argparse
from pathvalidate import sanitize_filename

def main(args):

	fmts = []
	if args.pdf:
		fmts += ['pdf']

	if args.epub:
		fmts += ['epub'] 

	if len(fmts) == 0:
		print("No format selected, choose at least one of pdf or epub")
		sys.exit()


	# insert here the folder you want the books to be downloaded:
	folder = os.getcwd() + '/downloads/'

	if not os.path.exists(folder):
		os.mkdir(folder)
		
	if not os.path.exists(args.url):
		books = pd.read_csv(args.url)

		# save table:
		books.to_csv('table.csv')
	else:
		books = pd.read_csv('table.csv', index_col=None, header=None)  

	# debug:
	# books = books.head()

	print('Download started.')
	
	for url, title, author in tqdm(books[['URL', 'Item Title', 'Authors']].values):

		for fmt in fmts:
			r = requests.get(url) 
			new_url = r.url

			new_url = url.replace('/book/','/content/%s/' % fmt)

			new_url = new_url.replace('%2F','/')
			new_url = new_url + '.%s' % fmt

			output_file = title + ' - ' + author + ' - ' + new_url.split('/')[-1]
			output_file = sanitize_filename(output_file)
			output_file = folder+output_file

			if not os.path.exists(output_file):
				myfile = requests.get(new_url, allow_redirects=True)
				try:
					open(output_file, 'wb').write(myfile.content)
				except OSError: 
					print("Error: filename is appears incorrect.")
			
	print('Download finished.')

if __name__ == '__main__':
	parser = argparse.ArgumentParser("Springer link download helper")
	parser.add_argument('url', type=str, help='link to springer search result csv file or local csv file')
	parser.add_argument('--pdf', action='store_true', help='Store pdf file')
	parser.add_argument('--epub', action='store_true', help='Store epub file')
	args = parser.parse_args()
	main(args)
