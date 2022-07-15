import dataScripy as dsc



def get_pe():
    pelist = dsc.get_code_pe(1,400)

    print(pelist)


if __name__ == '__main__':
    get_pe()