"""
The Steel for Life 'Blue Book' is the de facto source of
steel section data used by Structural Engineers in the
United Kingdom. Traditionally provided as a physical tome
of datasets for all the available steel section geometries
in each given category of section (e.g., UB, PFC etc.), the
same data is now more readily available from the Steel for
Life website: https://www.steelforlifebluebook.co.uk.

To facilitate the use and distribution of the steel section
data in a format more conducive to software development,
the available Excel files for each section category have
been downloaded and converted into JSON files.

The original Excel files are available within this repo,
alongside the exported JSON files. For most users, having
access to the JSON files themselves may be adequate. However,
for those who prefer to understand the internals of these
data transformation processes, the original source script
is provided herein.
"""

import json

import pandas as pd


print("Welcome to the Steel for Life 'Blue Book' parser.")

print("Loading the system configuration file...")
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

xlsx_file_count = len(config)
print(f"\nFound {xlsx_file_count} .xlsx file(s) to process.\n")

for i in range(xlsx_file_count):

    if config[i]:

        try:
            input_file = config[i]['inputFile']
            output_file = config[i]['outputFile']
            column_labels = config[i]['columnLabels']

            empty_rows = {
                'header': config[i]['headerRowCount'],
                'footer': config[i]['footerRowCount']
            }

            print(f"\tReading {i + 1}/{xlsx_file_count}: {input_file}.")
            df = pd.read_excel(input_file)

            print(f"\t\tTrimming empty rows.")
            df = df.iloc[empty_rows['header']:-empty_rows['footer']]

            print(f"\t\tDetermining section availability.")
            df[df.columns[2]] = df.iloc[:, 2].apply(lambda x: x == '+' or x == '#')

            print(f"\t\tCleaning data.")
            df.fillna(method='ffill', inplace=True)
            df[df.columns[1]] = df.iloc[:, 1].apply(lambda s: s if 'x' in str(s) else f'x{s}')
            df['Section'] = df.iloc[:, 0] + ' ' + df.iloc[:, 1]
            df.drop(df.columns[[0, 1]], axis=1, inplace=True)
            df.rename(columns=column_labels, inplace=True)
            df.set_index('Section', inplace=True)
            data = df.transpose().to_dict()

            print(f"\t\tStripping whitespace from section designations.")
            data = {k.translate({32: None}): v for k, v in data.items()}

            print(f"\t\tCasting numeric values to float.")
            for properties in data.values():
                for k, v in properties.items():
                    if not isinstance(v, bool):
                        try:
                            properties[k] = float(v)
                        except ValueError:
                            pass

            print(f"\t\tExporting to: {output_file}.\n")
            with open(output_file, mode='w', encoding='utf-8') as f:
                json.dump(data, f)

        except KeyError as err:
            print(f"Skipping sheet {i + 1}/{xlsx_file_count}: {err}.")
