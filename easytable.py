class EasyTable:
    data = []
    _hasHeader = False
    _rowLength = None
    _maxRowDataLength = None

    def from_data_with_header(data, padding=4):
        table = EasyTable(padding=padding)
        table.add_all(data)
        table._hasHeader = True
        return table

    def from_data(data, padding=4):
        table = EasyTable()
        table.add_all(data)
        return table

    def __init__(self, padding=4):
        self.pad = padding

    def __str__(self):
        if self.data == []:
            return ""

        def gen_row_str(row):
            formattedData = ['{:{align}{width}}'.format(str(datum), align='^', width=datumWidth)
                             for datum, datumWidth
                             in zip(row, self._maxRowDataLength)]
            return f"|{'|'.join(formattedData)}|\n"

        breakLine = f"+{'+'.join(['-'*datumWidth for datumWidth in self._maxRowDataLength])}+\n"
        rows = breakLine.join([gen_row_str(row) for row in self.data])

        return f"{breakLine}{rows}{breakLine}"

    def set_header(self, row):
        self._validate_row(row)
        if self._hasHeader:
            self.data[0] = row
        else:
            self.data.insert(0, row)
            self._hasHeader = True

    def add_all(self, rows):
        for row in rows:
            self.add_row(row)

    def _validate_row(self, row):
        assert len(row) != 0, "Rows cannot be empty"
        if type(row) not in (list, tuple):
            raise TypeError("Only lists/tuples can be added as rows")
        self._verify_data_length(row)
        self._set_max_row_datum_length(row)

    def add_row(self, row):
        self._validate_row(row)
        self.data.append(row)

    def _verify_data_length(self, data):
        if self._rowLength is None:
            self._rowLength = len(data)

        assert len(data) == self._rowLength, "All rows must have same length"

    def _set_max_row_datum_length(self, row):
        if self._maxRowDataLength is None:
            self._maxRowDataLength = [0 for _ in range(self._rowLength)]
        self._maxRowDataLength = [max(prevMax, newSize + self.pad) for prevMax, newSize
                                  in zip(self._maxRowDataLength, [len(str(datum)) for datum in row])]
