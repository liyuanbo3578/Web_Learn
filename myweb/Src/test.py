import threading
import os

#G:\big_file
ad=[fname for fname in os.listdir('G:/big_file/') if  fname.endswith('txt')]
num=int(round(len(ad)/20,0))
def test1():
    file01=ad[:num]
    for i in file01:
        f=open("G:/big_file/%s"%i,"r")
        print("01")
        f.close()




def test2():
    file02=ad[num:num*2]
    for i in file02:
        f=open("G:/big_file/%s"%i,"r")
        print("02")
        f.close()


def test3():
    file03=ad[num*2:num*3]
    for i in file03:
        f=open("G:/big_file/%s"%i,"r")
        print("03")
        f.close()

def test4():
    file04=ad[num*3:num*4]
    for i in file04:
        f=open("G:/big_file/%s"%i,"r")
        print("04")
        f.close()

def test5():
    file05=ad[num*4:num*5]
    for i in file05:
        f=open("G:/big_file/%s"%i,"r")
        print("05")
        f.close()

def test6():
    file06=ad[num*5:num*6]
    for i in file06:
        f=open("G:/big_file/%s"%i,"r")
        print("06")
        f.close()

def test7():
    file07=ad[num*6:num*7]
    for i in file07:
        f=open("G:/big_file/%s"%i,"r")
        print("07")
        f.close()

def test8():
    file08=ad[num*7:num*8]
    for i in file08:
        f=open("G:/big_file/%s"%i,"r")
        print("08")
        f.close()

def test9():
    file09=ad[num*8:num*9]
    for i in file09:
        f=open("G:/big_file/%s"%i,"r")
        print("09")
        f.close()

def test10():
    file10=ad[num*9:num*10]
    for i in file10:
        f=open("G:/big_file/%s"%i,"r")
        print("10")
        f.close()

def test11():
    file11=ad[num*10:num*11]
    for i in file11:
        f=open("G:/big_file/%s"%i,"r")
        print("11")
        f.close()        

def test12():
    file12=ad[num*11:num*12]
    for i in file12:
        f=open("G:/big_file/%s"%i,"r")
        print("12")
        f.close()
        
def test13():
    file13=ad[num*12:num*13]
    for i in file13:
        f=open("G:/big_file/%s"%i,"r")
        print("12")
        f.close()

def test14():
    file14=ad[num*13:num*14]
    for i in file14:
        f=open("G:/big_file/%s"%i,"r")
        print("14")
        f.close()

def test15():
    file15=ad[num*14:num*15]
    for i in file15:
        f=open("G:/big_file/%s"%i,"r")
        print("15")
        f.close() 

def test16():
    file16=ad[num*15:num*16]
    for i in file16:
        f=open("G:/big_file/%s"%i,"r")
        print("16")
        f.close()

def test17():
    file17=ad[num*16:num*17]
    for i in file17:
            f=open("G:/big_file/%s"%i,"r")
            print("17")
            f.close()

def test18():
    file18=ad[num*17:num*18]
    for i in file18:
        f=open("G:/big_file/%s"%i,"r")
        print("18")
        f.close()

def test19():
    file19=ad[num*18:num*19]
    for i in file19:
        f=open("G:/big_file/%s"%i,"r")
        print("19")
        f.close()
        
def test20():
    file20=ad[num*19:num*20]
    for i in file20:
        f=open("G:/big_file/%s"%i,"r")
        print("20")
        f.close()  
        
                

        
a1=threading.Thread(target=test1)
a2=threading.Thread(target=test2)
a3=threading.Thread(target=test3)
a4=threading.Thread(target=test4)
a5=threading.Thread(target=test5)
a6=threading.Thread(target=test6)
a7=threading.Thread(target=test7)
a8=threading.Thread(target=test8)
a9=threading.Thread(target=test9)
a10=threading.Thread(target=test10)
a11=threading.Thread(target=test11)
a12=threading.Thread(target=test12)
a13=threading.Thread(target=test13)
a14=threading.Thread(target=test14)
a15=threading.Thread(target=test15)
a16=threading.Thread(target=test16)
a17=threading.Thread(target=test17)
a18=threading.Thread(target=test18)
a19=threading.Thread(target=test19)
a20=threading.Thread(target=test20)



a1.start()
a2.start()
a3.start()
a4.start()
a5.start()
a6.start()
a7.start()
a8.start()
a9.start()
a10.start()
a11.start()
a12.start()
a13.start()
a14.start()
a15.start()
a16.start()
a17.start()
a18.start()
a19.start()
a20.start()

        f.close()
        
def test13():
    file13=ad[num*12:num*13]
    for i in file13:
        f=open("G:/big_file/%s"%i,"r")
        print("12")
        f.close()

