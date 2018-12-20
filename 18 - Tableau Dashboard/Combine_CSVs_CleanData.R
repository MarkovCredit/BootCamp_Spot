library(tidyverse)
library(data.table)
library(microbenchmark)

do.call_rbind_fread <- function(path, pattern = "*.csv") {
  files = list.files(path, pattern, full.names = TRUE)
  do.call(rbind, lapply(files, function(x) fread(x, stringsAsFactors = FALSE)))
}


data <- do.call_rbind_fread("//vcco1-hf-vp01/home/MLevine/Desktop/TripData")