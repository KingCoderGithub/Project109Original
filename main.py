import pandas as pd
import statistics
import csv

df = pd.read_csv("data.csv")
mathScore = df["math score"].to_list()
readingScore = df["reading score"].to_list()
writingScore = df["writing score"].to_list()

#Mean for height and Weight
mathMean = statistics.mean(mathScore)
readingMean = statistics.mean(readingScore)
writingMean = statistics.mean(writingScore)

#Median for height and weight
mathMedian = statistics.median(mathScore)
readingMedian = statistics.median(readingScore)
writingMedian = statistics.median(writingScore)

#Mode for height and weight
mathMode = statistics.mode(mathScore)
readingMode = statistics.mode(readingScore)
writingMode = statistics.mode(writingScore)

#Printing mean, median and mode to validate
print("Mean, Median and Mode of Math Score is {}, {} and {} respectively".format(mathMean, mathMedian, mathMode))
print("Mean, Median and Mode of Reading Score is {}, {} and {} respectively".format(readingMean, readingMedian, readingMode))
print("Mean, Median and Mode of Math Score is {}, {} and {} respectively".format(writingMean, writingMedian, writingMode))

#Standard deviation for height and weight
mathSTD = statistics.stdev(mathScore)
readingSTD = statistics.stdev(readingScore)
writingSTD = statistics.stdev(writingScore)

#1, 2 and 3 Standard Deviations for Math Score
mathSTDStart, mathSTDEnd = mathMean-mathSTD, mathMean+mathSTD
mathSTDStart, mathSTDEnd = mathMean-(2*mathSTD), mathMean+(2*mathSTD)
mathSTDStart, mathSTDEnd = mathMean-(3*mathSTD), mathMean+(3*mathSTD)

#1, 2 and 3 Standard Deviations for Reading Score
readingSTDStart, readingSTDEnd = readingMean-readingSTD, readingMean+readingSTD
readingSTDStart, readingSTDEnd = readingMean-(2*readingSTD), readingMean+(2*readingSTD)
readingSTDStart, readingSTDEnd = readingMean-(3*readingSTD), readingMean+(3*readingSTD)

#1, 2 and 3 Standard Deviations for Math Score
writingSTDStart, writingSTDEnd = writingMean-writingSTD, writingMean+writingSTD
writingSTDStart, writingSTDEnd = writingMean-(2*mathSTD), writingMean+(2*writingSTD)
writingSTDStart, writingSTDEnd = writingMean-(3*mathSTD), writingMean+(3*writingSTD)


#Percentage of data within 1, 2 and 3 Standard Deviations for Math Score
mathSTD1 = [result for result in mathScore if result > mathSTDStart and result < mathSTDEnd]
mathSTD2 = [result for result in mathScore if result > mathSTDStart and result < mathSTDEnd]
mathSTD3 = [result for result in mathScore if result > mathSTDStart and result < mathSTDEnd]

#Percentage of data within 1, 2 and 3 Standard Deviations for Reading Score
readingSTD1 = [result for result in readingScore if result > readingSTDStart and result < readingSTDEnd]
readingSTD2 = [result for result in readingScore if result > readingSTDStart and result < readingSTDEnd]
readingSTD3 = [result for result in readingScore if result > readingSTDStart and result < readingSTDEnd]

#Percentage of data within 1, 2 and 3 Standard Deviations for Reading Score
writingSTD1 = [result for result in writingScore if result > writingSTDStart and result < writingSTDEnd]
writingSTD2 = [result for result in writingScore if result > writingSTDStart and result < writingSTDEnd]
writingSTD3 = [result for result in writingScore if result > writingSTDStart and result < writingSTDEnd]

#Printing data for height and weight (Standard Deviation)
print("{}% of data for math score lies within 1 standard deviation".format(len(mathSTD1)*100.0/len(mathScore)))
print("{}% of data for math score within 2 standard deviations".format(len(mathSTD2)*100.0/len(mathScore)))
print("{}% of data for math score within 3 standard deviations".format(len(mathSTD3)*100.0/len(mathScore)))
print("{}% of data for reading score within 1 standard deviation".format(len(readingSTD1)*100.0/len(readingScore)))
print("{}% of data for reading score within 2 standard deviations".format(len(readingSTD2)*100.0/len(readingScore)))
print("{}% of data for reading score within 3 standard deviations".format(len(readingSTD3)*100.0/len(readingScore)))
print("{}% of data for writing score within 1 standard deviation".format(len(writingSTD1)*100.0/len(writingScore)))
print("{}% of data for writing score within 2 standard deviations".format(len(writingSTD2)*100.0/len(writingScore)))
print("{}% of data for writing score within 3 standard deviations".format(len(writingSTD3)*100.0/len(writingScore)))