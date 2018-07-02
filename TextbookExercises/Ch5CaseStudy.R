library("data.table")
library("ggplot2")
library("recommenderlab")
library("countrycode")

file_in <- "/Users/kailukowiak/DATA643/TextbookExercises/anonymous-msweb.test"

table_in <- read.csv(file_in, header = FALSE)
head(table_in)
table_users <- table_in[, 1:2]
table_users <- data.table(table_users)
setnames(table_users, 1:2, c("category", "value"))
table_users <- table_users[category %in% c("C", "V")]
head(table_users)


table_users[, chunk_user := cumsum(category == "C")]
head(table_users)


table_long <- table_users[, list(user = value[1], item = value[-1]), by =
                            "chunk_user"]
head(table_long)

table_long[, value := 1]
head(table_long)

table_wide <- reshape(data = table_long,
                      direction = 'wide',
                      idvar = 'user',
                      timevar = 'item',
                      v.names = 'value')

dim(table_wide)
