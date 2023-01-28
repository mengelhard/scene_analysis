import pandas as pd
import sys
from PIL import Image


def main():

    df = pd.read_csv(sys.argv[1])

    fn = df['filename'].sample(n=1).values[0]

    print(fn)

    print(df[df['filename'] == fn]['object'].value_counts())

    with Image.open(fn) as im:
    	im.show()


if __name__ == '__main__':
    main()