import urllib.request

# Try catch for API token
try:
    token = sys.argv[1]
except:
    token = input("\nToken not supplied. Please supply the API token:\n")
try:
    limit = sys.argv[2]
except:
    limit = input("\nLimit not supplied. Please supply the limit:\n")

# URL for the API requests    
rfIP = 'https://api.recordedfuture.com/v2/ip/demoevents'
rfHash = 'https://api.recordedfuture.com/v2/hash/demoevents'
rfDomain = 'https://api.recordedfuture.com/v2/domain/demoevents'
rfVuln = 'https://api.recordedfuture.com/v2/vulnerability/demoevents'

# Pull IPs
req = urllib.request.Request(rfIP+'?limit='+limit, None, {'X-RFToken': token})
with open('./events/rfIP.csv', 'w') as out:
    with urllib.request.urlopen(req) as res:
        encoding = res.headers.get_content_charset('utf-8')

    # For each line in the reply, extract the time, service policy, src IP and dst IP.
    # This should give us some easy correlations to C2 connections.
    
        out.write(res.read().decode(encoding))
        out.close()

# # Pull Hashes
# req = urllib.request.Request(rfHash+'?limit='+limit, None, {'X-RFToken': token})
# with open('./events/rfHash.csv', 'w') as out:
#     with urllib.request.urlopen(req) as res:
#         encoding = res.headers.get_content_charset('utf-8')

# # The output is very similar to CSV already; Check if splunk has a way to get headers from fields and delimit on colon.

#         out.write(res.read().decode(encoding))
#         out.close()

# # Pull Domains
# req = urllib.request.Request(rfDomain+'?limit='+limit, None, {'X-RFToken': token})
# with open('./events/rfDomain.csv', 'w') as out:
#     with urllib.request.urlopen(req) as res:
#         encoding = res.headers.get_content_charset('utf-8')\
    
# # For each line, extract: Time, IP, protocol, HTTP Method, Domain and Application

#         out.write(res.read().decode(encoding))
#         out.close()
               
# # Pull Vulnerabilities
# req = urllib.request.Request(rfVuln+'?limit='+limit, None, {'X-RFToken': token})
# with open('./events/rfVuln.csv', 'w') as out:
#     with urllib.request.urlopen(req) as res:
#         encoding = res.headers.get_content_charset('utf-8')

# # For each line extract: Time, Name, CVSS Vector, Hostname, Description, First-Seen, CVE Details

#         out.write(res.read().decode(encoding))
#         out.close()