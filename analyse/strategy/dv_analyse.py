from dataScripy import stockDividend as sd
from dataScripy import stockCode as sc

if __name__ == '__main__':
    code_pes = sc.get_code_pe(1,350)
    print(code_pes)

    for codes in code_pes:
        code = codes[0]
        code_name = codes[1]

        code_url = code.strip('"')

        try:
            last_dv = sd.get_recent_dv(code_url)
        except:
            #print(sd.get_url(code_url))
            #print('未查询到：' + code_name)

            continue

        if last_dv >5 and last_dv <8:
            print(code,code_name,last_dv)