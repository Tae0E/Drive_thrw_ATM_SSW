import requests;
with open('check.txt') as f:
    chk=f.readline()
if chk:
    with open('nfcID.txt') as f:
        nfcNumber=f.readline()
        print(nfcNumber)
    result=requests.post('http://35.200.117.1:8080/control.jsp?type=reservation&action=execute&nfcId='+nfcNumber)
    print(result.text)
