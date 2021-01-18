import pandas as pd
import csv

def flattenjson( b, delim ):
    val = {}
    for i in b.keys():
        if isinstance( b[i], dict ):
            get = flattenjson( b[i], delim )
            for j in get.keys():
                val[ i + delim + j ] = get[j]
        else:
            val[i] = b[i]

    return val


if __name__ == '__main__':

    json_list = pd.read_json('servicos.json').resposta

    json_flat = flattenjson(json_list[0], "__")

    csv_file = open('data_file.csv', 'w')
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(json_flat.keys())
    csv_writer.writerow(json_flat.values())

    csv_file.close()

    # flag = False


    # for json_obj in json_list:
    #     json_flat = flattenjson(json_obj, "__")

        # if flag is False:
        #     csv_writer.writerow(json_flat.keys())
        #     flag = True


        # #removendo unicodes indesejaveis
        # no_problems = []
        # for val in json_flat.values():
        #     if type(val) is str:
        #         x = val.replace('\u200b', '')
        #         y = val.replace('\ufb01', '')
        #         no_problems.append(x)
        #         no_problems.append(y)

        # csv_writer.writerow(no_problems)
    #
    # csv_file.close()
