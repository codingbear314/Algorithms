import sys
import functools
input=lambda:sys.stdin.readline().rstrip()

def ConvexHull(points):
    def ccw(a, b, c):
        x1, y1=a
        x2, y2=b
        x3, y3=c
        return (x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)

    def cmp(a, b):
        global lowest
        ccwed=ccw(a, lowest, b)
        if ccwed>0:
            return -1
        elif ccwed==0:
            if a[1]<b[1]:
                return 1
            elif a[1]>b[1]:
                return -1
            else:
                if a[0]<b[0]:
                    return 1
                else:
                    return -1
        else:
            return 1


    lowest=(10**5, 10**5)
    for i in points:
        if i[1]<lowest[1]:
            lowest=i
        elif i[1]==lowest[1]:
            if i[0]<lowest[0]:
                lowest=i

    sortedpoint=[]
    for i in points:
        if i!=lowest:
            sortedpoint.append(i)

    lowx, lowy=lowest[0], lowest[1]
    sortedpoint.sort(key=functools.cmp_to_key(cmp))

    #print(lowest)
    #print(sortedpoint)

    remaining_points=[lowest]+sortedpoint
    convex=[lowest, remaining_points[-1]]
    remaining_points.pop()
    inner=[]

    while len(remaining_points):
        assert len(convex)>=2
        a=convex[-2]
        cen=convex[-1]
        b=remaining_points[-1]
        ccwed=ccw(a, cen, b)

        if ccwed>0:
            #This is curved in the right direction
            convex.append(remaining_points.pop())
        elif ccwed<0:
            #This is curved in the wrong direction. We can know that cen is definatly wrong.
            convex.pop()
        else:
            #This is not a normal case, a, cen and b are all on one line. We remove cen, and insert b.
            convex.pop()
            convex.append(remaining_points.pop())


    convex.pop()
    return convex