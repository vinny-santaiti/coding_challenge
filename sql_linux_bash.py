# SQL query
# find duplicate emails
select email
from table_name
group by email
having count(*) > 1

# Score rank in ANSI TRANSACT SQL SERVER
select Score, 
RANK() OVER (ORDER BY Score DESC) as Rank
from Test
group by Score

""" Sample create and insert script, http://sqlfiddle.com 
CREATE TABLE Test (
    ID int,
    Score int, 
    PRIMARY KEY (ID)
);
GO
insert into Test (ID, Score) VALUES (1, 4);
GO
insert into Test (ID, Score) VALUES (2, 1);
GO
insert into Test (ID, Score) VALUES (3, 3);
GO
insert into Test (ID, Score) VALUES (4, 4);
GO
"""

# linux show last line of file1.txt
tail -n1 file1.txt

# bash script to count words in file
# tr = trsnlate or delete chars
# sort = alpha order, makes it easier to count with uniq
# uniq = counts lines by number of occurances
# awk = manipulates string patterns
#!/bin/sh
cat input_file.txt | (tr -d '[:punct:]' | tr ' ' '\n' | sort | uniq -c | awk '{print $2" "$1}') 
