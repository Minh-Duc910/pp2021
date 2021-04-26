class Student:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.d = ""

    def getname(self):
        return self.name

    def getid(self):
        return self.id

    def getd(self):
        return self.d

    def st_info(self):
        self.name = input("Student Name: ")
        self.id = input("Student ID: ")
        self.d = input("Date of birth: ")

    def show_st(self):
        stlist = {'ID: ': self.id, 'Name: ': self.name, 'Dob: ': self.d}
        print(stlist)


def numst():
    ns = int(input("Number of Student: "))
    return ns


if __name__ == '__main__':
    st = []
    nst = numst()
    for s in range(0, nst):
        nums = Student()
        nums.st_info()
        st += [nums]

    print("Student Info: ")
    for a in st:
        a.show_st()


class Course:
    def __init__(self):
        self.cname = ""
        self.cid = ""

    def getcname(self):
        return self.cname

    def getcid(self):
        return self.cid

    def c_info(self):
        self.cname = input("Course: ")
        self.cid = input("Course ID: ")

    def show_c(self):
        clist = {'ID: ': self.cid, 'Course: ': self.cname}
        print(clist)


def numc():
    nc = int(input("Number of Course: "))
    return nc


if __name__ == '__main__':
    crs = []
    ncrs = numc()
    for c in range(0, ncrs):
        numcr = Course()
        numcr.c_info()
        crs += [numcr]

    print("Course Info: ")
    for b in crs:
        b.show_c()


class Mark:
    def __init__(self):
        self.id = ""
        self.cid = ""
        self.mark = ""

    def getid(self):
        return self.id

    def getcid(self):
        return self.cid

    def getmark(self):
        return self.mark

    def update_mark(self):
        self.id = input("Student ID: ")
        self.cid = input("Course ID: ")
        self.mark = float(input("Mark:"))

    def show_m(self):
        mk = {'ID: ': self.id, 'Course ID: ': self.cid, 'Mark: ': self.mark}
        print(mk)


def st_attend():
    d = int(input("No. student taking exam: "))
    return d


if __name__ == '__main__':
    m = []
    mk = st_attend()
    for i in range(0, mk):
        mm = Mark()
        mm.update_mark()
        m += [mm]

    print("Mark: ")
    for k in m:
        k.show_m()
