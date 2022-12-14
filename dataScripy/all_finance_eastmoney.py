import pprint
import requests
from lxml import etree
from bs4 import BeautifulSoup

'''
参考文章：https://developer.51cto.com/article/645408.html

从eastmoney 根据code 获取所有的财务信息
'''


'''
获取主要指标：主要内容见：indict列表
'''

def get_zyzb_finance(code):
    indict = ['REPORT_DATE', 'REPORT_DATE_NAME', 'EPSJB', 'EPSKCJB', 'EPSXS', 'BPS', 'MGZBGJ', 'MGWFPLR', 'MGJYXJJE',
              'TOTALOPERATEREVE', 'MLR', 'PARENTNETPROFIT', 'KCFJCXSYJLR', 'TOTALOPERATEREVETZ', 'PARENTNETPROFITTZ',
              'KCFJCXSYJLRTZ', 'YYZSRGDHBZC', 'NETPROFITRPHBZC', 'KFJLRGDHBZC', 'ROEJQ', 'ROEKCJQ', 'ZZCJLL', 'XSJLL',
              'XSMLL', 'YSZKYYSR', 'XSJXLYYSR', 'JYXJLYYSR', 'TAXRATE', 'LD', 'SD', 'XJLLB', 'ZCFZL', 'QYCS', 'CQBL',
              'ZZCZZTS', 'CHZZTS', 'YSZKZZTS', 'TOAZZL', 'CHZZL', 'YSZKZZL', 'TOTALDEPOSITS', 'GROSSLOANS', 'LTDRR',
              'NEWCAPITALADER', 'HXYJBCZL', 'NONPERLOAN', 'BLDKBBL', 'NZBJE', 'TOTAL_ROI', 'NET_ROI', 'EARNED_PREMIUM',
              'COMPENSATE_EXPENSE', 'SURRENDER_RATE_LIFE', 'SOLVENCY_AR', 'JZB', 'JZC', 'JZBJZC', 'ZYGPGMJZC',
              'ZYGDSYLZQJZB', 'YYFXZB', 'JJYWFXZB', 'ZQZYYWFXZB', 'ZQCXYWFXZB', 'RZRQYWFXZB', 'EPSJBTZ', 'BPSTZ',
              'MGZBGJTZ', 'MGWFPLRTZ', 'MGJYXJJETZ', 'ROEJQTZ', 'ZZCJLLTZ', 'ZCFZLTZ', 'REPORT_YEAR', 'ROIC', 'ROICTZ',
              'NBV_LIFE', 'NBV_RATE', 'NHJZ_CURRENT_AMT', 'DJD_TOI_YOY', 'DJD_DPNP_YOY', 'DJD_DEDUCTDPNP_YOY',
              'DJD_TOI_QOQ', 'DJD_DPNP_QOQ', 'DJD_DEDUCTDPNP_QOQ']
    zyzb_dict = {}

    #处理code
    if (code[0] == '6' or code[0] == '9'):
        code = 'SH' + code
        code_url = 'SH' + code
    else:
        code = 'SZ' + code
        code_url = 'SZ' + code

    url = f'http://f10.eastmoney.com/NewFinanceAnalysis/ZYZBAjaxNew?type=0&code={code}'
    html = requests.get(url)
    zyzb_json = html.json()

    stock_name = zyzb_json['data'][0]['SECURITY_NAME_ABBR']

    print(stock_name)

    for data in zyzb_json['data']:
        for key in data:
            if key in indict:
                if key not in zyzb_dict:
                    zyzb_dict[key] = []

                zyzb_dict[key].append(data[key])
    return zyzb_dict


'''
获取lrb主要参数：主要内容见：indict列表

return:
'''
def get_lrb_finace(code):

    indict =  ['REPORT_DATE', 'REPORT_TYPE', 'SECURITY_TYPE_CODE', 'TOTAL_OPERATE_INCOME', 'TOTAL_OPERATE_INCOME_YOY', 'OPERATE_INCOME', 'OPERATE_INCOME_YOY', 'INTEREST_INCOME', 'INTEREST_INCOME_YOY', 'EARNED_PREMIUM', 'EARNED_PREMIUM_YOY', 'FEE_COMMISSION_INCOME', 'FEE_COMMISSION_INCOME_YOY', 'OTHER_BUSINESS_INCOME', 'OTHER_BUSINESS_INCOME_YOY', 'TOI_OTHER', 'TOI_OTHER_YOY', 'TOTAL_OPERATE_COST', 'TOTAL_OPERATE_COST_YOY', 'OPERATE_COST', 'OPERATE_COST_YOY', 'INTEREST_EXPENSE', 'INTEREST_EXPENSE_YOY', 'FEE_COMMISSION_EXPENSE', 'FEE_COMMISSION_EXPENSE_YOY', 'RESEARCH_EXPENSE', 'RESEARCH_EXPENSE_YOY', 'SURRENDER_VALUE', 'SURRENDER_VALUE_YOY', 'NET_COMPENSATE_EXPENSE', 'NET_COMPENSATE_EXPENSE_YOY', 'NET_CONTRACT_RESERVE', 'NET_CONTRACT_RESERVE_YOY', 'POLICY_BONUS_EXPENSE', 'POLICY_BONUS_EXPENSE_YOY', 'REINSURE_EXPENSE', 'REINSURE_EXPENSE_YOY', 'OTHER_BUSINESS_COST', 'OTHER_BUSINESS_COST_YOY', 'OPERATE_TAX_ADD', 'OPERATE_TAX_ADD_YOY', 'SALE_EXPENSE', 'SALE_EXPENSE_YOY', 'MANAGE_EXPENSE', 'MANAGE_EXPENSE_YOY', 'ME_RESEARCH_EXPENSE', 'ME_RESEARCH_EXPENSE_YOY', 'FINANCE_EXPENSE', 'FINANCE_EXPENSE_YOY', 'FE_INTEREST_EXPENSE', 'FE_INTEREST_EXPENSE_YOY', 'FE_INTEREST_INCOME', 'FE_INTEREST_INCOME_YOY', 'ASSET_IMPAIRMENT_LOSS', 'ASSET_IMPAIRMENT_LOSS_YOY', 'CREDIT_IMPAIRMENT_LOSS', 'CREDIT_IMPAIRMENT_LOSS_YOY', 'TOC_OTHER', 'TOC_OTHER_YOY', 'FAIRVALUE_CHANGE_INCOME', 'FAIRVALUE_CHANGE_INCOME_YOY', 'INVEST_INCOME', 'INVEST_INCOME_YOY', 'INVEST_JOINT_INCOME', 'INVEST_JOINT_INCOME_YOY', 'NET_EXPOSURE_INCOME', 'NET_EXPOSURE_INCOME_YOY', 'EXCHANGE_INCOME', 'EXCHANGE_INCOME_YOY', 'ASSET_DISPOSAL_INCOME', 'ASSET_DISPOSAL_INCOME_YOY', 'ASSET_IMPAIRMENT_INCOME', 'ASSET_IMPAIRMENT_INCOME_YOY', 'CREDIT_IMPAIRMENT_INCOME', 'CREDIT_IMPAIRMENT_INCOME_YOY', 'OTHER_INCOME', 'OTHER_INCOME_YOY', 'OPERATE_PROFIT_OTHER', 'OPERATE_PROFIT_OTHER_YOY', 'OPERATE_PROFIT_BALANCE', 'OPERATE_PROFIT_BALANCE_YOY', 'OPERATE_PROFIT', 'OPERATE_PROFIT_YOY', 'NONBUSINESS_INCOME', 'NONBUSINESS_INCOME_YOY', 'NONCURRENT_DISPOSAL_INCOME', 'NONCURRENT_DISPOSAL_INCOME_YOY', 'NONBUSINESS_EXPENSE', 'NONBUSINESS_EXPENSE_YOY', 'NONCURRENT_DISPOSAL_LOSS', 'NONCURRENT_DISPOSAL_LOSS_YOY', 'EFFECT_TP_OTHER', 'EFFECT_TP_OTHER_YOY', 'TOTAL_PROFIT_BALANCE', 'TOTAL_PROFIT_BALANCE_YOY', 'TOTAL_PROFIT', 'TOTAL_PROFIT_YOY', 'INCOME_TAX', 'INCOME_TAX_YOY', 'EFFECT_NETPROFIT_OTHER', 'EFFECT_NETPROFIT_OTHER_YOY', 'EFFECT_NETPROFIT_BALANCE', 'EFFECT_NETPROFIT_BALANCE_YOY', 'UNCONFIRM_INVEST_LOSS', 'UNCONFIRM_INVEST_LOSS_YOY', 'NETPROFIT', 'NETPROFIT_YOY', 'PRECOMBINE_PROFIT', 'PRECOMBINE_PROFIT_YOY', 'CONTINUED_NETPROFIT', 'CONTINUED_NETPROFIT_YOY', 'DISCONTINUED_NETPROFIT', 'DISCONTINUED_NETPROFIT_YOY', 'PARENT_NETPROFIT', 'PARENT_NETPROFIT_YOY', 'MINORITY_INTEREST', 'MINORITY_INTEREST_YOY', 'DEDUCT_PARENT_NETPROFIT', 'DEDUCT_PARENT_NETPROFIT_YOY', 'NETPROFIT_OTHER', 'NETPROFIT_OTHER_YOY', 'NETPROFIT_BALANCE', 'NETPROFIT_BALANCE_YOY', 'BASIC_EPS', 'BASIC_EPS_YOY', 'DILUTED_EPS', 'DILUTED_EPS_YOY', 'OTHER_COMPRE_INCOME', 'OTHER_COMPRE_INCOME_YOY', 'PARENT_OCI', 'PARENT_OCI_YOY', 'MINORITY_OCI', 'MINORITY_OCI_YOY', 'PARENT_OCI_OTHER', 'PARENT_OCI_OTHER_YOY', 'PARENT_OCI_BALANCE', 'PARENT_OCI_BALANCE_YOY', 'UNABLE_OCI', 'UNABLE_OCI_YOY', 'CREDITRISK_FAIRVALUE_CHANGE', 'CREDITRISK_FAIRVALUE_CHANGE_YOY', 'OTHERRIGHT_FAIRVALUE_CHANGE', 'OTHERRIGHT_FAIRVALUE_CHANGE_YOY', 'SETUP_PROFIT_CHANGE', 'SETUP_PROFIT_CHANGE_YOY', 'RIGHTLAW_UNABLE_OCI', 'RIGHTLAW_UNABLE_OCI_YOY', 'UNABLE_OCI_OTHER', 'UNABLE_OCI_OTHER_YOY', 'UNABLE_OCI_BALANCE', 'UNABLE_OCI_BALANCE_YOY', 'ABLE_OCI', 'ABLE_OCI_YOY', 'RIGHTLAW_ABLE_OCI', 'RIGHTLAW_ABLE_OCI_YOY', 'AFA_FAIRVALUE_CHANGE', 'AFA_FAIRVALUE_CHANGE_YOY', 'HMI_AFA', 'HMI_AFA_YOY', 'CASHFLOW_HEDGE_VALID', 'CASHFLOW_HEDGE_VALID_YOY', 'CREDITOR_FAIRVALUE_CHANGE', 'CREDITOR_FAIRVALUE_CHANGE_YOY', 'CREDITOR_IMPAIRMENT_RESERVE', 'CREDITOR_IMPAIRMENT_RESERVE_YOY', 'FINANCE_OCI_AMT', 'FINANCE_OCI_AMT_YOY', 'CONVERT_DIFF', 'CONVERT_DIFF_YOY', 'ABLE_OCI_OTHER', 'ABLE_OCI_OTHER_YOY', 'ABLE_OCI_BALANCE', 'ABLE_OCI_BALANCE_YOY', 'OCI_OTHER', 'OCI_OTHER_YOY', 'OCI_BALANCE', 'OCI_BALANCE_YOY', 'TOTAL_COMPRE_INCOME', 'TOTAL_COMPRE_INCOME_YOY', 'PARENT_TCI', 'PARENT_TCI_YOY', 'MINORITY_TCI', 'MINORITY_TCI_YOY', 'PRECOMBINE_TCI', 'PRECOMBINE_TCI_YOY', 'EFFECT_TCI_BALANCE', 'EFFECT_TCI_BALANCE_YOY', 'TCI_OTHER', 'TCI_OTHER_YOY', 'TCI_BALANCE', 'TCI_BALANCE_YOY', 'ACF_END_INCOME', 'ACF_END_INCOME_YOY']
    lrb_dict = {}

    #处理code
    if (code[0] == '6' or code[0] == '9'):
        code = 'SH' + code
        code_url = 'SH' + code
    else:
        code = 'SZ' + code
        code_url = 'SZ' + code

    url = f'http://f10.eastmoney.com/NewFinanceAnalysis/lrbAjaxNew?companyType=4&reportDateType=0&reportType=1&dates=2020-12-31%2C2020-09-30%2C2020-06-30%2C2020-03-31%2C2019-12-31&code={code}'
    html = requests.get(url)
    zyzb_json = html.json()

    stock_name = zyzb_json['data'][0]['SECURITY_NAME_ABBR']


    for data in zyzb_json['data']:
        for key in data:
            if key in indict:
               if key not in lrb_dict :
                   lrb_dict[key] =[]

               lrb_dict[key].append(data[key])
    return lrb_dict



if __name__ == '__main__':
    indict =  ['REPORT_DATE', 'REPORT_TYPE', 'TOTAL_OPERATE_INCOME', 'TOTAL_OPERATE_INCOME_YOY', 'OPERATE_INCOME', 'OPERATE_INCOME_YOY', 'INTEREST_INCOME', 'INTEREST_INCOME_YOY', 'EARNED_PREMIUM', 'EARNED_PREMIUM_YOY', 'FEE_COMMISSION_INCOME', 'FEE_COMMISSION_INCOME_YOY', 'OTHER_BUSINESS_INCOME', 'OTHER_BUSINESS_INCOME_YOY', 'TOI_OTHER', 'TOI_OTHER_YOY', 'TOTAL_OPERATE_COST', 'TOTAL_OPERATE_COST_YOY', 'OPERATE_COST', 'OPERATE_COST_YOY', 'INTEREST_EXPENSE', 'INTEREST_EXPENSE_YOY', 'FEE_COMMISSION_EXPENSE', 'FEE_COMMISSION_EXPENSE_YOY', 'RESEARCH_EXPENSE', 'RESEARCH_EXPENSE_YOY', 'SURRENDER_VALUE', 'SURRENDER_VALUE_YOY', 'NET_COMPENSATE_EXPENSE', 'NET_COMPENSATE_EXPENSE_YOY', 'NET_CONTRACT_RESERVE', 'NET_CONTRACT_RESERVE_YOY', 'POLICY_BONUS_EXPENSE', 'POLICY_BONUS_EXPENSE_YOY', 'REINSURE_EXPENSE', 'REINSURE_EXPENSE_YOY', 'OTHER_BUSINESS_COST', 'OTHER_BUSINESS_COST_YOY', 'OPERATE_TAX_ADD', 'OPERATE_TAX_ADD_YOY', 'SALE_EXPENSE', 'SALE_EXPENSE_YOY', 'MANAGE_EXPENSE', 'MANAGE_EXPENSE_YOY', 'ME_RESEARCH_EXPENSE', 'ME_RESEARCH_EXPENSE_YOY', 'FINANCE_EXPENSE', 'FINANCE_EXPENSE_YOY', 'FE_INTEREST_EXPENSE', 'FE_INTEREST_EXPENSE_YOY', 'FE_INTEREST_INCOME', 'FE_INTEREST_INCOME_YOY', 'ASSET_IMPAIRMENT_LOSS', 'ASSET_IMPAIRMENT_LOSS_YOY', 'CREDIT_IMPAIRMENT_LOSS', 'CREDIT_IMPAIRMENT_LOSS_YOY', 'TOC_OTHER', 'TOC_OTHER_YOY', 'FAIRVALUE_CHANGE_INCOME', 'FAIRVALUE_CHANGE_INCOME_YOY', 'INVEST_INCOME', 'INVEST_INCOME_YOY', 'INVEST_JOINT_INCOME', 'INVEST_JOINT_INCOME_YOY', 'NET_EXPOSURE_INCOME', 'NET_EXPOSURE_INCOME_YOY', 'EXCHANGE_INCOME', 'EXCHANGE_INCOME_YOY', 'ASSET_DISPOSAL_INCOME', 'ASSET_DISPOSAL_INCOME_YOY', 'ASSET_IMPAIRMENT_INCOME', 'ASSET_IMPAIRMENT_INCOME_YOY', 'CREDIT_IMPAIRMENT_INCOME', 'CREDIT_IMPAIRMENT_INCOME_YOY', 'OTHER_INCOME', 'OTHER_INCOME_YOY', 'OPERATE_PROFIT_OTHER', 'OPERATE_PROFIT_OTHER_YOY', 'OPERATE_PROFIT_BALANCE', 'OPERATE_PROFIT_BALANCE_YOY', 'OPERATE_PROFIT', 'OPERATE_PROFIT_YOY', 'NONBUSINESS_INCOME', 'NONBUSINESS_INCOME_YOY', 'NONCURRENT_DISPOSAL_INCOME', 'NONCURRENT_DISPOSAL_INCOME_YOY', 'NONBUSINESS_EXPENSE', 'NONBUSINESS_EXPENSE_YOY', 'NONCURRENT_DISPOSAL_LOSS', 'NONCURRENT_DISPOSAL_LOSS_YOY', 'EFFECT_TP_OTHER', 'EFFECT_TP_OTHER_YOY', 'TOTAL_PROFIT_BALANCE', 'TOTAL_PROFIT_BALANCE_YOY', 'TOTAL_PROFIT', 'TOTAL_PROFIT_YOY', 'INCOME_TAX', 'INCOME_TAX_YOY', 'EFFECT_NETPROFIT_OTHER', 'EFFECT_NETPROFIT_OTHER_YOY', 'EFFECT_NETPROFIT_BALANCE', 'EFFECT_NETPROFIT_BALANCE_YOY', 'UNCONFIRM_INVEST_LOSS', 'UNCONFIRM_INVEST_LOSS_YOY', 'NETPROFIT', 'NETPROFIT_YOY', 'PRECOMBINE_PROFIT', 'PRECOMBINE_PROFIT_YOY', 'CONTINUED_NETPROFIT', 'CONTINUED_NETPROFIT_YOY', 'DISCONTINUED_NETPROFIT', 'DISCONTINUED_NETPROFIT_YOY', 'PARENT_NETPROFIT', 'PARENT_NETPROFIT_YOY', 'MINORITY_INTEREST', 'MINORITY_INTEREST_YOY', 'DEDUCT_PARENT_NETPROFIT', 'DEDUCT_PARENT_NETPROFIT_YOY', 'NETPROFIT_OTHER', 'NETPROFIT_OTHER_YOY', 'NETPROFIT_BALANCE', 'NETPROFIT_BALANCE_YOY', 'BASIC_EPS', 'BASIC_EPS_YOY', 'DILUTED_EPS', 'DILUTED_EPS_YOY', 'OTHER_COMPRE_INCOME', 'OTHER_COMPRE_INCOME_YOY', 'PARENT_OCI', 'PARENT_OCI_YOY', 'MINORITY_OCI', 'MINORITY_OCI_YOY', 'PARENT_OCI_OTHER', 'PARENT_OCI_OTHER_YOY', 'PARENT_OCI_BALANCE', 'PARENT_OCI_BALANCE_YOY', 'UNABLE_OCI', 'UNABLE_OCI_YOY', 'CREDITRISK_FAIRVALUE_CHANGE', 'CREDITRISK_FAIRVALUE_CHANGE_YOY', 'OTHERRIGHT_FAIRVALUE_CHANGE', 'OTHERRIGHT_FAIRVALUE_CHANGE_YOY', 'SETUP_PROFIT_CHANGE', 'SETUP_PROFIT_CHANGE_YOY', 'RIGHTLAW_UNABLE_OCI', 'RIGHTLAW_UNABLE_OCI_YOY', 'UNABLE_OCI_OTHER', 'UNABLE_OCI_OTHER_YOY', 'UNABLE_OCI_BALANCE', 'UNABLE_OCI_BALANCE_YOY', 'ABLE_OCI', 'ABLE_OCI_YOY', 'RIGHTLAW_ABLE_OCI', 'RIGHTLAW_ABLE_OCI_YOY', 'AFA_FAIRVALUE_CHANGE', 'AFA_FAIRVALUE_CHANGE_YOY', 'HMI_AFA', 'HMI_AFA_YOY', 'CASHFLOW_HEDGE_VALID', 'CASHFLOW_HEDGE_VALID_YOY', 'CREDITOR_FAIRVALUE_CHANGE', 'CREDITOR_FAIRVALUE_CHANGE_YOY', 'CREDITOR_IMPAIRMENT_RESERVE', 'CREDITOR_IMPAIRMENT_RESERVE_YOY', 'FINANCE_OCI_AMT', 'FINANCE_OCI_AMT_YOY', 'CONVERT_DIFF', 'CONVERT_DIFF_YOY', 'ABLE_OCI_OTHER', 'ABLE_OCI_OTHER_YOY', 'ABLE_OCI_BALANCE', 'ABLE_OCI_BALANCE_YOY', 'OCI_OTHER', 'OCI_OTHER_YOY', 'OCI_BALANCE', 'OCI_BALANCE_YOY', 'TOTAL_COMPRE_INCOME', 'TOTAL_COMPRE_INCOME_YOY', 'PARENT_TCI', 'PARENT_TCI_YOY', 'MINORITY_TCI', 'MINORITY_TCI_YOY', 'PRECOMBINE_TCI', 'PRECOMBINE_TCI_YOY', 'EFFECT_TCI_BALANCE', 'EFFECT_TCI_BALANCE_YOY', 'TCI_OTHER', 'TCI_OTHER_YOY', 'TCI_BALANCE', 'TCI_BALANCE_YOY', 'ACF_END_INCOME', 'ACF_END_INCOME_YOY']
    lrb_dict = {}

    url = 'http://f10.eastmoney.com/NewFinanceAnalysis/lrbAjaxNew?companyType=4&reportDateType=0&reportType=1&dates=2022-03-31%2C2021-12-31%2C2021-09-30%2C2021-06-30%2C2021-03-31&code=SZ000651'
    html = requests.get(url)
    zyzb_json = html.json()

    stock_name = zyzb_json['data'][0]['SECURITY_NAME_ABBR']
    print(stock_name)


    for data in zyzb_json['data']:
        for key in data:
            if key in indict:
               if key not in lrb_dict :
                   lrb_dict[key] =[]

               lrb_dict[key].append(data[key])
    print(lrb_dict)





