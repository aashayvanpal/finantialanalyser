from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Aashay','name2':"Second Name"})

def dashboard(request):
    var = 10
    import pandas as pd
    import matplotlib.pyplot as plt 
    from matplotlib.pyplot import figure 
    df = pd.read_csv("/home/aashay/code/aashay/StocksPredictor/Finantial analyser/Balance.csv").dropna()



    x=df['Date']
    y=df['Balance']

    print("Max achieved balance :Rs",max(y))
    cur_bal=df.tail(1)['Balance'].iloc[0]
    print('Current Balance : ',cur_bal)
    # 200000 is goal to achieve
    print("Still need :Rs",200000-cur_bal)

    plt.figure(figsize=(11,5)) 
    plt.plot(x,y,marker='P')
    plt.xlabel('Date',fontsize = 15)
    plt.ylabel('Balance',rotation=90,fontsize = 15)

    plt.xticks(rotation=45)
    plt.legend(['Balance'])
    plt.savefig('balance.jpg')

    # plt.show()

    return render(request,'dashboard.html',
    {
        "var":"30",
        "df":df,
        "cur_bal":cur_bal,
        "need":(200000-cur_bal),
        "url":"file:///home/aashay/code/Python-Projects/finantialanalyser/me.jpg"
    })

def plan(request):
    return render(request,'plan.html',{'number':'2'})

