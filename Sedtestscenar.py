import os
from datetime import datetime 
import urllib


def ping(server):
  timestamp1 = datetime.today()
  result = os.system("ping -n 1 {}".format(server)) 
  if result == 0:
    # ping command success
    timestamp2 = datetime.today()
    diff = timestamp2 - timestamp1
    pingLatency = (diff.days * 24 * 3600 * 1000) + (diff.seconds * 1000) + (diff.microseconds/1000)
    return pingLatency
  else:
    return -1 

def fetch(url):
  timestamp1 = datetime.today() 
  handle = urllib.urlopen(url)
  if handle.getcode() == 200:
    # fetch url success
    timestamp2 = datetime.today()
    diff = timestamp2 - timestamp1
    fetchLatency = (diff.days * 24 * 3600 * 1000) + (diff.seconds * 1000) + (diff.microseconds/1000)
    return fetchLatency
  else:
    return -1

def pingTest(hostname, count):
    timeseq = []
    for i in range(count):
        x = ping(hostname)
        timeseq.append(x)
    sum=0  
    for i in timeseq:
        sum = sum + i         
        average = sum/count
    return average
   
    
if __name__ == "__main__":
    results = pingTest ("www.google.com", 5)
    print results
    resultsfetchLatency = fetch("http://www.google.com")
    print "fetch latency = {} ms".format(fetchLatency)
  
