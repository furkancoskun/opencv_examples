import cv2
import numpy as np
import serial

#ser = serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_ODD,stopbits=serial.STOPBITS_TWO,bytesize=serial.SEVENBITS)


dosya = '/home/frkn/Desktop/maze_threshold_cropped.jpg'
image = cv2.imread(dosya)
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image_gray = np.float32(image_gray)
dst = cv2.cornerHarris(image_gray,2,3,0.04)

dst = cv2.dilate(dst,None)
		
image[dst>0.01*dst.max()] = [0,0,255]

coord = np.where(np.all(image == (0, 0, 255), axis=-1))
coord_sum = np.zeros(len(coord[0]))
coord_dif = np.zeros(len(coord[0]))
for i in range(len(coord[0])):
	coord_sum [i] = coord[0][i]+coord[1][i]
	coord_dif [i] = coord[0][i]-coord[1][i]

sagalt_y = coord[0][coord_sum.tolist().index(max(coord_sum))]
sagalt_x = coord[1][coord_sum.tolist().index(max(coord_sum))]
solust_y = coord[0][coord_sum.tolist().index(min(coord_sum))]
solust_x = coord[1][coord_sum.tolist().index(min(coord_sum))]
solalt_y = coord[0][coord_dif.tolist().index(max(coord_dif))]
solalt_x = coord[1][coord_dif.tolist().index(max(coord_dif))]
sagust_y = coord[0][coord_dif.tolist().index(min(coord_dif))]
sagust_x = coord[1][coord_dif.tolist().index(min(coord_dif))]


brKareSayi= 15 #labda  15 #gercekte 37 #kalibrasyonda 19
brKareBoyut= 70 #labda  70 #gercekte 45 #kalibrasyonda 90
cıktıBoyut = brKareSayi * brKareBoyut #labda 1050 #gercekte 1990 #kalibrasyonda 2000
ek = 70 #labda 70
img = cv2.imread(dosya,0)
offset = 10

pts1 = np.float32([[solust_x-offset,solust_y-offset],[sagust_x+offset,sagust_y-offset],[solalt_x-offset,solalt_y+offset],[sagalt_x+offset,sagalt_y+offset]])
pts2 = np.float32([[0,0],[cıktıBoyut,0],[0,cıktıBoyut],[cıktıBoyut,cıktıBoyut]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(cıktıBoyut,cıktıBoyut))
kernel = np.ones((ek,ek),np.uint8)
dilation = cv2.erode(dst,kernel,iterations=1)
dlted=dilation.copy()
np.asarray(dlted)

maze = np.divide(dilation.reshape(brKareSayi,brKareBoyut,brKareSayi,brKareBoyut).sum(axis=(1,3)),brKareBoyut*brKareBoyut)
maze = maze.astype(int)
a = 100
maze[ maze <= a ] = 1
maze[ maze > a ] = 0

cv2.imwrite('0.jpg',dst)
cv2.imwrite('1.jpg',dilation)

#print(dst)

def cikmazDoldur(en,boy):
	sayac = 0
	for i in range(boy):
		for j in range(en):
			if((i == 0 or i == en-1 or j == 0 or j == boy-1) and lbt1[i][j]==0):
				lbt1[i][j]=1
				continue
			elif(lbt1[i][j]==0):
				if(lbt1[i][j-1]+lbt1[i][j+1]+lbt1[i-1][j]+lbt1[i+1][j] == 3):
					lbt1[i][j]=1
					sayac = sayac+1
	print ("%d cikmaz dolduruldu" % sayac)
	return sayac

lbt = maze.copy()
lbt[0][3] = 3
lbt[11][0] = 4
#lbt[3][2] = 0
boy = len(lbt)
en = len(lbt[0])

lbt1 = lbt.copy()
 
lbt2 = lbt.copy()
 

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
print(lbt2)

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
					instr.append(right)
					instr.append(right_counter)
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
					instr.append(right)
					instr.append(right_counter)
					right_counter=0
					left_counter=0
				elif(col>old_col) :
					left_counter=left_counter+1
					instr.append(left)
					instr.append(left_counter)	
					left_counter=0
					right_counter=0
				a=-1	

					
			else :
				row=row
				col=col
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
					instr.append(right)
					instr.append(right_counter)
					right_counter=0
					left_counter=0
				elif(row>old_row) :
					left_counter=left_counter+1
					instr.append(left)
					instr.append(left_counter)
					left_counter=0
					right_counter=0
				b=1

				
			else :
				row=row
				col=col
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
					instr.append(right)
					instr.append(right_counter)
					right_counter=0
					left_counter=0
				elif(row<old_row) :
					left_counter=left_counter+1
					instr.append(left)
					instr.append(left_counter)
					left_counter=0	
					right_counter=0
				b=-1	
			else :
				row=row
				col=col
	old_row=row
	old_col=col
	row=row+a
	col=col+b
	a=0
	b=0
instr.append(2)
print(instr)




