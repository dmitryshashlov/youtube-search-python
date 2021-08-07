from youtubesearchpython import *
import fileinput

def main():

    for track in fileinput.input():
        customSearch = CustomSearch(track, VideoSortOrder.relevance, language = 'en', region = 'US', limit = 1)
        print(customSearch.result(mode = ResultMode.json))

if __name__ == '__main__':
    main()
