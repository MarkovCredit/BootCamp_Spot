library(AppliedPredictiveModeling)
library(ggplot2)
library(caret)
library(dplyr)



#read in the training dataset; Kaggle already split the data into training and testing
df <- read.csv(file = file.choose(), stringsAsFactors =  FALSE)
str(df)
df$AdoptionSpeed <- as.factor(df$AdoptionSpeed)

#feature plot of the first few columns
featurePlot(x = df[,c('Type','Age','Breed1','Breed2','Gender','Color1')], 
            y = df$AdoptionSpeed, 
            plot = "box",
            ## Add a key at the top
            auto.key = list(columns = 3))

#check for near zero var for the numerics
nums <- unlist(lapply(df, is.numeric))  
df_nums <- df[,nums]

nzv <- nearZeroVar(df_nums, saveMetrics= TRUE)
nzv
#check for missing values using a summary function and then incomplete cases
summary(df)
missing <- df[!complete.cases(df),]

#correlated predictors
descrCor <-  cor(df_nums)
highCorr <- sum(abs(descrCor[upper.tri(descrCor)]) > .999)
highCorr
summary(descrCor[upper.tri(descrCor)])

#use the nnet package for multi-class predictions



