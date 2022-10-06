

class csvToHtml:
    def __init__(self, csv_file, output_file='table.html', style='table table-bordered') -> None:
        self.csv_content = self.csvContent(csv_file)
        self.output = output_file
        self.table_style = style
        print(self.generateHtml())

    def filter_(self, text):
        text = text.replace('\n', '')
        return text

    def csvContent(self, csv):
        with open(csv, 'r', encoding='utf-8') as file:
            return file.readlines()

    def genCols(self, type="thead"):
        thead_tr = self.csv_content[0]
        thead_tr = thead_tr.split(',')
        thead = f'<{type}>\n    <tr>\n'
        thead = thead + f'        <th scope="col">#</th>\n'
        for k in thead_tr:
            k = self.filter_(k)
            o = f'        <th scope="col">{k}</th>\n'
            thead = thead + o
        thead = thead + f'    <tr/>\n</{type}>'
        return thead

    def genBody(self):
        tbody = '<tbody>'
        count = 0
        for data in self.csv_content[1::]:
            count += 1
            c = self.filter_(data)
            tr = '\n    <tr>\n'
            tr = tr + f'\n        <td scope="row">{count}</td>\n'
            for l in c.split(','):
                tr = tr + f'        <td>{l}</td>\n'
            tbody = tbody + tr + '    </tr>\n'
        return tbody

    def generateHtml(self):
        theads = self.genCols()
        tfoots = self.genCols('tfoot')
        tbody = self.genBody()
        table = f"""
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css">
<table class='{self.table_style}'>
    {theads}
    {tfoots}
    {tbody}
</table>
        """
        self.writeHtml(table)
        return table

    def writeHtml(self, text):
        text = str(text).encode('utf-8')
        with open(self.output, 'wb') as file:
            file.write(text)


csv_filename = './data.csv'

csvToHtml(csv_filename)
