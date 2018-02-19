import sys
import numpy
import random
import PyPluMA

# Scaling is done to make median=1
class CSVMapRangePlugin:
   def input(self, filename):
      self.myfile = filename+".file1.csv"
      self.myfile2 = filename+".file2.csv"

   def run(self):
      filestuff = open(self.myfile, 'r')
      filestuff2 = open(self.myfile2, 'r')

      self.firstline = filestuff.readline()
      self.firstline2 = filestuff2.readline()
      lines = []
      for line in filestuff:
         lines.append(line)
      lines2 = []
      for line2 in filestuff2:
         lines2.append(line2)

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.bacteria2 = self.firstline2.split(',')
      if (self.bacteria2.count('\"\"') != 0):
         self.bacteria2.remove('\"\"')

      self.n = len(self.bacteria)
      self.ADJ = []#numpy.zeros([self.m, self.n])
      self.ADJ2 = []
      i = 0
      for i in range(self.m):
            self.ADJ.append([])
            self.ADJ2.append([])
            contents = lines[i].split(',')
            contents2 = lines2[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               value = float(contents[j+1].strip())
               self.ADJ[i].append(value)#[j] = value
               value2 = float(contents2[j+1].strip())
               self.ADJ2[i].append(value2)
            i += 1


  
   def output(self, filename):
      for i in range(self.m):
         minimumA = min(self.ADJ[i])
         maximumA = max(self.ADJ[i])
         minimumB = min(self.ADJ2[i])
         maximumB = max(self.ADJ2[i])
         for j in range(self.n):
            self.ADJ[i][j] = minimumB + ((self.ADJ[i][j] - minimumA)/(maximumA - minimumA))*(maximumB - minimumB)
            if (self.ADJ[i][j] > 100):
               PyPluMA.log("WARNING: "+str(self.ADJ[i][j])+" "+str(maximumB))
      filestuff2 = open(filename, 'w')
      filestuff2.write(self.firstline)
      
      for i in range(self.m):
         filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.ADJ[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



