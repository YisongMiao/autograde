# autograde
Author: CS4248 TA team.
Purpose: Transform the submission from LumiNUS into a form that is easy to grade by batch.
Please do not include student sensitive information in this public repo.

## traverse.py
convert the LumiNUS download into following data structure:

```
/data
/data/Q1
/data/Q1/A0000001L.py
...
/data/Q2
/data/Q2/A0000001L.py
...
```

Output as per 19 Feb evening zip downloaded from LumiNUS:
```
/Users/yisong/.conda/envs/autograde/bin/python /Users/yisong/autograde/script/traverse.py
Q1:
Unzipped number is: 0
Copied number is 157
Q2:
Unzipped number is: 0
Copied number is 148
Q2:
Unzipped number is: 0
Copied number is 9
Q3:
Unzipped number is: 0
Copied number is 157
Q4:
Unzipped number is: 0
Copied number is 156
done
```

We have 2 Q2, this is because we have typo, and some students fixed in the filename.


## ta.py
import a student's Class into ta.py and execute that. 

Output:
```
/Users/yisong/.conda/envs/autograde/bin/python /Users/yisong/autograde/script/ta.py
<class 'A0000001L.Tokenizer'>
Successfully import a class from a student
```