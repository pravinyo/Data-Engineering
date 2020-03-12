import csv
import pandas as pd
import sqlalchemy as db
import sys


def SQLFunction():
    engine = db.create_engine('sqlite://', echo=False)
    df = pd.read_csv(sys.argv[1], sep=',')

    df['Date'] = pd.to_datetime(df.Date)
    df['Date'] = df['Date'].dt.strftime('%Y-%M-%d %I:%M:%S %p')

    df.to_sql('stats', con=engine, if_exists='fail', index= False)

    with open(sys.argv[2], mode='w') as output:
        writer = csv.writer(output, delimiter = ',')

        writer.writerow(['Border','Measure','Date','Total','Rolling Average'])

        for row in engine.execute("WITH statistics AS ("
                                  "SELECT Border, Measure, Date, SUM(Value) AS sums "
                                  "FROM stats "
                                  "GROUP BY 1, 2, 3 "
                                  "ORDER BY 3 DESC, 4 DESC, 2 DESC, 1 DESC) "
                                  "SELECT Border, Measure, Date, sums, "
                                  "(SELECT ROUND(AVG(s1.sums),0) "
                                  "FROM statistics AS s1 "
                                  "WHERE s1.border = s.border "
                                  "AND s1.measure = s.measure "
                                  "AND s1.date < s.date) "
                                  "FROM statistics as s "
                                  "ORDER BY 3 DESC, 4 DESC, 1 DESC, 2 DESC;"):
            writer.writerow(row)



if __name__ == "__main__":
    SQLFunction()
