from dataScripy import stock as k
import datetime


if __name__ == '__main__':
    today = str(datetime.date.today())
    thirty_ago =str(datetime.date.today() - datetime.timedelta(30))


    k.get_k_line()

    lt = df.values.tolist()

    lenth = len(lt) - 1
    if (lenth > 10):
        thirty = (float(lt[lenth][5]) - float(lt[0][5])) / float(lt[0][5])
        ten = (float(lt[lenth][5]) - float(lt[lenth // 2][5])) / float(lt[10][5])
        if (thirty < -0.6):
            print(code)