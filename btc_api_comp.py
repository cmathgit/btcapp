'''
	Programmer: Cruz Macias
	Problem Description: Parse, store, and visualize information returned from the Bitcoin Public REST API.
	This endpoint returns the current price of BTC in USD, British Pound, and Euros.

		https://api.coindesk.com/v1/bpi/currentprice.json

	Component Details: Use os.system() module to send an api request to the console, in particular,
		the Client URL (cURL) command and store the returned JSON array locally in .json file.
		Open the file containing the returned JSON array, process the key values into a tabular format (.tsv).

	Run Python in CMD: python btc_api_comp.py

'''
# import module(s)
import os
import sys
import json
import datetime
import os.path

# declare pathnames
api_req = 'curl -# -o "coindesk_payload.json" https://api.coindesk.com/v1/bpi/currentprice.json'
payload_path = 'coindesk_payload.json'
payload_parse = 'btc_rates.tsv'

# print a message to the console
print("Command: ", api_req)
# use os.system() module to send a command to the console, i.e., run the api request
os.system(api_req)


# read the file found in payload_parse
print("\nData Table: ", payload_parse)
print("************************************************")

# create/open the tsv file to store the output of the parsed json array under all (a+) permissions using the open function
tsv_table = open(payload_parse, 'a+')
# commment out after the first run, write header to the tsv file
# tsv_table.write("monetary_code\trate_as_float\tdate_as_iso\n")

with open(payload_path, 'r') as apir:

	# load the json file containing the api response
	json_arr = json.load(apir)

	# dump the json array into a python string
	json_payload = json.dumps(json_arr)

	# load the string into a python object
	jtop_obj = json.loads(json_payload)

	# refer to the json file for names of keys
	# grab the datetime key pair, e.g., ['time']['updatedISO'] = 2022-08-31T18:36:00+00:00
	time_updISO = jtop_obj['time']['updatedISO']
	print("\n[time][updatedISO]: ", '{}'.format(time_updISO))

	# United States Dollar Rate of Bitcoin
	# grab the ['bpi']['USD']['code'] and ['bpi']['USD']['rate_float']
	usd_code = jtop_obj['bpi']['USD']['code']
	usd_rate_f = jtop_obj['bpi']['USD']['rate_float']
	usd_descr = jtop_obj['bpi']['USD']['description']

	# write the key pair values to a row in the TSV table
	tsv_table.write('{}\t{}\t{}\n'.format(usd_code, usd_rate_f, time_updISO))

	print("[bpi][USD]", '\n[description]:\t{}\n[code]:\t{}\n[rate_float]:\t{}'.format(usd_descr, usd_code, usd_rate_f))

	# British Pounds Rate of Bitcoin
	# grab the ['bpi']['GBP']['code'] and ['bpi']['GBP']['rate_float']
	gbp_code = jtop_obj['bpi']['GBP']['code']
	gbp_rate_f = jtop_obj['bpi']['GBP']['rate_float']
	gbp_descr = jtop_obj['bpi']['GBP']['description']

	# write the key pair values to a row in the TSV table
	tsv_table.write('{}\t{}\t{}\n'.format(gbp_code, gbp_rate_f, time_updISO))

	print("[bpi][GBP]", '\n[description]:\t{}\n[code]:\t{}\n[rate_float]:\t{}'.format(gbp_descr, gbp_code, gbp_rate_f))

	# Euro Rate of Bitcoin
	# grab the ['bpi']['EUR']['code'] and ['bpi']['EUR']['rate_float']
	eur_code = jtop_obj['bpi']['EUR']['code']
	eur_rate_f = jtop_obj['bpi']['EUR']['rate_float']
	eur_descr = jtop_obj['bpi']['EUR']['description']

	# write the key pair values to a row in the TSV table
	tsv_table.write('{}\t{}\t{}\n'.format(eur_code, eur_rate_f, time_updISO))

	print("[bpi][EUR]", '\n[description]:\t{}\n[code]:\t{}\n[rate_float]:\t{}'.format(eur_descr, eur_code, eur_rate_f))

	# print the entire contents of the returned payload
	print("\n JSON Payload:", json_arr)

print("************************************************")

# close the file object
tsv_table.close()
