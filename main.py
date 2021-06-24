import requests
import json
import socket
from optparse import OptionParser
import sys

# Definitions
url = 'https://api.abuseipdb.com/api/v2/check'
api_key = ""
default_timeframe = 30
result_list = []
parser = OptionParser()

parser.add_option("-i", "--input", dest="fileinput",
	help="Enter Your Source IP Input File Path")

parser.add_option("-o", "--output", dest="fileoutput",
	help="Enter Your Result Output Path")

parser.add_option("-l", "--apilist", dest="fileapilist",
	help="Enter Your API List Path")

parser.add_option("-a", "--apikey", dest="apikeyinput",
	help="Enter Your API Key")

parser.add_option("-d", "--maxage", dest="maxagetime",
	help="Enter Your Max Age In Days")

(options, args) = parser.parse_args()



try:
    input_ips = open("inpu1t.txt","r").readlines()
except:
    if not options.fileinput:
        print("Please Enter A Valid Input Source IP File Name.")
        sys,exit(1)
    else:
        filename = options.fileinput
        input_ips = open(filename,"r").readlines()

if options.maxagetime:
    default_timeframe = options.maxagetime

if not options.fileoutput:
    outputname = "out.csv"
outputfile = open(options.fileoutput, "w")

multiple_api = False
if options.fileapilist:
    api_list = open(options.fileapilist, "r").readlines()
    multiple_api = True
else:
    apis = options.apikeyinput



def IPValidCheck(ip):
    try:
        socket.inet_aton(ip)
        return True
    except:
        return False


def CheckIP(ip, apikey=None):
    global result_list
    ip = ip.replace(" ", "")
    if IPValidCheck(ip):
        querystring = {
            'ipAddress': ip,
            'maxAgeInDays': f"{default_timeframe}"
        }
        headers = {
            'Accept': 'application/json',
            'Key': api_key
        }
        response = requests.request(method='GET', url=url, headers=headers, params=querystring)
        decodedResponse = json.loads(response.text)
        temp_result = []
        try:
            temp_result.append(decodedResponse["data"]["ipAddress"])
            temp_result.append(decodedResponse["data"]["abuseConfidenceScore"])
            temp_result.append(decodedResponse["data"]["totalReports"])
            temp_result.append(decodedResponse["data"]["countryCode"])
            result_list.append(temp_result)
            return 0
        except:
            if "Daily rate limit" in decodedResponse["errors"][0]["detail"]:
                print("API Limit Reached!")
                print("Trying To Use Another API Key...")
                return 2
    else:
        return 1

api_lists = []
if not multiple_api:
    api_key = apis
else:
    tmp_api_lists = open(options.fileapilist, "r").readlines()
    for apiitem in tmp_api_lists:
        f_api = apiitem.replace("\n","")
        f_api = f_api.replace(" ","")
        api_lists.append(f_api)
    api_key = api_lists[0]
    del api_lists[0]


for ip_addr in input_ips:
    check_status = CheckIP(ip_addr)
    ip_addr = ip_addr.replace('\n', '')
    ip_addr = ip_addr.replace(' ', '')
    if check_status==1:
        print(f"IP Address \"{ip_addr}\" Is Not Valid!")
    elif check_status==2:
        if not multiple_api:
            print("There Is No Other API Available!")
            print("Exiting...")
            break
        else:
            input_ips.append(ip_addr)
            try:
                api_key = api_lists[0]
                del api_lists[0]
            except IndexError:
                print("There Is No Other API Available!")
                print("Exiting...")


outputfile.write(f"IP Address,Confidence Score,Total Reports,Country Code\n")
for results in result_list:
    outputfile.write(f"{results[0]},{results[1]},{results[2]},{results[3]}\n")


