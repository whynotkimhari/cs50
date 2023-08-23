# report-of-searching-algorithms 2.x ver
***CAUTIONS 1: ALL VALUES IN THIS ARE UNCERTAIN TO DETERMINE WHICH ALGORITHM IS "THE BEST" FOR ALL CASES. <br/>
***CAUTIONS 2: ALL VALUES ARE RESULTS WHEN RUNNING THIS COMPARISON IDEA ON MY OLD AND POOR LAPTOP. <br/>
***CAUTIONS 3: ALL VALUES MAYBE DIFFRENT AT EACH RUNNING TIME. <br/>
report of searching algorithms include QuickSort, MergeSort, HeapSort, and IntroSort.

## data folder
data folder includes ten sets of data. Each set contains 1 million random real numbers (or double). </br>
set 1 is sorted in ASC order, set 2 is sorted in DSC order, and 8 sets left are in random order. <br/>
data folder also contains a program to generate all ten sets above which is generate.py.

## values folder
values folder includes {algorithm}.txt. <br/>
{algorithm}.txt contains ten given back values of using {algorithm} to sort ten datasets.

## algorithms
HeapSort.cpp, IntroSort.cpp, MergeSort.cpp, and QuickSort.cpp. They are all in one that is runner.cpp. <br/>
runner.cpp has three main parts which are Headers, Main, and Footers. <br/>
Headers defines Footers for Main to use it while running the programme. <br/>

## main function
data go to the programme by file stream which is file input - fi. Data go out of the programme with the same idea which is file output - fo. <br/>
each time, the programme will choose 1 output path to write the time running on it, with each output path, ten input path is chosen to read the data. <br/>
to compute the time (sec) that algorithms work i.e programme spend how long in solving by using that algorithm. Notify that this amount of time does not includes anything else except the algorithm works. <br/>

## visualization given back values
visualize.py: using given back values to draw a line graph which is img.png. <br/>
![alt text](https://github.com/whynotkimhari/report-of-searching-algorithms/blob/024670623cfc8c8f9dcd7ab77aa7e182c54b2d83/img.png)

## requiments.txt
you needn't to use this part of this report. This is just some functions to visualize more specific about the values after running the programme. <br/>
you even needn't to do this if it has already on you own, if any <br/>
or if you want to, here it is how to use:<br/>
using
```bash
pip install -r requiments.txt
```

## disclaimer n ps
again, this report does not confirm anything true for all cases. <br/>
through this report, we should learn that each sorting algorithm has it strength and weakness. <br/>
so we can not jugde anything just by some aspects. Some may the worst in this situation but they may also be the best in another. <br/>
thanks for reading to this the end line of file. i'm appreciate it.
