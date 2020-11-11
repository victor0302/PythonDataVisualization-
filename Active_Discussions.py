import requests
from plotly import offline
from operator import itemgetter


# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
# request
r = requests.get(url)
# tells us if successful or not
print("Status code:", r.status_code)

# Process information
submission_ids = r.json()

# list that is a dictionary format of each story/discussion with title, link, comments
submission_dicts = []

for submission_id in submission_ids[:15]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()

    # # builds a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

# sorting the list of dictionaries by comments in descending order
# to key the comments in the listed dictionary as the value to sort by
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# lists to store each values of the dictionary for graph
titles, comments, labels  = [], [], [],
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    comments.append(submission_dict['comments'])
    story = submission_dict['title']
    link = submission_dict['link']
    repo_link = f"<a href='{link}'>{story}</a>"
    labels.append(repo_link)



# Make visualization.
data = [{'type': 'bar',
         'x': titles,
         'y': comments,
         'text': labels,
         'marker': {
             'color': 'rgb(60, 100, 150)',
             'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
         }, 'opacity': 0.6,
         }]
my_layout = {'title': 'highest commented stories - Hacker News',
             'titlefont': {'size': 28},
             'xaxis': {
                 'titlefont': {'size': 24},
                 'tickfont': {'size': 10}
             },
             'yaxis': {
                 'title': 'Comments',
                 'titlefont': {'size': 24},
                 'tickfont': {'size': 14},
             },
             }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_HackerNews_Comments.html')
