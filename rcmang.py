from tkinter import *
from tkinter import messagebox
from tabulate import tabulate
from datetime import datetime
import mysql.connector as pysql
from pathlib import Path

#global variables
#begins
authuser=''
hostname=''
username=''
pwd=''
fname='finalreport.txt'
emppcd='224'
candpcd='422'
usnmlist=['dumdum', 'damdam', 'heheboi']
apllist=[]
comblist=[]
selectedlist=[]
waitinglist=[]
rejectedlist=[]

win1 = Tk()

f1=Path('sqltext.txt')

def readcred():
    global hostname,username,pwd,comblist,apllist,selectedlist,waitinglist,rejectedlist
    f=open('sqltext.txt','r')
    hostname=f.readline()
    username=f.readline()
    pwd=f.readline()
    f.seek(0)
    f.close()

    conn=pysql.connect(host=hostname, user=username, password=pwd,charset='utf8')
    if True:
        cursor=conn.cursor()
        cursor.execute('use test')
        cursor.execute('select * from selected')
        selectedlist=list(cursor.fetchall())
        cursor.execute('select * from waiting')
        waitinglist=list(cursor.fetchall())
        cursor.execute('select * from rejected')
        rejectedlist=list(cursor.fetchall())

    comblist=list(selectedlist + waitinglist + rejectedlist)

    for a in comblist:
        apllist.append(a[0])
    conn.commit()
    conn.close()

txts='Congratulations!! We are glad to have you work with us at PEGASUS.\nFor further info regarding your placement, feel free to contact us\n on our helpdesk, at helpdesk@pegasus.org' 

txtw='You are currently in our waiting list. You are still eligible to \n claim vacant positions before the closing date. It\'s our pleasure\n keeping you informed. Thank you.' 

txtr='You were not selected, or were removed from the list. We appreciate your\n concern to invest your time and efforts in applying for this job.\n We wish you luck for a good future.'
#ends

win1.title('Recruitment Portal')
win1.geometry('480x240')


labl= Label(win1, text = 'Welcome to Recruitment Portal.\n\nPlease choose your position.\n\n')
labl.pack()

def eb():
    if f1.exists():
        readcred()

    else:
        statslabl.config(text='Please complete the process in your terminal')
        import init_sql_connection
        readcred()
        statslabl.config(text='')
    
    def login():
        
        if usnm.get() in usnmlist:            
            if (ebpcd.get()==emppcd):
                ebportal()       
            else:
                messagebox.showerror('Oops..', "Password is incorrect.")
                eb()
        else:
            messagebox.showerror('Oops..', "Username not found in registry.")
            eb()
    
    def ebportal():
        ebport = Toplevel(wineb)
        ebport.title('Portal')

        portlabl=Label(ebport, text='Please select an option:- ')
        portlabl.grid()

        def viewoption():
            voption=Toplevel(ebport)
            voption.title('View mode')

            def showtable1():
                table=Toplevel(voption)
                table.title('Selected List')
        
                class Table:
    
                    def __init__(self,table1):
        
                        for i in range(len(selectedlist)):
                            for j in range(len(selectedlist[0])):
                
                                self.e = Entry(table1, width=20, fg='blue',font=('Arial',16,'bold'))                  
                                self.e.grid(row=i, column=j)
                                self.e.insert(END, selectedlist[i][j])
                t=Table(table)

            sbtn=Button(voption,text='Selected List',command=showtable1)
            sbtn.grid()

            def showtable2():
                table=Toplevel(voption)
                table.title('Waiting List')
        
                class Table:
    
                    def __init__(self,table1):
        
                        for i in range(len(waitinglist)):
                            for j in range(len(waitinglist[0])):
                
                                self.e = Entry(table1, width=20, fg='blue',font=('Arial',16,'bold'))                  
                                self.e.grid(row=i, column=j)
                                self.e.insert(END, waitinglist[i][j])
                t=Table(table)

            wbtn=Button(voption,text='Waiting List',command=showtable2)
            wbtn.grid()

            def showtable3():
                table=Toplevel(voption)
                table.title('Rejected List')
        
                class Table:
    
                    def __init__(self,table1):
        
                        for i in range(len(rejectedlist)):
                            for j in range(len(rejectedlist[0])):
                
                                self.e = Entry(table1, width=20, fg='blue',font=('Arial',16,'bold'))                  
                                self.e.grid(row=i, column=j)
                                self.e.insert(END, rejectedlist[i][j])
                t=Table(table)                

            rbtn=Button(voption,text='Rejected list',command=showtable3)
            rbtn.grid()

        viewbtn=Button(ebport,text='View list',command=viewoption)
        viewbtn.grid()

        def editoption():
            eoption=Toplevel(ebport)
            eoption.title('List: Edit mode')

            edmlabl=Label(eoption, text='Please choose an option:-')
            edmlabl.grid()

            def restore():
                global selectedlist, waitinglist, rejectedlist
                selectedlist=[(12431,'Kruba'),(12432,'Sundhar'),(12433,'Tamil'),(12434,'Avinash'),(12435,'Vidhya')]
                waitinglist=[(12426,'Shivani'),(12427,'Dhikshita'),(12428,'Shreeman'),(12429,'Pritam'),(12430,'Kaushik')]
                rejectedlist=[(12421,'Mahi'),(12422,'Aaryan'),(12423,'Vaishnavi'),(12424,'Prakshana'),(12425,'Shubha')]
                update()

                done=Toplevel(eoption)
                done.title('Status')
                done.geometry('250x100')
                pslabl=Label(done,text='Done!')
                pslabl.pack()
                okbtn=Button(done,text='Ok',command=quit)
                okbtn.pack()
        
            def remscreen():
                remwind=Toplevel(eoption)
                remwind.title('Remove applicants')
                remlabl=Label(remwind, text='Enter Applicant no: ')
                remlabl.grid()
                rementry=Entry(remwind,width=16)
                rementry.grid(column=1,row=0)

                def remcand():
                    global selectedlist, waitinglist, rejectedlist
                    if (int(rementry.get()) in apllist):
                        for i in comblist:
                            if (int(rementry.get())==i[0]):
                                rejectedlist.append(i)
                                if (i in selectedlist):
                                    selectedlist.remove(i)
                                    selectedlist.append(waitinglist[0])
                                    waitinglist.remove(waitinglist[0])
                                elif (i in waitinglist):
                                    waitinglist.remove(i)
                        pslabl.config(text='Successfully removed applicants from existing list.\n Waiting list applicants were replaced.\nYou can close this window now.')   
                    else:
                        messagebox.showerror('Oops..', "Applicant not found in registry.")
                        remscreen()

                rembtn=Button(remwind,text='Remove',command=remcand)
                rembtn.grid()

                pslabl=Label(remwind,text='')
                pslabl.grid()

            deletebtn=Button(eoption,text='Remove applicants',command=remscreen)
            deletebtn.grid()

            resetbtn=Button(eoption,text='Reset all lists',command=restore)
            resetbtn.grid()

        editbtn=Button(ebport,text='Edit list',command=editoption)
        editbtn.grid()

        def savescreen():
            upscr=Toplevel()
            upscr.title('Save final list')

            def savefile():
                now= datetime.now()
                date= now.strftime('%d/%m/%Y on %H:%M:%S')
                head=['Applicant no','Name']
                stable=tabulate(selectedlist, headers=head, tablefmt='grid')
                wtable=tabulate(waitinglist, headers=head, tablefmt='grid')
                rtable=tabulate(rejectedlist, headers=head, tablefmt='grid')
                f=open(fname.get()+'.txt','w')
                f.write('PEGASUS Inc.,')
                f.write('\nDated, ')
                f.write(str(date))
                f.write('\nJob interview final list:- ')
                f.write('\nSelected list:-\n')
                f.write(stable)
                f.write('\nWaiting list:-\n')
                f.write(wtable)
                f.write('\nRejected list:-\n')
                f.write(rtable)
                f.write('\nSavefile authorised by: ')
                f.write(usnm.get())
                f.close()
                statslabl.config(text=('File '+(fname.get()+'.txt')+' has been successfully saved to the disk!'))
                update()
        
            flabl=Label(upscr,text="Enter filename [no extensions]: ")
            flabl.grid()
            fname=Entry(upscr,width=18)
            fname.grid()
            savebtn=Button(upscr, text='Save',command=savefile)
            savebtn.grid()
            statslabl=Label(upscr,text='')
            statslabl.grid()

        uploadbtn=Button(ebport,text='Save final list',command=savescreen)
        uploadbtn.grid()
    
    wineb = Toplevel(win1)
    wineb.title('Employer Login')
    wineb.geometry('320x200')

    usnmlabl = Label(wineb, text='Username:  ')
    usnmlabl.grid()

    usnm = Entry(wineb, width=24)
    usnm.grid(column=1, row=0)

    ebpcdlabl = Label(wineb, text='Passcode:  ')
    ebpcdlabl.grid()

    ebpcd = Entry(wineb,show='*', width=22)
    ebpcd.grid(column=1,row=1)
        
    loginbtn = Button(wineb, text='Login', command=login)
    loginbtn.grid(column=1, row=2)

    def update(): #flushing values into database
        conn1=pysql.connect(host=hostname, user=username, password=pwd,charset='utf8')
        cursor1=conn1.cursor()
        cursor1.execute('use test')
        cursor1.execute('delete from selected')
        cursor1.execute('delete from waiting')
        cursor1.execute('delete from rejected')
        sql='insert into selected values (%s, %s)'
        cursor1.executemany(sql,selectedlist)
        conn1.commit()
        sql='insert into waiting values (%s, %s)'
        cursor1.executemany(sql,waitinglist)
        conn1.commit()
        sql='insert into rejected values (%s, %s)'
        cursor1.executemany(sql,rejectedlist)
        conn1.commit()
        conn1.close()

    update()  


def es():
    wines = Toplevel(win1)
    wines.title('Candidate Details')
    wines.geometry('320x200')

    aplnolabl = Label(wines, text='Applicant No:  ')
    aplnolabl.grid()

    aplno = Entry(wines, width=24)
    aplno.grid(column=1, row=0)

    espcdlabl = Label(wines, text='Passcode:  ')
    espcdlabl.grid()

    espcd = Entry(wines,show='*', width=22)
    espcd.grid(column=1, row=1)

    def result():
        if (int(aplno.get()) in apllist):
            for j in apllist:       
                if (espcd.get()==candpcd):
                    esportal()
                    break    
                else:
                    messagebox.showerror('Oops..', "Password is incorrect.")
                    break                
        else:        
            messagebox.showerror('Oops..', "Username not found in registry.")
            es()

    def esportal():  
        res = Toplevel(wines)
        res.title('Results')
        truetxt=''

        for cand in comblist:
            if (cand[0]==int(aplno.get())):
                if cand in selectedlist:
                    truetxt=('Hey, '+cand[1]+'! '+txts)
                    reslabl=Label(res,text=truetxt,font=('Arial',25), bg="white",fg='green')
                    reslabl.grid()

                elif cand in waitinglist:
                    truetxt=('Hey, '+cand[1]+'! '+txtw)
                    reslabl=Label(res,text=truetxt,font=('Arial',25), bg="silver",fg='yellow')
                    reslabl.grid()

                elif cand in rejectedlist:
                    truetxt=('Hey, '+cand[1]+'! '+txtr)
                    reslabl=Label(res,text=truetxt,font=('Arial',25), bg="silver",fg='red')
                    reslabl.grid()

    def checkfile():
        if f1.exists():
            readcred()
            result()
        else:
            messagebox.showerror('DATABASE NOT FOUND!!!', 'This could mean that the results are not yet declared. Please try again later.')

    rsltbtn=Button(wines, text='Check Results', command=checkfile)
    rsltbtn.grid(column=1,row=2)

ebbtn= Button(win1, text='Employer', command=eb)
ebbtn.pack()

esbtn= Button(win1, text='Candidate', command=es)
esbtn.pack()

statslabl=Label(win1, text='')
statslabl.pack()
              
win1.mainloop()
