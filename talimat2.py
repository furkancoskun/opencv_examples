import serial

ser = serial.Serial('/dev/ttyACM0',9600)
def yazdir():
    for i in range(boy):
        for j in range(en):
            print(lbt2[i][j], end = "")
        print("")



def cikmazDoldur(en,boy):
    sayac = 0
    for i in range(boy):
        for j in range(en):
            if((i == 0 or i == en-1 or j == 0 or j == boy-1) and lbt1[i][j]==0):               
                lbt1[i][j] = 1
                continue
            elif(lbt1[i][j]==0):
                if(lbt1[i][j-1]+lbt1[i][j+1]+lbt1[i-1][j]+lbt1[i+1][j] == 3):
                        lbt1[i][j]=1
                        sayac = sayac+1
    print ("%d cikmaz dolduruldu" % sayac)
#    yazdir()
    return sayac

lbt = [
        [1,1,1,0,1,1,1,1,1,3,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,1,1,1,0,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],
        [1,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
        [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,1,0,1,0,0,0,1],
        [1,0,1,0,1,1,1,1,1,0,1,0,1,1,1],
        [1,0,1,0,1,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1,0,1,1,1,0,1,0,1],
        [0,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
        [1,1,1,0,1,0,1,1,1,0,1,1,1,0,1],
        [1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,4,1]
    ]

boy = len(lbt)
en = len(lbt[0])

lbt1 = [
        [1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,1,1,1,0,1,1,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],
        [1,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
        [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,1,0,1,0,0,0,1],
        [1,0,1,0,1,1,1,1,1,0,1,0,1,1,1],
        [1,0,1,0,1,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1,0,1,1,1,0,1,0,1],
        [1,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
        [1,1,1,0,1,0,1,1,1,0,1,1,1,0,1],
        [1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,3,1]
    ]
 
lbt2 =[
        [1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,1,1,1,0,1,1,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],
        [1,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
        [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,1,0,1,0,0,0,1],
        [1,0,1,0,1,1,1,1,1,0,1,0,1,1,1],
        [1,0,1,0,1,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1,0,1,1,1,0,1,0,1],
        [1,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
        [1,1,1,0,1,0,1,1,1,0,1,1,1,0,1],
        [1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,3,1]
    ]

for i in range(boy):
    for j in range(en):
        lbt1[i][j] = lbt[i][j]
        if(lbt[i][j]==3) :
                row_entry =i
                col_entry =j
        if(lbt[i][j]==4) :
            row_end =i
            col_end =j

print("Labirent eni: %s, boyu: %s " % (en,boy))
hesapla = True

while hesapla:
    hesapla = cikmazDoldur(en,boy)
print("\n")

for i in range(boy):
    for j in range(en):
        lbt2[i][j] = lbt1[i][j]+lbt[i][j]

yazdir()

right=0
left=1
right_counter=0
left_counter=0
instr=[]
row=row_entry
col=col_entry   
old_row=row
old_col=col
a=0
b=0

while(lbt2[row][col]!=8) :
        print("Current row: %s , Current column: %s   Previous row: %s , Previous column: %s"  % (row, col, old_row, old_col))
        print("\n")
#Downward
        if(row!=boy-1) :
                if(row>=old_row) :
                        if(lbt2[row+1][col]==1) :
                                if(col>old_col) :
                                        right_counter=right_counter+1
                                elif(col<old_col) :
                                        left_counter=left_counter+1
                        elif(lbt2[row+1][col]==0 or lbt2[row+1][col]==8) :
                                if(col>old_col) :
                                        right_counter=right_counter+1
                                        instr.append("%s" %right)
										instr.append("%s" %right_counter)
                                        right_counter=0
                                        left_counter=0
                                elif(col<old_col) :
                                        left_counter=left_counter+1
                                        instr.append(left)
										instr.append(left_counter)
                                        left_counter=0
                                        right_counter=0
                                a=1
                                
                        else :
                                row=row
                                col=col
        print("Current row: %s , Current column: %s   Previous row: %s , Previous column: %s "   % (row, col, old_row, old_col))
        print("\n")
#Upward
        if(row!=0) :
                if(row<=old_row) :
                        if(lbt2[row-1][col]==1) :
                                if(col<old_col) :
                                        right_counter=right_counter+1
                                elif(col>old_col) :
                                        left_counter=left_counter+1
                        elif(lbt2[row-1][col]==0 or lbt2[row-1][col]==8) :
                                if(col<old_col) :
                                        right_counter=right_counter+1
                                        instr.append("%s" %right)
										instr.append("%s" %right_counter)
                                        right_counter=0
                                        left_counter=0
                                elif(col>old_col) :
                                        left_counter=left_counter+1
                                        instr.append("%s" %left)     
										instr.append("%s" %left_counter)
                                        left_counter=0
                                        right_counter=0
                                a=-1    

                                        
                        else :
                                row=row
                                col=col
        print("Current row: %s , Current column: %s   Previous row: %s , Previous column: %s"  % (row, col, old_row, old_col))
        print("\n")
#Rightward
        if(col!=en-1) :
                if(col>=old_col) :
                        if(lbt2[row][col+1]==1) :
                                if(row<old_row) :
                                        right_counter=right_counter+1
                                elif(row>old_row) :
                                        left_counter=left_counter+1
                        elif(lbt2[row][col+1]==0 or lbt2[row][col+1]==8) :
                                if(row<old_row) :
                                        right_counter=right_counter+1
                                        instr.append("%s" %right)
										instr.append("%s" %right_counter)
                                        right_counter=0
                                        left_counter=0
                                elif(row>old_row) :
                                        left_counter=left_counter+1
                                        instr.append("%s" %left)
										instr.append("%s" %left_counter)
                                        left_counter=0
                                        right_counter=0
                                b=1

                                
                        else :
                                row=row
                                col=col
        print("Current row: %s , Current column: %s   Previous row: %s , Previous column: %s"  % (row, col, old_row, old_col))
        print("\n")
#Leftward
        if(col!=0) :
                if(col<=old_col) :
                        if(lbt2[row][col-1]==1) :
                                if(row>old_row) :
                                        right_counter=right_counter+1
                                elif(row<old_row) :
                                        left_counter=left_counter+1
                        elif(lbt2[row][col-1]==0 or lbt2[row][col-1]==8) :
                                if(row>old_row) :
                                        right_counter=right_counter+1
                                        instr.append("%s" %right)
										instr.append("%s" %right_counter)
                                        right_counter=0
                                        left_counter=0
                                elif(row<old_row) :
                                        left_counter=left_counter+1
                                        instr.append("%s" %left)
										instr.append("%s" %left_counter)
                                        left_counter=0  
                                        right_counter=0
                                b=-1    
                        else :
                                row=row
                                col=col
                                
        if(not(row == old_row or b == 0)):
                right_counter = 0
                left_counter=0
        
        if(not(col == old_col or a == 0)):
                right_counter=0
                left_counter=0
        old_row=row
        old_col=col


        row=row+a
        col=col+b
        a=0
        b=0
        
print(instr)
ser.write(instr)
