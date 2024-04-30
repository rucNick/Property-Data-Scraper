import pandas as pd


def search_legal_description(description):
    # Load data only once if this function will be called multiple times
    global df
    if 'df' not in globals():
        df = pd.read_csv('property_data.csv')  # Ensure the filename matches your CSV file

    # Perform a case-insensitive substring search
    matches = df[df['Legal Description'].str.contains(description, case=False, na=False)]
    if not matches.empty:
        return matches[['Legal Description', 'Address']].to_dict('records')  # Changed to return the Address column
    else:
        return "Legal description not found."


if __name__ == "__main__":
    while True:
        description_to_search = input("Enter legal description to search (or type 'exit' to quit): ")
        if description_to_search.lower() == 'exit':
            break
        results = search_legal_description(description_to_search)
        if isinstance(results, str):
            print(results)
        else:
            for result in results:
                print(f"Legal Description: {result['Legal Description']}")
                print(f"Address: {result['Address']}")
