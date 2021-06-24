# AbuseIPChecker
Check IP Address List Malicious Status Using AbuseIP Database.<br/>
If You Want To Check A List Of IP Addresses To See If They Are Malicious Using AbuseIP Database, You Can Simply Use This Code And Rest In Peace...!

# How Does It Work?
This tool will use the AbuseIP API in order to check malicious status of an IP Address.<br/>
the free API limitation is "1,000 IP Checks & Reports / Day", if you want to bypass that, create multiple accounts using icognito tabs
and then add the APIs in a txt list (1 API per line) and feed it to the tool

# How To Use It
They are only couple of switches you need to know about the tool<br/>

### Input File (Mandatory):
Using -i or --input, you need to specify input IP list file path name.<br/>
* You can also create an "input.txt" file in the same path as the code, and not using this switch 
* File format is one IP per line

### Output File (Optional):
Using -o or --output, you need to specify output file name for results.<br/>
* Output file must have ".csv" extenstion

### API List (Optional):
Using -l or --apilist, you need to specify input API List file path name.<br/>
* File format is one API per line

### API Key (Optional):
Using -a or --apikey, you need to feed your single API key to the tool.<br/>
* E.x: -a "kjhiy2bjg827387kljdff...."

### Maximum Age (Optional):
Using -d or --maxage, you need to specify your max age for reports (day).<br/>
* Default value is 30days

## Example:
* python main.py -i "input.txt" -a "86frh80dd21b....66aayhe6a4" -o "outputfile.csv" -d 35
