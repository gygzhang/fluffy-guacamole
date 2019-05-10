
import urllib3
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib3 import response
import re
import os
import gzip

def download():
    http = urllib3.PoolManager()
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



    data={"modality_value": "T1",
            "from_select": "1",
            "slice_value": "1mm",
            "noise_value": "pn3",
            "field_value": "rf20"}


    '''
    --the forwarding url
    https://brainweb.bic.mni.mcgill.ca/cgi/brainweb1?
    from_select=1&modality_value=T1&slice_value=1mm&noise_value=pn3&field_value=rf20&download=%5BDownload%5D
    '''

    _url = "https://brainweb.bic.mni.mcgill.ca/cgi/brainweb1?" \
                   "from_select={from_select}&modality_value={modality_value}&slice_value={slice_value}&" \
                   "noise_value={noise_value}&" \
                   "field_value={field_value}&download=%5BDownload%5D".format(**data)


    '''
    noise_list=['pn3','pn1','pn0']
    modality_list=['T1','T2','PD']
    
    noise_iter = iter(noise_list)
    modality_iter = iter(modality_list)
    #0-5
    _new = query_data['do_download_alias']
    _old = ''
    for noise in noise_list:
        for modality in modality_list:
            query_data['do_download_alias'].replace(next(noise_iter),rep)
            
    '''

    query_data = {
    'do_download_alias': 'T1+ICBM+normal+1mm+pn3+rf20',
    'format_value': 'raw_byte',
    'zip_value': 'gnuzip',
    'who_name':'' ,
    'who_institution': '',
    'who_email':''
    }



    do_download_alias = ['T1+ICBM+normal+1mm+pn3+rf20',
                         'PD+ICBM+normal+1mm+pn3+rf20',
                         'T1+ICBM+normal+1mm+pn1+rf20',
                         'PD+ICBM+normal+1mm+pn1+rf20',
                         'T1+ICBM+normal+1mm+pn0+rf20',
                         'PD+ICBM+normal+1mm+pn0+rf20'
                         ]
    for i in range(6):
        query_data['do_download_alias']=do_download_alias[i]
        download_url = 'https://brainweb.bic.mni.mcgill.ca/cgi/brainweb1?' \
                       'do_download_alias={do_download_alias}&format_value={format_value}&' \
                       'zip_value={zip_value}&who_name={who_name}&who_institution={who_institution}&' \
                       'who_email={who_email}&' \
                       'download_for_real=%5BStart+download%21%5D'.format(**query_data)
        r = http.request("GET",download_url)
        filename = re.findall("filename", str(r.headers['Content-disposition']))
        filename = re.split(r"=", str(r.headers['Content-disposition']))[1]
        pathname = os.getcwd()+"\\dataset\\"

        with open(pathname + filename, 'wb') as fw:
            fw.write(r.data)

        input = gzip.GzipFile(pathname + filename, 'rb')
        s = input.read()
        input.close()


        decps_name = pathname + filename
        os.remove(decps_name)
        decps_name = decps_name.split('.gz')[0]

        output = open(decps_name, 'wb')
        output.write(s)
        output.close()
    #t = urllib3.HTTPResponse()

    print(r.headers['Content-disposition'])

    print(filename)



    #filename =''
    #for v in data:
    #    filename+=v+'&'
    #filename+='.zip'
    #rd = vars(r)
    #print()
    #print("aaa")
    print(os.listdir("D:\\MLDLRL\\brainweb\\"))



    #soup = BeautifulSoup(r.data,"html.parser")
    #print(soup)
    #a = HTTPResponse()

    '''
    https://brainweb.bic.mni.mcgill.ca/cgi/brainweb1?do_download_alias=T1+ICBM+normal+1mm+pn3+rf20&format_value=raw_byte&zip_value=gnuzip&who_name=&who_institution=&who_email=&download_for_real=%5BStart+download%21%5D
    '''

    return pathname