
import numpy as np
import cv2 as cv

img=cv.imread("medicine_with_noise.jpg")
blurred = cv.GaussianBlur(img, (19,19),0)
background = np.ones((878,1168,3),dtype=np.uint8)*255
print(blurred.shape)



#สีเหลือง b/g/r 
upper_range_yellow=np.array([128,165,178]) # ค่าสูงสุดของ h,s และ v ที่ต้องการตรวจจับ
lower_range_yellow=np.array([40,90,98]) # ค่าต่ำสุดของ h,s และ v ที่ต้องการตรวจจับ
mask_yellow = cv.inRange(blurred,lower_range_yellow,upper_range_yellow) #สร้าง mask จากช่วง hsv ที่กำหนด
mask_indices1=np.where(mask_yellow==255) # 2.2.1 
output_imagey = np.zeros(img.shape, dtype = "uint8")
output_imagey[mask_indices1] =blurred[mask_indices1] # 2.2.2

#ดึงยาสีเหลือง
axis_yellow=np.zeros((878,1168),dtype=np.uint8)
axis_yellow1=np.zeros((878,1168),dtype=np.uint8)
find0,contours0=cv.findContours(mask_yellow,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
for ints0 in range(len(find0)):
    zone0 =cv.contourArea(find0[ints0])
    print(zone0)
    if zone0 == 7932.5 :
        cv.drawContours(axis_yellow,find0,ints0,(255,255,255),-1)
    if zone0 == 8198.5 :
        cv.drawContours(axis_yellow1,find0,ints0,(255,255,255),-1)

yellow =np.where(axis_yellow==255)
yellow_1 =np.where(axis_yellow1==255)
background [yellow[0]-180, yellow[1]+250] = blurred[yellow]
background [yellow_1[0]-280, yellow_1[1]-50] = blurred[yellow_1]


#สีชมพู
upper_range_pink=np.array([196,177,220]) # ค่าสูงสุดของ h,s และ v ที่ต้องการตรวจจับ
lower_range_pink=np.array([118,110,140]) # ค่าต่ำสุดของ h,s และ v ที่ต้องการตรวจจับ
mask_pink = cv.inRange(blurred,lower_range_pink,upper_range_pink) #สร้าง mask จากช่วง hsv ที่กำหนด
mask_indices2=np.where(mask_pink==255) # 2.2.1 
output_imagep = np.zeros(img.shape, dtype = "uint8")
output_imagep[mask_indices2] =blurred[mask_indices2] # 2.2.2

#ดึงยาสีชมพู
axis_pink=np.zeros((878,1168),dtype=np.uint8)
axis_pink1=np.zeros((878,1168),dtype=np.uint8)
axis_pink2=np.zeros((878,1168),dtype=np.uint8)
axis_pink3=np.zeros((878,1168),dtype=np.uint8)
axis_pink4=np.zeros((878,1168),dtype=np.uint8)
find1,contours1=cv.findContours(mask_pink,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
for ints1 in range(len(find1)):
    zone1 =cv.contourArea(find1[ints1])
    print(zone1)
    if zone1 == 3023.0:
        cv.drawContours(axis_pink,find1,ints1,(255,255,255),-1)
    if zone1 == 2379.5 :
        cv.drawContours(axis_pink1,find1,ints1,(255,255,255),-1)
    if zone1 == 1949.0 :
        cv.drawContours(axis_pink2,find1,ints1,(255,255,255),-1)
    if zone1 == 2154.0 :
        cv.drawContours(axis_pink3,find1,ints1,(255,255,255),-1)
    if zone1 == 2218.5 :
        cv.drawContours(axis_pink4,find1,ints1,(255,255,255),-1)

pink =np.where(axis_pink==255)
pink_1 =np.where(axis_pink1==255)
pink_2 =np.where(axis_pink2==255)
pink_3 =np.where(axis_pink3==255)
pink_4 =np.where(axis_pink4==255)

background [pink[0]-480,pink[1]-80,] = blurred[pink]
background [pink_1[0]-450,pink_1[1]-420,] = blurred[pink_1]
background [pink_2[0]-420,pink_2[1]-430,] = blurred[pink_2]
background [pink_3[0]-190,pink_3[1]-200,] = blurred[pink_3]
background [pink_4[0]-120,pink_4[1]-0,] = blurred[pink_4]

# สีฟ้า
upper_range_blue=np.array([208,160,116]) # ค่าสูงสุดของ h,s และ v ที่ต้องการตรวจจับ
lower_range_blue=np.array([109,90,72]) # ค่าต่ำสุดของ h,s และ v ที่ต้องการตรวจจับ
mask_blue = cv.inRange(blurred,lower_range_blue,upper_range_blue) #สร้าง mask จากช่วง hsv ที่กำหนด
mask_indices3=np.where(mask_blue==255) # 2.2.1 
output_imageb = np.zeros(img.shape, dtype = "uint8")
output_imageb[mask_indices3] =blurred[mask_indices3] # 2.2.2

#ดึงยาสีฟ้า
axis_blue=np.zeros((878,1168),dtype=np.uint8)
axis_blue1=np.zeros((878,1168),dtype=np.uint8)
axis_blue2=np.zeros((878,1168),dtype=np.uint8)
axis_blue3=np.zeros((878,1168),dtype=np.uint8)
find2,contours2=cv.findContours(mask_blue,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
for ints2 in range(len(find2)):
    zone2 =cv.contourArea(find2[ints2])
    print(zone2)
    if zone2 == 836.0 :
        cv.drawContours(axis_blue,find2,ints2,(255,255,255),-1)
    if zone2 == 1140.0 :
        cv.drawContours(axis_blue1,find2,ints2,(255,255,255),-1)
    if zone2 == 1253.0 :
        cv.drawContours(axis_blue2,find2,ints2,(255,255,255),-1)
    if zone2 == 1147.5 :
        cv.drawContours(axis_blue3,find2,ints2,(255,255,255),-1)

blue =np.where(axis_blue==255)
blue_1 =np.where(axis_blue1==255)
blue_2 =np.where(axis_blue2==255)
blue_3 =np.where(axis_blue3==255)
background [blue[0]+360,blue[1]-100,] = blurred[blue]
background [blue_1[0]+200,blue_1[1]-10,] = blurred[blue_1]
background [blue_2[0]+100,blue_2[1]-40,] = blurred[blue_2]
background [blue_3[0]+30,blue_3[1]-150,] = blurred[blue_3]



# สีดำ
upper_range_black=np.array([134,120,128]) # ค่าสูงสุดของ h,s และ v ที่ต้องการตรวจจับ
lower_range_black=np.array([38,40,34]) # ค่าต่ำสุดของ h,s และ v ที่ต้องการตรวจจับ
mask_black = cv.inRange(blurred,lower_range_black,upper_range_black) #สร้าง mask จากช่วง hsv ที่กำหนด
mask_indices4=np.where(mask_black==255) # 2.2.1 
output_imagebl = np.zeros(img.shape, dtype = "uint8")
output_imagebl[mask_indices4] =blurred[mask_indices4] # 2.2.2

#ดึงยาสีดำ
axis_black=np.zeros((878,1168),dtype=np.uint8)
axis_black1=np.zeros((878,1168),dtype=np.uint8)
axis_black2=np.zeros((878,1168),dtype=np.uint8)
find3,contours3=cv.findContours(mask_black,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
for ints3 in range(len(find3)):
    zone3 =cv.contourArea(find3[ints3])
    print(zone3)
    if zone3 == 3925.5 :
        cv.drawContours(axis_black,find3,ints3,(255,255,255),-1)
    if zone3 == 3726.0 :
        cv.drawContours(axis_black1,find3,ints3,(255,255,255),-1)
    if zone3 == 4119.5 :
        cv.drawContours(axis_black2,find3,ints3,(255,255,255),-1)
#ย้ายเม็ด
black =np.where(axis_black==255)
black_1 =np.where(axis_black1==255)
black_2 =np.where(axis_black2==255)
background [black[0]+100,black[1]+520] = blurred[black]
background [black_1[0]+400,black_1[1]+200] = blurred[black_1]
background [black_2[0]+170,black_2[1]+400] = blurred[black_2]

#สีครีม
upper_range_cream=np.array([176,192,215]) # ค่าสูงสุดของ h,s และ v ที่ต้องการตรวจจับ
lower_range_cream=np.array([99,108,128]) # ค่าต่ำสุดของ h,s และ v ที่ต้องการตรวจจับ
mask_cream = cv.inRange(blurred,lower_range_cream,upper_range_cream) #สร้าง mask จากช่วง hsv ที่กำหนด
mask_indices5=np.where(mask_cream==255) # 2.2.1 
output_imagec = np.zeros(img.shape, dtype = "uint8")
output_imagec[mask_indices5] =blurred[mask_indices5] # 2.2.2

#ดึงยาสีครีม
axis_cream=np.zeros((878,1168),dtype=np.uint8)
axis_cream1=np.zeros((878,1168),dtype=np.uint8)
axis_cream2=np.zeros((878,1168),dtype=np.uint8)
find4,contours4=cv.findContours(mask_cream,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
for ints4 in range(len(find4)):
    zone4 =cv.contourArea(find4[ints4])
    print(zone4)
    if zone4== 3760.5 :
        cv.drawContours(axis_cream,find4,ints4,(255,255,255),-1)
    if zone4== 3974.0 :
        cv.drawContours(axis_cream1,find4,ints4,(255,255,255),-1)
    if zone4== 3053.0 :
        cv.drawContours(axis_cream2,find4,ints4,(255,255,255),-1)

cream =np.where(axis_cream==255)
cream_1 =np.where(axis_cream1==255)
cream_2 =np.where(axis_cream2==255)
background [cream[0]-780,cream[1]+370] = blurred[cream]
background [cream_1[0]-150,cream_1[1]-90] = blurred[cream_1]
background [cream_2[0]-250,cream_2[1]-350] = blurred[cream_2]

#rectangle (ภาพ,มุมที่ 1(บนซ้าย),มุมที่ 2(ล่างขวา),สี,ความหนา)
#pink
cv.rectangle(background,(110,70),(330,300),(0,0,0),(3))
#blue
cv.rectangle(background,(400,480),(200,660),(0,0,0),(3))
#black
cv.rectangle(background,(690,550),(950,750),(0,0,0),(3))
#cream
cv.rectangle(background,(510,200),(740,410),(0,0,0),(3))
#yellow
cv.rectangle(background,(790,20),(1140,210),(0,0,0),(3))

#ใส่ข้อความภาพ
cv.putText(background,"Med1: 5 tablet",(110,50),cv.FONT_HERSHEY_DUPLEX,0.8,(0,0,0,cv.LINE_4))
cv.putText(background,"Med2: 3 tablet",(510,180),cv.FONT_HERSHEY_DUPLEX,0.8,(0,0,0,cv.LINE_4))
cv.putText(background,"Med5: 4 tablet",(200,460),cv.FONT_HERSHEY_DUPLEX,0.8,(0,0,0,cv.LINE_4))
cv.putText(background,"Med3: 3 Capsule",(790,250),cv.FONT_HERSHEY_DUPLEX,0.8,(0,0,0,cv.LINE_4))
cv.putText(background,"Med4: 2 Capsule",(690,530),cv.FONT_HERSHEY_DUPLEX,0.8,(0,0,0,cv.LINE_4))

cv.imshow("original", img)
cv.imshow("Gaussian", blurred)
# cv.imshow("yellow",output_imagey)
# cv.imshow("pink",output_imagep)
# cv.imshow("blue",output_imageb)
# cv.imshow("black",output_imagebl)
# cv.imshow("cream",output_imagec)
cv.imshow("bk",background)

cv.waitKey()







