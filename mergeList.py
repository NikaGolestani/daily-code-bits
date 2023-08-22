def merge_intervals(intervals):
    #sort intervals so we can eliminate problems with start point
    intervals.sort()
    merged_intervals=[]
    length=len(intervals)
    #check for each interval 
    for i in range(length):
        #if the end of i is in the i+1 interval change the start point of i+1 to start point of i
        if  i!=length-1 and intervals[i][1]<intervals[i+1][1] and intervals[i][1]>intervals[i+1][0]:
            intervals[i+1][0]=intervals[i][0]
        #if the end point of i is one less than strat point of i+1 since there is no number to cover in between change the start of i+1 to start of i
        elif i!=length-1 and intervals[i][1]+1==intervals[i+1][0]:
            intervals[i+1][0]=intervals[i][0]
        #if start and end of the interval is included in the last one ignore it
        elif i!=0 and intervals[i][0]>=intervals[i-1][0] and intervals[i][1]<=intervals[i-1][1]:
            continue
        #if there is no relation with next or previous one add it to merged list because it cannot be merged anymore
        else :
            merged_intervals.append(intervals[i])
    return merged_intervals

test_case_1 = [[1, 3], [2, 6], [8, 19], [9, 18]]
test_case_2 = [[1, 5], [6, 10], [11, 15]]
test_case_3 = [[2, 4], [5, 7], [8, 10]]
test_case_4 = [[1, 3], [2, 4], [5, 6], [7, 9]]
test_case_5 = [[1, 3], [4, 6], [2, 5], [7, 10]]

print(merge_intervals(test_case_1))
print(merge_intervals(test_case_2))
print(merge_intervals(test_case_3))
print(merge_intervals(test_case_4))
print(merge_intervals(test_case_5))