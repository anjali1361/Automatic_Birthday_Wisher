import pandas as pd
import datetime

def sendEmail(to,sub,msg):
    print(f"Email to {to} sent with subject: {sub} and message: {msg}")
    pass

if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    #print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow =datetime.datetime.now().strftime("%y")
    #print(today)
    #print(type(today))
    writeInd =[]

    for index,item in df.iterrows():
        #print(index,item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")#conerting type of birthday-date displayed to match it to today's date
        #print(bday)
        msg='Wishing you a very happy birthday on this special ocassion I want to thank you for coming into my life. Always be like and do not leave me ever'
        if(today==bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'],"Happy Birthday,",item['Dialogue'])
            writeInd.append(index)#saving index to which email is sent for the particular year

    #print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']#prints row and column index using loc function
        print(yr)
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)#year upgraded after wishing
        print(df.loc[i, 'Year'])

    #print(df)
    df.to_excel('data.xlsx',index=False)