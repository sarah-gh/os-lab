boys = ['Ali','Reza','Yasin','Benyamin','Mehrdad','Sajjad','Aidin','Shahin','Amirhossein','Sina']
girls = ['Sara','Zari','Neda','Homa','Eli','Goli','Mary','Mina','Kimia','Melika']
girls = set(girls)
print([(boys[i],girls.pop()) for i in range(len(boys))])