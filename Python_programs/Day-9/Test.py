#In this practice exercise, we use a "for" loop to automate the analysis of a log file and
#identify lines containing the word "error." This demonstrates how loops can be used to process data and
#extract relevant information efficiently.

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)