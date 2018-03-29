class EasyTable:
    def __init__(self, header=None, padding=4):
        self.header = header
        self.data = []
        self.pad = padding

    def __str__(self):
        colWidth = dict()

        if self.header:
            for col in range(len(self.header)):
                colWidth[col] = len(str(self.header[col])) + self.pad
        if len(self.data) >= 1:
            for rows in self.data:
                for col in range(len(rows)):
                    newWidth = len(str(rows[col])) + self.pad
                    if col not in colWidth.keys():
                        colWidth[col] = newWidth
                    else:
                        if newWidth > colWidth[col]:
                            colWidth[col] = newWidth
        breakLine = "+"
        row = "|"
        out = ""
        
        if self.header:
            for col in range(len(self.header)):
                breakLine += "-"*colWidth[col] + "+"
                row +=  '{:{align}{width}}'.format(str(self.header[col]), align='^', width=colWidth[col]) + '|'
            out += breakLine + "\n" + row + "\n" + breakLine
        else:
            for rows in self.data:
                for col in range(len(rows)):
                    breakLine += "-"*colWidth[col] + "+"
            out += breakLine

        for rows in self.data:
            row = "|"
            for col in range(len(rows)):
                row +=  '{:{align}{width}}'.format(str(rows[col]), align='^', width=colWidth[col]) + '|'
            out += "\n" + row
        return out + "\n" + breakLine
                

    def set_header(self, header):
        pass
            

    def add_row(self, inList):
        if self.header:
            minLen = len(self.header)
        elif self.data != []:
            minLen = len(self.data[0])
        else:
            minLen = 0

            
        if type(inList) not in (list, tuple):
            raise TypeError("Only lists/tuples can be added as rows")
        elif len(inList) == 0:
            raise IndexError("The row cannot be empty")
        elif type(inList[0]) == list:
            for rows in inList:
                if len(rows) is (minLen):
                    self.data.append(rows)
                else:
                    raise IndexError("The length of all rows must be equal to the header and other rows")
        elif len(inList) is (minLen):
            self.data.append(inList)
        else:
            raise IndexError("The length of all rows must be equal to the header and other rows")

    
