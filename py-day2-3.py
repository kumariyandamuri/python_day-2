''' write a program to read sno,sname,group,3 subjects
    and print total and avg
ex:sno=1,name=sai,group=mpcs,s1=80,s2=70,s3=60
output:total:210,avg-70'''
sno=int(input("Enter student number:"))
name=input("Enter student name:")
group=input("Enter studemt group:")
s1=int(input("Enter First sub marks:"))
s2=int(input("Enter Second  sub marks:"))
s3=int(input("Enter Third sub marks:"))
total=s1+s2+s3
print("Total Marks :",total)
avg=total/3
print("Average Marks:",avg)
