import csv
import math
import random
import time
jumneuron=6
dataset=[]
neuron=[]
dev=2
lr=0.1
def generateneuron():
	return [random.uniform(0,17),random.uniform(0,17)]
with open('Tugas 2 ML Genap 2018-2019 Dataset Tanpa Label.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		dataset.append(row)
def jarakNO(neuron,objek):
	return math.pow((neuron[0]-float(objek[0])),2)+math.pow((neuron[1]-float(objek[1])),2)
def jarakNN(a,b):
	return math.pow((a[0]-b[0]),2)+math.pow((a[1]-b[1]),2)
def getterdekat(a):
	jarak=10000000000000000000000
	min=0
	for x in range(jumneuron):
		sementara = jarakNO(neuron[x],a) 
		if jarak > sementara:
			jarak=sementara
			min=x
	return min,jarak
def findT(a,b):
	return math.exp(-1*jarakNN(a,b)/(2*dev*dev))
def deltaw(a,b,c,d):
	return lr*findT(a,b)*(float(c[d])-a[d])
for i in range(jumneuron) : 
    neuron.append(generateneuron())
for i in range(100):
	for x in dataset:
		nterdekat,j=getterdekat(x)
		n1=(nterdekat+1)%jumneuron
		n2=(nterdekat-1)%jumneuron
		for z in range(2):
			neuron[n1][z]=neuron[n1][z]+deltaw(neuron[n1],neuron[nterdekat],x,z)
		for z in range(2):
			neuron[n2][z]=neuron[n2][z]+deltaw(neuron[n2],neuron[nterdekat],x,z)
		for z in range(2):
			neuron[nterdekat][z]=neuron[nterdekat][z]+deltaw(neuron[nterdekat],neuron[nterdekat],x,z)
	dev=dev*math.exp(-i/2)
	lr=lr*math.exp(-i/2)
	if dev < 0.00000000000000000000001:
		dev=2
	if lr < 0.00000000000000000000001:
		lr=0.1
sse=0
with open('hasil.csv', 'w', newline='\n') as writeFile:
	writer = csv.writer(writeFile,dialect='excel')
	for x in dataset:
		cluster,s=getterdekat(x)
		sse+=math.sqrt(s)
		writer.writerow([x[0],x[1],cluster])
writeFile.close()
print("sse : ",sse)
print("jumneuron : ",jumneuron)