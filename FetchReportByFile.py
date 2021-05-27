import sys
import resultprocessor as rp
import json

def check_for_override(report_request, option, parameter, isNumeric = False):
    if "-" + option in sys.argv:
            for indx in range(0, len(sys.argv)):
                if sys.argv[indx] == "-" + option:
                    if isNumeric:
                        report_request[parameter] = int(sys.argv[indx + 1])
                    else:
                        report_request[parameter] = sys.argv[indx + 1]
                    break

def call_api(client):
    if len(sys.argv) >= 2:
        report_object = None
        with open(sys.argv[1]) as f_in:
            report_object = json.load(f_in)

        check_for_override(report_object, "PAGESIZE", "pageSize")
        check_for_override(report_object, "START", "startTime")
        check_for_override(report_object, "END", "endTime")

        max_pages = 0
        if "-MAXPAGES" in sys.argv:
            for indx in range(0, len(sys.argv)):
                if sys.argv[indx] == "-MAXPAGES":
                    max_pages = int(sys.argv[indx + 1])
                    break

        if "-ALL" in sys.argv or max_pages > 0:
            pageNumber = 0
            data_available = True
            print('{\n\t "data":[\n') # Output start of array
            while data_available:
                data_available = False # assume no until proven otherwise
                report_object["page"] = pageNumber
                response = client.fetch_report(report_object)
                if response:
                    if "data" in client.result:
                        records = client.result["data"]
                        if "data" in records:
                            # If the number of records returned is less than the page size, we've reached the end. 
                            # Occasionally, if the number of records is an exact multiple of pageSize, then it may result in one extra call that returns no rows.
                            if len(records["data"]) == report_object["pageSize"]:
                                data_available = True 
                                pageNumber += 1
                                if max_pages > 0 and pageNumber > max_pages:
                                    data_available = False
                            # print comma separator between rows except if it's the last row and there's no more data.
                            for index, row in enumerate(records["data"]): 
                                if index < len(records["data"]) - 1:
                                    print(json.dumps(row, sort_keys=False, indent=4), end=",")
                                else:
                                    if data_available:
                                        print(json.dumps(row, sort_keys=False, indent=4), end=",")
                                    else:
                                        print(json.dumps(row, sort_keys=False, indent=4))

            print("\n]\n}") # Print end of array
        else:
            rp.process_response(client, client.fetch_report(report_object))
    else:
        print("FetchReportByFile {filename.json} [-PAGESIZE ###] [-START ########## ] [-UNTIL ########## ] [-MAXPAGES ###] | [-ALL] \n \
                Returns the results of a report query as defined in a file. \n \
                -PAGESIZE overrides rows per call to fetch.  \n \
                -START overides startDate (epoch milliseconds time format)  \n \
                -END overrides endDate (epoch milliseconds time format) \n \
                -MAXPAGES limit number of pages of data returned \n \
                -ALL retrieves all pages(data) as single large array   \n ")

if __name__ == "__main__":
    rp.main(call_api)