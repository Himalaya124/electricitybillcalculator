
from bangla_speaker import speak_bangla
from english_speaker import speak_english
print("=" * 60)
print("Welcome to the Electricity Bill Calculator".center(60))
print("Created by Nafis".center(60))
print("Version 1.1".center(60))
print("=" * 60)
# lan=input("Type language English or Bangla : 
while True:
    try:
        unit = int(input("\nEnter consumed unit (must be a positive integer): "))
        if unit < 0:
            print("⚠️  Unit cannot be negative. Please try again.")
        else:
            break  # Valid input — exit the loop
    except ValueError:
        print("⚠️  Invalid input! Please enter an integer value.")
bill=float(0)
while unit!=0:
    if unit>0 and unit<=75:
        bill+=(unit*5.26)
        unit=0
    elif unit>=76 and unit<=200:
        temp=unit
        temp-=75
        unit-=temp
        bill+=(temp*7.20)
    elif unit>=201 and unit<=300:
        temp=unit
        temp-=200
        unit-=temp
        bill+=(temp*7.59)
    elif unit>=301 and unit<=400:
        temp=unit
        temp-=300
        unit-=temp
        bill+=(temp*8.02)
    elif unit>=401 and unit<=600:
        temp=unit
        temp-=400
        unit-=temp
        bill+=(temp*12.67)
    elif unit>600:
        temp=unit
        temp-=600
        unit-=temp
        bill+=(temp*14.61)
    else:
        print("Enter valid consumed unit")
bill+=42
vat=(bill*5)/100
bill+=vat
if bill-int(bill)>=0.50:
    bill=bill.__ceil__()
else:
    bill=int(bill)

# if lan.lower()=="english":
    # w= f"YOUR ELECTRICITY BILL OF PREVIOUS MONTH IS {bill} TAKA ONLY. PLEASE PAY IT ON TIME."
    # speak_english(w)
    # while True:
    #     speak_english("ENTER 1 TO HEAR AGAIN OR ENTER 0 TO CLOSE THE PROGRAM.")
    #     i = int(input())
    #     if i == 1:
    #         speak_english(w)
    #     else:
    #         break
    # speak_english("THANKS FOR USING OUR PROGRAM.")
print(f"\nYour electricity bill of previous month is {bill} taka only. Please pay it on time.")
print("\nThanks for using my program.")

# else:
    # b= f"আপনার গত মাসের বিদ্যুৎ বিল {bill} টাকা মাত্র। অনুগ্রহ করে সময়মতো পরিশোধ করুন।"
    # speak_bangla(b)
    # while True:

    #     speak_bangla("আবার শুনতে ১ চাপুন অথবা প্রোগ্রাম বন্ধ করতে ০ চাপুন।")
    #     i = int(input())
    #     if i == 1:

    #         speak_bangla(b)
    #     else:
    #         break
    # speak_bangla("আমাদের প্রোগ্রাম ব্যবহার করার জন্য ধন্যবাদ।")
    # print(f"আপনার গত মাসের বিদ্যুৎ বিল {bill} টাকা মাত্র। অনুগ্রহ করে সময় মতো পরিশোধ করুন।")
