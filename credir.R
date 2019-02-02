###2019/1/28###
###fankai###
install.packages("car")
library("car")
library("nortest")
install.packages("fBasics")
library("fBasics")
###### loading dataset ######
df.all.train<-read.csv("train_dataset1.csv")
df.all.train.temp<-read.csv("train_dataset.csv")
df.all.test<-read.csv("test_dataset.csv")
df.all.test.temp<-read.csv("test_dataset.csv")
mat.age<-as.matrix(df.all.train[,3])
df.all.train$age<-mat.age
###### dataset message ######
summary(df.all.train)
df.cor.train<-cor(df.all.train[2:30]) #corealation
barplot(df.cor.train[29,1:10])
barplot(df.cor.train[29,11:16])
barplot(df.cor.train[29,16:28])
hist(df.all.train$age)              #distribution
hist(df.all.train$netage)
hist(df.all.train$fee)
hist(df.all.train$X6mconsum)
hist(df.all.train$mfee)
hist(df.all.train$mrsum)
hist(df.all.train$circle)
hist(df.all.train$mallt)
hist(df.all.train$emall)
hist(df.all.train$diliv)
hist(df.all.train$mmm)
hist(df.all.train$videot)
hist(df.all.train$plane)
hist(df.all.train$train)
hist(df.all.train$tripappt)

###### processing missing value and outlier ######
quantile(df.all.train$age,0.01) #1%
quantile(df.all.train$age,0.99) #99%
for (i in 1:50000) #age 
{ 
  if(df.all.train[i,3]<=18)
    df.all.train[i,3]<-18
}
for (i in 1:50000) #age
{ 
  if(df.all.train[i,3]>=71)
    df.all.train[i,3]<-71
}
for (i in 1:50000) #netage
{ 
  if(df.all.train[i,"netage"]<=5)
    df.all.train[i,"netage"]<-5
}
for (i in 1:50000) #netage
{ 
  if(df.all.train[i,"netage"]>=274)
    df.all.train[i,"netage"]<-274
}
for (i in 1:50000) #fee
{ 
  if(df.all.train[i,"fee"]>=299)
    df.all.train[i,"fee"]<-299
}
for (i in 1:50000) #6 month average consumption == 0
{ 
  if(df.all.train[i,"X6mconsum"]<=12)
    df.all.train[i,"X6mconsum"]<-12
}
for (i in 1:50000) #6 month average consumption == 0
{ 
  if(df.all.train[i,"X6mconsum"]>=279)
    df.all.train[i,"X6mconsum"]<-279
}
for (i in 1:50000) #mfee
{ 
  if(df.all.train[i,"mfee"]<=10)
    df.all.train[i,"mfee"]<-10
}
for (i in 1:50000) #mfee
{ 
  if(df.all.train[i,"mfee"]>=295)
    df.all.train[i,"mfee"]<-295
}
for (i in 1:50000) #month rsum
{ 
  if(df.all.train[i,"mrsum"]<=10)
    df.all.train[i,"mrsum"]<-10
}
for (i in 1:50000) #month rsum
{ 
  if(df.all.train[i,"mrsum"]>=700)
    df.all.train[i,"mrsum"]<-700
}
for (i in 1:50000) #circle
{ 
  if(df.all.train[i,"circle"]<=1)
    df.all.train[i,"circle"]<-1
}
for (i in 1:50000) #circle
{ 
  if(df.all.train[i,"circle"]>=244)
    df.all.train[i,"circle"]<-244
}
for (i in 1:50000) #mallt
{ 
  if(df.all.train[i,"mallt"]>=92)
    df.all.train[i,"mallt"]<-92
}
for (i in 1:50000) #e-mall
{ 
  if(df.all.train[i,"emall"]>=14451)
    df.all.train[i,"emall"]<-14451
}
for (i in 1:50000) #diliv
{ 
  if(df.all.train[i,"diliv"]>=66)
    df.all.train[i,"diliv"]<-6
}
for (i in 1:50000) #economic
{ 
  if(df.all.train[i,"mmm"]>=8645)
    df.all.train[i,"mmm"]<-8645
}
for (i in 1:50000) #video
{ 
  if(df.all.train[i,"videot"]>=44341)
    df.all.train[i,"videot"]<-44341
}
for (i in 1:50000) #plane
{ 
  if(df.all.train[i,"plane"]>=7)
    df.all.train[i,"plane"]<-7
}
for (i in 1:50000) #train
{ 
  if(df.all.train[i,"train"]>=7)
    df.all.train[i,"train"]<-7
}
for (i in 1:50000) #traveller app
{ 
  if(df.all.train[i,"tripappt"]>=293)
    df.all.train[i,"tripappt"]<-293
}
###### normal test ######
hist(df.all.train$age)
df.all.train$age<-log(df.all.train$age)
hist(df.all.train$netage)
df.all.train$netage<-log(df.all.train$netage)
hist(df.all.train$fee)
df.all.train$fee<-sqrt(df.all.train$fee)
hist(df.all.train$X6mconsum)
df.all.train$X6mconsum<-log(df.all.train$X6mconsum)
hist(df.all.train$mfee)
df.all.train$mfee<-log(df.all.train$mfee)
hist(df.all.train$mrsum)
df.all.train$mrsum<-log(df.all.train$mrsum)
hist(df.all.train$circle)
df.all.train$circle<-log(df.all.train$circle)
hist(df.all.train$mallt)
df.all.train$mallt<-sqrt(df.all.train$mallt)
hist(df.all.train$emall)
df.all.train$emall<-sqrt(df.all.train$emall)
hist(df.all.train$diliv)
df.all.train$diliv<-sqrt(df.all.train$diliv)
hist(df.all.train$mmm)
df.all.train$mmm<-sqrt(df.all.train$mmm)
hist(df.all.train$videot)
df.all.train$videot<-sqrt(df.all.train$videot)
hist(df.all.train$plane)
df.all.train$plane<-sqrt(df.all.train$plane)
hist(df.all.train$train)
df.all.train$train<-sqrt(df.all.train$train)
hist(df.all.train$tripappt)
df.all.train$tripappt<-sqrt(df.all.train$tripappt)
###### linear regression ######
fit1<-lm(credit~+age+uni+X4G+netage+ptd+fee+X6mconsum+mfee+mrsum+arr+sensitive+blak
         +circle+mall+mallt+wanda+samclub+cinema+sightsee+gym+emall+diliv+registration+
          mmm+videot+train+plane+tripappt,df.all.train)
summary(fit1)
confint(fit1)
par(mfrow=c(2,2))
plot(fit1)
###### normalization ######
for (i in 2:29) 
{
  df.all.train[,i]<-scale(df.all.train[,i],center = TRUE,scale = TRUE)
}
write.csv(df.all.train,"train_data.csv")
###


for (i in 2:29) 
{
  df.all.test[,i]<-scale(df.all.test[,i],center = TRUE,scale = TRUE)
}
write.csv(df.all.test,"test_data.csv")

###### submit ######
df.temp<-read.csv("submit.csv",header = FALSE)
quantile(df.temp$V1,0.001) #1%
quantile(df.temp$V1,0.999) #99%
for (i in 1:50000) #6 month average consumption == 0
{ 
  if(df.all.train[i,"X6mconsum"]>=279)
    df.all.train[i,"X6mconsum"]<-279
}
for (i in 1:50000) #mfee
{ 
  if(df.all.train[i,"mfee"]<=10)
    df.all.train[i,"mfee"]<-10
}
write.csv(df.temp,file = "final.csv",fileEncoding = "UTF-8")