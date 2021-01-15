import pandas as pd
import datetime
import smtplib#helps ins ending email
import os
from secure import password


os.chdir(r"C:\Users\rajes\PycharmProjects\Automate_Birthday_Wish")#to trigger whether scheduler run or not
#os.mkdir("testing")

# Enter your authentication details
GMAIL_ID = 'anjalikumari13617@gmail.com'
GMAIL_PSWD = password


def sendEmail(to, sub, msg):#sending mail via SMTP protocol
    print(f"Email to {to} sent with subject: {sub} and message {msg}" )
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()
    

if __name__ == "__main__":
    #just for testing
    # sendEmail(GMAIL_ID, "subject", "test message")
    # exit()

    df = pd.read_excel("data.xlsx")
    print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    #print(type(yearNow))
    writeInd = []
    for index, item in df.iterrows():
        # print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")#extracting day and month using strftime function
        # print(bday)
        if(today == bday) and yearNow in str(item['Year']):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)

    print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)
        print(df.loc[i, 'Year'])

    #print(df)
    df.to_excel('data.xlsx', index=False)