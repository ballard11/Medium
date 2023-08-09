#setwd("/Users/benjaminballard/Documents/OklahomaR")
#setwd("/Users/benjaminballard/Documents/OklahomaR")

setwd("C:/Users/Ben/OneDrive/Documents/Medium Posts/MediumPosts-main")

library(ggplot2)
library(tidyverse)
library(ggthemes)

#install.packages("ggthemes")

df<-read.csv("OklahomaOverall.csv", header=TRUE)

df<-df%>%
  filter(Year>=1950)

df$Team <- "Oklahoma"


#Group by Conference and calculate average 
groupeddf<-df%>%
  group_by(Conf)%>%
  summarise(AvgWins=mean(OverallW,na.rm=T),AvgWinPct=mean(OverallPct,na.rm=T),Avg.AP.Pre=mean(AP.Pre,na.rm=T),Avg.AP.Post=mean(AP.Post,na.rm=T)) %>% 
  mutate(RankDelta = Avg.AP.Pre-Avg.AP.Post)


#Create DF -> Over and Under-Rated by Year
Yeardf<-df%>%
  group_by(Year)%>%
  summarise(AvgWins=mean(OverallW,na.rm=T),AvgWinPct=mean(OverallPct,na.rm=T),Avg.AP.Pre=mean(AP.Pre,na.rm=T),Avg.AP.Post=mean(AP.Post,na.rm=T)) %>% 
  mutate(RankDelta = Avg.AP.Pre-Avg.AP.Post) %>% 
  arrange(desc(Year))




plot <-ggplot(data = Yeardf) +
  geom_point(mapping = aes(x = Year, y = AvgWins))+
  labs(title = "OU Wins by Year", x = "Year", y = "Wins", color = "Legend Title\n")+
  theme_hc() 

print(plot)


#Strength of SChedule
plot2 <-ggplot(data = df) +
  geom_point(mapping = aes(x = Year, y = SOS,color=Conf))+
  labs(title = "OU Strength of Schedule by Year", x = "Years", y = "SOS", color = "Conference\n")+
  theme_hc() 

print(plot2)

#Strength of SChedule
plot3 <-ggplot(data = df) +
  geom_point(mapping = aes(x = Year, y = SRS,color=Conf))+
  labs(title = "OU SRS by Year", x = "Years", y = "SRS", color = "Conference\n")+
  theme_hc() 

print(plot3)




##Density plot of Overall WinPercentage
ggplot(df,aes(OverallPct))+
  geom_density()


ggplot(df,aes(OverallPct))+
  geom_histogram(bins=30,fill="blue")





###############################
#attempt at regression

ggplot(df, aes(x=AP.Pre,y=AP.Post))+
  geom_point()+
  labs(x="APPre", y="APPost",
       title="OU AP Pre and AP Post")

#Q4 Correlation
res <- cor.test(df$AP.Pre, df$AP.Post, 
                method = "pearson")
res
#.30 lose correlation

result1<-lm(data=df,AP.Pre ~ AP.Post)
summary(result1)  #R2 .07

##########

ggplot(df, aes(x=SOS,y=AP.Post))+
  geom_point()+
  labs(x="SOS", y="APPost",
       title="OU AP Pre and AP Post")

res <- cor.test(df$AP.Post, df$SOS, 
                method = "pearson")
#more correlation with SOS and Post AP than Pre



#############


dfnd<-read.csv("NotreDame.csv", header=TRUE)

dfnd$Team <- "NotreDame"

dfnd<-dfnd%>%
  filter(Year>=1950)




#MERGED INTO 1 DF.  DID COMBINED IN THE NOTRE DAME SCRIPT
Combineddf<-merge(df,dfnd, all=TRUE)

##Density plot of Overall WinPercentage
ggplot(Combineddf,aes(OverallPct,colour = Team))+
  labs(x="Overall Win Pct", y="Density Function",
       title="OU vs. Notre Dame Win Probability")+
  geom_density()




#ggplot(Combineddf,aes(OverallPct))+
#  geom_histogram(bins=30,fill="blue")





##Density plot of Overall WinPercentage
ggplot(Combineddf,aes(OverallPct,colour = Team))+
  labs(x="Overall Win Pct", y="Density Function",
       title="OU vs. Notre Dame Win Probability")+
  geom_density()

#HEY I Created a function
floor_decade    = function(value){ return(value - value %% 10) } 

#Make new decade column
Combineddf<-Combineddf %>% 
  mutate(decade = round_to_decade(Combineddf$Year))



##Density plot of Overall WinPercentage
ggplot(Combineddf,aes(OverallPct,colour = Team))+
  labs(x="Overall Win Pct", y="Density Function",
       title="OU vs. Notre Dame Win Probability")+
  geom_density()


####this works
ggplot(Combineddf,aes(OverallPct,color = Team))+
  labs(x="Overall Win Pct", y="Density Function",
       title="OU vs. Notre Dame Win Probability")+
  geom_density()


##Density plot of Overall WinPercentage
ggplot(Combineddf, aes(x=Year,y=OverallPct,colour=Team))+
  geom_point()+
  labs(x="SOS", y="APPost",
       title="OU AP Pre and AP Post")+
  geom_smooth(method=lm,se=FALSE)+
  facet_wrap(~decade)


#Would be nice to autoscale

Then you could show how quickly a team improved or fell off a cliff.