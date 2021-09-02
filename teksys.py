sen="Developed a powerful and complete HRM and Payroll software for company to automate their workflows (ex-daily attendance, salary calculation and run, payslip, Sprint calculation etc)."
# sen = ""
# sen = None
#sen = 1
#method 1
# l=[]
# for i in sen.split():
#     l.append(i[::-1])
# l2=" ".join(l)
# print(l2)
# print(type(l2))

##method 2
def reverse_word_senetance(sen):
    if sen == '' or sen == None:
        return "pass some sentence bro"
    elif isinstance(sen, str):
        sen1=sen.replace("(","( ")
        sen2=sen1.replace(")"," )")
        sen3=sen2.replace(","," ,")
        sen4=sen3.replace("."," .")
        print(sen4)
        l=[]
        s=''
        for i in sen4.split():
             s=s+" "+str(i[::-1])
        return s
    else :
        return "only string datatype allowed bro"

print(reverse_word_senetance(sen))