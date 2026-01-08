from loader import load_videos
from collections import Counter


videos = load_videos('data/youtube_trending_videos.csv')
print('Videos Loaded:', len(videos))

def c_vid_n_chan(videos):  # counts videos and channels, i abriviate as
# it is easier for me to remember when calling them later
    total_videos = len(videos)
    channels = set(video['channel_title'] for video in videos)
    return total_videos, len(channels)

def vid_per_cat(videos):
    return Counter(video['category_id'] for video in videos)

def srch_vid_by_title(videos, title):
    for video in videos:
        if title.lower() in video['title'].lower():
            return video
    return None

#here i implement a menu, similar to ones used in calculators, to allow users
#to choose what they would like to see or which data they would like to read
#as well as giving them the choice to select multiple funtions, and exit when they are ready
def user():
    videos = []

    while True:
        print() # i have added extra prints to make the output simpler to read to the user
        print('1. Load Data')
        print('2. Count Videos and Channels')
        print('3. Videos per Catagory')
        print('4. Find Video by Title')
        print('5. Exit')
        print()
#in each of these choices i call a defenition from above which completes
#the task assigned to the option
        choice = input('Choose an Option:')
        print()
        if choice == '1':
            videos = load_videos('data/youtube_trending_videos.csv')
            print('The System has loaded', len(videos), 'Videos')

        elif choice == '2':
            if not videos:
                print('Load Data First')
            else:
                v, c = c_vid_n_chan(videos)
                print('The System has loaded', v, 'Videos and', c, 'Channels')

        elif choice == '3':
            if not videos:
                print('Load Data First')
            else:
                counts = vid_per_cat(videos)
                print('The System has loaded these counts for Videos per Catagory:', counts)

        elif choice == '4':
            if not videos:
                print('Load Data First')
            else:
                titles = input('Enter the Title you wish to search: ')
                video = srch_vid_by_title(videos, titles)
                if video:
                    print('The system found a Video with this Title:', video['title'])
                else:
                    print('Video not Found')

        elif choice == '5':
            break

        else:
            print('Invalid Choice')

user()