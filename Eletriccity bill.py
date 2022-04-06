#Electricity bill

n=int(input("Units consumed :"))
rate=0
gst=0
final=0
if (n<=55):
    rate=1.20
elif (n>=56 and n<100):
    rate=1.80
elif(n>=101 and n<+249):
    rate=2.40
elif(n>=250 and n<=450):
    rate=3.00
elif(n>450):
    rate=8.00

bill=n*rate
if(bill>450):
    gst=bill*0.18
elif(bill<100):
    bill=100
i = input("How Would You Like to View the Bill\n a) Detailed\n b) Only Amount\n (a/b):")
if(i=='a'):
    print("Units Consumed:",n)
    print("Rate Applicable:",rate)
    print("GST (18%):",gst)
final = gst+bill
print("Final Amount:",final)
    


