# Loading data
df <- read.csv("csvs/Lombard.csv")

# partition data
trainingcases <- sample(nrow(df), nrow(df))
training <- df[trainingcases, ]

bluechoc <- lm(X8 ~ X9, data=training)
summary(bluechoc)

#bluebana <- lm(X7 ~ X9, data=training)
#summary(bluebana) 

# found that there is a statistical significance: R^2 of 0.8243
#chocbana <- lm(X8 ~ X9, data=training)
#summary(chocbana)
# no relationship, small R^2
