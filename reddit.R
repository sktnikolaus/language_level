setwd('/Users/nikolaus/Documents/Stanford2ndRound/MS&E231/Project/language_level')
reddit = read.table("avg_no_topics_per_avg_user_total.txt",header=TRUE)

library(ggplot2)
library(dplyr)

red<-data.frame(reddit)

red_modified <- red[which(red$avg_no_topics<200),]

z = c(11.7, 12.0)
tex<-c('str')

hist_cut <- ggplot(red_modified, aes(x=avg_no_topics))
hist_cut <- hist_cut + geom_histogram(binwidth=5)# geom_bar(position="dodge",bindwidth=5) # defaults to stacking
hist_cut <- hist_cut + geom_vline(xintercept = z,colour="blue",show_guide=T)
hist_cut<- hist_cut + geom_vline(xintercept = 8.27,colour="red")
hist_cut <- hist_cut + annotate("text", max(z)+100, 250, label = "Democrats",color='blue')
hist_cut <- hist_cut + annotate("text", max(z)+100, 300, label = "Republicans",color='red')
hist_cut

senti = read.table("sentiment.txt",header=TRUE)

senti_clean<-senti[which(senti$sentiment!=0.0),]

senti_liberal<-senti_clean[which(senti_clean$topic=='Liberal'),]
senti_democrats<-senti_clean[which(senti_clean$topic=='democrats'),]
senti_republican<-senti_clean[which(senti_clean$topic=='Republican'),]

hist_lib<-ggplot(senti_liberal,aes(x=sentiment))+geom_histogram(binwidth=0.15)
hist_lib

hist_lib<-ggplot(senti_democrats,aes(x=sentiment))+geom_histogram(binwidth=0.1)
hist_lib

hist_lib<-ggplot(senti_republican,aes(x=sentiment))+geom_histogram(binwidth=0.15)
hist_lib
#senti_grouped<-senti_clean  %>% group_by(topic)  %>% 



