import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wl = WordNetLemmatizer()


class NLTK:
    def __init__(self):
        self.data = None
        self.df = None

    def read_data(self, file_name: str):
        read = pd.read_csv(file_name)
        self.df = pd.DataFrame(read)
        return self.df

    def inspect_column(self, updated_col: str, col_name: str):
        self.data = pd.DataFrame()
        self.data[updated_col] = self.df[col_name]
        return self.data[updated_col]

    def tokenize_column(self, col_name: str):
        self.data['token'] = self.data[col_name].apply(word_tokenize)
        return self.data['token']

    def porter_stemmer(self):
        self.data['porter_stemmer'] = self.data['token'].apply(lambda x: [ps.stem(y) for y in x])
        return self.data['porter_stemmer']

    def wordnet_lem(self):
        self.data['wordnet_lem'] = self.data['token'].apply(lambda x: [wl.lemmatize(y) for y in x])
        return self.data['wordnet_lem']

    def print_output(self):
        return print(self.data)

    def convert_csv(self, file_name: str):
        output = self.data.to_csv(file_name)
        return output


def main():
    summarize = NLTK()
    summarize.read_data("Musical_instruments_reviews.csv")
    summarize.inspect_column("original_summary", "summary")
    summarize.tokenize_column('original_summary')
    summarize.porter_stemmer()
    summarize.wordnet_lem()
    summarize.print_output()


if __name__ == '__main__':
    main()
