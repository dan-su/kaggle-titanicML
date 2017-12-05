import csv
class CsvProcessor:
    debug = False;
    header = []
    data = []

    def __init__(self, csvname, debug = False):
        with open(csvname, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            self.header = reader.next()
            for row in reader:
                self.data += [row]
        self.debug = debug

    def get_header(self):
        """Returns header line of csv passed in

        :return: 1st line of csv
        :rtype: list object of generic type
        """
        return self.header

    def get_data(self):
        """Returns data of csv passed in

        :return: 2-n lines of csv
        :rtype: list of all one same generic type
        """
        return self.data

    def get_avg(self, column):
        """Returns the average of all numbers in the column specified

        :param column: index of data
        :type column: int

        :return: average of the specified column
        :rtype: int
        """
        total = 0
        try:
            for row in self.data:
                total += float(row[column])
            if self.debug:
                return "Avg: " + str(total/len(self.data))
            else:
                return total/len(self.data)
        except IndexError:
            raise
        except TypeError:
            raise

    def get_sum(self, column):
        """Returns the sum of all numbers in the column specified

        :param column: index of data
        :type column: int

        :return: sum of the specified column
        :rtype: int
        """
        total = 0
        try:
            for row in self.data:
                total += float(row[column])
            if self.debug:
                return "Sum: " + str(total)
            else:
                return total
        except IndexError:
            raise
        except TypeError:
            raise

    def get_occurrences(self, column):
        """Returns the occurrences of all variables of data in the column specified

        :param column: index of data
        :type column: int

        :return: occurrences of all variables of the specified column
        :rtype: dict of type (generic, int)
        """
        occurrence_set = dict()
        try:
            for row in self.data:
                if (row[column] in occurrence_set):
                    occurrence_set[row[column]] += 1
                else:
                    occurrence_set[row[column]] = 1
            if self.debug:
                return "Occurrence Set: " + str(occurrence_set)
            else:
                return occurrence_set
        except IndexError:
            raise
        except TypeError:
            raise
