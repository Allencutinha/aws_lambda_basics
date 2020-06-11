import json

print('Loading function')


def lambda_starts():
    print("\n\n====================Lambda starts here==============================")


def lambda_ends():
    print("\n\n====================Lambda ends here==============================")


def print_record_stats(record):
    lamba_string = "Transient App - "
    print("\t\tTransient App - EVENT HEADER")
    print(f"event Id     : {record['eventID']}")
    print(f"event Name   : {record['eventName']}")
    print(f"event version: {record['eventVersion']}")
    print(f"event source : {record['eventSource']}")
    print(f"aws region   : {record['awsRegion']}")
    print("\n")


def print_number_of_records_processed(event):
    report_change = 'Successfully processed {} records.'.format(
        len(event['Records']))
    print(report_change)


def print_dictionary(dict):
    for value in dict.values():
        print(value)


def get_dictionary_val(dict):
    values = []
    dict_vals = ""
    for value in dict.values():
        values.append(value)
        dict_vals = dict_vals+"\t"+str(value)
    return dict_vals


def print_seeker_details(seeker_details):
    seeker = seeker_details['L'][0]['M']
    print("======Seeker details=======")
    print(f"\tname   : {get_dictionary_val(seeker['name'])}")
    print(f"\temail  : {get_dictionary_val(seeker['email'])}")
    print(f"\tstatus : {get_dictionary_val(seeker['status'])}")
    print("======**************=======")


def print_new_image(newImage):
    print("\t\t NEW IMAGE DETAILS")
    print(
        f"is volunteer Job : {(get_dictionary_val(newImage['isVolunteerJob']))}")
    print(f"amount      : {(get_dictionary_val(newImage['amount']))}")
    print(f"jobStatus   : {(get_dictionary_val(newImage['jobStatus']))}")
    print(f"address     : {(get_dictionary_val(newImage['address']))}")
    print(f"pinCode     : {(get_dictionary_val(newImage['pinCode']))}")
    print(f"city        : {(get_dictionary_val(newImage['city']))}")
    print(f"typename    : {(get_dictionary_val(newImage['__typename']))}")
    print(f"description : {(get_dictionary_val(newImage['description']))}")
    print(f"createdAt   : {(get_dictionary_val(newImage['createdAt']))}")
    print(f"jobID       : {(get_dictionary_val(newImage['jobID']))}")
    print(f"noOfHours   : {(get_dictionary_val(newImage['noOfHours']))}")
    print(f"startTime   : {(get_dictionary_val(newImage['startTime']))}")
    print(f"endTime     : {(get_dictionary_val(newImage['endTime']))}")
    print(f"id          : {(get_dictionary_val(newImage['id']))}")
    print(f"jobType     : {(get_dictionary_val(newImage['jobType']))}")
    print(f"startDate   : {(get_dictionary_val(newImage['startDate']))}")
    print(f"updatedAt   : {(get_dictionary_val(newImage['updatedAt']))}")
    print_seeker_details(newImage['seekerDetails'])


def process_record(record):
    event_name = record['eventName']
    print("eventName : " + event_name)
    print_dictionary(record["dynamodb"]["NewImage"]['address'])
    print_new_image(record["dynamodb"]["NewImage"])
    return event_name


def lambda_handler(event, context):
    lambda_starts()
    for record in event['Records']:
        print_record_stats(record)
        event_name = process_record(record)

    print_number_of_records_processed(event)
    lambda_ends()
    return (f"The event that occured in our db is {event_name}")
