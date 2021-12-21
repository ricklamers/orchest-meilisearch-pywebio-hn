# A simple script to calculate BMI
import pywebio
import requests
import orchest
import meilisearch

from pywebio.input import input, actions
from pywebio.output import put_text, put_markdown, put_html, clear

def show_search():
    
    query = ""
    while len(query) == 0:
        query = input("Input a query")
    
    meili_service = orchest.get_service("meilisearch")
    meili_connection_string = f"http://{meili_service['internal_hostname']}:{meili_service['ports'][0]}"
    
    client = meilisearch.Client(meili_connection_string)
    results = client.index('comments').search(query, {'limit': 100000})
    
    put_markdown(f"You searched for **{query}**. Found {len(results['hits'])} results.")
    
    if not results['hits']:
        put_text("Did not find any results.")
        
    for result in results['hits']:
        put_html(result['username'] + " said: <div style='font-family:monospace; font-size:0.9em'>" + result['body'].replace("\n", "<br />") + "</div><hr>")
        
def search():
    show_search()
    
    if actions("", ["Search again"]):
        clear()
        search()
    

if __name__ == '__main__':
    pywebio.start_server(search, port=8080, debug=True)